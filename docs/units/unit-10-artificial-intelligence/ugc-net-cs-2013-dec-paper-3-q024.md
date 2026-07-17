# Question 24

*UGC NET CS · 2013 Dec Paper 3 · Knowledge Representation and Reasoning · Unification and Substitution*

The objective of ________ procedure is to di scover at least one ________ that causes two literals to match.

- **A.** unification, validation
- **B.** unification, substitution
- **C.** substitution, unification
- **D.** minimax, maximum

> [!TIP]
> **Correct answer: B. unification, substitution**

## Solution

Unification attempts to find a substitution for variables that makes two literals or terms identical. If one exists, a most general unifier is preferred because it imposes no unnecessary bindings.

## Key Points

- Unification procedure → substitution (ideally an MGU) that makes terms match.

## Why the other options are incorrect

Validation is not the object returned by unification. Option C reverses the procedure and its result. Minimax is an adversarial-search method unrelated to matching logical literals.
