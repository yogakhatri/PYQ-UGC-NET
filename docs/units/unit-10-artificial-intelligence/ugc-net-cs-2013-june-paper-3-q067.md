# Question 67

*UGC NET CS · 2013 June Paper 3 · Logic Programming · Negation as Failure in Prolog*

Which one of the following is a correct implementation of the meta- predicate “not” in PROLOG (Here G represents a goal) ?

- **A.** not(G):– !, call(G), fail. not(G).
- **B.** not(G):– call(G), !, fail. not(G).
- **C.** not(G):– call(G), fail, !. not(G).
- **D.** not(G):– call(G), fail. not(G):– !.

> [!TIP]
> **Correct answer: B. not(G):– call(G), !, fail. not(G).**

## Solution

Negation as failure should fail when G succeeds and succeed when G cannot be proved. In option B, call(G) is tried first. If it succeeds, the cut commits to that clause and fail makes not(G) fail. If call(G) fails, execution never reaches the cut, so Prolog tries the second fact not(G), which succeeds. This implements the required operational behavior.

## Key Points

- Prolog negation pattern: call the goal, cut on success, force failure; otherwise fall through and succeed.

## Why the other options are incorrect

A cuts before trying G, so failure of G cannot fall through to the success clause. C places the cut after fail, where it can never be reached. D lets the second clause succeed even after the first clause proves G and then fails, so it makes not(G) succeed incorrectly.
