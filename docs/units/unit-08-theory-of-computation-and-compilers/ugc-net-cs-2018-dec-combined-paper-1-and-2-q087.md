# Question 87

*UGC NET CS · 2018 Dec Paper 1 And 2 · Unsolvable Problems and Computational Complexity · Decidability of Automata and Turing-Machine Properties*

Consider: (i) whether a finite-state automaton halts on all inputs; (ii) whether a given context-free language is regular; (iii) whether a Turing machine computes the product of two numbers. Which problems are undecidable?

- **1.** Only (i) and (iii) are undecidable
- **2.** Only (ii) and (iii) are undecidable
- **3.** Only (i) and (ii) are undecidable
- **4.** (i), (ii), and (iii) are undecidable

> [!TIP]
> **Correct answer: 2. Only (ii) and (iii) are undecidable**

## Solution

Problem (i) is decidable: an ordinary finite automaton processes one symbol per transition and stops after a finite input is consumed, so it halts on every input. Problem (ii)—whether an arbitrary context-free language is regular—is undecidable. Problem (iii) asks whether a given Turing machine computes one particular nontrivial function on all relevant inputs; by Rice’s theorem/equivalent program-property reductions, this semantic property is undecidable. Hence only (ii) and (iii) are undecidable, option 2.

## Key Points

- Finite-automaton execution is structurally bounded; nontrivial semantic properties of Turing-machine computations are undecidable.

## Why the other options are incorrect

Options 1, 3, and 4 wrongly include the finite-automaton halting question among the undecidable cases. Finite automata have no unbounded work-tape computation and consume finite input in finitely many steps.
