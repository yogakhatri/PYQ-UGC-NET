# Question 16

*UGC NET CS · 2014 Dec Paper 2 · Relational Algebra · Division and Universal Queries*

Division operation is ideally suited to handle queries of the type :

- **A.** customers who have no account in any of the branches in Delhi.
- **B.** customers who have an account at all branches in Delhi.
- **C.** customers who have an account in atleast one branch in Delhi.
- **D.** customers who have only joint account in any one branch in Delhi

> [!TIP]
> **Correct answer: B. customers who have an account at all branches in Delhi.**

## Solution

Relational division answers universal 'for every' queries. If AccountAt(customer,branch) is divided by the relation containing all Delhi branches, the result contains exactly those customers paired with every required branch. Therefore it finds customers who have an account at all branches in Delhi.

## Key Points

- Division R(X,Y)÷S(Y) returns X values related to every Y value in S.

## Why the other options are incorrect

A is a universal negative and is more naturally expressed with NOT EXISTS or set difference. C asks for at least one matching branch, handled by selection/join. D adds conditions about joint accounts and one branch, not the all-values pattern division represents.
