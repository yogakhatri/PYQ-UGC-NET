#!/usr/bin/env python3
"""Generate the Unit 1 guide and machine-readable datasets from reviewed records.

The records in this file are intentionally hand-reviewed.  Extraction/OCR is used to
locate questions, but mathematical notation and answers are normalized here only after
checking the source page.
"""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TOPICS = {
    "Mathematical Logic": {
        "concept": "Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.",
        "formula": "p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).",
        "shortcut": "For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.",
        "trap": "The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.",
    },
    "Sets and Relations": {
        "concept": "A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive. Floor and ceiling functions map a real number to its neighbouring integers and are handled by separating integer and fractional parts.",
        "formula": "|P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|; x=⌊x⌋+{x}, where 0≤{x}<1.",
        "shortcut": "Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.",
        "trap": "Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.",
    },
    "Counting, Mathematical Induction and Discrete Probability": {
        "concept": "Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.",
        "formula": "nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).",
        "shortcut": "Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.",
        "trap": "Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.",
    },
    "Group Theory": {
        "concept": "A group has closure, associativity, an identity and inverses; an abelian group also commutes. Homomorphisms preserve the operation, automorphisms are isomorphisms from a structure to itself, and fields are commutative integral domains in which every nonzero element is invertible.",
        "formula": "For finite G and H≤G, |H| divides |G| (Lagrange). Every finite integral domain is a field.",
        "shortcut": "To refute an ideal claim, multiply a typical element on the left and right by a completely general ring element.",
        "trap": "A numerical divisibility fact does not establish that one group is a subgroup of another.",
    },
    "Graph Theory": {
        "concept": "Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.",
        "formula": "Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.",
        "shortcut": "Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.",
        "trap": "Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.",
    },
    "Boolean Algebra": {
        "concept": "Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.",
        "formula": "x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.",
        "shortcut": "For four-option identities, test 0/1 assignments; a single counterexample removes an option.",
        "trap": "A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.",
    },
    "Optimization": {
        "concept": "Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.",
        "formula": "PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.",
        "shortcut": "For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.",
        "trap": "The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.",
    },
}


RECORDS: list[dict] = []


def add(
    year: int,
    session: str,
    qno: str,
    page: int,
    topic: str,
    subtopic: str,
    question: str,
    options: list[str],
    answer: int | str,
    solution: list[str],
    *,
    source: str | None = None,
    question_id: str | None = None,
    status: str = "independently-verified",
    official: str | None = None,
    note: str | None = None,
    secondary: str | None = None,
    canonical: str | None = None,
) -> None:
    source = source or f"sources/ugc-net-cs-{year}-{session.lower().replace(' ', '-')}.pdf"
    qid = f"UGCNET-CS-{year}-{session.lower().replace(' ', '-')}-Q{qno}"
    if isinstance(answer, int):
        correct_option = answer
        correct_answer = options[answer - 1]
    else:
        correct_option = None
        correct_answer = answer
    RECORDS.append(
        {
            "id": qid,
            "exam": "UGC NET Computer Science and Applications",
            "year": year,
            "session": session,
            "shift": None,
            "paper": "Paper II" if year >= 2018 else "Paper II/III",
            "questionNumber": str(qno),
            "questionId": question_id,
            "sourceFile": source,
            "sourcePage": page,
            "unit": "Unit 1: Discrete Structures and Optimization",
            "topic": topic,
            "subtopic": subtopic,
            "secondaryUnit": secondary,
            "question": question,
            "options": [{"number": i + 1, "text": value} for i, value in enumerate(options)],
            "correctOption": correct_option,
            "correctAnswer": correct_answer,
            "answerStatus": status,
            "officialAnswer": official,
            "solutionSteps": solution,
            "concept": TOPICS[topic]["concept"],
            "formulaOrRule": TOPICS[topic]["formula"],
            "shortcut": TOPICS[topic]["shortcut"],
            "commonTrap": TOPICS[topic]["trap"],
            "optionAnalysis": [
                {
                    "number": i + 1,
                    "verdict": "correct option" if correct_option == i + 1 else "not the correct option",
                    "explanation": (
                        f"This matches the independently derived result: {correct_answer}."
                        if correct_option == i + 1
                        else f"This does not match the independently derived result ({correct_answer}); the decisive computation or defining property is shown in the solution steps."
                    ),
                }
                for i in range(len(options))
            ],
            "canonicalExplanation": canonical or qid,
            "reviewNote": note,
            "sourceAnchor": f"../{source}#page={page}",
        }
    )


# December 2025 session, held January 2026. Source pages were visually checked.
SRC26 = "sources/ugc-net-cs-2026-jan-dec-2025-session-combined-paper-1-and-2.pdf"
add(2026, "Dec 2025 Jan 2026", "51", 47, "Group Theory", "Rings, integral domains and fields",
    "Which statement is false?",
    ["Every field is an integral domain.", "Every integral domain is a field.", "Every finite integral domain is a field.", "Z_p is a field iff p is prime."], 2,
    ["A field has no zero divisors, so (1) is true.", "Z is an integral domain but not a field because 2 has no multiplicative inverse in Z.", "The standard finiteness argument makes multiplication by a nonzero element bijective, proving (3); (4) is also standard."],
    source=SRC26, question_id="6119872209")
add(2026, "Dec 2025 Jan 2026", "52", 48, "Group Theory", "Rings and ideals",
    "Let S be the subring of M₂(Z) consisting of all diagonal matrices diag(a,b). What kind of ideal is S?",
    ["Left but not right ideal", "Right but not left ideal", "Both left and right ideal", "Neither left nor right ideal"], 4,
    ["Take D=diag(a,b) and an arbitrary matrix X.", "XD can have nonzero off-diagonal entries, so XD need not lie in S; likewise DX need not lie in S.", "Thus S is a subring but neither a left nor a right ideal."],
    source=SRC26, question_id="6119872210")
add(2026, "Dec 2025 Jan 2026", "53", 49, "Group Theory", "Groups and Lagrange theorem",
    "Assertion: the order of (Z₅*,×) divides the order of (Z₁₃*,×). Reason: the order of a subgroup divides the order of the group.",
    ["Both true; R explains A", "Both true; R does not explain A", "A true; R false", "A false; R true"], 2,
    ["The multiplicative unit groups have orders φ(5)=4 and φ(13)=12; hence 4 divides 12.", "Lagrange's theorem is true.", "No subgroup embedding was stated, so Lagrange's theorem is not the reason for this numerical divisibility fact."],
    source=SRC26, question_id="6119872211", note="The source prints Z₅ and Z₁₃ with multiplication; these must be read as their nonzero unit groups for them to be groups.")
add(2026, "Dec 2025 Jan 2026", "54", 49, "Sets and Relations", "Partial ordering",
    "On A=N×N define (a,b) R (c,d) iff a≤c or b≤d. Assertion: R is a partial order. Reason: a partial order is reflexive, antisymmetric and transitive.",
    ["Both true; R explains A", "Both true; R does not explain A", "A true; R false", "A false; R true"], 4,
    ["R is reflexive, but antisymmetry fails: (1,2)R(2,1) because 1≤2, and (2,1)R(1,2) because 1≤2 in the second coordinate, although the pairs differ.", "Therefore the assertion is false.", "The reason correctly states the three defining properties of a partial order."],
    source=SRC26, question_id="6119872212")
add(2026, "Dec 2025 Jan 2026", "55", 50, "Mathematical Logic", "Predicates and nested quantifiers",
    "Over all integers, which are true? A ∀n∃m(n²<m); B ∃n∃m(n+m=4 ∧ n−m=2); C ∃n∃m(n²+m²=5); D ∃m∀n(m+n=0); E ∀m∃n(m+n=0).",
    ["A,B,C only", "A,B,C,D only", "A,B,C,E only", "B,C,D,E only"], 3,
    ["A: choose m=n²+1. B: n=3,m=1. C: n=1,m=2.", "D is impossible because one fixed m cannot equal −n for every integer n.", "E is true by choosing n=−m. Hence A,B,C,E."],
    source=SRC26, question_id="6119872213")
add(2026, "Dec 2025 Jan 2026", "56", 51, "Mathematical Logic", "Tautologies and rules of inference",
    "Which implications are tautologies? A [¬p∧(p∨q)]→q; B ¬p→(p→q); C [p∧(p→q)]→q; D ¬(p→q)→q.",
    ["A,B only", "B,D only", "A,B,C only", "B,C,D only"], 3,
    ["A's antecedent simplifies to ¬p∧q, so A is true. B is true because p false makes p→q true.", "C is modus ponens and is a tautology.", "For D choose p=true,q=false: its antecedent is true and consequent false. Thus D is not a tautology."],
    source=SRC26, question_id="6119872214")
add(2026, "Dec 2025 Jan 2026", "57", 52, "Graph Theory", "Planar graphs and crossing numbers",
    "Arrange K₆, K₇, K₄,₄ and K₅,₅ in ascending order of minimum crossing number.",
    ["K₆,K₇,K₄,₄,K₅,₅", "K₄,₄,K₅,₅,K₆,K₇", "K₆,K₄,₄,K₇,K₅,₅", "K₇,K₅,₅,K₆,K₄,₄"], 3,
    ["Known crossing numbers are cr(K₆)=3, cr(K₄,₄)=4, cr(K₇)=9 and cr(K₅,₅)=16.", "Ascending order is therefore K₆, K₄,₄, K₇, K₅,₅."],
    source=SRC26, question_id="6119872215")
add(2026, "Dec 2025 Jan 2026", "58", 53, "Graph Theory", "Prefix notation and rooted expression trees",
    "Arrange the source's four prefix expressions A–D in ascending value: A='− * 2 / 8 4 3'; B='↑ − * 3 6 * 4 2 5'; C='+ − ↑ 3 2 ↑ 2 3 / 6 − 4 2'; D='* + 3 + 3 ↑ 3 + 1 1 3'.",
    ["A,D,C,B", "A,C,D,B", "A,B,C,D", "C,A,D,B"], 2,
    ["Evaluate prefix expressions from the innermost/rightmost complete subexpressions.", "A=2(8/4)−3=1; B=(18−8)^5=100000; C=(9−8)+6/(4−2)=4; D=[3+(3+3^(1+1))]·3=45.", "Thus A<C<D<B."],
    source=SRC26, question_id="6119872216", secondary="Unit 7: Data Structures and Algorithms")
add(2026, "Dec 2025 Jan 2026", "59", 54, "Boolean Algebra", "Boolean identities",
    "Match: domination, associative, distributive and absorption laws with I x+1=1; II x+yz=(x+y)(x+z); III x+xy=x; IV x+(y+z)=(x+y)+z.",
    ["A-I,B-II,C-IV,D-III", "A-I,B-IV,C-II,D-III", "A-III,B-IV,C-II,D-I", "A-III,B-II,C-IV,D-I"], 2,
    ["Domination is I, associativity is IV, distributivity is II, and absorption is III.", "The resulting match is A-I, B-IV, C-II, D-III."],
    source=SRC26, question_id="6119872217")
add(2026, "Dec 2025 Jan 2026", "60", 55, "Optimization", "Integer, transportation and nonlinear programming",
    "Match methods to problem types: branch-and-bound; north-west corner; Lagrange multiplier; Wolfe's modified method versus integer; transportation; nonlinear; quadratic programming.",
    ["A-III,B-II,C-IV,D-I", "A-I,B-III,C-IV,D-II", "A-II,B-I,C-IV,D-III", "A-IV,B-I,C-II,D-III"], 2,
    ["Branch-and-bound is a standard integer-programming method; north-west corner constructs a transportation BFS.", "Lagrange multipliers handle constrained nonlinear optimization; Wolfe's modified simplex handles quadratic programming.", "Therefore A-I,B-III,C-IV,D-II."],
    source=SRC26, question_id="6119872218")

# June 2025: Unit 1 occupies Q51–Q55 before the architecture block begins.
SRC25 = "sources/ugc-net-cs-2025-june-combined-paper-1-and-2.pdf"
add(2025, "June 2025", "51", 43, "Counting, Mathematical Induction and Discrete Probability", "Inclusion-exclusion principle",
    "Among 120 people, 65 eat rice, 45 bread, 42 curd; 20 eat rice and bread, 25 rice and curd, 15 bread and curd, and 8 all three. How many eat at least one?",
    ["56", "100", "92", "65"], 2,
    ["Apply three-set inclusion–exclusion.", "65+45+42−20−25−15+8=100."], source=SRC25, question_id="4255894956")
add(2025, "June 2025", "52", 43, "Counting, Mathematical Induction and Discrete Probability", "Permutations",
    "From a pack of 42 cards, three are chosen one after another without replacement. In how many ways?",
    ["1722", "1752", "68880", "6880"], 3,
    ["The wording 'one after another' makes order significant.", "Use 42P3=42·41·40=68,880."], source=SRC25, question_id="4255894957")
add(2025, "June 2025", "53", 44, "Counting, Mathematical Induction and Discrete Probability", "Discrete probability and inclusion-exclusion",
    "A positive integer is selected uniformly from 1 through 200. What is the probability that it is divisible by 2 or 5?",
    ["2/5", "3/5", "4/5", "1/5"], 2,
    ["There are 100 multiples of 2, 40 multiples of 5 and 20 multiples of 10.", "Favourable count=100+40−20=120, so probability=120/200=3/5."], source=SRC25, question_id="4255894958")
