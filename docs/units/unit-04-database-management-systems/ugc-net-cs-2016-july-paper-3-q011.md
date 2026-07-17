# Question 11

*UGC NET CS · 2016 July Paper 3 · SQL · Join, GROUP BY and HAVING Evaluation*

Consider the following ORACLE relations : R (A, B, C) = {<1, 2, 3>, <1, 2, 0>, <1, 3, 1>, <6, 2, 3>, <1, 4, 2>, <3, 1, 4> } S (B, C, D) = {<2, 3, 7>, <1, 4, 5>, <1, 2, 3>, <2, 3, 4>, <3, 1, 4>}. Consider the following two SQL queries SQ1 and SQ2 : SQ1 : SELECT R⋅B, AVG (S⋅B) FROM R, S WHERE R⋅A = S⋅C AND S⋅D < 7 GROUP BY R⋅B; SQ2 : SELECT DISTINCT S⋅B, MIN (S⋅C) FROM S GROUP BY S⋅B HAVING COUNT (DISTINCT S⋅D) > 1; If M is the number of tuples returned by SQ1 and N is the number of tuples returned by SQ2 then

- **1.** M = 4, N = 2
- **2.** M = 5, N = 3
- **3.** M = 2, N = 2
- **4.** M = 3, N = 3

> [!TIP]
> **Correct answer: 1. M = 4, N = 2**

## Solution

For SQ1, `S.D<7` leaves S rows whose C values are 4,2,3,1. Joining on R.A=S.C produces groups for R.B=1,2,3,4: the A=1 rows yield B=2,3,4 through the S row with C=1, and the A=3 row yields B=1 through the S row with C=3. Hence M=4. For SQ2, S.B=1 has two distinct D values {5,3}, S.B=2 has {7,4}, and S.B=3 has only {4}; only the first two groups pass HAVING, so N=2. Therefore option 1 is correct.

## Key Points

- Evaluate SQL in order: FROM/JOIN → WHERE → GROUP BY → aggregates/HAVING → SELECT; count final groups, not intermediate rows.

## Why the other options are incorrect

M counts output groups, not raw join tuples, and N counts groups surviving `COUNT(DISTINCT S.D)>1`. Values 5 or 3 result from counting intermediate rows or all B groups rather than the final grouped outputs. A circulated key selecting option 3 conflicts with direct SQL evaluation.

## Additional Information

The final SQ1 rows are keyed by R.B={1,2,3,4}; the final SQ2 rows are keyed by S.B={1,2}. This explicit result-key check makes M=4,N=2 independently reproducible.
