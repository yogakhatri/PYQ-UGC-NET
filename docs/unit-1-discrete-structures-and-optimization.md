# Unit 1: Discrete Structures and Optimization

[Project home](../README.md) · [All units](README.md) · [Official syllabus](syllabus.md)

> Based on the official UGC NET Computer Science syllabus. Source filenames, PDF pages, internal IDs and verification details remain available in the structured data and audits, while this guide stays focused on learning.

## Contents

- [Coverage and limitations](#coverage-and-source-limitation)
- [Exam-oriented concept handbook](#exam-oriented-concept-handbook)
  - [Mathematical Logic](#mathematical-logic)
  - [Sets and Relations](#sets-and-relations)
  - [Counting, Mathematical Induction and Discrete Probability](#counting-mathematical-induction-and-discrete-probability)
  - [Group Theory](#group-theory)
  - [Graph Theory](#graph-theory)
  - [Boolean Algebra](#boolean-algebra)
  - [Optimization](#optimization)
- [Solved previous-year questions](#solved-previous-year-questions)
  - [2026](#2026)
  - [2025](#2025)
  - [2024](#2024)
  - [2023](#2023)
  - [2022](#2022)
  - [2021](#2021)
  - [2020](#2020)
  - [2019](#2019)
  - [2018](#2018)
  - [2017](#2017)
  - [2016](#2016)
  - [2015](#2015)
  - [2014](#2014)
  - [2013](#2013)
  - [2012](#2012)
  - [2011](#2011)
  - [2010](#2010)
  - [2009](#2009)
- [Validation summary](#validation-summary)

## Coverage and source limitation

This guide contains **143 reviewed and solved Unit 1 questions** from the verified UGC NET corpus. See the [extraction audit](../data/unit-1-audit.md) for validation details and the explicitly accounted source-defect queue.
No verifiable Rajasthan SET Computer Science question paper or official key is present in the supplied repository; four descriptively named Rajasthan PDFs are RPSC recruitment papers and are excluded rather than mislabelled as SET.

### Topic counts

| Topic | Questions |
|---|---:|
| Mathematical Logic | 17 |
| Sets and Relations | 24 |
| Counting, Mathematical Induction and Discrete Probability | 27 |
| Group Theory | 7 |
| Graph Theory | 29 |
| Boolean Algebra | 16 |
| Optimization | 23 |

## Exam-oriented concept handbook

### Mathematical Logic

Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Formula/rule:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).

**Fast method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.

**Common trap:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

### Sets and Relations

A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Formula/rule:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.

**Fast method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.

**Common trap:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

### Counting, Mathematical Induction and Discrete Probability

Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Formula/rule:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).

**Fast method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.

**Common trap:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

### Group Theory

A group has closure, associativity, an identity and inverses; an abelian group also commutes. Homomorphisms preserve the operation, automorphisms are isomorphisms from a structure to itself, and fields are commutative integral domains in which every nonzero element is invertible.

**Formula/rule:** For finite G and H≤G, |H| divides |G| (Lagrange). Every finite integral domain is a field.

**Fast method:** To refute an ideal claim, multiply a typical element on the left and right by a completely general ring element.

**Common trap:** A numerical divisibility fact does not establish that one group is a subgroup of another.

### Graph Theory

Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Formula/rule:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.

**Fast method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.

**Common trap:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

### Boolean Algebra

Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Formula/rule:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.

**Fast method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.

**Common trap:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

### Optimization

Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Formula/rule:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.

**Fast method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.

**Common trap:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

## Solved previous-year questions

### 2026

---

#### Question 1

*UGC NET Dec 2025 Jan 2026, original Q51*

Which statement is false?

1. Every field is an integral domain.
2. Every integral domain is a field.
3. Every finite integral domain is a field.
4. Z_p is a field iff p is prime.

**Correct answer:** 2 — Every integral domain is a field.

**Build the basics**

This question tests **Rings, integral domains and fields**. A group has closure, associativity, an identity and inverses; an abelian group also commutes. Homomorphisms preserve the operation, automorphisms are isomorphisms from a structure to itself, and fields are commutative integral domains in which every nonzero element is invertible.

**Step-by-step reasoning**

1. A field has no zero divisors, so (1) is true.
2. Z is an integral domain but not a field because 2 has no multiplicative inverse in Z.
3. The standard finiteness argument makes multiplication by a nonzero element bijective, proving (3); (4) is also standard.

**Conclusion**

The reasoning gives option 2: **Every integral domain is a field**.

**How to solve similar questions**

- **Rule to remember:** For finite G and H≤G, |H| divides |G| (Lagrange). Every finite integral domain is a field.
- **Fast exam method:** To refute an ideal claim, multiply a typical element on the left and right by a completely general ring element.
- **Common mistake to avoid:** A numerical divisibility fact does not establish that one group is a subgroup of another.

---

#### Question 2

*UGC NET Dec 2025 Jan 2026, original Q52*

Let S be the subring of M₂(Z) consisting of all diagonal matrices diag(a,b). What kind of ideal is S?

1. Left but not right ideal
2. Right but not left ideal
3. Both left and right ideal
4. Neither left nor right ideal

**Correct answer:** 4 — Neither left nor right ideal

**Build the basics**

This question tests **Rings and ideals**. A group has closure, associativity, an identity and inverses; an abelian group also commutes. Homomorphisms preserve the operation, automorphisms are isomorphisms from a structure to itself, and fields are commutative integral domains in which every nonzero element is invertible.

**Step-by-step reasoning**

1. Take D=diag(a,b) and an arbitrary matrix X.
2. XD can have nonzero off-diagonal entries, so XD need not lie in S; likewise DX need not lie in S.
3. Thus S is a subring but neither a left nor a right ideal.

**Conclusion**

The reasoning gives option 4: **Neither left nor right ideal**.

**How to solve similar questions**

- **Rule to remember:** For finite G and H≤G, |H| divides |G| (Lagrange). Every finite integral domain is a field.
- **Fast exam method:** To refute an ideal claim, multiply a typical element on the left and right by a completely general ring element.
- **Common mistake to avoid:** A numerical divisibility fact does not establish that one group is a subgroup of another.

---

#### Question 3

*UGC NET Dec 2025 Jan 2026, original Q53*

Assertion: the order of (Z₅*,×) divides the order of (Z₁₃*,×). Reason: the order of a subgroup divides the order of the group.

1. Both true; R explains A
2. Both true; R does not explain A
3. A true; R false
4. A false; R true

**Correct answer:** 2 — Both true; R does not explain A

**Build the basics**

This question tests **Groups and Lagrange theorem**. A group has closure, associativity, an identity and inverses; an abelian group also commutes. Homomorphisms preserve the operation, automorphisms are isomorphisms from a structure to itself, and fields are commutative integral domains in which every nonzero element is invertible.

**Step-by-step reasoning**

1. The multiplicative unit groups have orders φ(5)=4 and φ(13)=12; hence 4 divides 12.
2. Lagrange's theorem is true.
3. No subgroup embedding was stated, so Lagrange's theorem is not the reason for this numerical divisibility fact.

**Conclusion**

The reasoning gives option 2: **Both true; R does not explain A**.

**How to solve similar questions**

- **Rule to remember:** For finite G and H≤G, |H| divides |G| (Lagrange). Every finite integral domain is a field.
- **Fast exam method:** To refute an ideal claim, multiply a typical element on the left and right by a completely general ring element.
- **Common mistake to avoid:** A numerical divisibility fact does not establish that one group is a subgroup of another.

> **Important wording note:** The source prints Z₅ and Z₁₃ with multiplication; these must be read as their nonzero unit groups for them to be groups.

---

#### Question 4

*UGC NET Dec 2025 Jan 2026, original Q54*

On A=N×N define (a,b) R (c,d) iff a≤c or b≤d. Assertion: R is a partial order. Reason: a partial order is reflexive, antisymmetric and transitive.

1. Both true; R explains A
2. Both true; R does not explain A
3. A true; R false
4. A false; R true

**Correct answer:** 4 — A false; R true

**Build the basics**

This question tests **Partial ordering**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. R is reflexive, but antisymmetry fails: (1,2)R(2,1) because 1≤2, and (2,1)R(1,2) because 1≤2 in the second coordinate, although the pairs differ.
2. Therefore the assertion is false.
3. The reason correctly states the three defining properties of a partial order.

**Conclusion**

The reasoning gives option 4: **A false; R true**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 5

*UGC NET Dec 2025 Jan 2026, original Q55*

Over all integers, which are true? A ∀n∃m(n²<m); B ∃n∃m(n+m=4 ∧ n−m=2); C ∃n∃m(n²+m²=5); D ∃m∀n(m+n=0); E ∀m∃n(m+n=0).

1. A,B,C only
2. A,B,C,D only
3. A,B,C,E only
4. B,C,D,E only

**Correct answer:** 3 — A,B,C,E only

**Build the basics**

This question tests **Predicates and nested quantifiers**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. A: choose m=n²+1. B: n=3,m=1. C: n=1,m=2.
2. D is impossible because one fixed m cannot equal −n for every integer n.
3. E is true by choosing n=−m. Hence A,B,C,E.

**Conclusion**

The reasoning gives option 3: **A,B,C,E only**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 6

*UGC NET Dec 2025 Jan 2026, original Q56*

Which implications are tautologies? A [¬p∧(p∨q)]→q; B ¬p→(p→q); C [p∧(p→q)]→q; D ¬(p→q)→q.

1. A,B only
2. B,D only
3. A,B,C only
4. B,C,D only

**Correct answer:** 3 — A,B,C only

**Build the basics**

This question tests **Tautologies and rules of inference**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. A's antecedent simplifies to ¬p∧q, so A is true. B is true because p false makes p→q true.
2. C is modus ponens and is a tautology.
3. For D choose p=true,q=false: its antecedent is true and consequent false. Thus D is not a tautology.

**Conclusion**

The reasoning gives option 3: **A,B,C only**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 7

*UGC NET Dec 2025 Jan 2026, original Q57*

Arrange K₆, K₇, K₄,₄ and K₅,₅ in ascending order of minimum crossing number.

1. K₆,K₇,K₄,₄,K₅,₅
2. K₄,₄,K₅,₅,K₆,K₇
3. K₆,K₄,₄,K₇,K₅,₅
4. K₇,K₅,₅,K₆,K₄,₄

**Correct answer:** 3 — K₆,K₄,₄,K₇,K₅,₅

**Build the basics**

This question tests **Planar graphs and crossing numbers**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. Known crossing numbers are cr(K₆)=3, cr(K₄,₄)=4, cr(K₇)=9 and cr(K₅,₅)=16.
2. Ascending order is therefore K₆, K₄,₄, K₇, K₅,₅.

**Conclusion**

The reasoning gives option 3: **K₆,K₄,₄,K₇,K₅,₅**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 8

*UGC NET Dec 2025 Jan 2026, original Q58*

Arrange the source's four prefix expressions A–D in ascending value: A='− * 2 / 8 4 3'; B='↑ − * 3 6 * 4 2 5'; C='+ − ↑ 3 2 ↑ 2 3 / 6 − 4 2'; D='* + 3 + 3 ↑ 3 + 1 1 3'.

1. A,D,C,B
2. A,C,D,B
3. A,B,C,D
4. C,A,D,B

**Correct answer:** 2 — A,C,D,B

**Build the basics**

This question tests **Prefix notation and rooted expression trees**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. Evaluate prefix expressions from the innermost/rightmost complete subexpressions.
2. A=2(8/4)−3=1; B=(18−8)^5=100000; C=(9−8)+6/(4−2)=4; D=[3+(3+3^(1+1))]·3=45.
3. Thus A<C<D<B.

**Conclusion**

The reasoning gives option 2: **A,C,D,B**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 9

*UGC NET Dec 2025 Jan 2026, original Q59*

Match: domination, associative, distributive and absorption laws with I x+1=1; II x+yz=(x+y)(x+z); III x+xy=x; IV x+(y+z)=(x+y)+z.

1. A-I,B-II,C-IV,D-III
2. A-I,B-IV,C-II,D-III
3. A-III,B-IV,C-II,D-I
4. A-III,B-II,C-IV,D-I

**Correct answer:** 2 — A-I,B-IV,C-II,D-III

**Build the basics**

This question tests **Boolean identities**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. Domination is I, associativity is IV, distributivity is II, and absorption is III.
2. The resulting match is A-I, B-IV, C-II, D-III.

**Conclusion**

The reasoning gives option 2: **A-I,B-IV,C-II,D-III**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

---

#### Question 10

*UGC NET Dec 2025 Jan 2026, original Q60*

Match methods to problem types: branch-and-bound; north-west corner; Lagrange multiplier; Wolfe's modified method versus integer; transportation; nonlinear; quadratic programming.

1. A-III,B-II,C-IV,D-I
2. A-I,B-III,C-IV,D-II
3. A-II,B-I,C-IV,D-III
4. A-IV,B-I,C-II,D-III

**Correct answer:** 2 — A-I,B-III,C-IV,D-II

**Build the basics**

This question tests **Integer, transportation and nonlinear programming**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. Branch-and-bound is a standard integer-programming method; north-west corner constructs a transportation BFS.
2. Lagrange multipliers handle constrained nonlinear optimization; Wolfe's modified simplex handles quadratic programming.
3. Therefore A-I,B-III,C-IV,D-II.

**Conclusion**

The reasoning gives option 2: **A-I,B-III,C-IV,D-II**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

### 2025

---

#### Question 11

*UGC NET June 2025, original Q51*

Among 120 people, 65 eat rice, 45 bread, 42 curd; 20 eat rice and bread, 25 rice and curd, 15 bread and curd, and 8 all three. How many eat at least one?

1. 56
2. 100
3. 92
4. 65

**Correct answer:** 2 — 100

**Build the basics**

This question tests **Inclusion-exclusion principle**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Apply three-set inclusion–exclusion.
2. 65+45+42−20−25−15+8=100.

**Conclusion**

The reasoning gives option 2: **100**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 12

*UGC NET June 2025, original Q52*

From a pack of 42 cards, three are chosen one after another without replacement. In how many ways?

1. 1722
2. 1752
3. 68880
4. 6880

**Correct answer:** 3 — 68880

**Build the basics**

This question tests **Permutations**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. The wording 'one after another' makes order significant.
2. Use 42P3=42·41·40=68,880.

**Conclusion**

The reasoning gives option 3: **68880**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 13

*UGC NET June 2025, original Q53*

A positive integer is selected uniformly from 1 through 200. What is the probability that it is divisible by 2 or 5?

1. 2/5
2. 3/5
3. 4/5
4. 1/5

**Correct answer:** 2 — 3/5

**Build the basics**

This question tests **Discrete probability and inclusion-exclusion**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. There are 100 multiples of 2, 40 multiples of 5 and 20 multiples of 10.
2. Favourable count=100+40−20=120, so probability=120/200=3/5.

**Conclusion**

The reasoning gives option 2: **3/5**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 14

*UGC NET June 2025, original Q54*

For A(x,y,z)=x(y'z)', identify its complete sum-of-products form.

1. xyz+x'y'z'+x'y'z'
2. xyz'+x'y'z+x'y'z'
3. xyz'+xy'z+x'y'z'
4. xyz+xyz'+xy'z'

**Correct answer:** 4 — xyz+xyz'+xy'z'

**Build the basics**

This question tests **Canonical sum-of-products**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. De Morgan gives (y'z)'=y+z', so A=xy+xz'.
2. Expand to minterms: xy(z+z')+xz'(y+y')=xyz+xyz'+xy'z'.
3. Duplicate xyz' is retained once, giving option 4.

**Conclusion**

The reasoning gives option 4: **xyz+xyz'+xy'z'**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

---

#### Question 15

*UGC NET June 2025, original Q55*

Choose the correct statement for a group G.

1. If (xy)²=x²y² for all x,y, then G is commutative.
2. If x³=e for all x, then G is commutative.
3. If x⁵=e for all x, then G is commutative.
4. A subgroup of an abelian group need not be abelian.

**Correct answer:** 1 — If (xy)²=x²y² for all x,y, then G is commutative.

**Build the basics**

This question tests **Abelian groups**. A group has closure, associativity, an identity and inverses; an abelian group also commutes. Homomorphisms preserve the operation, automorphisms are isomorphisms from a structure to itself, and fields are commutative integral domains in which every nonzero element is invertible.

**Step-by-step reasoning**

1. xyxy=xxyy. Left-cancel x and right-cancel y to obtain yx=xy.
2. Groups of odd exponent can be nonabelian, so (2) and (3) are not general theorems.
3. Every subgroup inherits the operation and therefore commutes when G does; (4) is false.

**Conclusion**

The reasoning gives option 1: **If (xy)²=x²y² for all x,y, then G is commutative**.

**How to solve similar questions**

- **Rule to remember:** For finite G and H≤G, |H| divides |G| (Lagrange). Every finite integral domain is a field.
- **Fast exam method:** To refute an ideal claim, multiply a typical element on the left and right by a completely general ring element.
- **Common mistake to avoid:** A numerical divisibility fact does not establish that one group is a subgroup of another.

### 2024

---

#### Question 16

*UGC NET June 2024, original Q72*

Which have truth value true over all integers? A ∀n∃m(n²<m); B ∃n∀m(n<m²); C ∃n∃m(n²+m²=5); D ∃n∃m(n²+m²=6); E ∃n∃m(m+n=4 ∧ n−m=1).

1. A,B,C only
2. B,C,E only
3. C,D,E only
4. B,D only

**Correct answer:** 1 — A,B,C only

**Build the basics**

This question tests **Nested quantifiers over integers**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. A is true with m=n²+1; B is true with n=−1; C is true with (1,2).
2. No two integer squares sum to 6, so D is false.
3. Solving E gives half-integers n=5/2,m=3/2, so E is false.

**Conclusion**

The reasoning gives option 1: **A,B,C only**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 17

*UGC NET June 2024, original Q84*

Simplify F(A,B,C)=Σ(0,2,6) using don't-cares d(A,B,C)=Σ(1,3,5).

1. A'C'+BC'
2. B+AC
3. A+BC'
4. A'+BC'

**Correct answer:** 4 — A'+BC'

**Build the basics**

This question tests **Karnaugh-map simplification with don't-cares**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. Put 1 at minterms 0,2,6 and X at 1,3,5.
2. Group 0,1,2,3 to obtain A'. Group 2 and 6 to obtain BC'.
3. Hence F=A'+BC'.

**Conclusion**

The reasoning gives option 4: **A'+BC'**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

---

#### Question 18

*UGC NET June 2024, original Q88*

Arrange K₃, K₄, K₂,₂ and C₅ in increasing order of their numbers of spanning trees.

1. K₃,K₄,K₂,₂,C₅
2. K₃,K₂,₂,K₄,C₅
3. K₃,K₂,₂,C₅,K₄
4. C₅,K₄,K₂,₂,K₃

**Correct answer:** 3 — K₃,K₂,₂,C₅,K₄

**Build the basics**

This question tests **Spanning-tree enumeration**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. Cayley gives τ(K₃)=3 and τ(K₄)=16.
2. τ(K₂,₂)=2^(2−1)2^(2−1)=4 and a cycle C₅ has 5 spanning trees.
3. Thus 3<4<5<16.

**Conclusion**

The reasoning gives option 3: **K₃,K₂,₂,C₅,K₄**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 19

*UGC NET June 2024, original Q93*

A length-four bit string is uniformly random. Given that the first bit is 0, what is the probability that it contains at least three consecutive 0s?

1. 1/2
2. 5/16
3. 5/8
4. 1/4

**Correct answer:** 4 — 1/4

**Build the basics**

This question tests **Conditional probability on bit strings**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Conditioning on first bit 0 leaves 2³=8 equally likely strings.
2. Only 0000 and 0001 contain 000; hence 2/8=1/4.

**Conclusion**

The reasoning gives option 4: **1/4**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 20

*UGC NET June 2024, original Q96*

Arrange by increasing cardinality: A₁={{1,2},{3}}; A₂={{1},{2},{3},{4}}; A₃={{1,2,3,4,5,6}}; A₄={{1,2},{2,3,4},{5}}; A₅={{1},{2},{3},{4},{5}}.

1. A₁,A₂,A₄,A₅,A₃
2. A₁,A₂,A₅,A₄,A₃
3. A₁,A₃,A₄,A₂,A₅
4. A₃,A₁,A₄,A₂,A₅

**Correct answer:** 4 — A₃,A₁,A₄,A₂,A₅

**Build the basics**

This question tests **Cardinality of nested sets**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. Count top-level elements, not the numbers inside them: |A₁|=2, |A₂|=4, |A₃|=1, |A₄|=3, |A₅|=5.
2. Increasing order is A₃,A₁,A₄,A₂,A₅.

**Conclusion**

The reasoning gives option 4: **A₃,A₁,A₄,A₂,A₅**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 21

*UGC NET June 2024, original Q99*

Auditorium chairs are labelled by one letter followed by an integer from 01 through 99, starting A01. What is the maximum number of labels?

1. 2600
2. 2574
3. 2340
4. 2366

**Correct answer:** 2 — 2574

**Build the basics**

This question tests **Product rule**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. There are 26 choices for the letter and 99 choices from 01 through 99.
2. By the product rule, 26·99=2574.

**Conclusion**

The reasoning gives option 2: **2574**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 22

*UGC NET August 2024, original Q92*

Order the K-map steps: A group the largest clusters of 1s; B draw the K-map; C write the simplified expression; D transfer truth-table values.

1. B,D,A,C
2. D,B,A,C
3. B,A,D,C
4. A,B,C,D

**Correct answer:** 1 — B,D,A,C

**Build the basics**

This question tests **Karnaugh-map procedure**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. First draw the correctly labelled map, then transfer the values.
2. Next make maximal power-of-two groups, and finally translate groups into implicants: B,D,A,C.

**Conclusion**

The reasoning gives option 1: **B,D,A,C**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

---

#### Question 23

*UGC NET August 2024, original Q107*

A fair coin is tossed three times. For the event 'exactly one head or exactly two heads', assess A n(S)=8,n(E)=4; B n(E)=6,n(S)=8; C P(E)=3/4; D P(E)=1/2.

1. A,B,C,D
2. B,C only
3. A,D only
4. C,D only

**Correct answer:** 2 — B,C only

**Build the basics**

This question tests **Binomial probability**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. The sample space has 8 outcomes.
2. There are C(3,1)+C(3,2)=3+3=6 favourable outcomes, so P=6/8=3/4.
3. Thus B and C alone are true.

**Conclusion**

The reasoning gives option 2: **B,C only**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 24

*UGC NET August 2024, original Q124*

On {1,2,3,4}, which listed relations are reflexive? R₁={(1,1),(1,2),(2,1),(2,2),(3,4),(4,1),(4,4)}; R₂={(1,1),(1,2),(2,1)}; R₃={(1,1),(1,2),(1,4),(2,1),(2,2),(3,3),(4,1),(4,4)}; R₄={(2,1),(3,1),(3,2),(4,1),(4,2),(4,3)}; R₅={(1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)}.

1. R₁,R₂,R₃
2. R₁,R₄,R₅
3. R₄,R₅
4. R₃,R₅

**Correct answer:** 4 — R₃,R₅

**Build the basics**

This question tests **Reflexive relations**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. Reflexivity requires all four diagonal pairs.
2. R₃ and R₅ contain (1,1),(2,2),(3,3),(4,4). Each of R₁,R₂,R₄ misses at least one.
3. Therefore R₃,R₅ only.

**Conclusion**

The reasoning gives option 4: **R₃,R₅**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 25

*UGC NET August 2024, original Q126*

Match: A same colour when drawing 2 from 6 white,4 red; B king or queen from 52 cards; C 1 red,2 white from 6R,4W,8B; D 2 blue,1 red from that bag, with I 3/68, II 14/68, III 2/13, IV 7/15.

1. A-II,B-IV,C-I,D-III
2. A-III,B-IV,C-II,D-I
3. A-IV,B-III,C-II,D-I
4. A-IV,B-III,C-I,D-II

**Correct answer:** 4 — A-IV,B-III,C-I,D-II

**Build the basics**

This question tests **Hypergeometric probability**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. A=[C(6,2)+C(4,2)]/C(10,2)=21/45=7/15=IV; B=8/52=2/13=III.
2. C=C(6,1)C(4,2)/C(18,3)=36/816=3/68=I.
3. D=C(8,2)C(6,1)/C(18,3)=168/816=14/68=II.

**Conclusion**

The reasoning gives option 4: **A-IV,B-III,C-I,D-II**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 26

*UGC NET August 2024, original Q127*

For n≥3, Dirac's sufficient condition guarantees that G is Hamiltonian when every vertex has degree at least what?

1. n
2. 2n
3. n/2
4. 4n

**Correct answer:** 3 — n/2

**Build the basics**

This question tests **Hamiltonian circuits**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. Dirac's theorem states δ(G)≥n/2 for a simple n-vertex graph with n≥3.
2. This condition is sufficient, not necessary.

**Conclusion**

The reasoning gives option 3: **n/2**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 27

*UGC NET August 2024, original Q135*

Match Dijkstra, Floyd–Warshall, Bellman–Ford and Prim with the four descriptions printed in List II.

1. A-II,B-I,C-III,D-IV
2. A-II,B-I,C-IV,D-III
3. A-I,B-II,C-III,D-IV
4. A-III,B-II,C-IV,D-I

**Correct answer:** 2 — A-II,B-I,C-IV,D-III

**Build the basics**

This question tests **Shortest paths and spanning-tree algorithms**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. The intended matches are Dijkstra→single-source nonnegative weights (II) and Floyd–Warshall→all-pairs paths (I).
2. The paper's descriptions III and IV are corrupted/misprinted: bubble sort and strongly connected components do not describe Prim or Bellman–Ford.
3. Option 2 is the only option preserving the two valid matches and is therefore the intended key, but the item is defective.

**Conclusion**

The reasoning gives option 2: **A-II,B-I,C-IV,D-III**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

> **Important wording note:** List-II items III and IV do not match either Bellman–Ford or Prim. Treat option 2 as intended, not as a technically valid full matching.

### 2023

---

#### Question 28

*UGC NET June 2023, original Q2*

Match A A△B; B A−(B∪C); C A−(B∩C); D A∩(B−C) with I (A−B)∪(A−C); II (A−B)∩(A−C); III (A−B)∪(B−A); IV (A∩B)−(A∩C).

1. A-III,B-II,C-I,D-IV
2. A-II,B-I,C-IV,D-III
3. A-I,B-IV,C-II,D-III
4. A-IV,B-III,C-I,D-II

**Correct answer:** 1 — A-III,B-II,C-I,D-IV

**Build the basics**

This question tests **Set operations and symmetric difference**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. Symmetric difference is III. De Morgan set laws give A−(B∪C)=(A−B)∩(A−C)=II and A−(B∩C)=(A−B)∪(A−C)=I.
2. A∩(B−C)=(A∩B)−(A∩C)=IV.

**Conclusion**

The reasoning gives option 1: **A-III,B-II,C-I,D-IV**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 29

*UGC NET June 2023, original Q19*

On N×N, (a,b)R(c,d) iff ad(b+c)=bc(a+d). What kind of relation is R?

1. Reflexive only
2. Symmetric only
3. Partial order
4. Equivalence relation

**Correct answer:** 4 — Equivalence relation

**Build the basics**

This question tests **Equivalence relations**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. Divide by abcd (positive): the condition becomes 1/a+1/b=1/c+1/d.
2. Equality of the value f(a,b)=1/a+1/b is reflexive, symmetric and transitive.
3. Therefore R is an equivalence relation.

**Conclusion**

The reasoning gives option 4: **Equivalence relation**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 30

*UGC NET June 2023, original Q30*

Assess: A a monoid identity is unique; B a monoid is a group if every element has an inverse; C a semigroup requires closure, associativity and identity; D a quasigroup is closed under its operation.

1. A,B only
2. A,B,D only
3. B,C,D only
4. A,C only

**Correct answer:** 2 — A,B,D only

**Build the basics**

This question tests **Semigroups and monoids**. A group has closure, associativity, an identity and inverses; an abelian group also commutes. Homomorphisms preserve the operation, automorphisms are isomorphisms from a structure to itself, and fields are commutative integral domains in which every nonzero element is invertible.

**Step-by-step reasoning**

1. A and B are defining theorems. C is false because identity is not required for a semigroup.
2. A quasigroup is a set with a closed binary operation satisfying unique division, so D is true.
3. Hence A,B,D.

**Conclusion**

The reasoning gives option 2: **A,B,D only**.

**How to solve similar questions**

- **Rule to remember:** For finite G and H≤G, |H| divides |G| (Lagrange). Every finite integral domain is a field.
- **Fast exam method:** To refute an ideal claim, multiply a typical element on the left and right by a completely general ring element.
- **Common mistake to avoid:** A numerical divisibility fact does not establish that one group is a subgroup of another.

---

#### Question 31

*UGC NET June 2023, original Q66*

Match PERT, optimistic time, CPM and pessimistic time with non-repetitive projects, repetitive projects, shortest time and longest time.

1. A-I,B-II,C-III,D-IV
2. A-II,B-IV,C-I,D-III
3. A-IV,B-I,C-III,D-II
4. A-I,B-III,C-II,D-IV

**Correct answer:** 4 — A-I,B-III,C-II,D-IV

**Build the basics**

This question tests **PERT-CPM terminology**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. PERT is probabilistic and suited to non-repetitive projects; CPM is deterministic and commonly used for repetitive projects.
2. Optimistic is the shortest plausible time and pessimistic the longest.
3. Thus A-I,B-III,C-II,D-IV.

**Conclusion**

The reasoning gives option 4: **A-I,B-III,C-II,D-IV**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

---

#### Question 32

*UGC NET June 2023, original Q70*

There are m marked points on AB and n on AC, excluding A. How many triangles can be formed using these points together with A?

1. mn(m+n−1)/2
2. mn(m+n−2)/2
3. mn(m+n)/2
4. mn

**Correct answer:** 2 — mn(m+n−2)/2

**Build the basics**

This question tests **Combinations and geometric counting**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. A non-collinear triple must use points from both rays.
2. Choose two from AB and one from AC, or one from AB and two from AC: C(m,2)n+mC(n,2).
3. This equals mn[(m−1)+(n−1)]/2=mn(m+n−2)/2.

**Conclusion**

The reasoning gives option 2: **mn(m+n−2)/2**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 33

*UGC NET June 2023, original Q81*

Requests arrive at a mean rate 20 per hour. Under a Poisson model, what is the probability of no request during 45 minutes?

1. e^(−20)
2. e^(−15)
3. 15e^(−15)
4. 1−e^(−15)

**Correct answer:** 2 — e^(−15)

**Build the basics**

This question tests **Poisson distribution**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. For 45 minutes the mean is λt=20·3/4=15.
2. Poisson P(X=0)=e^(−15)15⁰/0!=e^(−15).

**Conclusion**

The reasoning gives option 2: **e^(−15)**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 34

*UGC NET June 2023, original Q85*

How many automorphisms does the additive group (Z,+) have?

1. 1
2. 2
3. Countably infinite
4. Uncountably infinite

**Correct answer:** 2 — 2

**Build the basics**

This question tests **Automorphisms of the integers**. A group has closure, associativity, an identity and inverses; an abelian group also commutes. Homomorphisms preserve the operation, automorphisms are isomorphisms from a structure to itself, and fields are commutative integral domains in which every nonzero element is invertible.

**Step-by-step reasoning**

1. A homomorphism is determined by f(1)=k and has f(n)=kn.
2. It is bijective only for k=1 or k=−1.
3. Hence there are two automorphisms.

**Conclusion**

The reasoning gives option 2: **2**.

**How to solve similar questions**

- **Rule to remember:** For finite G and H≤G, |H| divides |G| (Lagrange). Every finite integral domain is a field.
- **Fast exam method:** To refute an ideal claim, multiply a typical element on the left and right by a completely general ring element.
- **Common mistake to avoid:** A numerical divisibility fact does not establish that one group is a subgroup of another.

---

#### Question 35

*UGC NET Dec 2022 Mar 15 Shift 1, original Q1*

Which is not logically equivalent to P→Q?

1. ¬P∨Q
2. ¬Q→¬P
3. ¬(P∧¬Q)
4. ¬Q→P

**Correct answer:** 4 — ¬Q→P

**Build the basics**

This question tests **Propositional equivalence**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. P→Q is ¬P∨Q and equals its contrapositive ¬Q→¬P.
2. Negating the sole falsifying case gives ¬(P∧¬Q).
3. ¬Q→P is Q∨P, which differs; take P=false,Q=true.

**Conclusion**

The reasoning gives option 4: **¬Q→P**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 36

*UGC NET Dec 2022 Mar 15 Shift 1, original Q2*

Seven distinct people leave a lift at three ordered stops, with at least one person at every stop. How many assignments are possible?

1. 2187
2. 1932
3. 1806
4. 1260

**Correct answer:** 3 — 1806

**Build the basics**

This question tests **Inclusion-exclusion and onto functions**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Count onto functions from 7 people to 3 stops.
2. 3⁷−C(3,1)2⁷+C(3,2)1⁷=2187−384+3=1806.

**Conclusion**

The reasoning gives option 3: **1806**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 37

*UGC NET Dec 2022 Mar 15 Shift 1, original Q4*

Students receive one of seven grades. What minimum class size guarantees at least six students with the same grade?

1. 35
2. 42
3. 36
4. 43

**Correct answer:** 3 — 36

**Build the basics**

This question tests **Pigeonhole principle**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. To avoid six in any grade, place at most five in each of seven boxes: 7·5=35.
2. One more student forces a box to contain six, so the minimum is 36.

**Conclusion**

The reasoning gives option 3: **36**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 38

*UGC NET Dec 2022 Mar 15 Shift 1, original Q6*

Simplify F(A,B,C,D)=Σ(3,4,5,6,7,11,15).

1. AB+C'D
2. A'B+CD
3. AC+BD
4. A'B+B'C

**Correct answer:** 2 — A'B+CD

**Build the basics**

This question tests **Karnaugh-map simplification**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. Minterms 4,5,6,7 form the implicant A'B.
2. Minterms 3,7,11,15 form CD.
3. Together they cover exactly the specified set, so F=A'B+CD.

**Conclusion**

The reasoning gives option 2: **A'B+CD**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

---

#### Question 39

*UGC NET Dec 2022 Mar 15 Shift 1, original Q41*

Which group statements are correct? A every group has a zero element; B the only idempotent is identity; C an isomorphism G→G is an automorphism; D if every element is self-inverse then G is abelian.

1. B,C,D only
2. A,B,C
3. A,C,D
4. B,D only

**Correct answer:** 1 — B,C,D only

**Build the basics**

This question tests **Group properties**. A group has closure, associativity, an identity and inverses; an abelian group also commutes. Homomorphisms preserve the operation, automorphisms are isomorphisms from a structure to itself, and fields are commutative integral domains in which every nonzero element is invertible.

**Step-by-step reasoning**

1. A is false: groups require an identity, not a separate zero.
2. If x²=x, cancellation gives x=e, so B is true; C is the definition of automorphism.
3. If x=x⁻¹, then xy=(xy)⁻¹=y⁻¹x⁻¹=yx, so D is true.

**Conclusion**

The reasoning gives option 1: **B,C,D only**.

**How to solve similar questions**

- **Rule to remember:** For finite G and H≤G, |H| divides |G| (Lagrange). Every finite integral domain is a field.
- **Fast exam method:** To refute an ideal claim, multiply a typical element on the left and right by a completely general ring element.
- **Common mistake to avoid:** A numerical divisibility fact does not establish that one group is a subgroup of another.

---

#### Question 40

*UGC NET Dec 2022 Mar 15 Shift 1, original Q43*

For R={(1,3),(1,1),(3,1),(1,2),(3,3),(4,4)} on {1,2,3,4}, which classification is correct?

1. Reflexive and symmetric
2. Symmetric and transitive
3. Reflexive only
4. Neither reflexive, symmetric nor transitive

**Correct answer:** 4 — Neither reflexive, symmetric nor transitive

**Build the basics**

This question tests **Relation properties**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. (2,2) is absent, so R is not reflexive. (1,2) is present but (2,1) absent, so not symmetric.
2. (3,1) and (1,2) occur but (3,2) does not, so it is not transitive.

**Conclusion**

The reasoning gives option 4: **Neither reflexive, symmetric nor transitive**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 41

*UGC NET Dec 2022 Mar 15 Shift 1, original Q66*

Match linear programming, predicate logic, tree traversal and minimum spanning tree with Simplex, first-order logic, inorder and Prim.

1. A-I,B-II,C-III,D-IV
2. A-III,B-IV,C-II,D-I
3. A-IV,B-III,C-I,D-II
4. A-II,B-I,C-IV,D-III

**Correct answer:** 2 — A-III,B-IV,C-II,D-I

**Build the basics**

This question tests **Method classification**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. LP→Simplex (III), predicate logic→first-order logic (IV), traversal→inorder (II), MST→Prim (I).
2. This gives A-III,B-IV,C-II,D-I.

**Conclusion**

The reasoning gives option 2: **A-III,B-IV,C-II,D-I**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

---

#### Question 42

*UGC NET Dec 2022 Mar 11 Shift 2, original Q1*

What is the negation of 'Some students like hockey'?

1. Some students dislike hockey
2. Every student dislikes hockey
3. No student dislikes hockey
4. Every student likes hockey

**Correct answer:** 2 — Every student dislikes hockey

**Build the basics**

This question tests **Negating quantified statements**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. The statement is ∃x(Student(x)∧LikesHockey(x)).
2. Its negation is ∀x(Student(x)→¬LikesHockey(x)): every student does not like hockey.

**Conclusion**

The reasoning gives option 2: **Every student dislikes hockey**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 43

*UGC NET Dec 2022 Mar 11 Shift 2, original Q2*

On integer pairs define (x,y)R(u,v) iff x<u and y>v. Which classification applies under the paper's reflexive definition of partial order?

1. Neither partial order nor equivalence relation
2. Partial but not total order
3. Total order
4. Equivalence relation

**Correct answer:** 1 — Neither partial order nor equivalence relation

**Build the basics**

This question tests **Strict partial orders**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. R is irreflexive because x<x is false; hence it is not a (reflexive) partial order and not an equivalence relation.
2. It is a strict partial order in terminology that uses irreflexive+transitive; the options use the non-strict convention.

**Conclusion**

The reasoning gives option 1: **Neither partial order nor equivalence relation**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

> **Important wording note:** Terminology-sensitive: R is a strict partial order, but not a reflexive partial order.

---

#### Question 44

*UGC NET Dec 2022 Mar 11 Shift 2, original Q4*

A nested conditional returns true for (x>25,y>100), false; (x≤25,y≤100), true; (x>25,y≤100), false; otherwise true. When is the overall result true?

1. iff y≤100
2. iff x≤25
3. iff x>25
4. iff y>100

**Correct answer:** 2 — iff x≤25

**Build the basics**

This question tests **Boolean conditions**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. The four branches partition all possibilities.
2. Both branches with x>25 are false and both with x≤25 are true, independent of y.
3. Therefore the result is true iff x≤25.

**Conclusion**

The reasoning gives option 2: **iff x≤25**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 45

*UGC NET Dec 2022 Mar 11 Shift 2, original Q7*

Simplify F=Σ(0,2,5,7,8,10,13,15).

1. BD+B'D'
2. B'D+BD'
3. A'C'+AC
4. C'D+CD'

**Correct answer:** 1 — BD+B'D'

**Build the basics**

This question tests **Karnaugh-map simplification**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. The minterms are precisely those for which B and D are equal; A and C vary freely.
2. Thus F=BD+B'D', the XNOR of B and D.

**Conclusion**

The reasoning gives option 1: **BD+B'D'**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

---

#### Question 46

*UGC NET Dec 2022 Mar 11 Shift 2, original Q42*

Assess: A a Boolean algebra can have five elements; B complements are unique; C a Boolean-algebra lattice is not relatively complemented; D a product of Boolean algebras is Boolean.

1. A,C
2. B,D
3. A,B,D
4. B,C,D

**Correct answer:** 2 — B,D

**Build the basics**

This question tests **Structure of Boolean algebras**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. Finite Boolean algebras have 2^n elements, so A is false. Complements are unique, so B true.
2. Boolean algebras are complemented (indeed relatively complemented), so C false; products preserve Boolean operations, so D true.

**Conclusion**

The reasoning gives option 2: **B,D**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

---

#### Question 47

*UGC NET Dec 2022 Mar 11 Shift 2, original Q66*

Match planar graph, bipartite graph, PERT and CPM with 4-colourable, 2-colourable, probabilistic and deterministic.

1. A-I,B-II,C-III,D-IV
2. A-II,B-III,C-IV,D-I
3. A-IV,B-I,C-II,D-III
4. A-III,B-IV,C-I,D-II

**Correct answer:** 4 — A-III,B-IV,C-I,D-II

**Build the basics**

This question tests **PERT-CPM and graph colouring**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. Every planar graph is 4-colourable; a bipartite graph is 2-colourable.
2. PERT is probabilistic and CPM deterministic.
3. So A-III,B-IV,C-I,D-II.

**Conclusion**

The reasoning gives option 4: **A-III,B-IV,C-I,D-II**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

### 2022

---

#### Question 48

*UGC NET October 2022, original Q2*

Three equiprobable boxes contain respectively (2W,3B,4R), (3W,2B,2R), and (4W,1B,3R). Given that two drawn balls are one white and one red, what is the probability that box 1 was chosen?

1. 0.237
2. 0.723
3. 0.18
4. 0.452

**Correct answer:** 1 — 0.237

**Build the basics**

This question tests **Bayes theorem**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Likelihoods of WR are 8/C(9,2)=2/9, 6/C(7,2)=2/7 and 12/C(8,2)=3/7.
2. Equal box priors cancel in Bayes' ratio.
3. Posterior=(2/9)/(2/9+2/7+3/7)=14/59≈0.2373.

**Conclusion**

The reasoning gives option 1: **0.237**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 49

*UGC NET October 2022, original Q10*

For the printed equality-constrained maximization problem and proposed dual, which statement about the dual formulation is correct?

1. Dual objective and constraints are correct
2. Only objective is correct
3. Only constraints are correct
4. Neither is correct

**Correct answer:** 1 — Dual objective and constraints are correct

**Build the basics**

This question tests **Duality in linear programming**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. Equality constraints in a primal make the corresponding dual variables unrestricted in sign.
2. A maximization primal with nonnegative variables yields ≥ constraints in the dual when written with equality rows and unrestricted dual variables.
3. Using Aᵀy≥c and bᵀy gives the printed dual.

**Conclusion**

The reasoning gives option 1: **Dual objective and constraints are correct**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

> **Important wording note:** The source's OCR drops some subscripts; use PDF page 4 for the complete displayed primal/dual.

---

#### Question 50

*UGC NET October 2022, original Q64*

For ε=0.0005, define x Rε y iff |x−y|<ε. Which properties hold: A reflexive, B symmetric, C transitive?

1. A,B only
2. B,C only
3. A,C only
4. A,B,C

**Correct answer:** 1 — A,B only

**Build the basics**

This question tests **Approximate-equality relation**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. |x−x|=0<ε, so reflexive. Absolute distance is symmetric.
2. Transitivity fails: choose x=0,y=0.0004,z=0.0008. The first two gaps are <ε but |x−z| is not.
3. Thus A and B only.

**Conclusion**

The reasoning gives option 1: **A,B only**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 51

*UGC NET October 2022, original Q83*

Assess X: a∨[b∧(a∨c)]=(a∨b)∧(a∨c); Y: a∨(b∧c)=(a∨b)∧c.

1. X only
2. Y only
3. Both X and Y
4. Neither/dependent

**Correct answer:** 1 — X only

**Build the basics**

This question tests **Distributive identities**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. For X, absorption gives the left side a∨bc and distributivity gives the same right side.
2. Y is false; a=1,c=0 makes its left side 1 and right side 0.
3. Hence X only.

**Conclusion**

The reasoning gives option 1: **X only**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

---

#### Question 52

*UGC NET October 2022, original Q89*

Statement I: a grandparent is a parent of one's parent. Statement II: ∀g∀c[grandparent(g,c)→∃p(parent(g,p)∧parent(p,c))]. Assess them.

1. Both correct
2. Both incorrect
3. I correct, II incorrect
4. I incorrect, II correct

**Correct answer:** 1 — Both correct

**Build the basics**

This question tests **First-order predicate representation**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. Statement I gives the usual defining condition.
2. Statement II correctly says that whenever g is c's grandparent, an intermediate parent p exists.
3. Both statements are correct (though a biconditional would be needed for a complete definition).

**Conclusion**

The reasoning gives option 1: **Both correct**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

### 2021

---

#### Question 53

*UGC NET November 2021, original Q28*

Match A x+x=x; B x+0=x; C x+1=1; D x+xy=x with idempotent, identity, domination and absorption laws.

1. A-III,B-I,C-II,D-IV
2. A-I,B-II,C-III,D-IV
3. A-III,B-I,C-IV,D-II
4. A-II,B-IV,C-I,D-III

**Correct answer:** 3 — A-III,B-I,C-IV,D-II

**Build the basics**

This question tests **Boolean identities**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. x+x=x is idempotent (III); x+0=x is identity (I).
2. x+1=1 is domination (IV); x+xy=x is absorption (II).
3. Therefore option 3 is mathematically correct.

**Conclusion**

The reasoning gives option 3: **A-III,B-I,C-IV,D-II**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

> **Important wording note:** The supplied answer marks option 1, which swaps domination and absorption. Independent Boolean-algebra verification gives option 3.

---

#### Question 54

*UGC NET November 2021, original Q30*

Maximize 6x+5y subject to 2x−3y≤5, x+3y≤11, 4x+y≤15, x,y≥0. Find the optimum value.

1. 15
2. 25
3. 349/11
4. 30

**Correct answer:** 3 — 349/11

**Build the basics**

This question tests **Graphical solution of a linear program**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. The binding intersection x+3y=11 and 4x+y=15 gives x=34/11,y=29/11.
2. It satisfies 2x−3y≤5.
3. Objective=6(34/11)+5(29/11)=349/11≈31.73, larger than the other feasible vertices.

**Conclusion**

The reasoning gives option 3: **349/11**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

> **Important wording note:** The marked answer 15 is inconsistent with direct evaluation; (34/11,29/11) is feasible and yields 349/11.

### 2020

---

#### Question 55

*UGC NET November 2020, original Q51*

How many positive integers not exceeding 100 are either odd or perfect squares?

1. 63
2. 59
3. 55
4. 50

**Correct answer:** 3 — 55

**Build the basics**

This question tests **Inclusion-exclusion**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. There are 50 odd numbers and 10 squares 1² through 10².
2. Five squares are odd: 1,9,25,49,81.
3. Union size=50+10−5=55.

**Conclusion**

The reasoning gives option 3: **55**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 56

*UGC NET November 2020, original Q52*

In how many ways can six identical books be packed into four identical boxes, with empty boxes allowed?

1. 4
2. 6
3. 7
4. 9

**Correct answer:** 4 — 9

**Build the basics**

This question tests **Integer partitions**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Identical boxes mean unordered partitions of 6 into at most four positive parts.
2. The partitions are 6; 5+1; 4+2; 4+1+1; 3+3; 3+2+1; 3+1+1+1; 2+2+2; 2+2+1+1.
3. There are 9.

**Conclusion**

The reasoning gives option 4: **9**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 57

*UGC NET November 2020, original Q53*

Which pair is not logically equivalent?

1. [(p→r)∧(q→r)] and [(p∨q)→r]
2. p→q and ¬q→¬p
3. [(p∧q)∨(¬p∧¬q)] and p↔q
4. [(p∧q)→r] and [(p→r)∧(q→r)]

**Correct answer:** 4 — [(p∧q)→r] and [(p→r)∧(q→r)]

**Build the basics**

This question tests **Propositional equivalence**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. Options 1–3 are respectively implication distribution, contraposition and the standard biconditional expansion.
2. For option 4 take p=true,q=false,r=false: (p∧q)→r is true, but (p→r)∧(q→r) is false.
3. Therefore pair 4 is not equivalent.

**Conclusion**

The reasoning gives option 4: **[(p∧q)→r] and [(p→r)∧(q→r)]**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 58

*UGC NET November 2020, original Q54*

Maximize z=2x₁+3x₂ subject to 2x₁+x₂≤4, x₁+2x₂≤5, x₁,x₂≥0. Find the optimum.

1. 23
2. 9.5
3. 18
4. 8

**Correct answer:** 4 — 8

**Build the basics**

This question tests **Graphical linear programming**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. The constraint intersection is x₁=1,x₂=2.
2. Its objective is 2+6=8; axis vertices give at most 7.5 and 4.
3. Thus the optimum is 8.

**Conclusion**

The reasoning gives option 4: **8**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

---

#### Question 59

*UGC NET November 2020, original Q88*

What kind of clauses occur in conjunctive normal form?

1. Disjunctions of literals
2. Disjunctions of variables
3. Conjunctions of literals
4. Conjunctions of variables

**Correct answer:** 1 — Disjunctions of literals

**Build the basics**

This question tests **Conjunctive normal form**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. A literal is a variable or its negation.
2. CNF is a conjunction of clauses, and each clause is a disjunction of literals.

**Conclusion**

The reasoning gives option 1: **Disjunctions of literals**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 60

*UGC NET November 2020, original Q89*

On {a,b,c,d,e,f,g}, R={(a,a),(b,b),(c,d),(c,g),(d,g),(e,e),(f,f),(g,g)}. Which listed properties hold: A reflexive, B antisymmetric, C symmetric?

1. A only
2. C only
3. A and B
4. B and not A

**Correct answer:** 4 — B and not A

**Build the basics**

This question tests **Reflexive, symmetric and antisymmetric properties**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. (c,c) and (d,d) are absent, so not reflexive.
2. No distinct pair appears in both directions, hence antisymmetric.
3. (c,d) lacks (d,c), so not symmetric. Thus B and not A.

**Conclusion**

The reasoning gives option 4: **B and not A**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 61

*UGC NET November 2020, original Q90*

A purported proof derives P(c) and Q(c) separately from P(c)∨Q(c), then generalizes. Which step is invalid?

1. Proof is valid
2. Steps deriving P(c) and Q(c) by simplification
3. Only universal-generalization steps
4. Only final conjunction

**Correct answer:** 2 — Steps deriving P(c) and Q(c) by simplification

**Build the basics**

This question tests **Rules of inference**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. Simplification applies to a conjunction, not a disjunction.
2. From P(c)∨Q(c) neither disjunct follows by itself, so both claimed simplification steps are invalid.
3. All later steps rest on those invalid inferences.

**Conclusion**

The reasoning gives option 2: **Steps deriving P(c) and Q(c) by simplification**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 62

*UGC NET November 2020, original Q103*

Which of A–E are incorrect? A every tree is 2-colourable; B a bipartite graph has no even cycle; C G is 2-colourable iff bipartite; D maximum degree d permits d+1 colours; E O(|V|) edges imply O(log|V|) colours.

1. C,E
2. B,C
3. B,E
4. A,D

**Correct answer:** 3 — B,E

**Build the basics**

This question tests **Graph colouring**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. A,C,D are standard true bounds/characterizations.
2. B is false: bipartite graphs exclude odd cycles, not even cycles.
3. E is false; a clique on Θ(√V) vertices plus isolated vertices has O(V) edges but needs Θ(√V) colours. Hence B,E.

**Conclusion**

The reasoning gives option 3: **B,E**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

### 2019

---

#### Question 63

*UGC NET December 2019, original Q51*

A non-degenerate basic feasible solution of an m×n transportation problem contains exactly how many allocations, in what kind of positions?

1. m+n+1, independent
2. m+n−1, independent
3. m+n−1, appropriate
4. m−n+1, independent

**Correct answer:** 2 — m+n−1, independent

**Build the basics**

This question tests **Transportation basic feasible solutions**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. The transportation constraint matrix has rank m+n−1 for a balanced problem.
2. A non-degenerate BFS therefore has exactly m+n−1 positive basic allocations, and their cells must be independent (contain no closed loop).

**Conclusion**

The reasoning gives option 2: **m+n−1, independent**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

---

#### Question 64

*UGC NET December 2019, original Q52*

Maximize z=x₁+x₂ subject to x₁+2x₂≤2000, x₁+x₂≤1500, x₂≤600 and x₁,x₂≥0. Which listed solution is feasible and optimal?

1. x₁=750,x₂=750,z=1500
2. x₁=500,x₂=1000,z=1500
3. x₁=1000,x₂=500,z=1500
4. x₁=900,x₂=600,z=1500

**Correct answer:** 3 — x₁=1000,x₂=500,z=1500

**Build the basics**

This question tests **Graphical linear programming**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. The objective cannot exceed 1500 because x₁+x₂≤1500.
2. Option 3 attains 1500 and satisfies 1000+2(500)=2000 and x₂≤600.
3. Each other listed point violates either x₂≤600 or the first constraint.

**Conclusion**

The reasoning gives option 3: **x₁=1000,x₂=500,z=1500**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

---

#### Question 65

*UGC NET December 2019, original Q53*

The expression AB+A'B+AC+A'C is unaffected by which variable?

1. A
2. B
3. C
4. A,B,C

**Correct answer:** 1 — A

**Build the basics**

This question tests **Variable dependence**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. Factor B(A+A')+C(A+A').
2. Since A+A'=1, the expression is B+C.
3. A disappears, so changing A has no effect.

**Conclusion**

The reasoning gives option 1: **A**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

---

#### Question 66

*UGC NET December 2019, original Q54*

Find GLB and LUB under divisibility for A={3,9,12} and B={1,2,4,5,10}.

1. A:3,36; B:1,20
2. A:3,12; B:1,10
3. A:1,36; B:2,20
4. A:1,12; B:2,10

**Correct answer:** 1 — A:3,36; B:1,20

**Build the basics**

This question tests **Bounds in a divisibility poset**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. In the positive-integer divisibility poset, GLB is gcd and LUB is lcm.
2. gcd(A)=3,lcm(A)=36; gcd(B)=1,lcm(B)=20.

**Conclusion**

The reasoning gives option 1: **A:3,36; B:1,20**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 67

*UGC NET December 2019, original Q55*

On all people, aRb iff a is a brother of b. Is R symmetric, transitive, an equivalence relation, or a partial order?

1. No,No,No,No
2. No,No,Yes,No
3. No,Yes,No,No
4. No,Yes,Yes,No

**Correct answer:** 1 — No,No,No,No

**Build the basics**

This question tests **Properties of relations**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. If a male is brother of a female b, b is not a brother of a; thus not symmetric.
2. Sibling relations are not transitive: two people may each be siblings of b without being siblings of one another (e.g. blended families).
3. It is neither reflexive/equivalence nor a partial order.

**Conclusion**

The reasoning gives option 1: **No,No,No,No**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 68

*UGC NET December 2019, original Q57*

A tree has 2n vertices of degree 1, 3n of degree 2 and n of degree 3. Find its numbers of vertices and edges.

1. 12,11
2. 11,12
3. 10,11
4. 9,10

**Correct answer:** 1 — 12,11

**Build the basics**

This question tests **Trees and degree sum**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. V=6n and E=6n−1. The degree sum is 2n+6n+3n=11n.
2. Set 11n=2E=12n−2, giving n=2.
3. Hence V=12,E=11.

**Conclusion**

The reasoning gives option 1: **12,11**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 69

*UGC NET December 2019, original Q58*

How many reflexive relations exist on a four-element set?

1. 2¹²
2. 2²
3. 4²
4. 2

**Correct answer:** 1 — 2¹²

**Build the basics**

This question tests **Counting reflexive relations**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. All four diagonal pairs are forced.
2. The remaining 16−4=12 ordered pairs may each be included or excluded independently.
3. Count=2¹².

**Conclusion**

The reasoning gives option 1: **2¹²**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 70

*UGC NET December 2019, original Q84*

An ___ chart represents a project as a directed graph. The critical path is the ___ sequence of ___ tasks and defines project ___.

1. Activity,shortest,independent,cost
2. Activity,longest,dependent,duration
3. Activity,longest,independent,duration
4. Activity,shortest,dependent,duration

**Correct answer:** 2 — Activity,longest,dependent,duration

**Build the basics**

This question tests **Critical path method**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. An activity network is directed by precedence dependencies.
2. The critical path is the longest-duration sequence of dependent activities, and its length is the project duration.

**Conclusion**

The reasoning gives option 2: **Activity,longest,dependent,duration**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

---

#### Question 71

*UGC NET December 2019, original Q86*

A clique in an undirected graph is a vertex subset V' such that:

1. Every graph edge has both ends in V'
2. Every loop has an end in V'
3. Each pair of vertices in V' is joined by an edge
4. No pair in V' is joined

**Correct answer:** 3 — Each pair of vertices in V' is joined by an edge

**Build the basics**

This question tests **Cliques**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. The induced subgraph on a clique is complete.
2. Equivalently, every two distinct vertices selected in V' are adjacent.

**Conclusion**

The reasoning gives option 3: **Each pair of vertices in V' is joined by an edge**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 72

*UGC NET December 2019, original Q109*

S1 says (∀xP(x))∨(∀xQ(x)) and ∀x(P(x)∨Q(x)) are not equivalent. S2 says (∃xP(x))∧(∃xQ(x)) and ∃x(P(x)∧Q(x)) are not equivalent. Which are correct?

1. S1 only
2. S2 only
3. Both
4. Neither

**Correct answer:** 3 — Both

**Build the basics**

This question tests **Quantifiers and distribution**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. For S1, different objects may satisfy P and Q, making the second formula true while neither universal disjunct is true.
2. For S2, the two existential witnesses may differ, so the first can be true while no object satisfies both.
3. Both non-equivalence statements are correct.

**Conclusion**

The reasoning gives option 3: **Both**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 73

*UGC NET June 2019, original Q51*

For the poset ({3,5,9,15,24,45}, divides), which extremal elements exist?

1. Both greatest and least
2. Greatest but no least
3. Least but no greatest
4. Neither greatest nor least

**Correct answer:** 4 — Neither greatest nor least

**Build the basics**

This question tests **Partial orders under divisibility**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. A least element would have to divide every member; none of the listed elements divides both 3 and 5.
2. A greatest element must be divisible by every member; none is divisible by both 24 and 45.
3. Therefore neither exists.

**Conclusion**

The reasoning gives option 4: **Neither greatest nor least**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 74

*UGC NET June 2019, original Q53*

How many length-ten bit strings start with 1 or end with 00?

1. 320
2. 480
3. 640
4. 768

**Correct answer:** 3 — 640

**Build the basics**

This question tests **Inclusion-exclusion on bit strings**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Start with 1:2⁹. End with 00:2⁸. Both:2⁷.
2. Inclusion–exclusion gives 512+256−128=640.

**Conclusion**

The reasoning gives option 3: **640**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 75

*UGC NET June 2019, original Q54*

A connected planar graph has six vertices, each degree four. Into how many regions does a planar embedding divide the plane?

1. 6
2. 8
3. 12
4. 20

**Correct answer:** 2 — 8

**Build the basics**

This question tests **Euler formula for planar graphs**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. Degree sum=6·4=24=2E, so E=12.
2. Euler gives F=2−V+E=2−6+12=8.

**Conclusion**

The reasoning gives option 2: **8**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 76

*UGC NET June 2019, original Q55*

For what m,n does Kₘ,ₙ have a Hamilton circuit?

1. m≠n and both≥2
2. m≠n and both≥3
3. m=n and both≥2
4. m=n and both≥3

**Correct answer:** 3 — m=n and both≥2

**Build the basics**

This question tests **Hamiltonian cycles in complete bipartite graphs**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. A cycle in a bipartite graph alternates between the two parts, so a Hamilton cycle requires equal part sizes.
2. With m=n≥2, alternating through all vertices constructs such a cycle.

**Conclusion**

The reasoning gives option 3: **m=n and both≥2**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 77

*UGC NET June 2019, original Q57*

How many cards must be selected from a 52-card deck to guarantee at least three hearts?

1. 9
2. 13
3. 17
4. 42

**Correct answer:** 4 — 42

**Build the basics**

This question tests **Pigeonhole principle**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Worst case first select all 39 non-hearts and then two hearts: 41 cards without three hearts.
2. The 42nd card guarantees a third heart.

**Conclusion**

The reasoning gives option 4: **42**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

### 2018

---

#### Question 78

*UGC NET December 2018, original Q51*

Which are mathematical statements? I There will be snow in January; II What is the time now?; III Today is Sunday; IV You must study Discrete Mathematics.

1. I and III
2. I and II
3. II and IV
4. III and IV

**Correct answer:** 1 — I and III

**Build the basics**

This question tests **Statements and propositions**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. A statement is a declarative sentence that has a truth value.
2. I and III are declarative and can be true or false. II is a question and IV an imperative, so neither is a statement.

**Conclusion**

The reasoning gives option 1: **I and III**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 79

*UGC NET December 2018, original Q53*

A box has six red and four green balls. Four are selected. What is the probability of exactly two red and two green?

1. 1/14
2. 3/7
3. 1/35
4. 1/7

**Correct answer:** 2 — 3/7

**Build the basics**

This question tests **Hypergeometric probability**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Favourable selections=C(6,2)C(4,2)=15·6=90.
2. All selections=C(10,4)=210.
3. Probability=90/210=3/7.

**Conclusion**

The reasoning gives option 2: **3/7**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 80

*UGC NET December 2018, original Q54*

Survey counts are Bus 30, Train 35, Automobile 100, Bus∩Train 15, Bus∩Auto 15, Train∩Auto 20 and all three 5. How many respondents?

1. 120
2. 165
3. 160
4. 115

**Correct answer:** 1 — 120

**Build the basics**

This question tests **Three-set inclusion-exclusion**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Use |B∪T∪A|=sum singles−sum pairs+triple.
2. 30+35+100−15−15−20+5=120.

**Conclusion**

The reasoning gives option 1: **120**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 81

*UGC NET December 2018, original Q55*

Which are true? I every logic network can use only NAND or only NOR; II Boolean expressions/networks correspond to labelled acyclic digraphs; III no two Boolean algebras with n atoms are isomorphic; IV nonzero finite-Boolean-algebra elements are not uniquely joins of atoms.

1. I,IV
2. I,II,III
3. I,II
4. II,III,IV

**Correct answer:** 3 — I,II

**Build the basics**

This question tests **Boolean networks and finite Boolean algebras**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. NAND and NOR are each functionally complete, so I true; combinational logic networks are labelled DAGs, so II true.
2. All finite Boolean algebras with n atoms are isomorphic, making III false.
3. Each element is uniquely the join of the atoms below it, so IV false.

**Conclusion**

The reasoning gives option 3: **I,II**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

---

#### Question 82

*UGC NET December 2018, original Q58*

In a PERT activity-on-arrow network, what does a merge event represent?

1. Completion of two or more activities
2. Start of two or more activities
3. A dummy activity only
4. An isolated milestone

**Correct answer:** 1 — Completion of two or more activities

**Build the basics**

This question tests **PERT network events**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. Several incoming arrows terminate at a merge event.
2. It occurs only when all those predecessor activities have completed.

**Conclusion**

The reasoning gives option 1: **Completion of two or more activities**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

---

#### Question 83

*UGC NET December 2018, original Q59*

Maximize z=−2x₁−3x₂ subject to x₁+x₂≥2, 2x₁+x₂≤10, x₁+x₂≤8 and x₁,x₂≥0.

1. x₁=2,x₂=0,z=−4
2. x₁=2,x₂=6,z=−22
3. x₁=0,x₂=2,z=−6
4. x₁=6,x₂=2,z=−18

**Correct answer:** 1 — x₁=2,x₂=0,z=−4

**Build the basics**

This question tests **Dual-simplex/graphical LP**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. Maximizing a negative cost is minimizing 2x₁+3x₂.
2. The lower boundary x₁+x₂=2 is optimal; assign all two units to cheaper x₁.
3. At (2,0), z=−4 and all upper constraints hold.

**Conclusion**

The reasoning gives option 1: **x₁=2,x₂=0,z=−4**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

---

#### Question 84

*UGC NET December 2018, original Q76*

A ternary tree has 4 internal nodes of out-degree 1, 3 of out-degree 2 and 3 of out-degree 3. How many leaves?

1. 9
2. 10
3. 11
4. 12

**Correct answer:** 2 — 10

**Build the basics**

This question tests **Rooted m-ary trees**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. For a rooted tree, leaves=1+Σ_internal(outdegree−1).
2. L=1+4·0+3·1+3·2=10.

**Conclusion**

The reasoning gives option 2: **10**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 85

*UGC NET December 2018, original Q78*

For a proper 2-colouring, which statement is not correct?

1. G is bipartite
2. G is 2-colourable
3. G has cycles of odd length
4. G has no cycles of odd length

**Correct answer:** 3 — G has cycles of odd length

**Build the basics**

This question tests **Bipartite graphs and 2-colouring**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. A graph is bipartite iff it is 2-colourable iff it contains no odd cycle.
2. Therefore the assertion that it has odd cycles is the incorrect one.

**Conclusion**

The reasoning gives option 3: **G has cycles of odd length**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 86

*UGC NET July 2018, original Q25*

Characters A–E have probabilities 0.08,0.40,0.25,0.15,0.12. What average length does optimal binary Huffman coding achieve?

1. 2.4
2. 1.87
3. 3.0
4. 2.15

**Correct answer:** 4 — 2.15

**Build the basics**

This question tests **Prefix codes and Huffman coding**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. Merge 0.08+0.12=0.20; then 0.15+0.20=0.35; then 0.25+0.35=0.60; finally 0.40+0.60.
2. Resulting lengths are 1 for 0.40, 2 for 0.25, 3 for 0.15 and 4 for 0.08,0.12.
3. Weighted average=0.40+0.50+0.45+0.32+0.48=2.15.

**Conclusion**

The reasoning gives option 4: **2.15**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 87

*UGC NET July 2018, original Q26*

A strictly binary tree has 19 leaves. How many total nodes?

1. At most 37
2. Exactly 37
3. Exactly 35
4. At most 35

**Correct answer:** 2 — Exactly 37

**Build the basics**

This question tests **Strict/full binary trees**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. In a full binary tree, leaves=internal nodes+1.
2. Internal nodes=18 and total=18+19=37.

**Conclusion**

The reasoning gives option 2: **Exactly 37**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 88

*UGC NET July 2018, original Q29*

A full 5-ary tree has eight internal nodes. How many leaves?

1. 30
2. 33
3. 45
4. 125

**Correct answer:** 2 — 33

**Build the basics**

This question tests **Full m-ary trees**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. For a full m-ary tree, L=(m−1)I+1.
2. L=4·8+1=33.

**Conclusion**

The reasoning gives option 2: **33**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 89

*UGC NET July 2018, original Q53*

Events occur at 30 per hour. What is the probability of no event in 40 minutes under a Poisson model?

1. e^(−30)
2. e^(−12)
3. 20e^(−20)
4. e^(−20)

**Correct answer:** 4 — e^(−20)

**Build the basics**

This question tests **Poisson distribution**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Forty minutes is 2/3 hour, so mean count=30·2/3=20.
2. P(X=0)=e^(−20).

**Conclusion**

The reasoning gives option 4: **e^(−20)**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 90

*UGC NET July 2018, original Q80*

How many atomic outcomes are in the experiment of drawing an unordered five-card poker hand from 52 cards?

1. 2,598,960
2. 52⁵
3. 311,875,200
4. 120

**Correct answer:** 1 — 2,598,960

**Build the basics**

This question tests **Sample spaces**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Order within a hand does not matter and cards are not replaced.
2. The count is C(52,5)=2,598,960.

**Conclusion**

The reasoning gives option 1: **2,598,960**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 91

*UGC NET July 2018, original Q82*

Which statement about convex minimization is false?

1. If a local minimum exists, it is global
2. The set of all global minima is convex
3. The set of all global minima is concave
4. A strictly convex function, if it has a minimum, has a unique minimum

**Correct answer:** 3 — The set of all global minima is concave

**Build the basics**

This question tests **Convex optimization**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. For a convex objective over a convex feasible set, local minima are global and the minimizer set is convex.
2. Calling the minimizer set 'concave' is not a valid property; option 3 is false.

**Conclusion**

The reasoning gives option 3: **The set of all global minima is concave**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

---

#### Question 92

*UGC NET July 2018, original Q83*

For the source LPP maximize 100x₁+2x₂+5x₃ with its printed equality/inequalities and nonnegative variables, classify the solution.

1. x₁=100,x₂=x₃=0
2. Unbounded
3. No solution
4. x₁=50,x₂=70,x₃=60

**Correct answer:** 2 — Unbounded

**Build the basics**

This question tests **Unbounded linear programming**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. A feasible improving direction is d=(0,6,1,0).
2. It preserves 14d₁+d₂−6d₃+3d₄=0 and satisfies the two homogeneous ≤ directions.
3. The objective increases by 2·6+5·1=17 per unit, so the LP is unbounded.

**Conclusion**

The reasoning gives option 2: **Unbounded**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

---

#### Question 93

*UGC NET July 2018, original Q84*

For S={0,…,32}, p(i)=(33−i)/561. What is the probability that an even number of buffers are full?

1. 0.515
2. 0.785
3. 0.758
4. 0.485

**Correct answer:** 1 — 0.515

**Build the basics**

This question tests **Discrete probability distributions**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Sum over i=0,2,…,32: Σ_{k=0}^{16}(33−2k)=17·33−2·136=289.
2. P=289/561≈0.51515.

**Conclusion**

The reasoning gives option 1: **0.515**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 94

*UGC NET July 2018, original Q85*

Which is equivalent to ¬∃x Q(x)?

1. ∃x¬Q(x)
2. ∀x¬Q(x)
3. ¬∃x¬Q(x)
4. ∀xQ(x)

**Correct answer:** 2 — ∀x¬Q(x)

**Build the basics**

This question tests **Negating quantifiers**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. Move negation through the existential quantifier, changing it to universal.
2. Thus ¬∃xQ(x)≡∀x¬Q(x).

**Conclusion**

The reasoning gives option 2: **∀x¬Q(x)**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 95

*UGC NET July 2018, original Q86*

If Aᵢ={−i,…,−1,0,1,…,i}, what is ⋃_{i=1}^∞ Aᵢ?

1. Z
2. Q
3. R
4. C

**Correct answer:** 1 — Z

**Build the basics**

This question tests **Unions of sets**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. Every integer k occurs once i≥|k|.
2. No non-integer occurs in any Aᵢ, so the union is exactly Z.

**Conclusion**

The reasoning gives option 1: **Z**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 96

*UGC NET July 2018, original Q87*

Match: A ∀x∀y(f(x)=f(y)→x=y); B ∀y∃x(f(x)=y); C ∀x f(x)=k with I constant, II injective, III surjective.

1. A-I,B-II,C-III
2. A-III,B-II,C-I
3. A-II,B-I,C-III
4. A-II,B-III,C-I

**Correct answer:** 4 — A-II,B-III,C-I

**Build the basics**

This question tests **Injective, surjective and constant functions**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. A is injectivity (II), B surjectivity (III), C constancy (I).
2. Hence A-II,B-III,C-I.

**Conclusion**

The reasoning gives option 4: **A-II,B-III,C-I**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 97

*UGC NET July 2018, original Q88*

Which listed relation on {0,1,2,3} is an equivalence relation?

1. A relation missing (1,1)
2. {(0,0),(1,1),(2,2),(3,3)}
3. A non-transitive seven-pair relation
4. A non-symmetric five-pair relation

**Correct answer:** 2 — {(0,0),(1,1),(2,2),(3,3)}

**Build the basics**

This question tests **Equivalence relations**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. The identity relation contains every diagonal pair and no off-diagonal pairs.
2. It is reflexive, symmetric and transitive; each other printed option misses a required property.

**Conclusion**

The reasoning gives option 2: **{(0,0),(1,1),(2,2),(3,3)}**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 98

*UGC NET July 2018, original Q89*

Which defines an equivalence relation on all functions Z→Z?

1. f(x)−g(x)=1 for every x
2. f(0)=g(0) or f(1)=g(1)
3. f(0)=g(1) and f(1)=g(0)
4. f(x)−g(x)=k for every x, for some integer k

**Correct answer:** 4 — f(x)−g(x)=k for every x, for some integer k

**Build the basics**

This question tests **Equivalence relations on functions**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. Option 4 says functions differ by a constant. Difference 0 gives reflexivity; negating k gives symmetry; adding constants gives transitivity.
2. Options 1 and 3 are not reflexive; the OR in option 2 breaks transitivity.

**Conclusion**

The reasoning gives option 4: **f(x)−g(x)=k for every x, for some integer k**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 99

*UGC NET July 2018, original Q90*

Which statement is true?

1. (Z,≤) is not totally ordered
2. Subset inclusion is a partial order on P(S)
3. (Z,≠) is a poset
4. The displayed order graph is not a partial order

**Correct answer:** 2 — Subset inclusion is a partial order on P(S)

**Build the basics**

This question tests **Partial and total orders**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. Inclusion is reflexive, antisymmetric and transitive, hence a partial order.
2. Integers under ≤ are totally ordered, and ≠ is not reflexive; these eliminate 1 and 3.

**Conclusion**

The reasoning gives option 2: **Subset inclusion is a partial order on P(S)**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 100

*UGC NET July 2018, original Q99*

Simplify F(A,B,C,D)=Σ(0,1,2,8,9,12,13) with d=Σ(10,11,14,15).

1. AC'+B'C'+B'D'
2. A'C'+BD+B'C
3. A'B+C
4. AB'C+BD

**Correct answer:** — — AC'+B'C'+B'D'

**Build the basics**

This question tests **K-map with don't-cares**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. Use don't-cares to make groups 8,9,12,13→AC'; 0,1,8,9→B'C'; and 0,2,8,10→B'D'.
2. The minimal SOP is AC'+B'C'+B'D'.

**Conclusion**

The derived result is **AC'+B'C'+B'D'**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

> **Important wording note:** The PDF's overbars are poorly encoded; the normalized expression is authoritative and the source page preserves the printed choices.

### 2017

---

#### Question 101

*UGC NET January 2017 Paper II, original Q5*

For a simple n-vertex graph (n≥3), which listed degree/edge conditions are sufficient for Hamiltonicity?

1. Dirac and edge-count conditions
2. Ore and edge-count conditions
3. Dirac and Ore conditions
4. All listed conditions

**Correct answer:** 4 — All listed conditions

**Build the basics**

This question tests **Hamiltonian graph sufficient conditions**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. Dirac's δ≥n/2 and Ore's degree-sum condition are each sufficient.
2. The printed extremal edge-count bound is also a classical sufficient Hamiltonicity condition.
3. Thus all listed conditions are sufficient.

**Conclusion**

The reasoning gives option 4: **All listed conditions**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 102

*UGC NET January 2017 Paper II, original Q6*

From premises (P→Q)∧(R→S) and P∨R, which conclusion Y follows?

1. P∨R
2. P∨S
3. Q∨R
4. Q∨S

**Correct answer:** 4 — Q∨S

**Build the basics**

This question tests **Rules of inference**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. Use proof by cases on P∨R.
2. If P then Q; if R then S. Therefore at least one of Q or S holds, giving Q∨S.

**Conclusion**

The reasoning gives option 4: **Q∨S**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 103

*UGC NET January 2017 Paper III, original Q68*

Which statement about a closed loop used to improve a transportation solution is false?

1. The loop contains an odd number of cells
2. Right-angle turns are used
3. Occupied cells alternate with the trial cell
4. Plus and minus signs alternate

**Correct answer:** 1 — The loop contains an odd number of cells

**Build the basics**

This question tests **Transportation stepping-stone loops**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. A transportation adjustment loop always contains an even number of cells so that + and − positions alternate and balance is preserved.
2. Therefore 'odd number of cells' is false.

**Conclusion**

The reasoning gives option 1: **The loop contains an odd number of cells**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

### 2016

---

#### Question 104

*UGC NET July 2016 Paper II, original Q1*

How many equivalence relations on a five-element set have exactly three equivalence classes?

1. 15
2. 20
3. 25
4. 30

**Correct answer:** 3 — 25

**Build the basics**

This question tests **Counting equivalence relations**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. Such relations correspond to partitions of five labelled elements into three nonempty unlabeled blocks.
2. The Stirling number S(5,3)=25.

**Conclusion**

The reasoning gives option 3: **25**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 105

*UGC NET July 2016 Paper II, original Q2*

How many spanning trees do K₄ and K₂,₂ have, respectively?

1. 8 and 2
2. 16 and 2
3. 16 and 4
4. 8 and 4

**Correct answer:** 3 — 16 and 4

**Build the basics**

This question tests **Spanning-tree enumeration**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. Cayley gives τ(K₄)=4²=16.
2. For Kₘ,ₙ, τ=m^(n−1)n^(m−1), so τ(K₂,₂)=4.

**Conclusion**

The reasoning gives option 3: **16 and 4**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 106

*UGC NET July 2016 Paper II, original Q3*

If R and S are reflexive relations on A, which of R∪S and R∩S must be reflexive?

1. Union only
2. Intersection only
3. Both
4. Neither

**Correct answer:** 3 — Both

**Build the basics**

This question tests **Operations on reflexive relations**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. Every diagonal pair belongs to both R and S.
2. It therefore belongs to both their union and their intersection.

**Conclusion**

The reasoning gives option 3: **Both**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 107

*UGC NET July 2016 Paper II, original Q4*

A box has three cards: BB, RR and BR. A card and one visible side are chosen at random. Given the observed colour, what is the probability that the opposite side has the same colour?

1. 3/4
2. 2/3
3. 1/2
4. 1/3

**Correct answer:** 2 — 2/3

**Build the basics**

This question tests **Bayes theorem**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Condition on a colour, say black. The visible black side could be either of the two sides of BB or the one black side of BR: three equally likely exposed sides.
2. Two of those three belong to BB, so the opposite side matches with probability 2/3.

**Conclusion**

The reasoning gives option 2: **2/3**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 108

*UGC NET July 2016 Paper II, original Q6*

Which XOR equality is incorrect?

1. 0⊕0=0
2. 1⊕0=1
3. 1⊕1⊕0=1
4. 1⊕1=0

**Correct answer:** 3 — 1⊕1⊕0=1

**Build the basics**

This question tests **Exclusive-OR**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. XOR is parity: it is 1 iff an odd number of inputs are 1.
2. 1⊕1⊕0 has two ones and equals 0, so option 3 is incorrect.

**Conclusion**

The reasoning gives option 3: **1⊕1⊕0=1**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

---

#### Question 109

*UGC NET July 2016 Paper III, original Q36*

A triangulation of a simple n-gon uses how many noncrossing diagonals and produces how many triangles?

1. n−2 and n−3
2. n−3 and n−2
3. n and n−2
4. n−1 and n−1

**Correct answer:** 2 — n−3 and n−2

**Build the basics**

This question tests **Polygon triangulation**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. Induct by removing an ear, or use Euler's formula.
2. Every triangulation has n−3 diagonals and n−2 triangular faces.

**Conclusion**

The reasoning gives option 2: **n−3 and n−2**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 110

*UGC NET July 2016 Paper III, original Q62*

Which printed statements about the revised simplex method are correct?

1. A,B only
2. A,C only
3. B,C only
4. A,B,C

**Correct answer:** 4 — A,B,C

**Build the basics**

This question tests **Revised simplex method**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. Revised simplex stores/updates basis information rather than the full tableau, computes reduced costs and performs the same basis changes as simplex.
2. All three source statements describe these valid properties.

**Conclusion**

The reasoning gives option 4: **A,B,C**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

### 2015

---

#### Question 111

*UGC NET June 2015 Paper II, original Q1*

How many five-digit strings (leading zero allowed) have digit sum 7?

1. 66
2. 330
3. 495
4. 99

**Correct answer:** 2 — 330

**Build the basics**

This question tests **Stars and bars**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Since the sum is only 7, no digit can exceed 9; upper bounds are inactive.
2. Nonnegative solutions of x₁+…+x₅=7 number C(11,4)=330.

**Conclusion**

The reasoning gives option 2: **330**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 112

*UGC NET June 2015 Paper II, original Q2*

Two fair dice, black and red, are rolled. What is the probability that the black result divides the red result?

1. 22/36
2. 12/36
3. 14/36
4. 6/36

**Correct answer:** 3 — 14/36

**Build the basics**

This question tests **Discrete probability**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. For black values 1,…,6, the counts of red multiples are 6,3,2,1,1,1.
2. Total favourable=14 of 36.

**Conclusion**

The reasoning gives option 3: **14/36**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 113

*UGC NET June 2015 Paper II, original Q3*

In how many ways can 15 identical fish be placed into five distinct ponds with at least one in each?

1. 1001
2. 3876
3. 775
4. 200

**Correct answer:** 1 — 1001

**Build the basics**

This question tests **Stars and bars**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Positive solutions of x₁+…+x₅=15 are counted by C(14,4).
2. C(14,4)=1001.

**Conclusion**

The reasoning gives option 1: **1001**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 114

*UGC NET June 2015 Paper II, original Q4*

Assess: A DFS traverses rooted trees; B preorder/postorder/inorder list ordered rooted-tree vertices; C Huffman finds an optimal weighted binary tree; D topological sorting gives parents larger labels than children.

1. A,B
2. C,D
3. A,B,C
4. A,B,C,D

**Correct answer:** 3 — A,B,C

**Build the basics**

This question tests **Rooted-tree traversals and prefix codes**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. A,B,C are standard uses/properties.
2. With the usual topological order, a parent precedes (has a smaller position than) its child, so D as written is false.

**Conclusion**

The reasoning gives option 3: **A,B,C**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 115

*UGC NET June 2015 Paper II, original Q6*

Assess: A Boolean expressions/networks correspond to labelled acyclic digraphs; B an algebraically optimal expression need not give the simplest physical network; C greedy largest K-map groups need not always give a globally optimal expression.

1. A only
2. B only
3. A,B
4. A,B,C

**Correct answer:** 4 — A,B,C

**Build the basics**

This question tests **Boolean expressions and logic networks**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. A describes combinational networks; B accounts for gate sharing/fan-in/technology cost; C reflects that a greedy cover need not minimize the final cover.
2. All three are true.

**Conclusion**

The reasoning gives option 4: **A,B,C**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

---

#### Question 116

*UGC NET June 2015 Paper II, original Q9*

Match contraposition, exportation, reductio ad absurdum and equivalence with the four displayed implications.

1. A-I,B-II,C-III,D-IV
2. A-II,B-III,C-I,D-IV
3. A-III,B-II,C-IV,D-I
4. A-IV,B-II,C-III,D-I

**Correct answer:** 1 — A-I,B-II,C-III,D-IV

**Build the basics**

This question tests **Named propositional equivalences**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. (p→q)→(¬q→¬p) is contraposition; [(p∧q)→r]→[p→(q→r)] is exportation.
2. The contradiction form is reductio, and p↔q expands to (p→q)∧(q→p).

**Conclusion**

The reasoning gives option 1: **A-I,B-II,C-III,D-IV**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 117

*UGC NET December 2015 Paper II, original Q1*

How many five-person committees can be chosen from 20 men and 12 women with at least three women?

1. 75240
2. 52492
3. 41800
4. 9900

**Correct answer:** 2 — 52492

**Build the basics**

This question tests **Combinations**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Sum cases 3W2M,4W1M,5W: C(12,3)C(20,2)+C(12,4)C(20,1)+C(12,5).
2. =41800+9900+792=52492.

**Conclusion**

The reasoning gives option 2: **52492**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 118

*UGC NET December 2015 Paper II, original Q2*

Which source statement is false? A even degrees characterize Euler circuits; B exactly two odd vertices characterize a non-circuit Euler path; C Kₙ has a Hamilton circuit for n≥3; D C₆ is not bipartite but K₃ is bipartite.

1. A only
2. B,C
3. C only
4. D only

**Correct answer:** 4 — D only

**Build the basics**

This question tests **Euler, Hamilton and bipartite graphs**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. A–C are standard true theorems.
2. C₆ is even and therefore bipartite, while K₃ is an odd cycle and not bipartite; D reverses both facts.

**Conclusion**

The reasoning gives option 4: **D only**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 119

*UGC NET December 2015 Paper II, original Q3*

Which is not countable: negative integers, multiples of 7, even integers, or real numbers in (0,1/2)?

1. Negative and even integers
2. Multiples of 7 only
3. Even integers only
4. Reals in (0,1/2) only

**Correct answer:** 4 — Reals in (0,1/2) only

**Build the basics**

This question tests **Countability**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. Each listed integer subset has a simple enumeration and is countable.
2. Every nonempty real interval is uncountable by a scaling/bijection argument.

**Conclusion**

The reasoning gives option 4: **Reals in (0,1/2) only**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 120

*UGC NET December 2015 Paper II, original Q7*

For positive integers and P(m,n): m divides n, assess A ∃m∀nP(m,n); B ∀nP(1,n); C ∀m∀nP(m,n).

1. True,True,False
2. True,False,False
3. False,False,False
4. True,True,True

**Correct answer:** 1 — True,True,False

**Build the basics**

This question tests **Quantifiers and divisibility**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. Choose m=1 for A; B is the same universal divisibility fact.
2. C is false, e.g. 2 does not divide 1.

**Conclusion**

The reasoning gives option 1: **True,True,False**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 121

*UGC NET December 2015 Paper III, original Q52*

A basic feasible solution is called what if at least one basic variable is zero?

1. Degenerate
2. Non-degenerate
3. Infeasible
4. Unbounded

**Correct answer:** 1 — Degenerate

**Build the basics**

This question tests **Degeneracy in linear programming**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. This is exactly the definition of a degenerate BFS.
2. It may still be feasible and bounded; degeneracy concerns a zero-valued basic variable.

**Conclusion**

The reasoning gives option 1: **Degenerate**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

---

#### Question 122

*UGC NET December 2015 Paper III, original Q53*

A transportation initial solution is a non-degenerate BFS when it is feasible, has m+n−1 positive allocations, and those allocations are independent. Which conditions are required?

1. A,B only
2. A,C only
3. B,C only
4. A,B,C

**Correct answer:** 4 — A,B,C

**Build the basics**

This question tests **Transportation non-degeneracy**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. Feasibility is required, the rank requires m+n−1 basic cells, and independence excludes a loop.
2. All three conditions are necessary.

**Conclusion**

The reasoning gives option 4: **A,B,C**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

### 2014

---

#### Question 123

*UGC NET December 2014 Paper II, original Q4*

One integer is chosen uniformly from one million values, independently one million times. What is the approximate probability that a specified integer is chosen at least once?

1. 0.5
2. 0.632121
3. 0.367879
4. 1

**Correct answer:** 2 — 0.632121

**Build the basics**

This question tests **Repeated independent trials**. Counting problems reduce to product/sum rules, stars-and-bars, inclusion–exclusion, permutations or combinations. Probability is favourable equally likely outcomes divided by all outcomes; conditional probability changes the sample space, and Bayes reverses a condition.

**Step-by-step reasoning**

1. Complement probability is (1−10⁻⁶)^(10⁶).
2. Using (1−1/n)^n→e⁻¹ gives 1−e⁻¹≈0.632121.

**Conclusion**

The reasoning gives option 2: **0.632121**.

**How to solve similar questions**

- **Rule to remember:** nPr=n!/(n−r)!; nCr=n!/[r!(n−r)!]; P(A|B)=P(A∩B)/P(B); P(A|B)=P(B|A)P(A)/P(B).
- **Fast exam method:** Decide first whether order matters and whether replacement is allowed; that usually eliminates most options immediately.
- **Common mistake to avoid:** Pairwise intersections are added back only after being subtracted, and a three-way intersection is then added once.

---

#### Question 124

*UGC NET December 2014 Paper III, original Q67*

If an artificial variable remains basic with a positive value in the final simplex solution, what does it imply?

1. Alternative optimum
2. Original problem infeasible
3. Unbounded
4. Degenerate optimum only

**Correct answer:** 2 — Original problem infeasible

**Build the basics**

This question tests **Artificial variables**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. Phase I minimizes the sum of artificial variables.
2. A positive artificial value at its optimum means the original constraints cannot be satisfied without it, hence infeasible.

**Conclusion**

The reasoning gives option 2: **Original problem infeasible**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

---

#### Question 125

*UGC NET December 2014 Paper III, original Q68*

If a transportation BFS has fewer than m+n−1 occupied independent cells, it is:

1. Balanced
2. Unbalanced
3. Infeasible
4. Degenerate (none of the first three)

**Correct answer:** 4 — Degenerate (none of the first three)

**Build the basics**

This question tests **Transportation degeneracy**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. Fewer than the required rank number of positive basic allocations is transportation degeneracy.
2. It is independent of whether total supply equals demand.

**Conclusion**

The reasoning gives option 4: **Degenerate (none of the first three)**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

### 2013

---

#### Question 126

*UGC NET December 2013 Paper II, original Q31*

How is the dual of a Boolean expression obtained?

1. Complement every variable
2. Swap 0 and 1 only
3. Interchange + with · and 0 with 1
4. Reverse all literals

**Correct answer:** 3 — Interchange + with · and 0 with 1

**Build the basics**

This question tests **Duality principle**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. Boolean duality interchanges join/meet and their identities.
2. Variables and complements are left unchanged; +↔· and 0↔1.

**Conclusion**

The reasoning gives option 3: **Interchange + with · and 0 with 1**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

---

#### Question 127

*UGC NET December 2013 Paper II, original Q34*

Over positive integers, which is true: ∀m∀n(m divides n), or ∃m∀n(m divides n)?

1. Both
2. Universal only
3. Existential-universal only
4. Neither

**Correct answer:** 3 — Existential-universal only

**Build the basics**

This question tests **Quantifiers and divisibility**. Replace implication by ¬p ∨ q, push negations through quantifiers, and test validity by searching for a counterexample. A tautology is true under every valuation; an argument is valid when the conjunction of its premises implies its conclusion.

**Step-by-step reasoning**

1. The universal statement is false, e.g. 2∤1.
2. The existential statement is true with m=1.

**Conclusion**

The reasoning gives option 3: **Existential-universal only**.

**How to solve similar questions**

- **Rule to remember:** p→q ≡ ¬p∨q; ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- **Fast exam method:** For a proposed tautology, first try to make the consequent false and see whether the antecedent can still be true.
- **Common mistake to avoid:** The converse q→p is not the contrapositive ¬q→¬p, and quantifier order generally cannot be swapped.

---

#### Question 128

*UGC NET December 2013 Paper II, original Q36*

A forest with n vertices and t component trees has how many edges?

1. n+t
2. n−t
3. n−1
4. t−1

**Correct answer:** 2 — n−t

**Build the basics**

This question tests **Forests**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. Each component with nᵢ vertices has nᵢ−1 edges.
2. Summing gives n−t.

**Conclusion**

The reasoning gives option 2: **n−t**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 129

*UGC NET December 2013 Paper II, original Q37*

For f(x)=2x+3 and g(x)=3x+2, what are f∘g and g∘f?

1. 6x+7 and 6x+11
2. 6x+11 and 6x+7
3. 5x+5 and 5x+5
4. 6x+6 and 6x+6

**Correct answer:** 1 — 6x+7 and 6x+11

**Build the basics**

This question tests **Function composition**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. f(g(x))=2(3x+2)+3=6x+7.
2. g(f(x))=3(2x+3)+2=6x+11.

**Conclusion**

The reasoning gives option 1: **6x+7 and 6x+11**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 130

*UGC NET December 2013 Paper II, original Q39*

Kuratowski's theorem characterizes non-planar graphs using subdivisions of which graphs?

1. K₄ or K₂,₃
2. K₅ only
3. K₅ or K₃,₃
4. K₆ or K₄,₄

**Correct answer:** 3 — K₅ or K₃,₃

**Build the basics**

This question tests **Planarity and Kuratowski theorem**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. A finite graph is non-planar iff it contains a subdivision of K₅ or K₃,₃.
2. These are the two Kuratowski forbidden graphs.

**Conclusion**

The reasoning gives option 3: **K₅ or K₃,₃**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 131

*UGC NET December 2013 Paper III, original Q39*

Match clique and vertex cover with the source definitions.

1. Clique=minimal independent set; cover=maximal complete set
2. Clique=path; cover=cut
3. Clique=tree; cover=cycle
4. Clique=maximal complete vertex set; cover=a vertex subset incident to every edge

**Correct answer:** 4 — Clique=maximal complete vertex set; cover=a vertex subset incident to every edge

**Build the basics**

This question tests **Cliques and vertex covers**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. A clique is a complete subgraph (often maximal in this terminology).
2. A vertex cover meets every edge; the source uses a minimal such subset.

**Conclusion**

The reasoning gives option 4: **Clique=maximal complete vertex set; cover=a vertex subset incident to every edge**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 132

*UGC NET June 2013 Paper III, original Q23*

At an optimal simplex tableau, what does a zero reduced cost for a nonbasic variable indicate?

1. Infeasibility
2. Unboundedness
3. An alternative optimal solution
4. Degeneracy only

**Correct answer:** 3 — An alternative optimal solution

**Build the basics**

This question tests **Alternative optima in simplex**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. Entering a nonbasic variable with zero reduced cost does not change the objective.
2. If a feasible pivot exists, it produces another optimum.

**Conclusion**

The reasoning gives option 3: **An alternative optimal solution**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

### 2012

---

#### Question 133

*UGC NET June 2012 Paper II, original Q1*

The postfix expression AB+CD−* is naturally evaluated using which data structure?

1. Stack
2. Tree
3. Queue
4. Linked list

**Correct answer:** 1 — Stack

**Build the basics**

This question tests **Postfix expression evaluation**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. Scan left to right, push operands and pop the top two operands for each operator.
2. This last-in-first-out discipline is a stack.

**Conclusion**

The reasoning gives option 1: **Stack**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 134

*UGC NET June 2012 Paper II, original Q2*

A binary tree has postorder DEBFCA. Which proposed preorder is consistent?

1. ABFCDE
2. ADBFEC
3. ABDECF
4. None

**Correct answer:** 3 — ABDECF

**Build the basics**

This question tests **Tree traversals**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. Postorder ends with root A. The consistent subtree decomposition yields root-first order A,B,D,E,C,F.
2. Thus preorder is ABDECF.

**Conclusion**

The reasoning gives option 3: **ABDECF**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 135

*UGC NET June 2012 Paper II, original Q4*

How many colours suffice to properly colour the vertices of every planar graph?

1. 2
2. 3
3. 4
4. 5

**Correct answer:** 3 — 4

**Build the basics**

This question tests **Planar graph colouring**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. The Four Colour Theorem guarantees at most four colours for every planar graph.
2. K₄ is planar and needs four, so the universal bound is tight.

**Conclusion**

The reasoning gives option 3: **4**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 136

*UGC NET December 2012 Paper II, original Q4*

What is the power set of {∅}?

1. {∅}
2. ∅
3. {∅,{∅}}
4. {∅,∅,{∅}}

**Correct answer:** 3 — {∅,{∅}}

**Build the basics**

This question tests **Power sets**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. The set {∅} has one element, so its power set has two subsets.
2. They are ∅ and {∅}, hence {∅,{∅}}.

**Conclusion**

The reasoning gives option 3: **{∅,{∅}}**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

### 2011

---

#### Question 137

*UGC NET December 2011 Paper III, original Q3*

Maximize 2x₁+2x₂ subject to 3x₁+4x₂≤6, 6x₁+x₂≤3 and x₁,x₂≥0.

1. (0,0)
2. (2/7,9/7)
3. (1/2,0)
4. Unbounded

**Correct answer:** 2 — (2/7,9/7)

**Build the basics**

This question tests **Graphical/revised-simplex LP**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. Intersect 3x₁+4x₂=6 and 6x₁+x₂=3: x₁=2/7,x₂=9/7.
2. The objective is 22/7, exceeding the axis vertices 3 and 1.
3. Thus the intersection is optimal.

**Conclusion**

The reasoning gives option 2: **(2/7,9/7)**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

---

#### Question 138

*UGC NET December 2011 Paper III, original Q4*

Solve the transportation problem with costs [[8,5,6],[15,10,12],[3,9,10]], supplies [120,80,80] and demands [150,80,50].


**Correct answer:** — — Minimum cost 1900 (under the visually recovered supply 80)

**Build the basics**

This question tests **Transportation model**. Linear-programming optima occur at feasible extreme points. A basic feasible solution is degenerate when a basic variable is zero. Transportation BFSs normally have m+n−1 independent positive allocations; PERT uses probabilistic activity times while CPM is deterministic.

**Step-by-step reasoning**

1. Exploit the cheapest cell: send 80 from S3 to D1 at cost 3; D1 then needs 70.
2. Allocate S1→D1=70 and S1→D3=50; send S2→D2=80.
3. Total=80·3+70·8+50·6+80·10=1900. Opportunity-cost checks are nonnegative for this basis.

**Conclusion**

The derived result is **Minimum cost 1900 (under the visually recovered supply 80)**.

**How to solve similar questions**

- **Rule to remember:** PERT te=(to+4tm+tp)/6; variance=[(tp−to)/6]^2; tree/project critical path is the longest-duration path.
- **Fast exam method:** For a two-variable LP, list feasible intersections and evaluate the objective instead of running simplex.
- **Common mistake to avoid:** The critical path is longest in duration, not the path with the most activities; degeneracy is about basic variables/independent allocations.

> **Important wording note:** The scan reads the third supply as '8' in OCR; visual balance indicates 80. The normalized numeric answer is conditional on that recovery.

### 2010

---

#### Question 139

*UGC NET June 2010 Paper II, original Q1*

Two entities are called clones when all attributes in the stated complete attribute set (height, weight, complexion) are identical. Is cloning an equivalence relation?

1. True
2. False
3. Truth cannot be computed
4. None

**Correct answer:** 1 — True

**Build the basics**

This question tests **Equivalence relations**. A relation is reflexive when every diagonal pair occurs, symmetric when reversal preserves membership, antisymmetric when mutual relatedness forces equality, and transitive when two composable pairs force the third. A partial order is reflexive, antisymmetric and transitive.

**Step-by-step reasoning**

1. Equality of an attribute tuple is reflexive, symmetric and transitive.
2. Because the attribute set is stipulated to be complete for this definition, cloning is an equivalence relation.

**Conclusion**

The reasoning gives option 1: **True**.

**How to solve similar questions**

- **Rule to remember:** |P(A)|=2^|A|; |A∪B|=|A|+|B|−|A∩B|.
- **Fast exam method:** Disprove a relation property with one witness: a missing diagonal, an unreturned pair, a distinct two-way pair, or a missing composite pair.
- **Common mistake to avoid:** Symmetric and antisymmetric are not opposites; a relation can be both (for example, equality) or neither.

---

#### Question 140

*UGC NET June 2010 Paper II, original Q4*

Build the association graph from the five source sentences about I, professor, student, algorithms, maths, electronics and computer science. What is its chromatic number?

1. 2
2. 3
3. 4
4. None

**Correct answer:** 2 — 3

**Build the basics**

This question tests **Graph colouring from associations**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. The associations I–maths, I–student and student–maths form a triangle, so at least three colours are necessary.
2. A direct three-colouring of all remaining vertices is possible, so χ=3.

**Conclusion**

The reasoning gives option 2: **3**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

### 2009

---

#### Question 141

*UGC NET December 2009 Paper II, original Q6*

Simplify (X+Y+XY)(X+Z).

1. X+Y+Z
2. XY+XZ
3. X+YZ
4. XYZ

**Correct answer:** 3 — X+YZ

**Build the basics**

This question tests **Boolean simplification**. Boolean functions can be represented by truth tables, minterms/maxterms, SOP/POS forms and Karnaugh maps. Simplification uses identity, domination, idempotent, complement, absorption, distributive and De Morgan laws.

**Step-by-step reasoning**

1. Absorption gives X+Y+XY=X+Y.
2. Then (X+Y)(X+Z)=X+YZ.

**Conclusion**

The reasoning gives option 3: **X+YZ**.

**How to solve similar questions**

- **Rule to remember:** x+x=x; x·x=x; x+xy=x; x(x+y)=x; (x+y)'=x'y'; (xy)'=x'+y'.
- **Fast exam method:** For four-option identities, test 0/1 assignments; a single counterexample removes an option.
- **Common mistake to avoid:** A simplified SOP need not be a canonical (complete) SOP; canonical terms contain every variable.

---

#### Question 142

*UGC NET December 2009 Paper II, original Q21*

A strict/full binary tree has an odd number of leaves. What can be said about its total number of vertices?

1. Odd
2. Even
3. A power of two
4. Cannot be determined

**Correct answer:** 1 — Odd

**Build the basics**

This question tests **Full binary trees**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. For L leaves, a full binary tree has total nodes 2L−1.
2. If L is odd, 2L−1 is odd.

**Conclusion**

The reasoning gives option 1: **Odd**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

---

#### Question 143

*UGC NET December 2009 Paper II, original Q22*

How many edges does a complete graph on n vertices have?

1. n²
2. n(n−1)/2
3. n(n+1)/2
4. 2n

**Correct answer:** 2 — n(n−1)/2

**Build the basics**

This question tests **Complete graphs**. Use degree sums, Euler’s formula, colouring criteria and standard tree identities. A connected graph has an Euler circuit iff every degree is even; a graph is bipartite iff it has no odd cycle. A tree with n vertices has n−1 edges.

**Step-by-step reasoning**

1. Every unordered pair of distinct vertices contributes one edge.
2. There are C(n,2)=n(n−1)/2 such pairs.

**Conclusion**

The reasoning gives option 2: **n(n−1)/2**.

**How to solve similar questions**

- **Rule to remember:** Σdeg(v)=2|E|; planar connected V−E+F=2; τ(Kn)=n^(n−2); full m-ary leaves=(m−1)i+1.
- **Fast exam method:** Parity, degree sum and V−E+F often solve a graph MCQ without drawing the whole graph.
- **Common mistake to avoid:** Euler questions concern edges; Hamilton questions concern vertices. Necessary and sufficient degree conditions must not be confused.

## Validation summary

- Records: 143; unique IDs: 143.
- Source files represented: 31.
- Every record has a short exam/session reference, independently derived answer and step-by-step solution; options are preserved for objective questions.
- Full source filenames, PDF pages, IDs, classifications and verification states remain in `data/questions.json` for auditing, but are intentionally hidden from the study flow.
- Disputed and ambiguous items are also mirrored in `data/disputed-questions.md` and `data/classification-review.md`.

### Questions by year

| Year | Count |
|---:|---:|
| 2026 | 10 |
| 2025 | 5 |
| 2024 | 12 |
| 2023 | 20 |
| 2022 | 5 |
| 2021 | 2 |
| 2020 | 8 |
| 2019 | 15 |
| 2018 | 23 |
| 2017 | 3 |
| 2016 | 7 |
| 2015 | 12 |
| 2014 | 3 |
| 2013 | 7 |
| 2012 | 4 |
| 2011 | 2 |
| 2010 | 2 |
| 2009 | 3 |

---

[Back to contents](#contents) · [All units](README.md) · [Project home](../README.md)