add(2025, "June 2025", "54", 45, "Boolean Algebra", "Canonical sum-of-products",
    "For A(x,y,z)=x(y'z)', identify its complete sum-of-products form.",
    ["xyz+x'y'z'+x'y'z'", "xyz'+x'y'z+x'y'z'", "xyz'+xy'z+x'y'z'", "xyz+xyz'+xy'z'"], 4,
    ["De Morgan gives (y'z)'=y+z', so A=xy+xz'.", "Expand to minterms: xy(z+z')+xz'(y+y')=xyz+xyz'+xy'z'.", "Duplicate xyz' is retained once, giving option 4."], source=SRC25, question_id="4255894959")
add(2025, "June 2025", "55", 45, "Group Theory", "Abelian groups",
    "Choose the correct statement for a group G.",
    ["If (xy)²=x²y² for all x,y, then G is commutative.", "If x³=e for all x, then G is commutative.", "If x⁵=e for all x, then G is commutative.", "A subgroup of an abelian group need not be abelian."], 1,
    ["xyxy=xxyy. Left-cancel x and right-cancel y to obtain yx=xy.", "Groups of odd exponent can be nonabelian, so (2) and (3) are not general theorems.", "Every subgroup inherits the operation and therefore commutes when G does; (4) is false."], source=SRC25, question_id="4255894960")

# June and August 2024.  The June paper is explicitly labelled unofficial; its
# official option-ID key cannot be safely joined because the unofficial copy omits IDs.
SRC24J = "sources/ugc-net-cs-2024-june-unofficial-question-paper.pdf"
add(2024, "June 2024", "72", 4, "Mathematical Logic", "Nested quantifiers over integers",
    "Which have truth value true over all integers? A ∀n∃m(n²<m); B ∃n∀m(n<m²); C ∃n∃m(n²+m²=5); D ∃n∃m(n²+m²=6); E ∃n∃m(m+n=4 ∧ n−m=1).",
    ["A,B,C only", "B,C,E only", "C,D,E only", "B,D only"], 1,
    ["A is true with m=n²+1; B is true with n=−1; C is true with (1,2).", "No two integer squares sum to 6, so D is false.", "Solving E gives half-integers n=5/2,m=3/2, so E is false."], source=SRC24J, status="independently-verified; unofficial-paper")
add(2024, "June 2024", "84", 7, "Boolean Algebra", "Karnaugh-map simplification with don't-cares",
    "Simplify F(A,B,C)=Σ(0,2,6) using don't-cares d(A,B,C)=Σ(1,3,5).",
    ["A'C'+BC'", "B+AC", "A+BC'", "A'+BC'"], 4,
    ["Put 1 at minterms 0,2,6 and X at 1,3,5.", "Group 0,1,2,3 to obtain A'. Group 2 and 6 to obtain BC'.", "Hence F=A'+BC'."], source=SRC24J, status="independently-verified; unofficial-paper")
add(2024, "June 2024", "88", 7, "Graph Theory", "Spanning-tree enumeration",
    "Arrange K₃, K₄, K₂,₂ and C₅ in increasing order of their numbers of spanning trees.",
    ["K₃,K₄,K₂,₂,C₅", "K₃,K₂,₂,K₄,C₅", "K₃,K₂,₂,C₅,K₄", "C₅,K₄,K₂,₂,K₃"], 3,
    ["Cayley gives τ(K₃)=3 and τ(K₄)=16.", "τ(K₂,₂)=2^(2−1)2^(2−1)=4 and a cycle C₅ has 5 spanning trees.", "Thus 3<4<5<16."], source=SRC24J, status="independently-verified; unofficial-paper")
add(2024, "June 2024", "93", 8, "Counting, Mathematical Induction and Discrete Probability", "Conditional probability on bit strings",
    "A length-four bit string is uniformly random. Given that the first bit is 0, what is the probability that it contains at least three consecutive 0s?",
    ["1/2", "5/16", "5/8", "1/4"], 4,
    ["Conditioning on first bit 0 leaves 2³=8 equally likely strings.", "Only 0000 and 0001 contain 000; hence 2/8=1/4."], source=SRC24J, status="independently-verified; unofficial-paper")
add(2024, "June 2024", "96", 9, "Sets and Relations", "Cardinality of nested sets",
    "Arrange by increasing cardinality: A₁={{1,2},{3}}; A₂={{1},{2},{3},{4}}; A₃={{1,2,3,4,5,6}}; A₄={{1,2},{2,3,4},{5}}; A₅={{1},{2},{3},{4},{5}}.",
    ["A₁,A₂,A₄,A₅,A₃", "A₁,A₂,A₅,A₄,A₃", "A₁,A₃,A₄,A₂,A₅", "A₃,A₁,A₄,A₂,A₅"], 4,
    ["Count top-level elements, not the numbers inside them: |A₁|=2, |A₂|=4, |A₃|=1, |A₄|=3, |A₅|=5.", "Increasing order is A₃,A₁,A₄,A₂,A₅."], source=SRC24J, status="independently-verified; unofficial-paper")
add(2024, "June 2024", "99", 9, "Counting, Mathematical Induction and Discrete Probability", "Product rule",
    "Auditorium chairs are labelled by one letter followed by an integer from 01 through 99, starting A01. What is the maximum number of labels?",
    ["2600", "2574", "2340", "2366"], 2,
    ["There are 26 choices for the letter and 99 choices from 01 through 99.", "By the product rule, 26·99=2574."], source=SRC24J, status="independently-verified; unofficial-paper")

SRC24A = "sources/ugc-net-cs-2024-aug-combined-with-answers.pdf"
add(2024, "August 2024", "92", 59, "Boolean Algebra", "Karnaugh-map procedure",
    "Order the K-map steps: A group the largest clusters of 1s; B draw the K-map; C write the simplified expression; D transfer truth-table values.",
    ["B,D,A,C", "D,B,A,C", "B,A,D,C", "A,B,C,D"], 1,
    ["First draw the correctly labelled map, then transfer the values.", "Next make maximal power-of-two groups, and finally translate groups into implicants: B,D,A,C."], source=SRC24A, question_id="5330723767")
add(2024, "August 2024", "107", 69, "Counting, Mathematical Induction and Discrete Probability", "Binomial probability",
    "A fair coin is tossed three times. For the event 'exactly one head or exactly two heads', assess A n(S)=8,n(E)=4; B n(E)=6,n(S)=8; C P(E)=3/4; D P(E)=1/2.",
    ["A,B,C,D", "B,C only", "A,D only", "C,D only"], 2,
    ["The sample space has 8 outcomes.", "There are C(3,1)+C(3,2)=3+3=6 favourable outcomes, so P=6/8=3/4.", "Thus B and C alone are true."], source=SRC24A, question_id="5330723782")
add(2024, "August 2024", "124", 81, "Sets and Relations", "Reflexive relations",
    "On {1,2,3,4}, which listed relations are reflexive? R₁={(1,1),(1,2),(2,1),(2,2),(3,4),(4,1),(4,4)}; R₂={(1,1),(1,2),(2,1)}; R₃={(1,1),(1,2),(1,4),(2,1),(2,2),(3,3),(4,1),(4,4)}; R₄={(2,1),(3,1),(3,2),(4,1),(4,2),(4,3)}; R₅={(1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)}.",
    ["R₁,R₂,R₃", "R₁,R₄,R₅", "R₄,R₅", "R₃,R₅"], 4,
    ["Reflexivity requires all four diagonal pairs.", "R₃ and R₅ contain (1,1),(2,2),(3,3),(4,4). Each of R₁,R₂,R₄ misses at least one.", "Therefore R₃,R₅ only."], source=SRC24A, question_id="5330723799")
add(2024, "August 2024", "126", 82, "Counting, Mathematical Induction and Discrete Probability", "Hypergeometric probability",
    "Match: A same colour when drawing 2 from 6 white,4 red; B king or queen from 52 cards; C 1 red,2 white from 6R,4W,8B; D 2 blue,1 red from that bag, with I 3/68, II 14/68, III 2/13, IV 7/15.",
    ["A-II,B-IV,C-I,D-III", "A-III,B-IV,C-II,D-I", "A-IV,B-III,C-II,D-I", "A-IV,B-III,C-I,D-II"], 4,
    ["A=[C(6,2)+C(4,2)]/C(10,2)=21/45=7/15=IV; B=8/52=2/13=III.", "C=C(6,1)C(4,2)/C(18,3)=36/816=3/68=I.", "D=C(8,2)C(6,1)/C(18,3)=168/816=14/68=II."], source=SRC24A, question_id="5330723801")
add(2024, "August 2024", "127", 83, "Graph Theory", "Hamiltonian circuits",
    "For n≥3, Dirac's sufficient condition guarantees that G is Hamiltonian when every vertex has degree at least what?",
    ["n", "2n", "n/2", "4n"], 3,
    ["Dirac's theorem states δ(G)≥n/2 for a simple n-vertex graph with n≥3.", "This condition is sufficient, not necessary."], source=SRC24A, question_id="5330723802")
add(2024, "August 2024", "135", 90, "Graph Theory", "Shortest paths and spanning-tree algorithms",
    "Match Dijkstra, Floyd–Warshall, Bellman–Ford and Prim with the four descriptions printed in List II.",
    ["A-II,B-I,C-III,D-IV", "A-II,B-I,C-IV,D-III", "A-I,B-II,C-III,D-IV", "A-III,B-II,C-IV,D-I"], 2,
    ["The intended matches are Dijkstra→single-source nonnegative weights (II) and Floyd–Warshall→all-pairs paths (I).", "The paper's descriptions III and IV are corrupted/misprinted: bubble sort and strongly connected components do not describe Prim or Bellman–Ford.", "Option 2 is the only option preserving the two valid matches and is therefore the intended key, but the item is defective."], source=SRC24A, question_id="5330723810", status="disputed-source-defect", note="List-II items III and IV do not match either Bellman–Ford or Prim. Treat option 2 as intended, not as a technically valid full matching.", secondary="Unit 7: Data Structures and Algorithms")

# 2023 papers.
SRC23J = "sources/ugc-net-cs-2023-june-paper-2.pdf"
add(2023, "June 2023", "2", 3, "Sets and Relations", "Set operations and symmetric difference",
    "Match A A△B; B A−(B∪C); C A−(B∩C); D A∩(B−C) with I (A−B)∪(A−C); II (A−B)∩(A−C); III (A−B)∪(B−A); IV (A∩B)−(A∩C).",
    ["A-III,B-II,C-I,D-IV", "A-II,B-I,C-IV,D-III", "A-I,B-IV,C-II,D-III", "A-IV,B-III,C-I,D-II"], 1,
    ["Symmetric difference is III. De Morgan set laws give A−(B∪C)=(A−B)∩(A−C)=II and A−(B∩C)=(A−B)∪(A−C)=I.", "A∩(B−C)=(A∩B)−(A∩C)=IV."], source=SRC23J)
add(2023, "June 2023", "19", 13, "Sets and Relations", "Equivalence relations",
    "On N×N, (a,b)R(c,d) iff ad(b+c)=bc(a+d). What kind of relation is R?",
    ["Reflexive only", "Symmetric only", "Partial order", "Equivalence relation"], 4,
    ["Divide by abcd (positive): the condition becomes 1/a+1/b=1/c+1/d.", "Equality of the value f(a,b)=1/a+1/b is reflexive, symmetric and transitive.", "Therefore R is an equivalence relation."], source=SRC23J)
add(2023, "June 2023", "30", 18, "Group Theory", "Semigroups and monoids",
    "Assess: A a monoid identity is unique; B a monoid is a group if every element has an inverse; C a semigroup requires closure, associativity and identity; D a quasigroup is closed under its operation.",
    ["A,B only", "A,B,D only", "B,C,D only", "A,C only"], 2,
    ["A and B are defining theorems. C is false because identity is not required for a semigroup.", "A quasigroup is a set with a closed binary operation satisfying unique division, so D is true.", "Hence A,B,D."], source=SRC23J)
add(2023, "June 2023", "66", 36, "Optimization", "PERT-CPM terminology",
    "Match PERT, optimistic time, CPM and pessimistic time with non-repetitive projects, repetitive projects, shortest time and longest time.",
    ["A-I,B-II,C-III,D-IV", "A-II,B-IV,C-I,D-III", "A-IV,B-I,C-III,D-II", "A-I,B-III,C-II,D-IV"], 4,
    ["PERT is probabilistic and suited to non-repetitive projects; CPM is deterministic and commonly used for repetitive projects.", "Optimistic is the shortest plausible time and pessimistic the longest.", "Thus A-I,B-III,C-II,D-IV."], source=SRC23J)
add(2023, "June 2023", "70", 39, "Counting, Mathematical Induction and Discrete Probability", "Combinations and geometric counting",
    "There are m marked points on AB and n on AC, excluding A. How many triangles can be formed using these points together with A?",
    ["mn(m+n−1)/2", "mn(m+n−2)/2", "mn(m+n)/2", "mn"], 2,
    ["A non-collinear triple must use points from both rays.", "Choose two from AB and one from AC, or one from AB and two from AC: C(m,2)n+mC(n,2).", "This equals mn[(m−1)+(n−1)]/2=mn(m+n−2)/2."], source=SRC23J)
