# Question 1

*UGC NET CS · 2015 Dec Paper 2 · Combinatorics · Combinations with Constraints*

How many committees of five people can be chosen from 20 men and 12 women such that each committee contains at least three women?

- **1.** 75240
- **2.** 52492
- **3.** 41800
- **4.** 9900

> [!TIP]
> **Correct answer: 2. 52492**

## Solution

Split the committee count by the number of women. With exactly 3 women choose C(12,3)C(20,2) = 220×190 = 41,800 committees. With exactly 4 women choose C(12,4)C(20,1) = 495×20 = 9,900. With exactly 5 women choose C(12,5)C(20,0) = 792. These cases are disjoint, so the required total is 41,800 + 9,900 + 792 = 52,492.

## Key Points

- For an ‘at least’ restriction, partition the choices into disjoint exact-count cases and add their binomial counts.

## Why the other options are incorrect

41,800 counts only the 3-woman case, and 9,900 counts only the 4-woman case. 75,240 is not the sum of the three admissible cases. ‘At least three’ means 3, 4, or 5 women, not exactly 3.
