# Question 52

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Sets and Relations · Representation and Properties of Relations*

A relation R' is defined on ordered pairs of integers as: (x.y) R (u.v) if x<u and yov. Then R is

- **1.** Neither a partial order nor an equivalence relation
- **2.** A partial order but not a total order
- **3.** A total order
- **4.** An equivalence relation

> [!TIP]
> **Correct answer: 1. Neither a partial order nor an equivalence relation**

## Solution

The relation uses strict inequalities in both coordinates: (x,y) R (u,v) when x<u and y<v. It is irreflexive because x<x is never true. A partial order, under the standard definition, must be reflexive; an equivalence relation must also be reflexive (as well as symmetric and transitive). Hence this strict relation is neither a partial order nor an equivalence relation.

## Key Points

- Before testing the harder properties of a relation, test reflexivity.
- A strict ‘less-than’ relation is irreflexive.

## Why the other options are incorrect

Options 2 and 3 call it an order even though reflexivity fails. Option 4 fails because the relation is neither reflexive nor symmetric: if x<u, the reverse inequality u<x cannot hold simultaneously.
