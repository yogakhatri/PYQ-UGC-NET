# Question 74

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Software Design · Information Hiding*

3 Option 1D=457951 SB.D:89024 The cyclomatic complexity metric provides the designer with information regarding the number of...

- **1.** Cycles in the program
- **2.** Errors in the program
- **3.** Independent logic paths in the program
- **4.** Statements in the program

> [!TIP]
> **Correct answer: 3. Independent logic paths in the program**

## Solution

Cyclomatic complexity V(G)=E−N+2P measures the number of linearly independent control-flow paths. It guides basis-path testing by indicating how many independent paths require tests.

## Key Points

- Cyclomatic complexity = independent paths through the control-flow graph.

## Why the other options are incorrect

It is not a direct count of source statements, defects, or literal loop cycles.
