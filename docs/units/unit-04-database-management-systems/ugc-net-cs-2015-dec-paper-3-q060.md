# Question 60

*UGC NET CS · 2015 Dec Paper 3 · Relational Algebra and SQL · Inner and Full Outer Joins*

Suppose Oracle relation R(A,B) has tuples {(1,2),(1,3),(3,4)} and S(B,C) has tuples {(2,5),(4,6),(7,8)}. SQ1 performs R FULL JOIN S ON R.B=S.B, while SQ2 performs R INNER JOIN S ON R.B=S.B. How many tuples do SQ1 and SQ2 return, respectively?

- **1.** 2 and 6 respectively
- **2.** 6 and 2 respectively
- **3.** 2 and 4 respectively
- **4.** 4 and 2 respectively

> [!TIP]
> **Correct answer: 4. 4 and 2 respectively**

## Solution

Joining on B gives two matches: R's B=2 tuple joins S's B=2 tuple, and R's B=4 tuple joins S's B=4 tuple. Therefore the inner join returns 2 rows. The full outer join also preserves R's unmatched B=3 row and S's unmatched B=7 row, padding the missing side with NULLs, so it returns 2+1+1=4 rows. The pair is therefore 4 and 2, option 4.

## Key Points

- Full outer join = all matches + unmatched rows from the left + unmatched rows from the right.

## Why the other options are incorrect

Options 1 and 3 reverse or undercount the full-join result. Option 2's six rows would arise from adding both relation sizes without accounting for matched pairs being combined, but each of the two matches contributes one joined row, not two separate rows.
