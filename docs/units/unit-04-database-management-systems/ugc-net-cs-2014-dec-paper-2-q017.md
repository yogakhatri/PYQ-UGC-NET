# Question 17

*UGC NET CS · 2014 Dec Paper 2 · Relational Algebra and SQL · Self-Joins and Join Types*

Which of the following is true ? I. Implementation of self-join is possible in SQL with table alias. II. Outer-join operation is basic operation in relational algebra. III. Natural join and outer join operations are equivalent.

- **A.** I and II are correct.
- **B.** II and III are correct.
- **C.** Only III is correct.
- **D.** Only I is correct.

> [!TIP]
> **Correct answer: D. Only I is correct.**

## Solution

Statement I is true: assigning two aliases to the same table lets SQL treat it as two relation instances and perform a self-join. Statement II is false because classical relational algebra's primitive operations are selection, projection, union, difference, Cartesian product and rename; outer joins are derived/extended operations. Statement III is false because an outer join retains unmatched tuples with null padding, whereas a natural join does not. Only I is correct.

## Key Points

- Aliases enable self-join; outer join is extended algebra and preserves unmatched rows unlike natural join.

## Why the other options are incorrect

A incorrectly accepts II. B accepts both false statements II and III. C rejects the true self-join statement and accepts the false equivalence claim.
