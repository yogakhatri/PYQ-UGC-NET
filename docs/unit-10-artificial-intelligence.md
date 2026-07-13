# Unit 10: Artificial Intelligence

[Project home](../README.md) · [All units](README.md) · [Official syllabus](syllabus.md)

## Contents

- [How to use this guide](#status-and-use)
- [Unit-wide exam playbook](#unit-wide-exam-playbook)
- [1. Approaches to AI](#chapter-1)
- [2. Knowledge Representation](#chapter-2)
- [3. Planning](#chapter-3)
- [4. Natural Language Processing](#chapter-4)
- [5. Multi-Agent Systems](#chapter-5)
- [6. Fuzzy Sets](#chapter-6)
- [7. Genetic Algorithms](#chapter-7)
- [8. Artificial Neural Networks](#chapter-8)
- [Coverage and quality notes](#coverage-and-quality-notes)

## Status and use

This guide contains all **97 question blocks currently recoverable and assigned to Unit 10** from the local UGC NET archive. Questions are arranged chapter-wise and numbered continuously through the unit.

> [!WARNING]
> This is a working extraction inventory, not a complete solved guide. **0 answers are validated and 97 remain pending** in this unit. Some unit and chapter placements use fallback routing, and OCR or missing figures can make questions incomplete.

Use this file for question discovery and broad chapter revision. The chapter notes and exam methods are general, not question-specific solutions. Full source paths, PDF pages and classification states remain in the structured data for auditing.

## Unit-wide exam playbook

- **Core idea:** Represent states, knowledge, uncertainty, membership, or learning architecture explicitly before applying the AI technique.
- **Method:** For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation.
- **Rules/formulas:** A* uses f(n)=g(n)+h(n); an admissible heuristic never overestimates. Alpha-beta changes the number of explored nodes, not the minimax result.
- **Frequent traps:** Distinguish admissible from consistent heuristics, probability from fuzzy membership, supervised from reinforcement learning, and planning state from search operator.

## Chapter-wise concepts and PYQs

<a id="chapter-1"></a>

### 1. Approaches to AI (10 questions)

**What to master:** Turing Test and Rational Agents; State-Space Representation; Heuristic Search; Game Playing; Minimax; Alpha-Beta Cutoff.

**Exam lens:** Represent states, knowledge, uncertainty, membership, or learning architecture explicitly before applying the AI technique.

**Reusable method:** For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation.

**High-yield rules:** A* uses f(n)=g(n)+h(n); an admissible heuristic never overestimates. Alpha-beta changes the number of explored nodes, not the minimax result.

**Common traps:** Distinguish admissible from consistent heuristics, probability from fuzzy membership, supervised from reinforcement learning, and planning state from search operator.

---

#### Question 1

*UGC NET Dec 2013, Paper III, original Q24*

> The objective of ________ procedure is to di scover at least one ________ that causes two literals to match.

**Options**

- **A.** unification, validation
- **B.** unification, substitution
- **C.** substitution, unification
- **D.** minimax, maximum

**Chapter foundations**

This question belongs to the ideas covered by **Approaches to AI**. Revise these foundations: Turing Test and Rational Agents; State-Space Representation; Heuristic Search; Game Playing; Minimax; Alpha-Beta Cutoff.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Approaches to AI questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 2

*UGC NET Dec 2013, Paper III, original Q27*

> In alpha-beta pruning, _________ is used to cut off the search at maximizing level only and _________ is used to cut off the search at minimizing level only.

**Options**

- **A.** alpha, beta
- **B.** beta, alpha
- **C.** alpha, alpha
- **D.** beta, beta

**Chapter foundations**

This question belongs to the ideas covered by **Approaches to AI**. Revise these foundations: Turing Test and Rational Agents; State-Space Representation; Heuristic Search; Game Playing; Minimax; Alpha-Beta Cutoff.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Approaches to AI questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 3

*UGC NET June 2013, Paper III, original Q68*

> Which one of the following is not an informed search technique ?

**Options**

- **A.** Hill climbing search
- **B.** Best first search
- **C.** A* search
- **D.** Depth first search

**Chapter foundations**

This question belongs to the ideas covered by **Approaches to AI**. Revise these foundations: Turing Test and Rational Agents; State-Space Representation; Heuristic Search; Game Playing; Minimax; Alpha-Beta Cutoff.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Approaches to AI questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 4

*UGC NET Dec 2014, Paper III, original Q56*

> An A* algorithm is a heuristic search technique which

**Options**

- **A.** is like a depth-first search where most promising child is selected f or expansion
- **B.** generates all successor nodes and computes an estimate of distance (cost) from start node to a goal node through each of the successors. It then chooses the succ essor with shortest cost.
- **C.** saves all path lengths (costs) from start node to all ge nerated nodes and chooses shortest path for further expansion.
- **D.** none of the above

**Chapter foundations**

This question belongs to the ideas covered by **Approaches to AI**. Revise these foundations: Turing Test and Rational Agents; State-Space Representation; Heuristic Search; Game Playing; Minimax; Alpha-Beta Cutoff.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Approaches to AI questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 5

*UGC NET June 2015, Paper III, original Q59*

> Match the following with respect to heuristic search techniques : List - I List - Il
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Steepest - accent Hill Climbing (i) Keeps track of all partial paths which can be candidate for further exploration
> - **B.** Branch - and - bound (it) Discover problem state(s) that satisfy a set of constraints
> - **C.** Constraint satisfaction (iii) Detects difference between current state and goal state
> - **D.** Means - end - analysis (iv) Considers all moves from current state and selects best move Codes: (a) (b) (c) (d)

**Options**

1. (i) (iv) (iii) (ii)
2. (iv) (i) (ii) (iii)
3. (i) (iv) (il) (iii)
4. (iv) (ili)

**Chapter foundations**

This question belongs to the ideas covered by **Approaches to AI**. Revise these foundations: Turing Test and Rational Agents; State-Space Representation; Heuristic Search; Game Playing; Minimax; Alpha-Beta Cutoff.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Approaches to AI questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 6

*UGC NET July 2016, Paper III, original Q73*

> Consider the following game tree in which root is a maximizing node and children are visited left to right. What nodes will be pruned by the alpha-beta pruning ? A B C D E F G H I 31 28 21 56

**Options**

1. I
2. HI
3. CHI
4. GHI

**Chapter foundations**

This question belongs to the ideas covered by **Approaches to AI**. Revise these foundations: Turing Test and Rational Agents; State-Space Representation; Heuristic Search; Game Playing; Minimax; Alpha-Beta Cutoff.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Approaches to AI questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 7

*UGC NET Jan 2017, Paper III, original Q58*

> What is the best method to go for the game playing problem ?

**Options**

1. Optimal Search
2. Random Search
3. Heuristic Search
4. Stratified Search

**Chapter foundations**

This question belongs to the ideas covered by **Approaches to AI**. Revise these foundations: Turing Test and Rational Agents; State-Space Representation; Heuristic Search; Game Playing; Minimax; Alpha-Beta Cutoff.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Approaches to AI questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 8

*UGC NET Nov 2020, original Q113*

> Which of the following statements are true?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Minimax search is breadth-first: it processes all the nodes at a level before moving to a node in next level.
> - **B.** The effectiveness of the alpha-beta pruning is highly dependent on the order in which the states are examined.
> - **C.** The alpha-beta search algorithm computes the same optimal moves as minimax algorithm.
> - **D.** Optimal play in games of imperfact information does not require reasoning about the current and future belief states of each player. Choose the correct answer from the options given below:

**Options**

1. (A) and (C) only
2. (A) and (D) only
3. (B) and (C) only
4. (C) and (D) only 53622816950.2 53622816951.3 53622816952. 4

**Chapter foundations**

This question belongs to the ideas covered by **Approaches to AI**. Revise these foundations: Turing Test and Rational Agents; State-Space Representation; Heuristic Search; Game Playing; Minimax; Alpha-Beta Cutoff.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Approaches to AI questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 9

*UGC NET Nov 2020, original Q123*

> Match List I with List II List I List II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Greedy Best-First Search (L) Space complexity is O(d) where d=depth of the deepest optimal solution
> - **B.** A* (ID Incomplete even if the search space is finite.
> - **C.** Recursive Best First Search (III) Optimal if optimal solution is reachable: otherwise, returns the best reachable optimal solution.
> - **D.** SMA* (IV) Computation and space complexity is too high. Choose the correct answer from the options given below:

**Options**

1. A-II. B-IV. C-L. D.III
2. A-II, B-III. C-I. D-IV
3. A-II, B-II. C-IV. D-I
4. A-III, B-IV. C-II, D-I 53622816990.2 53622816991.3 53622816992.4

**Chapter foundations**

This question belongs to the ideas covered by **Approaches to AI**. Revise these foundations: Turing Test and Rational Agents; State-Space Representation; Heuristic Search; Game Playing; Minimax; Alpha-Beta Cutoff.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Approaches to AI questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 10

*UGC NET Dec 2025 session (Jan 2026), original Q138*

> Question Number : 138

**Chapter foundations**

This question belongs to the ideas covered by **Approaches to AI**. Revise these foundations: Turing Test and Rational Agents; State-Space Representation; Heuristic Search; Game Playing; Minimax; Alpha-Beta Cutoff.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Approaches to AI questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-2"></a>

### 2. Knowledge Representation (7 questions)

**What to master:** Logic; Semantic Networks; Frames; Rules; Scripts; Conceptual Dependency; Ontologies; Expert Systems; Uncertainty.

**Exam lens:** Represent states, knowledge, uncertainty, membership, or learning architecture explicitly before applying the AI technique.

**Reusable method:** For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation.

**High-yield rules:** A* uses f(n)=g(n)+h(n); an admissible heuristic never overestimates. Alpha-beta changes the number of explored nodes, not the minimax result.

**Common traps:** Distinguish admissible from consistent heuristics, probability from fuzzy membership, supervised from reinforcement learning, and planning state from search operator.

---

#### Question 11

*UGC NET Dec 2013, Paper III, original Q23*

> High level knowledge which relates to the use of sentences in different contexts and how the context affect the meaning of the sentences ?

**Options**

- **A.** Morphological
- **B.** Syntactic
- **C.** Semantic
- **D.** Pragmatic

**Chapter foundations**

This question belongs to the ideas covered by **Knowledge Representation**. Revise these foundations: Logic; Semantic Networks; Frames; Rules; Scripts; Conceptual Dependency; Ontologies; Expert Systems; Uncertainty.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Knowledge Representation questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 12

*UGC NET June 2013, Paper III, original Q72*

> Which of the following is a knowledge representation technique used to represent knowledge about stereotype situation ?

**Options**

- **A.** Semantic network
- **B.** Frames
- **C.** Scripts
- **D.** Conceptual Dependency

**Chapter foundations**

This question belongs to the ideas covered by **Knowledge Representation**. Revise these foundations: Logic; Semantic Networks; Frames; Rules; Scripts; Conceptual Dependency; Ontologies; Expert Systems; Uncertainty.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Knowledge Representation questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 13

*UGC NET Dec 2014, Paper III, original Q58*

> Match the following :
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Script i. Directed graph with labelled nodes for graphical representation of knowledge
> - **B.** Conceptual Dependencies ii. Knowledge about objects and events is stored in record-like structures consisting of slots and slot values.
> - **C.** Frames iii. Primitive concepts and rules to represent natural language statements
> - **D.** Associative Network iv. Frame like structures used to represent stereotypical patterns for commonly occurring events in terms of actors, roles, props and scenes Codes : a b c d

**Options**

- **A.** iv ii i iii
- **B.** iv iii ii i
- **C.** ii iii iv i
- **D.** i iii iv ii

**Chapter foundations**

This question belongs to the ideas covered by **Knowledge Representation**. Revise these foundations: Logic; Semantic Networks; Frames; Rules; Scripts; Conceptual Dependency; Ontologies; Expert Systems; Uncertainty.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Knowledge Representation questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 14

*UGC NET June 2015, Paper III, original Q56*

> Match the following knowledge representation techniques with their applications : List - I List - II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Frames (i) attributes and relationships Pictorial representation of objects, their
> - **B.** Conceptual dependencies (i) To describe real world stereotype events
> - **C.** Associative networks (iii) Record like structures for grouping closely related knowledge
> - **D.** Scripts (iv) Structures and primitives to represent sentences Codes: (a) (b) (c) (d)

**Options**

1. (iii) (iv) (i) (ii)
2. (iii) (iv) (ii) (i)
3. (iv) (ill) (i) (ii)
4. (iv) (iii) (ii) (i) J-8715 10 Paper-IlI

**Chapter foundations**

This question belongs to the ideas covered by **Knowledge Representation**. Revise these foundations: Logic; Semantic Networks; Frames; Rules; Scripts; Conceptual Dependency; Ontologies; Expert Systems; Uncertainty.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Knowledge Representation questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 15

*UGC NET July 2018, Paper II, original Q79*

> A knowledge base contains just one sentence, ∃ x AsHighAs ( x, Everest). Consider the following two sentences obtained after applying existential insta ntiation. (a) AsHighAs (Everest, Everest) (b) AsHighAs (Kilimanjaro, Everest) Which of the following is correct with respect to the above sentences ?

**Options**

1. Both sentence (a) and sentence (b) are sound conclusions.
2. Both sentence (a) and sentence (b) are unsound conclusions.
3. Sentence (a) is sound but sentence (b) is unsound.
4. Sentence (a) is unsound but sentence (b) is sound.

**Chapter foundations**

This question belongs to the ideas covered by **Knowledge Representation**. Revise these foundations: Logic; Semantic Networks; Frames; Rules; Scripts; Conceptual Dependency; Ontologies; Expert Systems; Uncertainty.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Knowledge Representation questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 16

*UGC NET June 2019, original Q122*

> On translating the expression given below into quadruple representation, how many operations are required? (i*j)+ (e+ f)*(a*b+c) 5 2. 6 3. 3 7 64635085824. 2 64635085825. 3 64635085826.4

**Chapter foundations**

This question belongs to the ideas covered by **Knowledge Representation**. Revise these foundations: Logic; Semantic Networks; Frames; Rules; Scripts; Conceptual Dependency; Ontologies; Expert Systems; Uncertainty.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Knowledge Representation questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 17

*UGC NET Nov 2020, original Q112*

> Which of the following statements are true? (A) A sentence a entails another sentence ß if B is true in few worlds where a is true. Forward chaining and backward chaining are very natural reasoning algorithms for knowledge bases in Horn form. (C) Sound inference algorithms derive all sentences that are entailed. (D) Propositional logic does not scale to environments of unbounded size. Choose the correct answer from the options given below:

**Options**

1. (A) and (B) only
2. (B) and (C) only
3. (C) and (D) only
4. (B) and (D) only 53622816946.2 53622816947.3 53622816948.4

**Chapter foundations**

This question belongs to the ideas covered by **Knowledge Representation**. Revise these foundations: Logic; Semantic Networks; Frames; Rules; Scripts; Conceptual Dependency; Ontologies; Expert Systems; Uncertainty.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Knowledge Representation questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-3"></a>

### 3. Planning (11 questions)

**What to master:** Components; Linear and Nonlinear Planning; Goal Stack; Hierarchical Planning; STRIPS; Partial-Order Planning.

**Exam lens:** Represent states, knowledge, uncertainty, membership, or learning architecture explicitly before applying the AI technique.

**Reusable method:** For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation.

**High-yield rules:** A* uses f(n)=g(n)+h(n); an admissible heuristic never overestimates. Alpha-beta changes the number of explored nodes, not the minimax result.

**Common traps:** Distinguish admissible from consistent heuristics, probability from fuzzy membership, supervised from reinforcement learning, and planning state from search operator.

---

#### Question 18

*UGC NET Dec 2013, Paper III, original Q25*

> If h * represents an estimate of the cost of getting from the current node N to the goal node and h represents actual cost of getting from the current node to the goal node, then A * algorithm gives an optimal solution if

**Options**

- **A.** h * is equal to h
- **B.** h * overestimates h
- **C.** h * underestimates h
- **D.** none of these

**Chapter foundations**

This question belongs to the ideas covered by **Planning**. Revise these foundations: Components; Linear and Nonlinear Planning; Goal Stack; Hierarchical Planning; STRIPS; Partial-Order Planning.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Planning questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 19

*UGC NET Dec 2013, Paper III, original Q26*

> The mean-end analysis process centers around the detection of differences between the current state and goal state. Once such a difference is isolated, an operator that can reduce the difference must be found. But perhaps that operator can not be applied to the current state. So a sub-problem of getting to a state in which it can be applied is set up. The kind of backward chaining in which operators are selected and then sub goals are set up to establish the precondition of operators is called

**Options**

- **A.** backward planning
- **B.** goal stack planning
- **C.** operator subgoaling
- **D.** operator overloading

**Chapter foundations**

This question belongs to the ideas covered by **Planning**. Revise these foundations: Components; Linear and Nonlinear Planning; Goal Stack; Hierarchical Planning; STRIPS; Partial-Order Planning.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Planning questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 20

*UGC NET June 2015, Paper II, original Q45*

> Which one from the following is highly associated activity of project planning?

**Options**

1. Keep track of the project progress.
2. Compare actual and planned progress and costs.
3. Identify the activities, milestones and deliverables produced by a project.
4. Both (2) and (3).

**Chapter foundations**

This question belongs to the ideas covered by **Planning**. Revise these foundations: Components; Linear and Nonlinear Planning; Goal Stack; Hierarchical Planning; STRIPS; Partial-Order Planning.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Planning questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 21

*UGC NET Jan 2017, Paper II, original Q50*

> Which of the following statements is/are true w.r.t. Enterprise Resource Planning (ERP) ? (A) ERP automates and integrates majority of business processes. (B) ERP provides access to information in a Real Time Environment. (C) ERP is inexpensive to implement.

**Options**

1. (A), (B) and (C) are false.
2. (A) and (B) false; (C) true.
3. (A) and (B) true; (C) false.
4. (A) true ; (B) and (C) are false. ____________

**Chapter foundations**

This question belongs to the ideas covered by **Planning**. Revise these foundations: Components; Linear and Nonlinear Planning; Goal Stack; Hierarchical Planning; STRIPS; Partial-Order Planning.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Planning questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 22

*UGC NET Jan 2017, Paper III, original Q57*

> In Artificial Intelligence (AI), what is present in the planning graph ?

**Options**

1. Sequence of levels
2. Literals
3. Variables
4. Heuristic estimates

**Chapter foundations**

This question belongs to the ideas covered by **Planning**. Revise these foundations: Components; Linear and Nonlinear Planning; Goal Stack; Hierarchical Planning; STRIPS; Partial-Order Planning.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Planning questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 23

*UGC NET Nov 2017, Paper II, original Q47*

> Which of the following statements about ERP system is true ?

**Options**

1. Most ERP software implementations fully achieve seamless integratio n.
2. ERP software packages are themselves combinations of seperate applicat ions for manufacturing, materials, resource planning, general ledger, human reso urces, procurement and order entry.
3. Integration of ERP systems can be achieved in only one way.
4. An ERP package implemented uniformly throughout an enterprise is li kely to contain very flexible connections to allow charges and software variation s.

**Chapter foundations**

This question belongs to the ideas covered by **Planning**. Revise these foundations: Components; Linear and Nonlinear Planning; Goal Stack; Hierarchical Planning; STRIPS; Partial-Order Planning.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Planning questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 24

*UGC NET July 2018, Paper II, original Q77*

> Consider the following English sentence : “Agra and Gwalior are both in India”. A student has written a logical sentence for the above English sentence i n First-Order Logic using predicate In(x, y), which means x is in y, as follows : In(Agra, India) w In(Gwalior, India) Which one of the following is correct with respect to the above logica l sentence ?

**Options**

1. It is syntactically valid but does not express the meaning of the Eng lish sentence.
2. It is syntactically valid and expresses the meaning of the English s entence also.
3. It is syntactically invalid but expresses the meaning of the Englis h sentence.
4. It is syntactically invalid and does not express the meaning of the E nglish sentence.

**Chapter foundations**

This question belongs to the ideas covered by **Planning**. Revise these foundations: Components; Linear and Nonlinear Planning; Goal Stack; Hierarchical Planning; STRIPS; Partial-Order Planning.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Planning questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 25

*UGC NET July 2018, Paper II, original Q78*

> Consider the following two sentences : (a) The planning graph data structure can be used to give a better heuristi c for a planning problem. (b) Dropping negative effects from every action schema in a planning pro blem results in a relaxed problem. Which of the following is correct with respect to the above sentences ?

**Options**

1. Both sentence (a) and sentence (b) are false.
2. Both sentence (a) and sentence (b) are true.
3. Sentence (a) is true but sentence (b) is false.
4. Sentence (a) is false but sentence (b) is true.

**Chapter foundations**

This question belongs to the ideas covered by **Planning**. Revise these foundations: Components; Linear and Nonlinear Planning; Goal Stack; Hierarchical Planning; STRIPS; Partial-Order Planning.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Planning questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 26

*UGC NET Nov 2020, original Q119*

> Match List I with List II List I List II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Branch-and-bound (I Keeps track of all partial paths which can be candidate for further exploration.
> - **B.** Steepest-accent hill climbing (I Detects difference between current state and goal state
> - **C.** Constraint satisfaction (III) Discovers problem state(s) that satisfy a set of constraints.
> - **D.** Means-end analysis (TV) Considers all moves from current state and selects best move Choose the correct answer from the options given below:

**Options**

1. A-I. B-IV. C-III, D-II
2. A-I. B-II. C-III. D-IV
3. A-II, B-I, C-III, D-IV
4. A-II. B-IV. C.III, D-I 53622816974.2 53622816975.3 53622816976.4

**Chapter foundations**

This question belongs to the ideas covered by **Planning**. Revise these foundations: Components; Linear and Nonlinear Planning; Goal Stack; Hierarchical Planning; STRIPS; Partial-Order Planning.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Planning questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 27

*UGC NET June 2024, original Q54*

> Arrange the following so that they can be placed in perfect/gppropriate order C. Modeling A. Planning Coral CROn E. Deployment D. Contrarication Choose the correct answer from the options given belon

**Options**

1. A. B, C, D. E
2. DA. C BE
3. A. D, B. C.E
4. B, CD, A. E

**Chapter foundations**

This question belongs to the ideas covered by **Planning**. Revise these foundations: Components; Linear and Nonlinear Planning; Goal Stack; Hierarchical Planning; STRIPS; Partial-Order Planning.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Planning questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 28

*UGC NET Dec 2025 session (Jan 2026), original Q119*

> Question Number : 119

**Chapter foundations**

This question belongs to the ideas covered by **Planning**. Revise these foundations: Components; Linear and Nonlinear Planning; Goal Stack; Hierarchical Planning; STRIPS; Partial-Order Planning.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Planning questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-4"></a>

### 4. Natural Language Processing (6 questions)

**What to master:** Grammar and Language; Parsing; Semantic Analysis; Pragmatics.

**Exam lens:** Represent states, knowledge, uncertainty, membership, or learning architecture explicitly before applying the AI technique.

**Reusable method:** For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation.

**High-yield rules:** A* uses f(n)=g(n)+h(n); an admissible heuristic never overestimates. Alpha-beta changes the number of explored nodes, not the minimax result.

**Common traps:** Distinguish admissible from consistent heuristics, probability from fuzzy membership, supervised from reinforcement learning, and planning state from search operator.

---

#### Question 29

*UGC NET July 2016, Paper III, original Q23*

> The regular expression for the co mplement of the language L = {anbm|n ≥ 4, m ≤ 3} is :

**Options**

1. ( λ + a + aa + aaa) b* + a* bbbb* + (a + b)* ba(a + b)*
2. ( λ + a + aa + aaa) b* + a* bbbbb* + (a + b)* ab(a + b)*
3. ( λ + a + aa + aaa) + a* bbbbb* + (a + b)* ab(a + b)*
4. ( λ + a + aa + aaa)b* + a* bbbbb* + (a + b)* ba(a + b)*

**Chapter foundations**

This question belongs to the ideas covered by **Natural Language Processing**. Revise these foundations: Grammar and Language; Parsing; Semantic Analysis; Pragmatics.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Natural Language Processing questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 30

*UGC NET July 2016, Paper III, original Q57*

> Given a Turing Machine M = ({q 0, q1, q2, q3}, {a, b}, {a, b, B}, δ, B, {q3}) Where δ is a transition function defined as δ(q0, a) = (q1, a, R) δ(q1, b) = (q2, b, R) δ(q2, a) = (q2, a, R) δ(q2, b) = (q3, b, R) The language L(M) accepted by th e Turing Machine is given as :

**Options**

1. aa*b
2. abab
3. aba*b
4. aba*

**Chapter foundations**

This question belongs to the ideas covered by **Natural Language Processing**. Revise these foundations: Grammar and Language; Parsing; Semantic Analysis; Pragmatics.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Natural Language Processing questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 31

*UGC NET Oct 2022, original Q14*

> Consider the language L = la™: n≥4,m ≤ 3) Which of the following regular expression represents language L? 1. aaaa*(2 + b + bb + bbb) 2. aaaaa*(b + bb + bbb) 3. aaaaa*(i +b+ bb + bbb)

**Chapter foundations**

This question belongs to the ideas covered by **Natural Language Processing**. Revise these foundations: Grammar and Language; Parsing; Semantic Analysis; Pragmatics.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Natural Language Processing questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 32

*UGC NET June 2023, Paper II, original Q43*

> Which is not the component of the natural language understanding process? (+2)

**Options**

- **A.** Morphological analysis
- **B.** Semantic analysis
- **C.** Pragmatic analysis
- **D.** Meaning analysis

**Chapter foundations**

This question belongs to the ideas covered by **Natural Language Processing**. Revise these foundations: Grammar and Language; Parsing; Semantic Analysis; Pragmatics.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Natural Language Processing questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 33

*UGC NET Aug 2024, original Q133*

> Match List - I with List - II. List - I List - II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Natural language processing (I) A method of training algorithm by rewarding desired behaviour and/or punishing undesired one.
> - **B.** Reinforcement learning (LI) System designed to emulate the decision making abilities of a human expert.
> - **C.** Support vector machine (III) A branch of Al focused on understanding and generating human language.
> - **D.** Expert system (IV) A machine learning technique that finds the hyper plane that best separates different class in a feature space. Choose the correct answer from the options given below : (1)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** (I),
> - **B.** -(I),
> - **C.** -(IV),
> - **D.** -(III) (2)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(III),
> - **B.** -(II),
> - **C.** -(I),
> - **D.** -(IV) (3)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(I),
> - **B.** -(1),
> - **C.** -(IV),
> - **D.** -(I) (4)

**Options**

- **A.** -(Il),
- **B.** -(IV),
- **C.** -(III,
- **D.** -(I)

**Chapter foundations**

This question belongs to the ideas covered by **Natural Language Processing**. Revise these foundations: Grammar and Language; Parsing; Semantic Analysis; Pragmatics.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Natural Language Processing questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 34

*UGC NET June 2025, original Q81*

> Consider the following DFA that generates set of strings over [=(a, b, c} Now identify that which of the followings is the best description of the language for the above DFA

**Options**

1. L= (a*+ b* + c*)*
2. L= (a+b + c)*(abc)*(a +b + c)*
3. L = (Set of strings, all starting with 'a, b, c' but ending with 'c')
4. L = {Set of strings, all having even count (including 0) of substring 'abc') 42558919377.2 42558919378. 3 42558919379.4

**Chapter foundations**

This question belongs to the ideas covered by **Natural Language Processing**. Revise these foundations: Grammar and Language; Parsing; Semantic Analysis; Pragmatics.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Natural Language Processing questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-5"></a>

### 5. Multi-Agent Systems (9 questions)

**What to master:** Agents and Objects; Agents and Expert Systems; Generic Structure; Semantic Web; Agent Communication; Ontology-Based Knowledge Sharing; Development Tools.

**Exam lens:** Represent states, knowledge, uncertainty, membership, or learning architecture explicitly before applying the AI technique.

**Reusable method:** For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation.

**High-yield rules:** A* uses f(n)=g(n)+h(n); an admissible heuristic never overestimates. Alpha-beta changes the number of explored nodes, not the minimax result.

**Common traps:** Distinguish admissible from consistent heuristics, probability from fuzzy membership, supervised from reinforcement learning, and planning state from search operator.

---

#### Question 35

*UGC NET July 2016, Paper II, original Q50*

> Given the following statements : (A) Strategic value of data mining is timestamping. (B) Information collection is an expensiv e process in building an expert system. Which of the following options is correct ?

**Options**

1. Both (A) and (B) are false.
2. Both (A) and (B) are true.
3. (A) is true, (B) is false.
4. (A) is false, (B) is true. ____________

**Chapter foundations**

This question belongs to the ideas covered by **Multi-Agent Systems**. Revise these foundations: Agents and Objects; Agents and Expert Systems; Generic Structure; Semantic Web; Agent Communication; Ontology-Based Knowledge Sharing; Development Tools.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multi-Agent Systems questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 36

*UGC NET Dec 2018, original Q141*

> An agent can improve its performance by . Perceiving 91394342562. Responding 91394342563. Learning 91394342564 Observing ingle Line Question Option: No

**Chapter foundations**

This question belongs to the ideas covered by **Multi-Agent Systems**. Revise these foundations: Agents and Objects; Agents and Expert Systems; Generic Structure; Semantic Web; Agent Communication; Ontology-Based Knowledge Sharing; Development Tools.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multi-Agent Systems questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 37

*UGC NET Dec 2018, original Q142*

> Which of the following is true for semi-dynamic environment? . The environment may change while the agent is deliberating. The environment itself does not change with the passage of time but the agent's 91394342566. performance score does. Even if the environment changes with the passage of time while deliberating, the 91394342567. performance score does not change. 91394342568. Environment and performance score, both change simultaneously. nestion Number: 142

**Chapter foundations**

This question belongs to the ideas covered by **Multi-Agent Systems**. Revise these foundations: Agents and Objects; Agents and Expert Systems; Generic Structure; Semantic Web; Agent Communication; Ontology-Based Knowledge Sharing; Development Tools.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multi-Agent Systems questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 38

*UGC NET July 2018, Paper II, original Q72*

> In Artificial Intelligence (AI), a simple reflex agent selects actions on the basis of_________.

**Options**

1. current percept, completely ignoring rest of the percept history.
2. rest of the percept history, completely ignoring current percept.
3. both current percept and complete percept history.
4. both current percept and just previous percept.

**Chapter foundations**

This question belongs to the ideas covered by **Multi-Agent Systems**. Revise these foundations: Agents and Objects; Agents and Expert Systems; Generic Structure; Semantic Web; Agent Communication; Ontology-Based Knowledge Sharing; Development Tools.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multi-Agent Systems questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 39

*UGC NET June 2019, original Q150*

> Reinforcement learning can be formalized in terms of in which the agent inutially only knows the set of possible and the set of posible actions.

**Options**

1. Markov decision processes, objects
2. Hidden states, objects
3. Markov decision processes, states
4. objects, states repp Your 64635085936.2 64635085937.3 64635085938.4

**Chapter foundations**

This question belongs to the ideas covered by **Multi-Agent Systems**. Revise these foundations: Agents and Objects; Agents and Expert Systems; Generic Structure; Semantic Web; Agent Communication; Ontology-Based Knowledge Sharing; Development Tools.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multi-Agent Systems questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 40

*UGC NET Nov 2021, original Q51*

> Which agent deals with the happy and unhappy state?

**Options**

1. Utility‐based agent
2. Model‐based agent
3. Goal‐based Agent
4. Learning Agent

**Chapter foundations**

This question belongs to the ideas covered by **Multi-Agent Systems**. Revise these foundations: Agents and Objects; Agents and Expert Systems; Generic Structure; Semantic Web; Agent Communication; Ontology-Based Knowledge Sharing; Development Tools.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multi-Agent Systems questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 41

*UGC NET June 2025, original Q120*

> Consider the following statements regarding Agent systems
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Agent system comprises of an agent and an environment on which it acts
> - **B.** The controller part of an agent receives percepts from its body and sends commands to the
> - **C.** Agents act in the world through actuators which are non-noisy and always reliable.
> - **D.** The actuators of an agent convert stimuli into percepts Choose the correct answer from the options given below:

**Options**

1. A, B Only
2. B, D Only
3. C, D Only
4. B, C, D Only 42558919533.2 42558919534.3 42558919535,4

**Chapter foundations**

This question belongs to the ideas covered by **Multi-Agent Systems**. Revise these foundations: Agents and Objects; Agents and Expert Systems; Generic Structure; Semantic Web; Agent Communication; Ontology-Based Knowledge Sharing; Development Tools.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multi-Agent Systems questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 42

*UGC NET Dec 2025 session (Jan 2026), original Q124*

> Question Number : 124

**Chapter foundations**

This question belongs to the ideas covered by **Multi-Agent Systems**. Revise these foundations: Agents and Objects; Agents and Expert Systems; Generic Structure; Semantic Web; Agent Communication; Ontology-Based Knowledge Sharing; Development Tools.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multi-Agent Systems questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 43

*UGC NET Dec 2025 session (Jan 2026), original Q125*

> Question Number : 125 , what are the key characteristics of individual agents?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** They must be identical in their capabilities and goals.
> - **B.** They are autonomous and act independently.
> - **C.** They interact with each other and their environment.
> - **D.** They are controlled by a single, centralized authority at all times. Choose the correct answer from the options given below:

**Options**

1. A, B & C Only
2. B, C & D Only
3. B & D Only
4. A & D Only 6119878898.2 6119878899.3 6119878900.4 Number : Yes Is Ouestion Mandatory : No Single Line Ouestion Option : No

**Chapter foundations**

This question belongs to the ideas covered by **Multi-Agent Systems**. Revise these foundations: Agents and Objects; Agents and Expert Systems; Generic Structure; Semantic Web; Agent Communication; Ontology-Based Knowledge Sharing; Development Tools.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multi-Agent Systems questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-6"></a>

### 6. Fuzzy Sets (17 questions)

**What to master:** Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam lens:** Represent states, knowledge, uncertainty, membership, or learning architecture explicitly before applying the AI technique.

**Reusable method:** For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation.

**High-yield rules:** A* uses f(n)=g(n)+h(n); an admissible heuristic never overestimates. Alpha-beta changes the number of explored nodes, not the minimax result.

**Common traps:** Distinguish admissible from consistent heuristics, probability from fuzzy membership, supervised from reinforcement learning, and planning state from search operator.

---

#### Question 44

*UGC NET Dec 2013, Paper III, original Q28*

> If A and B are two fuzzy sets with membership functions μA(x) = {0.2, 0.5, 0.6, 0.1, 0.9} μB(x) = {0.1, 0.5, 0.2, 0.7, 0.8} Then the value of μA ∩ B will be

**Options**

- **A.** {0.2, 0.5, 0.6, 0.7, 0.9}
- **B.** {0.2, 0.5, 0.2, 0.1, 0.8}
- **C.** {0.1, 0.5, 0.6, 0.1, 0.8}
- **D.** {0.1, 0.5, 0.2, 0.1, 0.8}

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 45

*UGC NET Dec 2013, Paper III, original Q29*

> The height h(A) of a fuzzy set A is defined as h(A) = sup A( x) x ∈ A Then the fuzzy set A is called normal when

**Options**

- **A.** h(A) = 0
- **B.** h(A) < 0
- **C.** h(A) = 1
- **D.** h(A) < 1

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 46

*UGC NET June 2013, Paper III, original Q73*

> A fuzzy set A on R is ________ iff A( λx1 + (1 – λ )x2) ≥ min [A( x1), A(x2)] for all x1, x2 ∈ R and all λ ∈ [0, 1], where min denotes the minimum operator.

**Options**

- **A.** Support
- **B.** α-cut
- **C.** Convex
- **D.** Concave

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 47

*UGC NET June 2013, Paper III, original Q74*

> If A and B are two fuzzy sets with membership functions μA(x) = {0.6, 0.5, 0.1, 0.7, 0.8} μB(x) = {0.9, 0.2, 0.6, 0.8, 0.5} Then the value of μ–––––A ∪ B(x) will be

**Options**

- **A.** {0.9, 0.5, 0.6, 0.8, 0.8}
- **B.** {0.6, 0.2, 0.1, 0.7, 0.5}
- **C.** {0.1, 0.5, 0.4, 0.2, 0.2}
- **D.** {0.1, 0.5, 0.4, 0.2, 0.3}

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 48

*UGC NET Dec 2014, Paper III, original Q71*

> A _________ point of a fuzzy set A is a point x ∈ X at which µ A(x) = 0.5

**Options**

- **A.** core
- **B.** support
- **C.** crossover
- **D.** α-cut

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 49

*UGC NET June 2015, Paper III, original Q71*

> Let A and B be two fuzzy integers defined as : А = 1(1, 0.3), (2, 0.6), (3, 1), (4, 0.7), (5, 0.2)} В = 1(10, 0.5), (11, 1), (12, 0.5)} Using fuzzy arithmetic operation given by MA +B(Z) = (MA (х) ДМВ(У)) x+Y = z f(A+B) is _ Note: = max 8 = min/

**Options**

1. (11, 0.8), (13, 1), (15,1)}
2. 1(11, 0.3), (12, 0.5), (13, 1), (14, 1), (15, 1), (16, 0.5), (17, 0.2)}
3. 1(11, 0.3), (12, 0.5), (13, 0.6), (14, 1), (15, 1), (16, 0.5), (17, 0.2)}
4. 1(11, 0.3), (12, 0.5), (13, 0.6), (14, 1), (15, 0.7), (16, 0.5), (17, 0.2)}

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 50

*UGC NET June 2015, Paper III, original Q72*

> Suppose the function y and a fuzzy integer number around - 4 for x are given as y = (x-3) +2. Around - 4 = 1(2, 0.3), (3, 0.6), (4, 1), (5, 0.6), (6, 0.3)) respectively. Then f (Around - 4) is given by :

**Options**

1. 1(2, 0.6), (3, 0.3), (6, 1), (11, 0.3)}
2. 1(2, 0.6), (3, 1), (6, 1), (11, 0.3)}
3. 1(2, 0.6), (3, 1), (6, 0.6), (11, 0.3)}
4. 1(2, 0.6), (3, 0.3), (6, 0.6), (11, 0.3)} J-8715 14 Paper-IlI

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 51

*UGC NET July 2016, Paper III, original Q65*

> Compute the value of adding the following two fuzzy integers : A = {(0.3, 1), (0.6, 2), (1 , 3), (0.7, 4), (0.2, 5)} B = {(0.5, 11), (1, 12), (0.5, 13)} Where fuzzy addition is defined as μA+B (z) = max x + y = z (min (μA(x), μB(x))) Then, f (A + B) is equal to

**Options**

1. {(0.5, 12), (0.6, 13), (1, 14), (0.7, 15), (0.7, 16), (1, 17), (1, 18)}
2. {(0.5, 12), (0.6, 13), (1, 14), ( 1, 15), (1, 16), (1, 17), (1, 18)}
3. {(0.3, 12), (0.5, 13), (0.5, 14), ( 1, 15), (0.7, 16), (0.5, 17), (0.2, 18)}
4. {(0.3, 12), (0.5, 13), (0.6, 14), ( 1, 15), (0.7, 16), (0.5, 17), (0.2, 18)}

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 52

*UGC NET Dec 2019, original Q112*

> A fuzzy conjunction operators, t (x. y). and a fuzzy disjunction operator. s (x.y). form a pair if they satisfy: t(x. y) = 1-s(1-x1 -y). sona If t(x.y) = xy -then s(x. y) is given by (x + y - ху)

**Options**

1. x + y
2. x+ y - 2xy 1 -ху 1-ху
3. х + у - ху 1 - ху
4. x + у - ху 1 + xy 61547541146.2 61547541147.3 61547541148.4

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 53

*UGC NET June 2019, original Q144*

> A fuzzy conjunction operator denoted as f(x, y) and a fuzzy disjunction operator denoted as s(x, y) form a dual pair if they satisfy the condition: 1. *(x, y) =1-s(x, y) O 2. *(x, y) = s(1 -x, 1 -y) 3. 1(x, y) =1-s(1-x, 1-y) "(x, y) = s(1+x, 1+ y) 64635085912. 2 64635085913.3 64635085914. 4

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 54

*UGC NET June 2019, original Q145*

> Let Aug denotes the o-cut of a fuzzy set 4 at ap. If cy < 0, then sona 1. Au, Aar 2. A 3. 4. CAar 64635085916. 2 64635085917.3 64635085918.4

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 55

*UGC NET Nov 2020, original Q90*

> Consider the following argument with premise V, (P(x) v Q(x)) and conclusion (VxP(x))A (VxQ(x))
>
> **Additional extracted choices — check the source page:**
>
> - **A.** V, (P(x) v Q(x)) Premise
> - **B.** P(c) V Q(c) Universal instantiation from (A)
> - **C.** P(c) Simplification from (B)
> - **D.** Vx P(x) Universal Generalization of (C) (E) Q(c) Simplification from (B) (F) V, Q(x) Universal Generalization of (E) (G) (V,P(x)) A (VxQ(x)) Conjunction of (D) and (F)

**Options**

1. This is a valid argument.
2. Steps (C) and (E) are not correct inferences
3. Steps (D) and (F) are not correct inferences
4. Step (G) is not a correct inference 53622816858.2 53622816859. 3 53622816860.4

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 56

*UGC NET Nov 2021, original Q29*

> Let (X, *) be a semigroup. Furthermore, for every a and b in X, if a ≠ b, then a*b ≠ b*a. Based on the defined seimigroup, choose the correct equalities from the options given below: A. For every a in X, a*a = a B. For every a, b in X, a*b *a= a C. For every a, b, c in X, a*b *c= a*c

**Options**

1. A and B only
2. A and C only
3. B and C only
4. A, B and C

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 57

*UGC NET June 2024, original Q80*

> For the fuzzy set A - (k, 03), (23, 0.7, (53, 04), the complement of A would be represen (1) A and B Only (2) Band COnly (2) 1(5, 0.3), (x 0.2), (xz 0.4)) (1) I=, D4). (xy, 0.3), (2g. 0.1)) (4) ((2y,. 0.21), (=≥ 0.28), (xy, 0.12)) (3) ((F, 0.7), (zz 0.3). (ty. 0.6))

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 58

*UGC NET June 2024, original Q96*

> Arrange the following sets in increasing ordes on the basis of their cardinality : A. A, = ([L 2), (3)) BL 02 = (
>
> **Additional extracted choices — check the source page:**
>
> 1. ,
> 2. .
> 3. .
> 4. ) C. A, - |(1, 2, 3, 4, 5, 6)) D. A, - ((1, 2). 12. 3, 4]. (5)) E. A, - (

**Options**

1. ,
2. ,
3. .
4. , (5]) Choose the correct answer from the options given celow : (1) A, B, D, E, C (2) A, B, E, D, C (3) A, C. D, B, E (A) C, A, D, B, E

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 59

