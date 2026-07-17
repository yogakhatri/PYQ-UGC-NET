# Question 103

*UGC NET CS · 2019 June Paper 1 And 2 · Software Testing · Statement, branch and path coverage*

In the context of software testing, which of the following statements is/are NOT correct? P: A minimal test set that achieves 100% path coverage will also achieve 100% statement coverage. Q: A minimal test set that achieves 100% path coverage will generally detect more faults than one that achieves 100% statement coverage. R : A minimal test set that achieves 100% statement coverage will generally detect more faults than one that achieves 100% branch coverage.

- **1.** R only
- **2.** Q only
- **3.** P and Q only
- **4.** Q and R only

> [!TIP]
> **Correct answer: 1. R only**

## Solution

P is correct because executing every feasible path necessarily executes every reachable statement. Q is also a reasonable testing-strength statement: path coverage exercises more distinct control-flow behaviours than statement coverage and generally exposes more faults. R is not correct because branch coverage is stronger than statement coverage; a statement-complete test set can still miss one outcome of a decision. Hence only R is incorrect.

## Key Points

- The usual strength order is statement coverage < branch coverage < path coverage, although complete path coverage may be infeasible with loops.

## Why the other options are incorrect

Options 2–4 mark Q, or both P and Q, as incorrect even though path coverage subsumes statement coverage and normally exercises more behaviour.
