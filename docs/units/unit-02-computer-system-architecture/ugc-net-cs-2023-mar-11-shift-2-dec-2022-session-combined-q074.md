# Question 74

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Multiprocessors · Interprocessor Communication and Synchronization*

OBID:187024 For a function of two variables, boundary value analysis yields.

- **1.** 4n+3 test cases
- **2.** 4n+1 test cases
- **3.** n+4 test cases
- **4.** 2n+4 test cases

> [!TIP]
> **Correct answer: 2. 4n+1 test cases**

## Solution

Normal boundary-value analysis for n independent input variables uses one nominal test plus four boundary tests per variable: minimum, just above minimum, just below maximum, and maximum. Holding all other variables nominal while varying one at a time gives 4n+1 test cases. For two variables this would be 9 tests.

## Key Points

- Normal BVA uses 4n+1 cases; robust BVA additionally tests just outside each boundary and uses 6n+1.

## Why the other options are incorrect

The counts 4n+3, n+4, and 2n+4 do not follow from the four boundary values required for each variable plus the single all-nominal case.