*UGC NET June 2024, original Q97*

> The Cardinality of a fuzzy set is

**Options**

1. 0
2. finite
3. infinite
4. not known

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 60

*UGC NET June 2025, original Q139*

> Match List I with List II List 1 (Operations on Fuzzy Sets) List II (Description)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Intersection 1. MA(x) + Mg (x) - M*(x). Mg(x)
> - **B.** Bounded Sum II. max(0, Ma(x) - Ng(x))
> - **C.** Bounded Difference III. min(1, Ma(x) + MB (x))
> - **D.** Algebraic Sum IV. min (Ma(x) , HB(x)) Choose the correct answer from the options given below:

**Options**

1. A→III, B→I, C→II, D→IV
2. A→III, B→II, C→IV, D→I
3. A→IV, B→III, C→II, D>I
4. A>II, B>I, C→III, D→IV 42558919608. 1 42558919610.3 42558919611.4

**Chapter foundations**

This question belongs to the ideas covered by **Fuzzy Sets**. Revise these foundations: Fuzziness; Membership Functions; Fuzzification and Defuzzification; Operations; Functions and Linguistic Variables; Relations; Rules and Inference; Fuzzy Control and Rule-Based Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Fuzzy Sets questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-7"></a>

### 7. Genetic Algorithms (9 questions)