add(2023, "June 2023", "81", 44, "Counting, Mathematical Induction and Discrete Probability", "Poisson distribution",
    "Requests arrive at a mean rate 20 per hour. Under a Poisson model, what is the probability of no request during 45 minutes?",
    ["e^(−20)", "e^(−15)", "15e^(−15)", "1−e^(−15)"], 2,
    ["For 45 minutes the mean is λt=20·3/4=15.", "Poisson P(X=0)=e^(−15)15⁰/0!=e^(−15)."], source=SRC23J)
add(2023, "June 2023", "85", 46, "Group Theory", "Automorphisms of the integers",
    "How many automorphisms does the additive group (Z,+) have?",
    ["1", "2", "Countably infinite", "Uncountably infinite"], 2,
    ["A homomorphism is determined by f(1)=k and has f(n)=kn.", "It is bijective only for k=1 or k=−1.", "Hence there are two automorphisms."], source=SRC23J)

SRC23S1 = "sources/ugc-net-cs-2023-mar-15-shift-1-dec-2022-session-combined.pdf"
add(2023, "Dec 2022 Mar 15 Shift 1", "1", 40, "Mathematical Logic", "Propositional equivalence",
    "Which is not logically equivalent to P→Q?",
    ["¬P∨Q", "¬Q→¬P", "¬(P∧¬Q)", "¬Q→P"], 4,
    ["P→Q is ¬P∨Q and equals its contrapositive ¬Q→¬P.", "Negating the sole falsifying case gives ¬(P∧¬Q).", "¬Q→P is Q∨P, which differs; take P=false,Q=true."], source=SRC23S1)
add(2023, "Dec 2022 Mar 15 Shift 1", "2", 41, "Counting, Mathematical Induction and Discrete Probability", "Inclusion-exclusion and onto functions",
    "Seven distinct people leave a lift at three ordered stops, with at least one person at every stop. How many assignments are possible?",
    ["2187", "1932", "1806", "1260"], 3,
    ["Count onto functions from 7 people to 3 stops.", "3⁷−C(3,1)2⁷+C(3,2)1⁷=2187−384+3=1806."], source=SRC23S1)
add(2023, "Dec 2022 Mar 15 Shift 1", "4", 41, "Counting, Mathematical Induction and Discrete Probability", "Pigeonhole principle",
    "Students receive one of seven grades. What minimum class size guarantees at least six students with the same grade?",
    ["35", "42", "36", "43"], 3,
    ["To avoid six in any grade, place at most five in each of seven boxes: 7·5=35.", "One more student forces a box to contain six, so the minimum is 36."], source=SRC23S1)
add(2023, "Dec 2022 Mar 15 Shift 1", "6", 42, "Boolean Algebra", "Karnaugh-map simplification",
    "Simplify F(A,B,C,D)=Σ(3,4,5,6,7,11,15).",
    ["AB+C'D", "A'B+CD", "AC+BD", "A'B+B'C"], 2,
    ["Minterms 4,5,6,7 form the implicant A'B.", "Minterms 3,7,11,15 form CD.", "Together they cover exactly the specified set, so F=A'B+CD."], source=SRC23S1)
add(2023, "Dec 2022 Mar 15 Shift 1", "41", 53, "Group Theory", "Group properties",
    "Which group statements are correct? A every group has a zero element; B the only idempotent is identity; C an isomorphism G→G is an automorphism; D if every element is self-inverse then G is abelian.",
    ["B,C,D only", "A,B,C", "A,C,D", "B,D only"], 1,
    ["A is false: groups require an identity, not a separate zero.", "If x²=x, cancellation gives x=e, so B is true; C is the definition of automorphism.", "If x=x⁻¹, then xy=(xy)⁻¹=y⁻¹x⁻¹=yx, so D is true."], source=SRC23S1)
add(2023, "Dec 2022 Mar 15 Shift 1", "43", 54, "Sets and Relations", "Relation properties",
    "For R={(1,3),(1,1),(3,1),(1,2),(3,3),(4,4)} on {1,2,3,4}, which classification is correct?",
    ["Reflexive and symmetric", "Symmetric and transitive", "Reflexive only", "Neither reflexive, symmetric nor transitive"], 4,
    ["(2,2) is absent, so R is not reflexive. (1,2) is present but (2,1) absent, so not symmetric.", "(3,1) and (1,2) occur but (3,2) does not, so it is not transitive."], source=SRC23S1)
add(2023, "Dec 2022 Mar 15 Shift 1", "66", 66, "Optimization", "Method classification",
    "Match linear programming, predicate logic, tree traversal and minimum spanning tree with Simplex, first-order logic, inorder and Prim.",
    ["A-I,B-II,C-III,D-IV", "A-III,B-IV,C-II,D-I", "A-IV,B-III,C-I,D-II", "A-II,B-I,C-IV,D-III"], 2,
    ["LP→Simplex (III), predicate logic→first-order logic (IV), traversal→inorder (II), MST→Prim (I).", "This gives A-III,B-IV,C-II,D-I."], source=SRC23S1, secondary="Unit 7: Data Structures and Algorithms")

SRC23S2 = "sources/ugc-net-cs-2023-mar-11-shift-2-dec-2022-session-combined.pdf"
add(2023, "Dec 2022 Mar 11 Shift 2", "1", 32, "Mathematical Logic", "Negating quantified statements",
    "What is the negation of 'Some students like hockey'?",
    ["Some students dislike hockey", "Every student dislikes hockey", "No student dislikes hockey", "Every student likes hockey"], 2,
    ["The statement is ∃x(Student(x)∧LikesHockey(x)).", "Its negation is ∀x(Student(x)→¬LikesHockey(x)): every student does not like hockey."], source=SRC23S2)
add(2023, "Dec 2022 Mar 11 Shift 2", "2", 32, "Sets and Relations", "Strict partial orders",
    "On integer pairs define (x,y)R(u,v) iff x<u and y>v. Which classification applies under the paper's reflexive definition of partial order?",
    ["Neither partial order nor equivalence relation", "Partial but not total order", "Total order", "Equivalence relation"], 1,
    ["R is irreflexive because x<x is false; hence it is not a (reflexive) partial order and not an equivalence relation.", "It is a strict partial order in terminology that uses irreflexive+transitive; the options use the non-strict convention."], source=SRC23S2, note="Terminology-sensitive: R is a strict partial order, but not a reflexive partial order.")
add(2023, "Dec 2022 Mar 11 Shift 2", "4", 33, "Mathematical Logic", "Boolean conditions",
    "A nested conditional returns true for (x>25,y>100), false; (x≤25,y≤100), true; (x>25,y≤100), false; otherwise true. When is the overall result true?",
    ["iff y≤100", "iff x≤25", "iff x>25", "iff y>100"], 2,
    ["The four branches partition all possibilities.", "Both branches with x>25 are false and both with x≤25 are true, independent of y.", "Therefore the result is true iff x≤25."], source=SRC23S2)
add(2023, "Dec 2022 Mar 11 Shift 2", "7", 34, "Boolean Algebra", "Karnaugh-map simplification",
    "Simplify F=Σ(0,2,5,7,8,10,13,15).",
    ["BD+B'D'", "B'D+BD'", "A'C'+AC", "C'D+CD'"], 1,
    ["The minterms are precisely those for which B and D are equal; A and C vary freely.", "Thus F=BD+B'D', the XNOR of B and D."], source=SRC23S2)
add(2023, "Dec 2022 Mar 11 Shift 2", "42", 44, "Boolean Algebra", "Structure of Boolean algebras",
    "Assess: A a Boolean algebra can have five elements; B complements are unique; C a Boolean-algebra lattice is not relatively complemented; D a product of Boolean algebras is Boolean.",
    ["A,C", "B,D", "A,B,D", "B,C,D"], 2,
    ["Finite Boolean algebras have 2^n elements, so A is false. Complements are unique, so B true.", "Boolean algebras are complemented (indeed relatively complemented), so C false; products preserve Boolean operations, so D true."], source=SRC23S2)
add(2023, "Dec 2022 Mar 11 Shift 2", "66", 54, "Optimization", "PERT-CPM and graph colouring",
    "Match planar graph, bipartite graph, PERT and CPM with 4-colourable, 2-colourable, probabilistic and deterministic.",
    ["A-I,B-II,C-III,D-IV", "A-II,B-III,C-IV,D-I", "A-IV,B-I,C-II,D-III", "A-III,B-IV,C-I,D-II"], 4,
    ["Every planar graph is 4-colourable; a bipartite graph is 2-colourable.", "PERT is probabilistic and CPM deterministic.", "So A-III,B-IV,C-I,D-II."], source=SRC23S2)

SRC22 = "sources/ugc-net-cs-2022-oct-with-answers.pdf"
add(2022, "October 2022", "2", 1, "Counting, Mathematical Induction and Discrete Probability", "Bayes theorem",
    "Three equiprobable boxes contain respectively (2W,3B,4R), (3W,2B,2R), and (4W,1B,3R). Given that two drawn balls are one white and one red, what is the probability that box 1 was chosen?",
    ["0.237", "0.723", "0.18", "0.452"], 1,
    ["Likelihoods of WR are 8/C(9,2)=2/9, 6/C(7,2)=2/7 and 12/C(8,2)=3/7.", "Equal box priors cancel in Bayes' ratio.", "Posterior=(2/9)/(2/9+2/7+3/7)=14/59≈0.2373."], source=SRC22, question_id="317")
add(2022, "October 2022", "10", 4, "Optimization", "Duality in linear programming",
    "For the printed equality-constrained maximization problem and proposed dual, which statement about the dual formulation is correct?",
    ["Dual objective and constraints are correct", "Only objective is correct", "Only constraints are correct", "Neither is correct"], 1,
    ["Equality constraints in a primal make the corresponding dual variables unrestricted in sign.", "A maximization primal with nonnegative variables yields ≥ constraints in the dual when written with equality rows and unrestricted dual variables.", "Using Aᵀy≥c and bᵀy gives the printed dual."], source=SRC22, question_id="325", note="The source's OCR drops some subscripts; use PDF page 4 for the complete displayed primal/dual.")
add(2022, "October 2022", "64", 21, "Sets and Relations", "Approximate-equality relation",
    "For ε=0.0005, define x Rε y iff |x−y|<ε. Which properties hold: A reflexive, B symmetric, C transitive?",
    ["A,B only", "B,C only", "A,C only", "A,B,C"], 1,
    ["|x−x|=0<ε, so reflexive. Absolute distance is symmetric.", "Transitivity fails: choose x=0,y=0.0004,z=0.0008. The first two gaps are <ε but |x−z| is not.", "Thus A and B only."], source=SRC22, question_id="379")
add(2022, "October 2022", "83", 29, "Boolean Algebra", "Distributive identities",
    "Assess X: a∨[b∧(a∨c)]=(a∨b)∧(a∨c); Y: a∨(b∧c)=(a∨b)∧c.",
    ["X only", "Y only", "Both X and Y", "Neither/dependent"], 1,
    ["For X, absorption gives the left side a∨bc and distributivity gives the same right side.", "Y is false; a=1,c=0 makes its left side 1 and right side 0.", "Hence X only."], source=SRC22, question_id="398")
add(2022, "October 2022", "89", 31, "Mathematical Logic", "First-order predicate representation",
    "Statement I: a grandparent is a parent of one's parent. Statement II: ∀g∀c[grandparent(g,c)→∃p(parent(g,p)∧parent(p,c))]. Assess them.",
    ["Both correct", "Both incorrect", "I correct, II incorrect", "I incorrect, II correct"], 1,
    ["Statement I gives the usual defining condition.", "Statement II correctly says that whenever g is c's grandparent, an intermediate parent p exists.", "Both statements are correct (though a biconditional would be needed for a complete definition)."], source=SRC22, question_id="404", secondary="Unit 10: Artificial Intelligence")

SRC21 = "sources/ugc-net-cs-2021-nov-with-answers.pdf"
add(2021, "November 2021", "21", 2, "Mathematical Logic", "Logical equivalence",
    "Which pairs are logically equivalent? A. ¬p→(q→r) and q→(p∨r). B. (p→q)→r and p→(q→r). C. (p→q)→(r→s) and (p→r)→(q→s).",
    ["A only", "A and B only", "B and C only", "A and C only"], 1,
    ["¬p→(q→r) simplifies to p∨¬q∨r. The other formula in A, q→(p∨r), simplifies to the same expression, so A is equivalent.",
     "In B, (p→q)→r becomes (p∧¬q)∨r, whereas p→(q→r) becomes ¬p∨¬q∨r. Taking p=false and r=false separates them, so B is not equivalent.",
     "C is not an equivalence; for example p=false, q=true, r=true, s=false makes the left formula false and the right formula true. Therefore only A holds."],
    source=SRC21, question_id="2351", status="official-final-key-matched", official="NTA final key: Question ID 2351, option 1",
    note="The stem and formulas were recovered by visual inspection of PDF page 2 because the broad text index retained only the choices.")
