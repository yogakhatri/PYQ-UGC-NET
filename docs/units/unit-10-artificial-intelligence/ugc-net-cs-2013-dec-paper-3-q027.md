# Question 27

*UGC NET CS · 2013 Dec Paper 3 · Adversarial Search · Alpha and Beta Cutoffs*

In alpha-beta pruning, _________ is used to cut off the search at maximizing level only and _________ is used to cut off the search at minimizing level only.

- **A.** alpha, beta
- **B.** beta, alpha
- **C.** alpha, alpha
- **D.** beta, beta

> [!TIP]
> **Correct answer: B. beta, alpha**

## Solution

At a maximizing node, a beta cutoff occurs once the node's value is at least the best upper bound beta already available to an ancestor MIN node. At a minimizing node, an alpha cutoff occurs once the value is at most alpha. Therefore the pair is beta, alpha.

## Key Points

- MAX level: beta cutoff.
- MIN level: alpha cutoff.

## Why the other options are incorrect

A reverses the levels; C and D use one bound for both node types. Alpha records MAX's best lower bound, while beta records MIN's best upper bound.