**What to master:** Encoding; Genetic Operators; Fitness Functions; GA Cycle; Problem Solving.

**Exam lens:** Represent states, knowledge, uncertainty, membership, or learning architecture explicitly before applying the AI technique.

**Reusable method:** For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation.

**High-yield rules:** A* uses f(n)=g(n)+h(n); an admissible heuristic never overestimates. Alpha-beta changes the number of explored nodes, not the minimax result.

**Common traps:** Distinguish admissible from consistent heuristics, probability from fuzzy membership, supervised from reinforcement learning, and planning state from search operator.

---

#### Question 61

*UGC NET Dec 2015, Paper III, original Q45*

> Reasoning strategies used in expert systems include Forward chaining, backward chaining and problem reduction Forward chaining, backward chaining and boundary mutation Forward chaining, backward chaining and back propagation Backward chaining, problem reduction and boundary mutation

**Chapter foundations**

This question belongs to the ideas covered by **Genetic Algorithms**. Revise these foundations: Encoding; Genetic Operators; Fitness Functions; GA Cycle; Problem Solving.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Genetic Algorithms questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 62

*UGC NET July 2018, Paper II, original Q73*

> In heuristic search algorithms in Artificial Intelligence (AI), i f a collection of admissible heuristics h1.......hm is available for a problem and none of them dominates any of the others, which should we choose ?