add(2021, "November 2021", "22", 2, "Sets and Relations", "Floor and ceiling functions",
    "Which statements are correct? I. ⌊2x⌋=⌊x⌋+⌊x+1/2⌋ for every real x. II. ⌊x+y⌋=⌊x⌋+⌊y⌋ for every real x and y.",
    ["Both I and II are true", "Both I and II are false", "I is true but II is false", "I is false but II is true"], 3,
    ["Write x=n+f with n=⌊x⌋ and 0≤f<1. Then ⌊2x⌋=2n+⌊2f⌋ and ⌊x⌋+⌊x+1/2⌋=2n+⌊f+1/2⌋. Both added floors are 0 for f<1/2 and 1 for f≥1/2, so I is true.",
     "II is not an identity because fractional parts can carry into the next integer. With x=y=0.6, ⌊x+y⌋=1 but ⌊x⌋+⌊y⌋=0.",
     "Thus Statement I is true and Statement II is false, giving option 3."],
    source=SRC21, question_id="2352", status="official-final-key-matched", official="NTA final key: Question ID 2352, option 3",
    note="The embedded answer overlay says both statements are true, but the final NTA key and the counterexample establish option 3.")
add(2021, "November 2021", "23", 2, "Counting, Mathematical Induction and Discrete Probability", "Onto assignments",
    "How many ways are there to assign five different jobs to four different employees if every employee receives at least one job?",
    ["1024", "625", "240", "20"], 3,
    ["Because five distinct jobs go to four employees and none may be empty, exactly one employee must receive two jobs and each other employee one.",
     "Choose the employee receiving two jobs in 4 ways, choose that employee's two jobs in C(5,2)=10 ways, and biject the remaining three jobs to the remaining three employees in 3!=6 ways.",
     "The product is 4·10·6=240. Equivalently, inclusion-exclusion gives 4^5-4·3^5+6·2^5-4=240."],
    source=SRC21, question_id="2353", status="official-final-key-matched", official="NTA final key: Question ID 2353, option 3",
    note="The embedded answer overlay marks 1024, which counts all functions and ignores the nonempty-employee condition; the final key corrects it to 240.")
add(2021, "November 2021", "24", 2, "Counting, Mathematical Induction and Discrete Probability", "Pigeonhole principle",
    "A warehouse has 50 aisles, 85 horizontal locations per aisle, and 5 shelves. What is the least number of products that guarantees two products in the same bin?",
    ["251", "426", "4251", "21251"], 4,
    ["A bin is identified by one choice from each coordinate, so the number of bins is 50·85·5=21,250.",
     "With 21,250 products it is still possible to put one product in every bin, so a collision is not yet forced.",
     "The next product must reuse a bin by the pigeonhole principle. Hence the least guaranteed number is 21,250+1=21,251."],
    source=SRC21, question_id="2354", status="official-final-key-matched", official="NTA final key: Question ID 2354, option 4",
    note="The source OCR says 'self'; visual inspection shows the intended warehouse coordinate is shelf. The embedded answer overlay is superseded by the final key.")
add(2021, "November 2021", "25", 2, "Counting, Mathematical Induction and Discrete Probability", "Recurrence relations",
    "A person may climb either one stair or two stairs at a time. In how many ways can the person climb eight stairs?",
    ["21", "24", "31", "34"], 4,
    ["Let a_n be the number of ways to reach stair n. The last move is either one stair after a_{n-1} or two stairs after a_{n-2}, so a_n=a_{n-1}+a_{n-2}.",
     "Use a_0=1 (the empty sequence) and a_1=1. The values are a_2=2, a_3=3, a_4=5, a_5=8, a_6=13, a_7=21 and a_8=34.",
     "Therefore eight stairs can be climbed in 34 ways, option 4. The distractor 21 is the count for seven stairs."],
    source=SRC21, question_id="2355", status="official-final-key-matched", official="NTA final key: Question ID 2355, option 4",
    note="The embedded answer overlay marks 21, but the final NTA key and the recurrence both give 34.")
add(2021, "November 2021", "26", 2, "Graph Theory", "Regular and wheel graphs",
    "For which value of n is the wheel graph W_n regular?",
    ["2", "3", "4", "5"], 2,
    ["Under the convention W_n=K_1+C_n, every rim vertex has degree 3 and the hub has degree n. Equality of all degrees requires n=3, so option 2 is correct under this convention.",
     "Another common convention uses W_n for a wheel of total order n, namely K_1+C_{n-1}. Then the hub has degree n-1, and regularity requires n-1=3, giving n=4 (option 3). In either notation the graph is K_4.",
     "The NTA final key accepts both options 2 and 3 because both wheel-indexing conventions are standard; the mathematical invariant is that the unique regular wheel is K_4."],
    source=SRC21, question_id="2356", status="official-final-key-multiple-options", official="NTA final key: Question ID 2356, options 2 and 3 accepted",
    note="Option 2 is stored as the primary answer because the stem's W_n notation often means K_1+C_n; option 3 is equally accepted under the order-n convention.")
RECORDS[-1]["correctAnswer"] = "n=3 (option 2) or n=4 (option 3), depending on the wheel-indexing convention"
RECORDS[-1]["optionAnalysis"] = [
    {"number": 1, "verdict": "incorrect", "explanation": "A cycle C_2 is not a simple cycle in the standard wheel definition."},
    {"number": 2, "verdict": "accepted", "explanation": "For W_n=K_1+C_n, n=3 makes both the hub and rim degrees equal to 3, producing K_4."},
    {"number": 3, "verdict": "accepted", "explanation": "For the convention where W_n has n total vertices, W_4=K_1+C_3=K_4, which is 3-regular."},
    {"number": 4, "verdict": "incorrect", "explanation": "Under either convention this wheel has a hub degree larger than the rim degree 3."},
]
add(2021, "November 2021", "27", 2, "Graph Theory", "Planarity and graph redrawings",
    "The source shows three graphs A, B and C. Which are planar? Graph A is a six-vertex crossing drawing with outer triangle a-d-f and vertices b,c,e subdividing its sides; graph B is the six-vertex octahedral graph; graph C contains a subdivision of K3,3.",
    ["A and B only", "B and C only", "A only", "B only"], 1,
    ["A's displayed edge crossing is not a vertex and does not prove nonplanarity. Moving one of the two crossing chords outside the outer triangle gives an embedding without crossings, so A is planar.",
     "B is the octahedral graph, isomorphic to K_{2,2,2}. It is the edge graph of a convex octahedron and therefore has a planar embedding, even though the supplied straight-line drawing has crossings.",
     "In C, suppressing the degree-2 subdivision vertices exposes a K3,3 subdivision. Kuratowski's theorem therefore makes C nonplanar. Exactly A and B are planar, so option 1 is correct."],
    source=SRC21, question_id="2357", status="official-final-key-matched", official="NTA final key: Question ID 2357, option 1",
    note="The three drawings were visually inspected at high resolution. The learning point is that crossings in a particular drawing do not by themselves establish nonplanarity.")
add(2021, "November 2021", "28", 3, "Boolean Algebra", "Boolean identities",
    "Match A x+x=x; B x+0=x; C x+1=1; D x+xy=x with idempotent, identity, domination and absorption laws.",
    ["A-III,B-I,C-II,D-IV", "A-I,B-II,C-III,D-IV", "A-III,B-I,C-IV,D-II", "A-II,B-IV,C-I,D-III"], 3,
    ["x+x=x is idempotent (III); x+0=x is identity (I).", "x+1=1 is domination (IV); x+xy=x is absorption (II).", "Therefore option 3 is mathematically correct."], source=SRC21, status="official-final-key-matched", official="NTA final key: Question ID 2358, option 3", note="The embedded answer overlay marks option 1, but the NTA final key agrees with the independent Boolean-algebra derivation: option 3.", question_id="2358")
add(2021, "November 2021", "29", 3, "Group Theory", "Semigroups and rectangular bands",
    "Let (X,*) be a semigroup in which a≠b implies a*b≠b*a. Which identities hold? A. a*a=a. B. (a*b)*a=a. C. (a*b)*c=a*c.",
    ["A and B only", "A and C only", "B and C only", "A, B and C"], 4,
    ["First prove idempotence. If a*a differed from a, the hypothesis would require (a*a)*a≠a*(a*a), but associativity makes these expressions equal. Hence a*a=a, proving A.",
     "Let x=a*b. Idempotence gives a*x=a*(a*b)=(a*a)*b=x. Now a and x*a commute: a*(x*a)=(a*x)*a=x*a, while (x*a)*a=x*(a*a)=x*a. The hypothesis forces a=x*a=(a*b)*a, proving B.",
     "To prove C, set x=(a*b)*c and y=a*c. Using B twice, x*y=a*b*(c*a*c)=a*b*c=x and y*x=(a*c*a)*b*c=a*b*c=x. Thus x and y commute; the hypothesis forces x=y, so (a*b)*c=a*c. All three identities hold and option 4 is correct."],
    source=SRC21, question_id="2359", status="official-final-key-matched", official="NTA final key: Question ID 2359, option 4",
    note="Here 'anti-commutative' means distinct elements never commute; it is not the ring identity ab=-ba.")
add(2021, "November 2021", "30", 3, "Optimization", "Graphical solution of a linear program",
    "Maximize 6x+5y subject to 2x−3y≤5, x+3y≤11, 4x+y≤15, x,y≥0. Find the optimum value.",
    ["15", "25", "349/11", "30"], 3,
    ["The binding intersection x+3y=11 and 4x+y=15 gives x=34/11,y=29/11.", "It satisfies 2x−3y≤5.", "Objective=6(34/11)+5(29/11)=349/11≈31.73, larger than the other feasible vertices."], source=SRC21, status="official-final-key-matched", official="NTA final key: Question ID 2360, option 3", note="The embedded answer overlay marks 15, but the NTA final key agrees with direct optimization: 349/11.", question_id="2360")

SRC20 = "sources/ugc-net-cs-2020-nov-combined-with-answers.pdf"
add(2020, "November 2020", "51", 62, "Counting, Mathematical Induction and Discrete Probability", "Inclusion-exclusion",
    "How many positive integers not exceeding 100 are either odd or perfect squares?",
    ["63", "59", "55", "50"], 3,
    ["There are 50 odd numbers and 10 squares 1² through 10².", "Five squares are odd: 1,9,25,49,81.", "Union size=50+10−5=55."], source=SRC20, question_id="5362284288")
add(2020, "November 2020", "52", 63, "Counting, Mathematical Induction and Discrete Probability", "Integer partitions",
    "In how many ways can six identical books be packed into four identical boxes, with empty boxes allowed?",
    ["4", "6", "7", "9"], 4,
    ["Identical boxes mean unordered partitions of 6 into at most four positive parts.", "The partitions are 6; 5+1; 4+2; 4+1+1; 3+3; 3+2+1; 3+1+1+1; 2+2+2; 2+2+1+1.", "There are 9."], source=SRC20, question_id="5362284289")
add(2020, "November 2020", "53", 63, "Mathematical Logic", "Propositional equivalence",
    "Which pair is not logically equivalent?",
    ["[(p→r)∧(q→r)] and [(p∨q)→r]", "p→q and ¬q→¬p", "[(p∧q)∨(¬p∧¬q)] and p↔q", "[(p∧q)→r] and [(p→r)∧(q→r)]"], 4,
    ["Options 1–3 are respectively implication distribution, contraposition and the standard biconditional expansion.", "For option 4 take p=true,q=false,r=false: (p∧q)→r is true, but (p→r)∧(q→r) is false.", "Therefore pair 4 is not equivalent."], source=SRC20, question_id="5362284290")
add(2020, "November 2020", "54", 64, "Optimization", "Graphical linear programming",
    "Maximize z=2x₁+3x₂ subject to 2x₁+x₂≤4, x₁+2x₂≤5, x₁,x₂≥0. Find the optimum.",
    ["23", "9.5", "18", "8"], 4,
    ["The constraint intersection is x₁=1,x₂=2.", "Its objective is 2+6=8; axis vertices give at most 7.5 and 4.", "Thus the optimum is 8."], source=SRC20, question_id="5362284291")
add(2020, "November 2020", "88", 92, "Mathematical Logic", "Conjunctive normal form",
    "What kind of clauses occur in conjunctive normal form?",
    ["Disjunctions of literals", "Disjunctions of variables", "Conjunctions of literals", "Conjunctions of variables"], 1,
    ["A literal is a variable or its negation.", "CNF is a conjunction of clauses, and each clause is a disjunction of literals."], source=SRC20, question_id="5362284325")
add(2020, "November 2020", "89", 93, "Sets and Relations", "Reflexive, symmetric and antisymmetric properties",
    "On {a,b,c,d,e,f,g}, R={(a,a),(b,b),(c,d),(c,g),(d,g),(e,e),(f,f),(g,g)}. Which listed properties hold: A reflexive, B antisymmetric, C symmetric?",
    ["A only", "C only", "A and B", "B and not A"], 4,
    ["(c,c) and (d,d) are absent, so not reflexive.", "No distinct pair appears in both directions, hence antisymmetric.", "(c,d) lacks (d,c), so not symmetric. Thus B and not A."], source=SRC20, question_id="5362284326")
add(2020, "November 2020", "90", 94, "Mathematical Logic", "Rules of inference",
    "A purported proof derives P(c) and Q(c) separately from P(c)∨Q(c), then generalizes. Which step is invalid?",
    ["Proof is valid", "Steps deriving P(c) and Q(c) by simplification", "Only universal-generalization steps", "Only final conjunction"], 2,
    ["Simplification applies to a conjunction, not a disjunction.", "From P(c)∨Q(c) neither disjunct follows by itself, so both claimed simplification steps are invalid.", "All later steps rest on those invalid inferences."], source=SRC20, question_id="5362284327")
