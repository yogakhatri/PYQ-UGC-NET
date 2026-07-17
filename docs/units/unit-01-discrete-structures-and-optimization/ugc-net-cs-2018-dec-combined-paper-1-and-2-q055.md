# Question 55

*UGC NET CS · 2018 Dec Paper 1 And 2 · Boolean Algebra · Functional Completeness, Circuits and Finite Boolean Algebras*

Which statements are true? (i) Every logic network is equivalent to one using only NAND gates or only NOR gates. (ii) Boolean expressions and logic networks correspond to labelled acyclic digraphs. (iii) No two Boolean algebras with n atoms are isomorphic. (iv) Nonzero elements of finite Boolean algebras are not uniquely expressible as joins of atoms.

- **1.** (i) and (iv) only
- **2.** (i), (ii) and (iii) only
- **3.** (i) and (ii) only
- **4.** (ii), (iii) and (iv) only

> [!TIP]
> **Correct answer: 3. (i) and (ii) only**

## Solution

Statement (i) is true because NAND alone and NOR alone are functionally complete: every Boolean function can be built using either gate type. Statement (ii) is true because a combinational circuit has no feedback path; its gate-dependency graph is a directed acyclic graph. Statement (iii) is false: finite Boolean algebras with the same number of atoms are isomorphic (both are power-set algebras on that many atoms). Statement (iv) is false because every element has a unique representation as the join of the atoms below it. Hence only (i) and (ii) are true, option 3.

## Key Points

- NAND/NOR are universal; combinational circuits are DAGs; a finite Boolean algebra is determined up to isomorphism by its atoms.

## Why the other options are incorrect

Options that include (iii) or (iv) accept claims contradicted by the representation theorem for finite Boolean algebras. Options omitting (i) or (ii) reject standard facts about universal gates and feedback-free combinational circuits.
