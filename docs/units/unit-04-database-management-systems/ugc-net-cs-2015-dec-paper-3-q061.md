# Question 61

*UGC NET CS · 2015 Dec Paper 3 · SQL · OR Predicates and Set Cardinality*

Query A selects people with Age>21 and returns 10 rows. Query B selects people with Height>180 and returns 7 rows. Query C uses WHERE (Age>21) OR (Height>180). Which option is a possible number of rows returned by Query C?

- **1.** 3
- **2.** 7
- **3.** 10
- **4.** 21

> [!TIP]
> **Correct answer: 3. 10**

## Solution

Let A be the 10 rows satisfying Age>21 and B the 7 rows satisfying Height>180. Query C returns the union A∪B, so |A∪B|=|A|+|B|−|A∩B|=17−|A∩B|. The overlap can contain from 0 through 7 rows, which makes the union size range from 17 down to 10. Therefore 10 is possible—for example, when all 7 rows of B are already among the 10 rows of A.

## Key Points

- For two result sets, max(|A|,|B|) ≤ |A∪B| ≤ |A|+|B|.

## Why the other options are incorrect

A union cannot have fewer rows than its larger input, so 3 and 7 are impossible when A already contains 10 rows. It cannot exceed 10+7=17, so 21 is impossible. Only option 3 lies in the valid interval [10,17].