add(2020, "November 2020", "103", 107, "Graph Theory", "Graph colouring",
    "Which of A–E are incorrect? A every tree is 2-colourable; B a bipartite graph has no even cycle; C G is 2-colourable iff bipartite; D maximum degree d permits d+1 colours; E O(|V|) edges imply O(log|V|) colours.",
    ["C,E", "B,C", "B,E", "A,D"], 3,
    ["A,C,D are standard true bounds/characterizations.", "B is false: bipartite graphs exclude odd cycles, not even cycles.", "E is false; a clique on Θ(√V) vertices plus isolated vertices has O(V) edges but needs Θ(√V) colours. Hence B,E."], source=SRC20, question_id="5362284340")

SRC19D = "sources/ugc-net-cs-2019-dec-combined-paper-1-and-2.pdf"
add(2019, "December 2019", "51", 42, "Optimization", "Transportation basic feasible solutions",
    "A non-degenerate basic feasible solution of an m×n transportation problem contains exactly how many allocations, in what kind of positions?",
    ["m+n+1, independent", "m+n−1, independent", "m+n−1, appropriate", "m−n+1, independent"], 2,
    ["The transportation constraint matrix has rank m+n−1 for a balanced problem.", "A non-degenerate BFS therefore has exactly m+n−1 positive basic allocations, and their cells must be independent (contain no closed loop)."], source=SRC19D, question_id="61547510491")
add(2019, "December 2019", "52", 43, "Optimization", "Graphical linear programming",
    "Maximize z=x₁+x₂ subject to x₁+2x₂≤2000, x₁+x₂≤1500, x₂≤600 and x₁,x₂≥0. Which listed solution is feasible and optimal?",
    ["x₁=750,x₂=750,z=1500", "x₁=500,x₂=1000,z=1500", "x₁=1000,x₂=500,z=1500", "x₁=900,x₂=600,z=1500"], 3,
    ["The objective cannot exceed 1500 because x₁+x₂≤1500.", "Option 3 attains 1500 and satisfies 1000+2(500)=2000 and x₂≤600.", "Each other listed point violates either x₂≤600 or the first constraint."], source=SRC19D, question_id="61547510492")
add(2019, "December 2019", "53", 44, "Boolean Algebra", "Variable dependence",
    "The expression AB+A'B+AC+A'C is unaffected by which variable?",
    ["A", "B", "C", "A,B,C"], 1,
    ["Factor B(A+A')+C(A+A').", "Since A+A'=1, the expression is B+C.", "A disappears, so changing A has no effect."], source=SRC19D, question_id="61547510493")
add(2019, "December 2019", "54", 45, "Sets and Relations", "Bounds in a divisibility poset",
    "Find GLB and LUB under divisibility for A={3,9,12} and B={1,2,4,5,10}.",
    ["A:3,36; B:1,20", "A:3,12; B:1,10", "A:1,36; B:2,20", "A:1,12; B:2,10"], 1,
    ["In the positive-integer divisibility poset, GLB is gcd and LUB is lcm.", "gcd(A)=3,lcm(A)=36; gcd(B)=1,lcm(B)=20."], source=SRC19D, question_id="61547510494")
add(2019, "December 2019", "55", 45, "Sets and Relations", "Properties of relations",
    "On all people, aRb iff a is a brother of b. Is R symmetric, transitive, an equivalence relation, or a partial order?",
    ["No,No,No,No", "No,No,Yes,No", "No,Yes,No,No", "No,Yes,Yes,No"], 1,
    ["If a male is brother of a female b, b is not a brother of a; thus not symmetric.", "Sibling relations are not transitive: two people may each be siblings of b without being siblings of one another (e.g. blended families).", "It is neither reflexive/equivalence nor a partial order."], source=SRC19D, question_id="61547510495")
add(2019, "December 2019", "57", 48, "Graph Theory", "Trees and degree sum",
    "A tree has 2n vertices of degree 1, 3n of degree 2 and n of degree 3. Find its numbers of vertices and edges.",
    ["12,11", "11,12", "10,11", "9,10"], 1,
    ["V=6n and E=6n−1. The degree sum is 2n+6n+3n=11n.", "Set 11n=2E=12n−2, giving n=2.", "Hence V=12,E=11."], source=SRC19D, question_id="61547510497")
add(2019, "December 2019", "58", 48, "Sets and Relations", "Counting reflexive relations",
    "How many reflexive relations exist on a four-element set?",
    ["2¹²", "2²", "4²", "2"], 1,
    ["All four diagonal pairs are forced.", "The remaining 16−4=12 ordered pairs may each be included or excluded independently.", "Count=2¹²."], source=SRC19D, question_id="61547510498")
add(2019, "December 2019", "84", 71, "Optimization", "Critical path method",
    "An ___ chart represents a project as a directed graph. The critical path is the ___ sequence of ___ tasks and defines project ___.",
    ["Activity,shortest,independent,cost", "Activity,longest,dependent,duration", "Activity,longest,independent,duration", "Activity,shortest,dependent,duration"], 2,
    ["An activity network is directed by precedence dependencies.", "The critical path is the longest-duration sequence of dependent activities, and its length is the project duration."], source=SRC19D, question_id="61547510524")
add(2019, "December 2019", "86", 72, "Graph Theory", "Cliques",
    "A clique in an undirected graph is a vertex subset V' such that:",
    ["Every graph edge has both ends in V'", "Every loop has an end in V'", "Each pair of vertices in V' is joined by an edge", "No pair in V' is joined"], 3,
    ["The induced subgraph on a clique is complete.", "Equivalently, every two distinct vertices selected in V' are adjacent."], source=SRC19D, question_id="61547510526")
add(2019, "December 2019", "109", 90, "Mathematical Logic", "Quantifiers and distribution",
    "S1 says (∀xP(x))∨(∀xQ(x)) and ∀x(P(x)∨Q(x)) are not equivalent. S2 says (∃xP(x))∧(∃xQ(x)) and ∃x(P(x)∧Q(x)) are not equivalent. Which are correct?",
    ["S1 only", "S2 only", "Both", "Neither"], 3,
    ["For S1, different objects may satisfy P and Q, making the second formula true while neither universal disjunct is true.", "For S2, the two existential witnesses may differ, so the first can be true while no object satisfies both.", "Both non-equivalence statements are correct."], source=SRC19D, question_id="61547510549")

SRC19J = "sources/ugc-net-cs-2019-june-combined-paper-1-and-2.pdf"
add(2019, "June 2019", "51", 43, "Sets and Relations", "Partial orders under divisibility",
    "For the poset ({3,5,9,15,24,45}, divides), which extremal elements exist?",
    ["Both greatest and least", "Greatest but no least", "Least but no greatest", "Neither greatest nor least"], 4,
    ["A least element would have to divide every member; none of the listed elements divides both 3 and 5.", "A greatest element must be divisible by every member; none is divisible by both 24 and 45.", "Therefore neither exists."], source=SRC19J, question_id="64635021792")
add(2019, "June 2019", "53", 44, "Counting, Mathematical Induction and Discrete Probability", "Inclusion-exclusion on bit strings",
    "How many length-ten bit strings start with 1 or end with 00?",
    ["320", "480", "640", "768"], 3,
    ["Start with 1:2⁹. End with 00:2⁸. Both:2⁷.", "Inclusion–exclusion gives 512+256−128=640."], source=SRC19J, question_id="64635021794")
add(2019, "June 2019", "54", 45, "Graph Theory", "Euler formula for planar graphs",
    "A connected planar graph has six vertices, each degree four. Into how many regions does a planar embedding divide the plane?",
    ["6", "8", "12", "20"], 2,
    ["Degree sum=6·4=24=2E, so E=12.", "Euler gives F=2−V+E=2−6+12=8."], source=SRC19J, question_id="64635021795")
add(2019, "June 2019", "55", 46, "Graph Theory", "Hamiltonian cycles in complete bipartite graphs",
    "For what m,n does Kₘ,ₙ have a Hamilton circuit?",
    ["m≠n and both≥2", "m≠n and both≥3", "m=n and both≥2", "m=n and both≥3"], 3,
    ["A cycle in a bipartite graph alternates between the two parts, so a Hamilton cycle requires equal part sizes.", "With m=n≥2, alternating through all vertices constructs such a cycle."], source=SRC19J, question_id="64635021796")
add(2019, "June 2019", "57", 48, "Counting, Mathematical Induction and Discrete Probability", "Pigeonhole principle",
    "How many cards must be selected from a 52-card deck to guarantee at least three hearts?",
    ["9", "13", "17", "42"], 4,
    ["Worst case first select all 39 non-hearts and then two hearts: 41 cards without three hearts.", "The 42nd card guarantees a third heart."], source=SRC19J, question_id="64635021798")

SRC18D = "sources/ugc-net-cs-2018-dec-combined-paper-1-and-2.pdf"
add(2018, "December 2018", "51", 45, "Mathematical Logic", "Statements and propositions",
    "Which are mathematical statements? I There will be snow in January; II What is the time now?; III Today is Sunday; IV You must study Discrete Mathematics.",
    ["I and III", "I and II", "II and IV", "III and IV"], 1,
    ["A statement is a declarative sentence that has a truth value.", "I and III are declarative and can be true or false. II is a question and IV an imperative, so neither is a statement."], source=SRC18D, question_id="91394310745")
add(2018, "December 2018", "53", 47, "Counting, Mathematical Induction and Discrete Probability", "Hypergeometric probability",
    "A box has six red and four green balls. Four are selected. What is the probability of exactly two red and two green?",
    ["1/14", "3/7", "1/35", "1/7"], 2,
    ["Favourable selections=C(6,2)C(4,2)=15·6=90.", "All selections=C(10,4)=210.", "Probability=90/210=3/7."], source=SRC18D, question_id="91394310747")
add(2018, "December 2018", "54", 48, "Counting, Mathematical Induction and Discrete Probability", "Three-set inclusion-exclusion",
    "Survey counts are Bus 30, Train 35, Automobile 100, Bus∩Train 15, Bus∩Auto 15, Train∩Auto 20 and all three 5. How many respondents?",
    ["120", "165", "160", "115"], 1,
    ["Use |B∪T∪A|=sum singles−sum pairs+triple.", "30+35+100−15−15−20+5=120."], source=SRC18D, question_id="91394310748")
add(2018, "December 2018", "55", 49, "Boolean Algebra", "Boolean networks and finite Boolean algebras",
    "Which are true? I every logic network can use only NAND or only NOR; II Boolean expressions/networks correspond to labelled acyclic digraphs; III no two Boolean algebras with n atoms are isomorphic; IV nonzero finite-Boolean-algebra elements are not uniquely joins of atoms.",
    ["I,IV", "I,II,III", "I,II", "II,III,IV"], 3,
    ["NAND and NOR are each functionally complete, so I true; combinational logic networks are labelled DAGs, so II true.", "All finite Boolean algebras with n atoms are isomorphic, making III false.", "Each element is uniquely the join of the atoms below it, so IV false."], source=SRC18D, question_id="91394310749")
add(2018, "December 2018", "58", 52, "Optimization", "PERT network events",
    "In a PERT activity-on-arrow network, what does a merge event represent?",
    ["Completion of two or more activities", "Start of two or more activities", "A dummy activity only", "An isolated milestone"], 1,
    ["Several incoming arrows terminate at a merge event.", "It occurs only when all those predecessor activities have completed."], source=SRC18D)
add(2018, "December 2018", "59", 53, "Optimization", "Dual-simplex/graphical LP",
    "Maximize z=−2x₁−3x₂ subject to x₁+x₂≥2, 2x₁+x₂≤10, x₁+x₂≤8 and x₁,x₂≥0.",
    ["x₁=2,x₂=0,z=−4", "x₁=2,x₂=6,z=−22", "x₁=0,x₂=2,z=−6", "x₁=6,x₂=2,z=−18"], 1,
    ["Maximizing a negative cost is minimizing 2x₁+3x₂.", "The lower boundary x₁+x₂=2 is optimal; assign all two units to cheaper x₁.", "At (2,0), z=−4 and all upper constraints hold."], source=SRC18D, question_id="91394310753")
add(2018, "December 2018", "76", 68, "Graph Theory", "Rooted m-ary trees",
    "A ternary tree has 4 internal nodes of out-degree 1, 3 of out-degree 2 and 3 of out-degree 3. How many leaves?",
    ["9", "10", "11", "12"], 2,
    ["For a rooted tree, leaves=1+Σ_internal(outdegree−1).", "L=1+4·0+3·1+3·2=10."], source=SRC18D, question_id="91394310770")
add(2018, "December 2018", "78", 70, "Graph Theory", "Bipartite graphs and 2-colouring",
    "For a proper 2-colouring, which statement is not correct?",
    ["G is bipartite", "G is 2-colourable", "G has cycles of odd length", "G has no cycles of odd length"], 3,
    ["A graph is bipartite iff it is 2-colourable iff it contains no odd cycle.", "Therefore the assertion that it has odd cycles is the incorrect one."], source=SRC18D, question_id="91394310772")

