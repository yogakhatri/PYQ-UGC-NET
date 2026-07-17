# Question 31

*UGC NET CS · 2012 Dec Paper 2 · Software Testing · Basis-Path Testing*

Basis-path testing falls under:

- **1.** System testing
- **2.** White-box testing
- **3.** Black-box testing
- **4.** Unit testing

> [!TIP]
> **Correct answer: 2. White-box testing**

## Solution

Basis-path testing examines a program's control-flow graph. Cyclomatic complexity gives the number of linearly independent paths, and test cases are designed to execute each independent basis path. Because the technique uses internal control structure and code paths, it is a white-box testing technique.

## Key Points

- Basis-path testing = control-flow graph + cyclomatic complexity + independent paths, so it is white-box testing.

## Why the other options are incorrect

Black-box testing derives cases from externally visible requirements without inspecting code. Unit and system testing describe testing levels, not structural-versus-functional technique classes; basis-path testing is often applied to units, but its defining category is white-box.