**Options**

1. h(n)= max{h 1(n),....,h m(n)}
2. h(n)= min{h 1(n),....,h m(n)}
3. h(n)= avg{h 1(n),....,h m(n)}
4. h(n)= sum{h 1(n),....,h m(n)}

**Chapter foundations**

This question belongs to the ideas covered by **Genetic Algorithms**. Revise these foundations: Encoding; Genetic Operators; Fitness Functions; GA Cycle; Problem Solving.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Genetic Algorithms questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 63

*UGC NET Dec 2019, original Q115*

> Let the population of chromosomes in genetic algorithm is represented in terms of binary number. The strength of fitness of a chromosome in decimal form, x. is given by S f(x) = f(x) wheref(x) = x? Ef(x) The population is given by P where: P= {01101. (11000), (01000). (10011)} The strength of fitness of chromosome (11000) is -

**Options**

1. 24
2. 576
3. 14.4
4. 49.2 Options :

**Chapter foundations**

This question belongs to the ideas covered by **Genetic Algorithms**. Revise these foundations: Encoding; Genetic Operators; Fitness Functions; GA Cycle; Problem Solving.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Genetic Algorithms questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 64

*UGC NET June 2019, original Q147*

> Consider the following :
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Evolution
> - **B.** Selection
> - **C.** Reproduction
> - **D.** Mutation Which of the following are found in genetic algorithms? 1. (b), (c) and (d) only 2. (b) and (d) only 3.