SRC18J = "sources/ugc-net-cs-2018-july-paper-2.pdf"
add(2018, "July 2018", "25", 8, "Graph Theory", "Prefix codes and Huffman coding",
    "Characters A–E have probabilities 0.08,0.40,0.25,0.15,0.12. What average length does optimal binary Huffman coding achieve?",
    ["2.4", "1.87", "3.0", "2.15"], 4,
    ["Merge 0.08+0.12=0.20; then 0.15+0.20=0.35; then 0.25+0.35=0.60; finally 0.40+0.60.", "Resulting lengths are 1 for 0.40, 2 for 0.25, 3 for 0.15 and 4 for 0.08,0.12.", "Weighted average=0.40+0.50+0.45+0.32+0.48=2.15."], source=SRC18J)
add(2018, "July 2018", "26", 8, "Graph Theory", "Strict/full binary trees",
    "A strictly binary tree has 19 leaves. How many total nodes?",
    ["At most 37", "Exactly 37", "Exactly 35", "At most 35"], 2,
    ["In a full binary tree, leaves=internal nodes+1.", "Internal nodes=18 and total=18+19=37."], source=SRC18J)
add(2018, "July 2018", "29", 9, "Graph Theory", "Full m-ary trees",
    "A full 5-ary tree has eight internal nodes. How many leaves?",
    ["30", "33", "45", "125"], 2,
    ["For a full m-ary tree, L=(m−1)I+1.", "L=4·8+1=33."], source=SRC18J)
add(2018, "July 2018", "53", 13, "Counting, Mathematical Induction and Discrete Probability", "Poisson distribution",
    "Events occur at 30 per hour. What is the probability of no event in 40 minutes under a Poisson model?",
    ["e^(−30)", "e^(−12)", "20e^(−20)", "e^(−20)"], 4,
    ["Forty minutes is 2/3 hour, so mean count=30·2/3=20.", "P(X=0)=e^(−20)."], source=SRC18J)
add(2018, "July 2018", "80", 19, "Counting, Mathematical Induction and Discrete Probability", "Sample spaces",
    "How many atomic outcomes are in the experiment of drawing an unordered five-card poker hand from 52 cards?",
    ["2,598,960", "52⁵", "311,875,200", "120"], 1,
    ["Order within a hand does not matter and cards are not replaced.", "The count is C(52,5)=2,598,960."], source=SRC18J)
add(2018, "July 2018", "82", 19, "Optimization", "Convex optimization",
    "Which statement about convex minimization is false?",
    ["If a local minimum exists, it is global", "The set of all global minima is convex", "The set of all global minima is concave", "A strictly convex function, if it has a minimum, has a unique minimum"], 3,
    ["For a convex objective over a convex feasible set, local minima are global and the minimizer set is convex.", "Calling the minimizer set 'concave' is not a valid property; option 3 is false."], source=SRC18J)
add(2018, "July 2018", "83", 19, "Optimization", "Unbounded linear programming",
    "For the source LPP maximize 100x₁+2x₂+5x₃ with its printed equality/inequalities and nonnegative variables, classify the solution.",
    ["x₁=100,x₂=x₃=0", "Unbounded", "No solution", "x₁=50,x₂=70,x₃=60"], 2,
    ["A feasible improving direction is d=(0,6,1,0).", "It preserves 14d₁+d₂−6d₃+3d₄=0 and satisfies the two homogeneous ≤ directions.", "The objective increases by 2·6+5·1=17 per unit, so the LP is unbounded."], source=SRC18J)
add(2018, "July 2018", "84", 20, "Counting, Mathematical Induction and Discrete Probability", "Discrete probability distributions",
    "For S={0,…,32}, p(i)=(33−i)/561. What is the probability that an even number of buffers are full?",
    ["0.515", "0.785", "0.758", "0.485"], 1,
    ["Sum over i=0,2,…,32: Σ_{k=0}^{16}(33−2k)=17·33−2·136=289.", "P=289/561≈0.51515."], source=SRC18J)
add(2018, "July 2018", "85", 20, "Mathematical Logic", "Negating quantifiers",
    "Which is equivalent to ¬∃x Q(x)?",
    ["∃x¬Q(x)", "∀x¬Q(x)", "¬∃x¬Q(x)", "∀xQ(x)"], 2,
    ["Move negation through the existential quantifier, changing it to universal.", "Thus ¬∃xQ(x)≡∀x¬Q(x)."], source=SRC18J)
add(2018, "July 2018", "86", 20, "Sets and Relations", "Unions of sets",
    "If Aᵢ={−i,…,−1,0,1,…,i}, what is ⋃_{i=1}^∞ Aᵢ?",
    ["Z", "Q", "R", "C"], 1,
    ["Every integer k occurs once i≥|k|.", "No non-integer occurs in any Aᵢ, so the union is exactly Z."], source=SRC18J)
add(2018, "July 2018", "87", 20, "Sets and Relations", "Injective, surjective and constant functions",
    "Match: A ∀x∀y(f(x)=f(y)→x=y); B ∀y∃x(f(x)=y); C ∀x f(x)=k with I constant, II injective, III surjective.",
    ["A-I,B-II,C-III", "A-III,B-II,C-I", "A-II,B-I,C-III", "A-II,B-III,C-I"], 4,
    ["A is injectivity (II), B surjectivity (III), C constancy (I).", "Hence A-II,B-III,C-I."], source=SRC18J)
add(2018, "July 2018", "88", 20, "Sets and Relations", "Equivalence relations",
    "Which listed relation on {0,1,2,3} is an equivalence relation?",
    ["A relation missing (1,1)", "{(0,0),(1,1),(2,2),(3,3)}", "A non-transitive seven-pair relation", "A non-symmetric five-pair relation"], 2,
    ["The identity relation contains every diagonal pair and no off-diagonal pairs.", "It is reflexive, symmetric and transitive; each other printed option misses a required property."], source=SRC18J)
add(2018, "July 2018", "89", 21, "Sets and Relations", "Equivalence relations on functions",
    "Which defines an equivalence relation on all functions Z→Z?",
    ["f(x)−g(x)=1 for every x", "f(0)=g(0) or f(1)=g(1)", "f(0)=g(1) and f(1)=g(0)", "f(x)−g(x)=k for every x, for some integer k"], 4,
    ["Option 4 says functions differ by a constant. Difference 0 gives reflexivity; negating k gives symmetry; adding constants gives transitivity.", "Options 1 and 3 are not reflexive; the OR in option 2 breaks transitivity."], source=SRC18J)
add(2018, "July 2018", "90", 21, "Sets and Relations", "Partial and total orders",
    "Which statement is true?",
    ["(Z,≤) is not totally ordered", "Subset inclusion is a partial order on P(S)", "(Z,≠) is a poset", "The displayed order graph is not a partial order"], 2,
    ["Inclusion is reflexive, antisymmetric and transitive, hence a partial order.", "Integers under ≤ are totally ordered, and ≠ is not reflexive; these eliminate 1 and 3."], source=SRC18J)
add(2018, "July 2018", "99", 23, "Boolean Algebra", "K-map with don't-cares",
    "Simplify F(A,B,C,D)=Σ(0,1,2,8,9,12,13) with d=Σ(10,11,14,15).",
    ["AC'+B'C'+B'D'", "A'C'+BD+B'C", "A'B+C", "AB'C+BD"], "AC'+B'C'+B'D'",
    ["Use don't-cares to make groups 8,9,12,13→AC'; 0,1,8,9→B'C'; and 0,2,8,10→B'D'.", "The minimal SOP is AC'+B'C'+B'D'."], source=SRC18J, status="independently-verified; option typography ambiguous", note="The PDF's overbars are poorly encoded; the normalized expression is authoritative and the source page preserves the printed choices.")

SRC17I2 = "sources/ugc-net-cs-2017-jan-paper-2.pdf"
add(2017, "January 2017 Paper II", "5", 3, "Graph Theory", "Hamiltonian graph sufficient conditions",
    "For a simple n-vertex graph (n≥3), which listed degree/edge conditions are sufficient for Hamiltonicity?",
    ["Dirac and edge-count conditions", "Ore and edge-count conditions", "Dirac and Ore conditions", "All listed conditions"], 4,
    ["Dirac's δ≥n/2 and Ore's degree-sum condition are each sufficient.", "The printed extremal edge-count bound is also a classical sufficient Hamiltonicity condition.", "Thus all listed conditions are sufficient."], source=SRC17I2)
add(2017, "January 2017 Paper II", "6", 3, "Mathematical Logic", "Rules of inference",
    "From premises (P→Q)∧(R→S) and P∨R, which conclusion Y follows?",
    ["P∨R", "P∨S", "Q∨R", "Q∨S"], 4,
    ["Use proof by cases on P∨R.", "If P then Q; if R then S. Therefore at least one of Q or S holds, giving Q∨S."], source=SRC17I2)
SRC17I3 = "sources/ugc-net-cs-2017-jan-paper-3.pdf"
add(2017, "January 2017 Paper III", "68", 14, "Optimization", "Transportation stepping-stone loops",
    "Which statement about a closed loop used to improve a transportation solution is false?",
    ["The loop contains an odd number of cells", "Right-angle turns are used", "Occupied cells alternate with the trial cell", "Plus and minus signs alternate"], 1,
    ["A transportation adjustment loop always contains an even number of cells so that + and − positions alternate and balance is preserved.", "Therefore 'odd number of cells' is false."], source=SRC17I3)

SRC16I2 = "sources/ugc-net-cs-2016-july-paper-2.pdf"
add(2016, "July 2016 Paper II", "1", 2, "Sets and Relations", "Counting equivalence relations",
    "How many equivalence relations on a five-element set have exactly three equivalence classes?",
    ["15", "20", "25", "30"], 3,
    ["Such relations correspond to partitions of five labelled elements into three nonempty unlabeled blocks.", "The Stirling number S(5,3)=25."], source=SRC16I2)
add(2016, "July 2016 Paper II", "2", 2, "Graph Theory", "Spanning-tree enumeration",
    "How many spanning trees do K₄ and K₂,₂ have, respectively?",
    ["8 and 2", "16 and 2", "16 and 4", "8 and 4"], 3,
    ["Cayley gives τ(K₄)=4²=16.", "For Kₘ,ₙ, τ=m^(n−1)n^(m−1), so τ(K₂,₂)=4."], source=SRC16I2)
add(2016, "July 2016 Paper II", "3", 2, "Sets and Relations", "Operations on reflexive relations",
    "If R and S are reflexive relations on A, which of R∪S and R∩S must be reflexive?",
    ["Union only", "Intersection only", "Both", "Neither"], 3,
    ["Every diagonal pair belongs to both R and S.", "It therefore belongs to both their union and their intersection."], source=SRC16I2)
add(2016, "July 2016 Paper II", "4", 2, "Counting, Mathematical Induction and Discrete Probability", "Bayes theorem",
    "A box has three cards: BB, RR and BR. A card and one visible side are chosen at random. Given the observed colour, what is the probability that the opposite side has the same colour?",
    ["3/4", "2/3", "1/2", "1/3"], 2,
    ["Condition on a colour, say black. The visible black side could be either of the two sides of BB or the one black side of BR: three equally likely exposed sides.", "Two of those three belong to BB, so the opposite side matches with probability 2/3."], source=SRC16I2)
add(2016, "July 2016 Paper II", "6", 3, "Boolean Algebra", "Exclusive-OR",
    "Which XOR equality is incorrect?",
    ["0⊕0=0", "1⊕0=1", "1⊕1⊕0=1", "1⊕1=0"], 3,
    ["XOR is parity: it is 1 iff an odd number of inputs are 1.", "1⊕1⊕0 has two ones and equals 0, so option 3 is incorrect."], source=SRC16I2)
SRC16I3 = "sources/ugc-net-cs-2016-july-paper-3.pdf"
add(2016, "July 2016 Paper III", "36", 8, "Graph Theory", "Polygon triangulation",
    "A triangulation of a simple n-gon uses how many noncrossing diagonals and produces how many triangles?",
    ["n−2 and n−3", "n−3 and n−2", "n and n−2", "n−1 and n−1"], 2,
    ["Induct by removing an ear, or use Euler's formula.", "Every triangulation has n−3 diagonals and n−2 triangular faces."], source=SRC16I3)
add(2016, "July 2016 Paper III", "62", 13, "Optimization", "Revised simplex method",
    "Which printed statements about the revised simplex method are correct?",
    ["A,B only", "A,C only", "B,C only", "A,B,C"], 4,
    ["Revised simplex stores/updates basis information rather than the full tableau, computes reduced costs and performs the same basis changes as simplex.", "All three source statements describe these valid properties."], source=SRC16I3)

SRC15J2 = "sources/ugc-net-cs-2015-june-paper-2.pdf"
add(2015, "June 2015 Paper II", "1", 2, "Counting, Mathematical Induction and Discrete Probability", "Stars and bars",
    "How many five-digit strings (leading zero allowed) have digit sum 7?",
    ["66", "330", "495", "99"], 2,
    ["Since the sum is only 7, no digit can exceed 9; upper bounds are inactive.", "Nonnegative solutions of x₁+…+x₅=7 number C(11,4)=330."], source=SRC15J2)
