# Question 89

*UGC NET CS · 2020 Nov With Answers · Relations · Reflexive, Symmetric and Antisymmetric Properties*

Consider the properties A. Reflexive, B. Antisymmetric, and C. Symmetric. Let A = {a, b, c, d, e, f, g} and R = {(a,a), (b,b), (c,d), (c,g), (d,g), (e,e), (f,f), (g,g)} be a relation on A. Which property or properties are satisfied by R?

- **1.** Only A
- **2.** Only C
- **3.** Both A and B
- **4.** B and not A

> [!TIP]
> **Correct answer: 4. B and not A**

## Solution

R is not reflexive because a reflexive relation on A must contain (x,x) for every x∈A, but (c,c) and (d,d) are missing. It is antisymmetric: whenever two different elements x and y occur as (x,y), the reverse pair (y,x) does not occur; the off-diagonal pairs are (c,d), (c,g), and (d,g). It is not symmetric because, for example, (c,d)∈R but (d,c)∉R. Thus B holds and A does not, option 4.

## Key Points

- Test relation properties by definition: all self-loops for reflexivity, reverse pairs for symmetry, and no two-way off-diagonal pair for antisymmetry.

## Why the other options are incorrect

Only A and both A-and-B incorrectly call the relation reflexive. Only C incorrectly calls it symmetric. Self-loops do not violate antisymmetry, because the condition permits x=y.