**Options**

- **A.** ,
- **B.** ,
- **C.** and
- **D.** irsonal Exam Guide 4. (a), (b) and (d) only 64635085924. 2 64635085925.3 64635085926.4

**Chapter foundations**

This question belongs to the ideas covered by **Genetic Algorithms**. Revise these foundations: Encoding; Genetic Operators; Fitness Functions; GA Cycle; Problem Solving.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Genetic Algorithms questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 65

*UGC NET Nov 2020, original Q140*

> Given below are two statements: Statement I: A genetic algorithm is a stochastie hill climbing search in which a large population of states is maintained. Statement II: In nondeterministic environments, agents can apply AND-OR search to generate contingent plans that reach the goal regardless of which outcomes occur during execution. In the light of the above statements. choose the Correct answer from the options given below

**Options**

1. Both Statement I and Statement II are true
2. Both Statement I and Statement Il are false
3. Statement I is correct but Statement II is false
4. Statement I is incorrect but Statement II is true 53622817058.2 53622817059.3 53622817060.4 Sub-Section Number: 33628171 Sub-Section Id : Question Shuffling Allowed : Yes

**Chapter foundations**

This question belongs to the ideas covered by **Genetic Algorithms**. Revise these foundations: Encoding; Genetic Operators; Fitness Functions; GA Cycle; Problem Solving.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Genetic Algorithms questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 66