add(2015, "June 2015 Paper II", "2", 2, "Counting, Mathematical Induction and Discrete Probability", "Discrete probability",
    "Two fair dice, black and red, are rolled. What is the probability that the black result divides the red result?",
    ["22/36", "12/36", "14/36", "6/36"], 3,
    ["For black values 1,…,6, the counts of red multiples are 6,3,2,1,1,1.", "Total favourable=14 of 36."], source=SRC15J2)
add(2015, "June 2015 Paper II", "3", 2, "Counting, Mathematical Induction and Discrete Probability", "Stars and bars",
    "In how many ways can 15 identical fish be placed into five distinct ponds with at least one in each?",
    ["1001", "3876", "775", "200"], 1,
    ["Positive solutions of x₁+…+x₅=15 are counted by C(14,4).", "C(14,4)=1001."], source=SRC15J2)
add(2015, "June 2015 Paper II", "4", 2, "Graph Theory", "Rooted-tree traversals and prefix codes",
    "Assess: A DFS traverses rooted trees; B preorder/postorder/inorder list ordered rooted-tree vertices; C Huffman finds an optimal weighted binary tree; D topological sorting gives parents larger labels than children.",
    ["A,B", "C,D", "A,B,C", "A,B,C,D"], 3,
    ["A,B,C are standard uses/properties.", "With the usual topological order, a parent precedes (has a smaller position than) its child, so D as written is false."], source=SRC15J2)
add(2015, "June 2015 Paper II", "6", 3, "Boolean Algebra", "Boolean expressions and logic networks",
    "Assess: A Boolean expressions/networks correspond to labelled acyclic digraphs; B an algebraically optimal expression need not give the simplest physical network; C greedy largest K-map groups need not always give a globally optimal expression.",
    ["A only", "B only", "A,B", "A,B,C"], 4,
    ["A describes combinational networks; B accounts for gate sharing/fan-in/technology cost; C reflects that a greedy cover need not minimize the final cover.", "All three are true."], source=SRC15J2)
add(2015, "June 2015 Paper II", "9", 3, "Mathematical Logic", "Named propositional equivalences",
    "Match contraposition, exportation, reductio ad absurdum and equivalence with the four displayed implications.",
    ["A-I,B-II,C-III,D-IV", "A-II,B-III,C-I,D-IV", "A-III,B-II,C-IV,D-I", "A-IV,B-II,C-III,D-I"], 1,
    ["(p→q)→(¬q→¬p) is contraposition; [(p∧q)→r]→[p→(q→r)] is exportation.", "The contradiction form is reductio, and p↔q expands to (p→q)∧(q→p)."], source=SRC15J2)
SRC15D2 = "sources/ugc-net-cs-2015-dec-paper-2.pdf"
add(2015, "December 2015 Paper II", "1", 2, "Counting, Mathematical Induction and Discrete Probability", "Combinations",
    "How many five-person committees can be chosen from 20 men and 12 women with at least three women?",
    ["75240", "52492", "41800", "9900"], 2,
    ["Sum cases 3W2M,4W1M,5W: C(12,3)C(20,2)+C(12,4)C(20,1)+C(12,5).", "=41800+9900+792=52492."], source=SRC15D2)
add(2015, "December 2015 Paper II", "2", 2, "Graph Theory", "Euler, Hamilton and bipartite graphs",
    "Which source statement is false? A even degrees characterize Euler circuits; B exactly two odd vertices characterize a non-circuit Euler path; C Kₙ has a Hamilton circuit for n≥3; D C₆ is not bipartite but K₃ is bipartite.",
    ["A only", "B,C", "C only", "D only"], 4,
    ["A–C are standard true theorems.", "C₆ is even and therefore bipartite, while K₃ is an odd cycle and not bipartite; D reverses both facts."], source=SRC15D2)
add(2015, "December 2015 Paper II", "3", 2, "Sets and Relations", "Countability",
    "Which is not countable: negative integers, multiples of 7, even integers, or real numbers in (0,1/2)?",
    ["Negative and even integers", "Multiples of 7 only", "Even integers only", "Reals in (0,1/2) only"], 4,
    ["Each listed integer subset has a simple enumeration and is countable.", "Every nonempty real interval is uncountable by a scaling/bijection argument."], source=SRC15D2)
add(2015, "December 2015 Paper II", "7", 3, "Mathematical Logic", "Quantifiers and divisibility",
    "For positive integers and P(m,n): m divides n, assess A ∃m∀nP(m,n); B ∀nP(1,n); C ∀m∀nP(m,n).",
    ["True,True,False", "True,False,False", "False,False,False", "True,True,True"], 1,
    ["Choose m=1 for A; B is the same universal divisibility fact.", "C is false, e.g. 2 does not divide 1."], source=SRC15D2)
SRC15D3 = "sources/ugc-net-cs-2015-dec-paper-3.pdf"
add(2015, "December 2015 Paper III", "52", 10, "Optimization", "Degeneracy in linear programming",
    "A basic feasible solution is called what if at least one basic variable is zero?",
    ["Degenerate", "Non-degenerate", "Infeasible", "Unbounded"], 1,
    ["This is exactly the definition of a degenerate BFS.", "It may still be feasible and bounded; degeneracy concerns a zero-valued basic variable."], source=SRC15D3)
add(2015, "December 2015 Paper III", "53", 10, "Optimization", "Transportation non-degeneracy",
    "A transportation initial solution is a non-degenerate BFS when it is feasible, has m+n−1 positive allocations, and those allocations are independent. Which conditions are required?",
    ["A,B only", "A,C only", "B,C only", "A,B,C"], 4,
    ["Feasibility is required, the rank requires m+n−1 basic cells, and independence excludes a loop.", "All three conditions are necessary."], source=SRC15D3)

SRC14I2 = "sources/ugc-net-cs-2014-dec-paper-2.pdf"
add(2014, "December 2014 Paper II", "4", 2, "Counting, Mathematical Induction and Discrete Probability", "Repeated independent trials",
    "One integer is chosen uniformly from one million values, independently one million times. What is the approximate probability that a specified integer is chosen at least once?",
    ["0.5", "0.632121", "0.367879", "1"], 2,
    ["Complement probability is (1−10⁻⁶)^(10⁶).", "Using (1−1/n)^n→e⁻¹ gives 1−e⁻¹≈0.632121."], source=SRC14I2)
SRC14I3 = "sources/ugc-net-cs-2014-dec-paper-3.pdf"
add(2014, "December 2014 Paper III", "67", 14, "Optimization", "Artificial variables",
    "If an artificial variable remains basic with a positive value in the final simplex solution, what does it imply?",
    ["Alternative optimum", "Original problem infeasible", "Unbounded", "Degenerate optimum only"], 2,
    ["Phase I minimizes the sum of artificial variables.", "A positive artificial value at its optimum means the original constraints cannot be satisfied without it, hence infeasible."], source=SRC14I3)
add(2014, "December 2014 Paper III", "68", 14, "Optimization", "Transportation degeneracy",
    "If a transportation BFS has fewer than m+n−1 occupied independent cells, it is:",
    ["Balanced", "Unbalanced", "Infeasible", "Degenerate (none of the first three)"], 4,
    ["Fewer than the required rank number of positive basic allocations is transportation degeneracy.", "It is independent of whether total supply equals demand."], source=SRC14I3)

SRC13D2 = "sources/ugc-net-cs-2013-dec-paper-2.pdf"
add(2013, "December 2013 Paper II", "31", 7, "Boolean Algebra", "Duality principle",
    "How is the dual of a Boolean expression obtained?",
    ["Complement every variable", "Swap 0 and 1 only", "Interchange + with · and 0 with 1", "Reverse all literals"], 3,
    ["Boolean duality interchanges join/meet and their identities.", "Variables and complements are left unchanged; +↔· and 0↔1."], source=SRC13D2)
add(2013, "December 2013 Paper II", "34", 8, "Mathematical Logic", "Quantifiers and divisibility",
    "Over positive integers, which is true: ∀m∀n(m divides n), or ∃m∀n(m divides n)?",
    ["Both", "Universal only", "Existential-universal only", "Neither"], 3,
    ["The universal statement is false, e.g. 2∤1.", "The existential statement is true with m=1."], source=SRC13D2)
add(2013, "December 2013 Paper II", "36", 8, "Graph Theory", "Forests",
    "A forest with n vertices and t component trees has how many edges?",
    ["n+t", "n−t", "n−1", "t−1"], 2,
    ["Each component with nᵢ vertices has nᵢ−1 edges.", "Summing gives n−t."], source=SRC13D2)
add(2013, "December 2013 Paper II", "37", 8, "Sets and Relations", "Function composition",
    "For f(x)=2x+3 and g(x)=3x+2, what are f∘g and g∘f?",
    ["6x+7 and 6x+11", "6x+11 and 6x+7", "5x+5 and 5x+5", "6x+6 and 6x+6"], 1,
    ["f(g(x))=2(3x+2)+3=6x+7.", "g(f(x))=3(2x+3)+2=6x+11."], source=SRC13D2)
add(2013, "December 2013 Paper II", "39", 8, "Graph Theory", "Planarity and Kuratowski theorem",
    "Kuratowski's theorem characterizes non-planar graphs using subdivisions of which graphs?",
    ["K₄ or K₂,₃", "K₅ only", "K₅ or K₃,₃", "K₆ or K₄,₄"], 3,
    ["A finite graph is non-planar iff it contains a subdivision of K₅ or K₃,₃.", "These are the two Kuratowski forbidden graphs."], source=SRC13D2)
SRC13D3 = "sources/ugc-net-cs-2013-dec-paper-3.pdf"
add(2013, "December 2013 Paper III", "39", 9, "Graph Theory", "Cliques and vertex covers",
    "Match clique and vertex cover with the source definitions.",
    ["Clique=minimal independent set; cover=maximal complete set", "Clique=path; cover=cut", "Clique=tree; cover=cycle", "Clique=maximal complete vertex set; cover=a vertex subset incident to every edge"], 4,
    ["A clique is a complete subgraph (often maximal in this terminology).", "A vertex cover meets every edge; the source uses a minimal such subset."], source=SRC13D3)
SRC13J3 = "sources/ugc-net-cs-2013-june-paper-3.pdf"
add(2013, "June 2013 Paper III", "23", 5, "Optimization", "Alternative optima in simplex",
    "At an optimal simplex tableau, what does a zero reduced cost for a nonbasic variable indicate?",
    ["Infeasibility", "Unboundedness", "An alternative optimal solution", "Degeneracy only"], 3,
    ["Entering a nonbasic variable with zero reduced cost does not change the objective.", "If a feasible pivot exists, it produces another optimum."], source=SRC13J3)

SRC12J = "sources/ugc-net-cs-2012-june-paper-2.pdf"
add(2012, "June 2012 Paper II", "1", 2, "Graph Theory", "Postfix expression evaluation",
    "The postfix expression AB+CD−* is naturally evaluated using which data structure?",
    ["Stack", "Tree", "Queue", "Linked list"], 1,
    ["Scan left to right, push operands and pop the top two operands for each operator.", "This last-in-first-out discipline is a stack."], source=SRC12J, secondary="Unit 7: Data Structures and Algorithms")
add(2012, "June 2012 Paper II", "2", 2, "Graph Theory", "Tree traversals",
    "A binary tree has postorder DEBFCA. Which proposed preorder is consistent?",
    ["ABFCDE", "ADBFEC", "ABDECF", "None"], 3,
    ["Postorder ends with root A. The consistent subtree decomposition yields root-first order A,B,D,E,C,F.", "Thus preorder is ABDECF."], source=SRC12J)
add(2012, "June 2012 Paper II", "4", 2, "Graph Theory", "Planar graph colouring",
    "How many colours suffice to properly colour the vertices of every planar graph?",
    ["2", "3", "4", "5"], 3,
    ["The Four Colour Theorem guarantees at most four colours for every planar graph.", "K₄ is planar and needs four, so the universal bound is tight."], source=SRC12J)
SRC12D = "sources/ugc-net-cs-2012-dec-paper-2.pdf"
add(2012, "December 2012 Paper II", "4", 2, "Sets and Relations", "Power sets",
    "What is the power set of {∅}?",
    ["{∅}", "∅", "{∅,{∅}}", "{∅,∅,{∅}}"], 3,
    ["The set {∅} has one element, so its power set has two subsets.", "They are ∅ and {∅}, hence {∅,{∅}}."], source=SRC12D)

SRC11 = "sources/ugc-net-cs-2011-dec-paper-3.pdf"
add(2011, "December 2011 Paper III", "3", 2, "Optimization", "Graphical/revised-simplex LP",
    "Maximize 2x₁+2x₂ subject to 3x₁+4x₂≤6, 6x₁+x₂≤3 and x₁,x₂≥0.",
    ["(0,0)", "(2/7,9/7)", "(1/2,0)", "Unbounded"], 2,
    ["Intersect 3x₁+4x₂=6 and 6x₁+x₂=3: x₁=2/7,x₂=9/7.", "The objective is 22/7, exceeding the axis vertices 3 and 1.", "Thus the intersection is optimal."], source=SRC11)
add(2011, "December 2011 Paper III", "4", 2, "Optimization", "Transportation model",
    "Solve the transportation problem with costs [[8,5,6],[15,10,12],[3,9,10]], supplies [120,80,80] and demands [150,80,50].",
    [], "Minimum cost 1900 (under the visually recovered supply 80)",
    ["Exploit the cheapest cell: send 80 from S3 to D1 at cost 3; D1 then needs 70.", "Allocate S1→D1=70 and S1→D3=50; send S2→D2=80.", "Total=80·3+70·8+50·6+80·10=1900. Opportunity-cost checks are nonnegative for this basis."], source=SRC11, status="ambiguous-scan", note="The scan reads the third supply as '8' in OCR; visual balance indicates 80. The normalized numeric answer is conditional on that recovery.")

SRC09 = "sources/ugc-net-cs-2009-dec-paper-2.pdf"
add(2009, "December 2009 Paper II", "6", 3, "Boolean Algebra", "Boolean simplification",
    "Simplify (X+Y+XY)(X+Z).",
    ["X+Y+Z", "XY+XZ", "X+YZ", "XYZ"], 3,
    ["Absorption gives X+Y+XY=X+Y.", "Then (X+Y)(X+Z)=X+YZ."], source=SRC09)
add(2009, "December 2009 Paper II", "21", 6, "Graph Theory", "Full binary trees",
    "A strict/full binary tree has an odd number of leaves. What can be said about its total number of vertices?",
    ["Odd", "Even", "A power of two", "Cannot be determined"], 1,
    ["For L leaves, a full binary tree has total nodes 2L−1.", "If L is odd, 2L−1 is odd."], source=SRC09)
add(2009, "December 2009 Paper II", "22", 6, "Graph Theory", "Complete graphs",
    "How many edges does a complete graph on n vertices have?",
    ["n²", "n(n−1)/2", "n(n+1)/2", "2n"], 2,
    ["Every unordered pair of distinct vertices contributes one edge.", "There are C(n,2)=n(n−1)/2 such pairs."], source=SRC09)

SRC10 = "sources/ugc-net-cs-2010-june-paper-2.pdf"
add(2010, "June 2010 Paper II", "1", 2, "Sets and Relations", "Equivalence relations",
    "Two entities are called clones when all attributes in the stated complete attribute set (height, weight, complexion) are identical. Is cloning an equivalence relation?",
    ["True", "False", "Truth cannot be computed", "None"], 1,
    ["Equality of an attribute tuple is reflexive, symmetric and transitive.", "Because the attribute set is stipulated to be complete for this definition, cloning is an equivalence relation."], source=SRC10)
add(2010, "June 2010 Paper II", "4", 2, "Graph Theory", "Graph colouring from associations",
    "Build the association graph from the five source sentences about I, professor, student, algorithms, maths, electronics and computer science. What is its chromatic number?",
    ["2", "3", "4", "None"], 2,
    ["The associations I–maths, I–student and student–maths form a triangle, so at least three colours are necessary.", "A direct three-colouring of all remaining vertices is possible, so χ=3."], source=SRC10)

DUPLICATE_GROUPS = [
    {
        "groupId": "U1-DUP-001",
        "type": "near-duplicate",
        "canonical": "UGCNET-CS-2013-december-2013-paper-ii-Q34",
        "members": ["UGCNET-CS-2013-december-2013-paper-ii-Q34", "UGCNET-CS-2015-december-2015-paper-ii-Q7"],
        "reason": "Same nested-quantifier divisibility test; notation and option grouping differ.",
    },
    {
        "groupId": "U1-DUP-002",
        "type": "conceptual-repeat",
        "canonical": "UGCNET-CS-2018-july-2018-Q26",
        "members": ["UGCNET-CS-2009-december-2009-paper-ii-Q21", "UGCNET-CS-2018-july-2018-Q26"],
        "reason": "Both reduce to the full-binary-tree identity N=2L−1.",
    },
    {
        "groupId": "U1-DUP-003",
        "type": "conceptual-repeat",
        "canonical": "UGCNET-CS-2018-december-2018-Q54",
        "members": ["UGCNET-CS-2018-december-2018-Q54", "UGCNET-CS-2025-june-2025-Q51"],
        "reason": "Three-set inclusion–exclusion with all singles, pairs and triple intersection supplied.",
    },
    {
        "groupId": "U1-DUP-004",
        "type": "near-duplicate",
        "canonical": "UGCNET-CS-2018-july-2018-Q85",
        "members": ["UGCNET-CS-2018-july-2018-Q85", "UGCNET-CS-2023-dec-2022-mar-11-shift-2-Q1"],
        "reason": "Both test ¬∃xP(x)≡∀x¬P(x); one is symbolic and one verbal.",
    },
    {
        "groupId": "U1-DUP-005",
        "type": "near-duplicate",
        "canonical": "UGCNET-CS-2019-december-2019-Q51",
        "members": ["UGCNET-CS-2015-december-2015-paper-iii-Q53", "UGCNET-CS-2019-december-2019-Q51"],
        "reason": "Same m+n−1 independent-allocation criterion for a non-degenerate transportation BFS.",
    },
    {
        "groupId": "U1-DUP-006",
        "type": "conceptual-repeat",
        "canonical": "UGCNET-CS-2016-july-2016-paper-ii-Q2",
        "members": ["UGCNET-CS-2016-july-2016-paper-ii-Q2", "UGCNET-CS-2024-june-2024-Q88"],
        "reason": "Both require Cayley and complete-bipartite spanning-tree counts.",
    },
]

_by_id = {r["id"]: r for r in RECORDS}
for _group in DUPLICATE_GROUPS:
    for _member in _group["members"]:
        _by_id[_member]["canonicalExplanation"] = _group["canonical"]


def validate() -> None:
    ids = [r["id"] for r in RECORDS]
    if len(ids) != len(set(ids)):
        dupes = [k for k, v in Counter(ids).items() if v > 1]
        raise ValueError(f"duplicate ids: {dupes}")
    for r in RECORDS:
        src = ROOT / r["sourceFile"]
        if not src.exists():
            raise FileNotFoundError(src)
        if r["correctOption"] is not None and not 1 <= r["correctOption"] <= len(r["options"]):
            raise ValueError(r["id"])
        if not r["solutionSteps"]:
            raise ValueError(f"missing solution: {r['id']}")


def write_outputs() -> None:
    validate()
    data_dir = ROOT / "data"
    docs_dir = ROOT / "docs"
    data_dir.mkdir(exist_ok=True)
    docs_dir.mkdir(exist_ok=True)

    (data_dir / "questions.json").write_text(json.dumps(RECORDS, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = ["id", "exam", "year", "session", "shift", "paper", "questionNumber", "questionId", "sourceFile", "sourcePage", "unit", "topic", "subtopic", "secondaryUnit", "question", "options", "correctOption", "correctAnswer", "answerStatus", "officialAnswer", "solutionSteps", "concept", "formulaOrRule", "shortcut", "commonTrap", "optionAnalysis", "canonicalExplanation", "reviewNote", "sourceAnchor"]
    with (data_dir / "questions.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for r in RECORDS:
            row = {k: r.get(k) for k in fields}
            row["options"] = json.dumps(r["options"], ensure_ascii=False)
            row["solutionSteps"] = json.dumps(r["solutionSteps"], ensure_ascii=False)
            row["optionAnalysis"] = json.dumps(r["optionAnalysis"], ensure_ascii=False)
            writer.writerow(row)

    by_topic = Counter(r["topic"] for r in RECORDS)
    by_year = Counter(r["year"] for r in RECORDS)
    lines = [
        "# Unit 1: Discrete Structures and Optimization",
        "",
        "[Project home](../README.md) · [All units](README.md) · [Official syllabus](syllabus.md)",
        "",
        "> Based on the official UGC NET Computer Science syllabus. Source filenames, PDF pages, internal IDs and verification details remain available in the structured data and audits, while this guide stays focused on learning.",
        "",
        "## Contents",
        "",
        "- [Coverage and limitations](#coverage-and-source-limitation)",
        "- [Exam-oriented concept handbook](#exam-oriented-concept-handbook)",
    ]
    lines.extend(f"  - [{topic}](#{''.join(ch.lower() if ch.isalnum() else '-' for ch in topic).strip('-').replace('--', '-')})" for topic in TOPICS)
    lines += [
        "- [Solved previous-year questions](#solved-previous-year-questions)",
    ]
    lines.extend(f"  - [{year}](#{year})" for year in sorted(by_year, reverse=True))
    lines += [
        "- [Validation summary](#validation-summary)",
        "",
        "## Coverage and source limitation",
        "",
        f"This guide contains **{len(RECORDS)} reviewed and solved Unit 1 questions** from the verified UGC NET corpus. See the [extraction audit](../data/unit-1-audit.md) for validation details and the explicitly accounted source-defect queue.",
        "This guide covers UGC NET sources only. No verifiable Rajasthan SET Computer Science question paper or official key is present, so Rajasthan SET coverage is not claimed.",
        "",
        "### Topic counts",
        "",
        "| Topic | Questions |",
        "|---|---:|",
    ]
    lines.extend(f"| {topic} | {by_topic.get(topic, 0)} |" for topic in TOPICS)
    lines += ["", "## Exam-oriented concept handbook", ""]
    for topic, info in TOPICS.items():
        lines += [f"### {topic}", "", info["concept"], "", f"**Formula/rule:** {info['formula']}", "", f"**Fast method:** {info['shortcut']}", "", f"**Common trap:** {info['trap']}", ""]

    lines += ["## Solved previous-year questions", ""]
    grouped: dict[int, list[dict]] = defaultdict(list)
    for r in RECORDS:
        grouped[r["year"]].append(r)
    unit_question_number = 0
    for year in sorted(grouped, reverse=True):
        lines += [f"### {year}", ""]
        for r in grouped[year]:
            unit_question_number += 1
            short_reference = f"UGC NET {r['session']}, original Q{r['questionNumber']}"
            lines += [
                "---",
                "",
                f"#### Question {unit_question_number}",
                "",
                f"*{short_reference}*",
                "",
                r["question"],
                "",
            ]
            for opt in r["options"]:
                lines.append(f"{opt['number']}. {opt['text']}")
            lines += [
                "",
                f"**Correct answer:** {r['correctOption'] or '—'} — {r['correctAnswer']}",
                "",
                "**Build the basics**",
                "",
                f"This question tests **{r['subtopic']}**. {r['concept']}",
                "",
                "**Step-by-step reasoning**",
                "",
            ]
            lines.extend(f"{i}. {step}" for i, step in enumerate(r["solutionSteps"], 1))
            conclusion_answer = str(r["correctAnswer"]).rstrip(".")
            conclusion = (
                f"The reasoning gives option {r['correctOption']}: **{conclusion_answer}**."
                if r["correctOption"] is not None
                else f"The derived result is **{conclusion_answer}**."
            )
            lines += [
                "",
                "**Conclusion**",
                "",
                conclusion,
                "",
                "**How to solve similar questions**",
                "",
                f"- **Rule to remember:** {r['formulaOrRule']}",
                f"- **Fast exam method:** {r['shortcut']}",
                f"- **Common mistake to avoid:** {r['commonTrap']}",
                "",
            ]
            if r["reviewNote"]:
                lines += [f"> **Important wording note:** {r['reviewNote']}", ""]

    lines += [
        "## Validation summary",
        "",
        f"- Records: {len(RECORDS)}; unique IDs: {len(set(r['id'] for r in RECORDS))}.",
        f"- Source files represented: {len(set(r['sourceFile'] for r in RECORDS))}.",
        "- Every record has a short exam/session reference, independently derived answer and step-by-step solution; options are preserved for objective questions.",
        "- Full source filenames, PDF pages, IDs, classifications and verification states remain in `data/questions.json` for auditing, but are intentionally hidden from the study flow.",
        "- Disputed and ambiguous items are also mirrored in `data/disputed-questions.md` and `data/classification-review.md`.",
        "",
        "### Questions by year",
        "",
        "| Year | Count |",
        "|---:|---:|",
    ]
    lines.extend(f"| {year} | {by_year[year]} |" for year in sorted(by_year, reverse=True))
    lines += ["", "---", "", "[Back to contents](#contents) · [All units](README.md) · [Project home](../README.md)", ""]
    (docs_dir / "unit-1-discrete-structures-and-optimization.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    stats = {
        "unit": 1,
        "title": "Discrete Structures and Optimization",
        "status": "complete-with-documented-source-defect-exceptions" if RECORDS else "not-started",
        "questionCount": len(RECORDS),
        "topicCounts": dict(sorted(by_topic.items())),
        "yearCounts": {str(k): v for k, v in sorted(by_year.items())},
        "sourceFileCount": len(set(r["sourceFile"] for r in RECORDS)),
        "rajasthanSetQuestionCount": 0,
        "rajasthanSetLimitation": "No verifiable Rajasthan SET paper/key supplied.",
    }
    (data_dir / "unit-1-statistics.json").write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")
    duplicate_payload = {
        "exactFileDuplicateGroups": [],
        "questionDuplicateGroups": DUPLICATE_GROUPS,
        "notes": [
            "The source inventory uses complete SHA-256 hashes for duplicate checking; no byte-identical files were found.",
            "Question groups are conservative: exact wording is not asserted unless type is exact; conceptual repeats share a canonical explanation while retaining separate source records.",
        ],
    }
    (data_dir / "duplicates.json").write_text(json.dumps(duplicate_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_outputs()
    print(f"Generated Unit 1 outputs for {len(RECORDS)} questions")