*UGC NET June 2023, Paper II, original Q72*

> Which of the following is not a mutation operator in a genetic algorithm? (+2)

**Options**

- **A.** Random resetting
- **B.** Scramble
- **C.** Inversion
- **D.** Difference Choose the correct answer from the options given below: repp a. A and B only b. Band D only c. C and D only a. D only lal Exams Guide

**Chapter foundations**

This question belongs to the ideas covered by **Genetic Algorithms**. Revise these foundations: Encoding; Genetic Operators; Fitness Functions; GA Cycle; Problem Solving.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Genetic Algorithms questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 67

*UGC NET Aug 2024, original Q105*

> Arrange the following steps in proper sequence involved in a Genetic Algorithm :
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Selection
> - **B.** Initialization
> - **C.** Crossover
> - **D.** Mutation Evaluation Choose the correct answer from the options given below : (1)

**Options**

- **A.** ,
- **B.** ,
- **C.** ,
- **D.** , (E) (2) (E), (A), (B), (D), (C) (3) (B), (E), (A), (C), (D) (4) (A), (C), (B), (D), (E)

**Chapter foundations**

This question belongs to the ideas covered by **Genetic Algorithms**. Revise these foundations: Encoding; Genetic Operators; Fitness Functions; GA Cycle; Problem Solving.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Genetic Algorithms questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 68

*UGC NET June 2024, original Q122*

> The parameter Actual count is used in Genetic Algorithm (GA) for : (1) Crossover (4) Encoding the Genebe Algorithm (2) Mutation (3) Selecting population

**Chapter foundations**

This question belongs to the ideas covered by **Genetic Algorithms**. Revise these foundations: Encoding; Genetic Operators; Fitness Functions; GA Cycle; Problem Solving.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Genetic Algorithms questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 69

*UGC NET June 2025, original Q88*

> Which of the followings is Not a parent selection technique used in genetic algorithm implementations

**Options**

1. Radial
2. Tournament
3. Boltzmann
4. Rank 42558919405.2 42558919406.3 42558919407.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Genetic Algorithms**. Revise these foundations: Encoding; Genetic Operators; Fitness Functions; GA Cycle; Problem Solving.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Genetic Algorithms questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-8"></a>

### 8. Artificial Neural Networks (28 questions)

**What to master:** Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam lens:** Represent states, knowledge, uncertainty, membership, or learning architecture explicitly before applying the AI technique.

**Reusable method:** For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation.

**High-yield rules:** A* uses f(n)=g(n)+h(n); an admissible heuristic never overestimates. Alpha-beta changes the number of explored nodes, not the minimax result.

**Common traps:** Distinguish admissible from consistent heuristics, probability from fuzzy membership, supervised from reinforcement learning, and planning state from search operator.

---

#### Question 70

*UGC NET Dec 2012, Paper II, original Q46*

> Back propagation is a learning No, Skill), then query to retrieve all technique that adjusts weights in the distinct pairs of posting-nos. requiring neural network by propagating weight skill is changes. (A) Select p.posting-No, p.posting-

**Options**

- **A.** Forward from source to sink No
- **B.** Backward from sink to source from position p
- **C.** Forward from source to hidden where p.skill = p.skill nodes and p.posting-No < p.posting-No
- **D.** Backward from since to hidden nodes (B) Select Pi posting-No, P2-posting- No

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 71

*UGC NET Dec 2013, Paper III, original Q30*

> An artificial neuron receives n inputs x1, x2,...., xn with weights w1, w2,...., wn attached to the input links. The weighted sum ________ is computed to be passed on to a non-linear filter φ called activation function to release the output.

**Options**

- **A.** Σ wi
- **B.** Σ xi
- **C.** Σ wi + Σ xi
- **D.** Σ wi ⋅ xi

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 72

*UGC NET June 2013, Paper III, original Q21*

> Which one of the following media is multidrop ?

**Options**

- **A.** Shielded Twisted pair cable
- **B.** Unshielded Twisted pair cable
- **C.** Thick Coaxial cable
- **D.** Fiber Optic cable

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 73

*UGC NET Dec 2014, Paper III, original Q70*

> Consider the following statements about a perception : I. Feature detector can be any function of the input parameters. II. Learning procedure only adjusts the connection weights to the output layer. Identify the correct statement out of the following :

**Options**

- **A.** I is false and II is false.
- **B.** I is true and II is false.
- **C.** I is false and II is true.
- **D.** I is true and II is true.

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 74

*UGC NET Dec 2015, Paper II, original Q3*

> Which of the following is/are not true ?

**Options**

- **A.** The set of negative integers is countable.
- **B.** The set of integers that are multiples of 7 is countable.
- **C.** The set of even integers is countable.
- **D.** The set of real numbers between 0 and ½ is countable. Codes : (1) (a) and (c) (3) b) only (4) (d) only

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 75

*UGC NET Dec 2015, Paper III, original Q64*

> Consider the two class classification task that consists of the following points : Class C1 : 1-1, - 1, 1-1, 1), 11, - 1] Class C2 : [1, 1] The decision boundary between the two classes C, and C2 using single perceptron is given by :

**Options**

1. x1-x2-0.5=0
2. - x1+X2-05=0
3. 0.5(x1+X2) - 1.5=0
4. xy+X2-0.5=0

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 76

*UGC NET June 2015, Paper III, original Q70*

> Consider the two class classification task that consists of the following points : Class C, : [1 1.5] -1.5] Class C2 : 1-2 2.5] [-2 - 2.5] The decision boundary between the two classes using single perceptron is given by :

**Options**

1. x+X2+1.5=0
2. x1+X2-1.5=0
3. xy +1.5=0
4. x1 - 1.5=0

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 77

*UGC NET July 2016, Paper II, original Q10*

> In a positive-edge-triggered JK flip-flop, if J and K both are high then the output will be _____ on the rising edge of the clock.

**Options**

1. No change
2. Set
3. Reset
4. Toggle

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 78

*UGC NET July 2016, Paper III, original Q13*

> Consider the Breshenham’s circle generation al gorithm for plotting a circle with centre (0, 0) and radius ‘r’ units in first quadrant. If the current point is ( xi, y i) and decision parameter is p i then what will be the next point ( xi + 1 , y i + 1 ) and updated decision parameter pi + 1 for pi ≥ 0 ?

**Options**

1. xi + 1 = xi + 1
2. xi + 1 = xi + 1 y i + 1 = yi yi + 1 = yi – 1 p i + 1 = pi + 4xi + 6 p i + 1 = pi + 4 (xi – yi) + 10
3. xi + 1 = xi
4. xi + 1 = xi – 1 y i + 1 = yi – 1 y i + 1 = yi p i + 1 = pi + 4 (xi – yi) + 6 p i + 1 = pi + 4xi + 10

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 79

*UGC NET Jan 2017, Paper III, original Q55*

> Consider following two rules R1 and R2 in logical reasoning in Artificial Intelligence (AI) : R1 : From α ⊃ β and α Inter β is known as Modus Tollens (MT) R2 : From α ⊃ β and β Inter α is known as Modus Ponens (MP)

**Options**

1. Only R1 is correct.
2. Only R2 is correct.
3. Both R1 and R2 are correct.
4. Neither R1 nor R2 is correct.

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 80

*UGC NET Jan 2017, Paper III, original Q59*

> Which of the following statements is true ?

**Options**

1. The sentence S is a logical consequence of S 1,…, Sn if and only if S 1 ∧ S2 ∧........ ∧ Sn → S is satisfiable.
2. The sentence S is a logical consequence of S 1,…, Sn if and only if S 1 ∧ S2 ∧........ ∧ Sn → S is valid.
3. The sentence S is a logical consequence of S 1,…, Sn if and only if S 1 ∧ S2 ∧........ ∧ Sn ∧ S is consistent.
4. The sentence S is a logical consequence of S 1,…, Sn if and only if S 1 ∧ S2 ∧........ ∧ Sn ∧ S is inconsistent.

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 81

*UGC NET Jan 2017, Paper III, original Q73*

> Which of the following neural netw orks uses supervised learning ? (A) Multilayer perceptron (B) Self organizing feature map (C) Hopfield network

**Options**

1. (A) only
2. (B) only
3. (A) and (B) only
4. (A) and (C) only

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 82

*UGC NET Nov 2017, Paper II, original Q48*

> Which of the following is not a Clustering method ?

**Options**

1. K - Mean method
2. Self Organizing feature map method
3. K - nearest neighbor method
4. Agglomerative method

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 83

*UGC NET Dec 2018, original Q81*

> Let r = a(a + b)*, s = aa*b and t = a*b be three regular expressions. Consider the following : (i) L(s) c L(r) and L(s) c L(t) (ii) L(r) c L(s) and L(s) c L(t) Choose the correct answer from the code given below : Code: . Only (i) is correct. 91394342322. Only (ii) is correct. 91394342323 Both (i) and (ii) are correct. 91394342324 Neither (i) nor (i) is correct. ingle Line Question Option: No

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 84

*UGC NET July 2018, Paper II, original Q71*

> In Artificial Intelligence (AI), an environment is uncertain if it i s ________.

**Options**

1. Not fully observable and not deterministic
2. Not fully observable or not deterministic
3. Fully observable but not deterministic
4. Not fully observable but deterministic

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 85

*UGC NET July 2018, Paper II, original Q74*

> Consider following sentences regarding A *, an informed search strategy in Artificial Intelligence (AI). (a) A* expands all nodes with f(n) < C *. (b) A* expands no nodes with f(n) /c47=3C*. (c) Pruning is integral to A *. Here, C* is the cost of the optimal solution path. Which of the following is correct with respect to the above statements ?

**Options**

1. Both statement (a) and statement (b) are true.
2. Both statement (a) and statement (c) are true.
3. Both statement (b) and statement (c) are true.
4. All the statements (a), (b) and (c) are true.

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 86

*UGC NET Dec 2019, original Q113*

> Let W,, represents weight between node i at layer k and node j at layer (k-1) of a given multilayer perceptron. The weight updation using gradient descent method is given by

**Options**

1. W(t + 1) = Wy(t) + a дЕ ow,, .0≤a ≤1
2. W, (t + 1) = W(t) - a aw, -.0≤a≤1
3. W, (t + 1) = a дЕ aW, .0 ≤ a ≤1
4. W(t+ 1) = -a 8E aW,, -0 ≤ a ≤1 Where a and E represents learning rate and Error in the output respectively. 61547541150. 2 61547541151.3 61547541152.4

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 87

*UGC NET Nov 2020, original Q86*

> Which of the following is NOT true in problem solving in artificial intelligence?

**Options**

1. Implements heuristic search techniques
2. Solution steps are not explicit
3. Knowledge is imprecise
4. It works on or implements repetition mechanism 53622816842.2 53622816843.3 53622816844. 4

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 88

*UGC NET Nov 2020, original Q106*

> Consider the following languages: 4, = {a* | 2 is an integer) 42 = {a** |Z≥0} La = [cow | we (a, b)*) Which of the languages is (are) regular? Choose the correct answer from the options given below: (1) Ly and L only (2) Ly and L, only (8) L, only (4) La only 53622816922. 2 53622816923. 3 53622816924.4

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 89

*UGC NET Nov 2021, original Q85*

> The reverse Polish notation of the following infix expression [A*{B+C*(D+E)}] / {F*(G+H)} is__________.

**Options**

1. ABCDE+*+*FGH+*/
2. ABCDE*++*FGH+*/
3. ABCDE+*+*FGH*+/
4. ABCDE+**+FGH+*/

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 90

*UGC NET Aug 2024, original Q104*

> Arrange the following steps in a proper sequence for the process of training a neural network.
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Weight initialization
> - **B.** Feed forward
> - **C.** Back Propagation
> - **D.** Loss Calculation (E) Weight Update Choose the correct answer from the options given below :

**Options**

1. (A), (B), (D), (C), (E)
2. (D), (B), (A), (C), (E)
3. (A), (C), (D), (B), (E)
4. (E), (C), (B), (D), (A)

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 91

*UGC NET Aug 2024, original Q132*

> Match List - I with List - II. List - I List - II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** The activation function (I) is called the delta rule.
> - **B.** The learning method of perceptron (11) is one of the key components of the perceptron as in the most common neural network architecture.
> - **C.** Areas of application of artificial neural (III) is always boolean like a switch. network include
> - **D.** The output of the perceptron (IV) system identification and control. Choose the correct answer from the options given below : (1)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(II),
> - **B.** -(IV),
> - **C.** -(III),
> - **D.** -(l) (2)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(IV),
> - **B.** -(IL),
> - **C.** -(II,
> - **D.** -(I) (3)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(II),
> - **B.** -(I),
> - **C.** -(IV),
> - **D.** -(III) (4)

**Options**

- **A.** -III,
- **B.** -(IV),
- **C.** -(I,
- **D.** -(l)

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 92

*UGC NET Aug 2024, original Q142*

> Artificial Neural Networks (ANNs) are inspired by :

**Options**

1. Quantum mechanics
2. Human brain's neural network
3. Computer Hardware architecture
4. Genetic algorithm

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 93

*UGC NET June 2024, original Q57*

> Arrange the following examples of Ath Intellipence (Al) in the order of increasing complexity A. Spam email detection using rule 192 Handwritten digit recopritiun sling shallow neural networke C. Image classification using cor dubional neural networts D. Autonomous driving using resurement learning algorithras Choose the correct answer from the optens given below (1) A. B. C, D (2) B, A, C, D (3) A 6, D. C

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 94

*UGC NET June 2024, original Q83*

> Back propagation is a learning technique that adjusts weights in the neural network by prope weight changes:

**Options**

1. Forward from source to hidden nodes
2. Backward from sink to source
3. Forward from source to sink
4. Backward from sink to hidden nodes

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 95

*UGC NET June 2025, original Q90*

> Consider the following table defining the sample inputs and corresponding target values for a perceptron model. Sample No x2 target w1 w2 1 1 S3 1 1 1 1 1 What shall be the value of updated weights after applying all the samples S1 to S4 (in the order S1, S2, S3, S4) to this model. Given that the initial weights w1=0, w2=0, learning rate =0.1 and no bias is involved in the perceptron. The activation function for this perceptron is given below Y_ observed= S- if yin > 0 10 if yin < 0

**Options**

1. w1=0.1, w2 = 0.1
2. w1=0.0, w2 = 0.2
3. w1=0.0, w2 = 0.1
4. W1=0.2, w2 = 0.2 42558919413.2 42558919414. 3 42558919415.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 96

*UGC NET Dec 2025 session (Jan 2026), original Q122*

> Question Number : 122

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 97

*UGC NET Dec 2025 session (Jan 2026), original Q128*

> Question Number : 128

**Chapter foundations**

This question belongs to the ideas covered by **Artificial Neural Networks**. Revise these foundations: Supervised, Unsupervised and Reinforcement Learning; Single and Multilayer Perceptrons; Self-Organizing Maps; Hopfield Network.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Artificial Neural Networks questions: For search show OPEN/CLOSED or minimax values; for logic ground and resolve; for fuzzy questions compute membership then aggregate and defuzzify; for neural nets calculate net input and activation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

## Coverage and quality notes

- Recovered question blocks in this unit: **97**
- Chapter placements with direct keyword support: **89**
- Chapter placements needing manual review: **8**
- Questions with validated answers in this guide: **0**
- OCR may flatten mathematical notation, tables, code indentation, and figures. Full audit references are retained in the structured data.
- Some combined Paper 1/Paper 2 scans and older papers lack a trustworthy embedded key. Such questions remain pending rather than receiving guessed answers.

---

[Back to contents](#contents) · [All units](README.md) · [Project home](../README.md)

