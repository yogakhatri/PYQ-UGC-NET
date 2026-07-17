# Question 71

*UGC NET CS · 2019 Dec Paper 1 And 2 · Relational Algebra · Natural Join Cardinality*

Relations R1(x,y) and R2(y,z) contain 50 and 30 tuples respectively. What is the maximum possible number of tuples in the natural join R1 ⋈ R2?

- **1.** 30
- **2.** 20
- **3.** 50
- **4.** 1500

> [!TIP]
> **Correct answer: 4. 1500**

## Solution

A natural join pairs tuples whose common attribute y is equal. The maximum occurs when every tuple of R1 has the same y value as every tuple of R2. Then each of the 50 R1 tuples joins with all 30 R2 tuples, producing 50×30=1500 tuples. Option 4 is therefore correct.

## Key Points

- Without key constraints, the worst-case equality join can be as large as the Cartesian product.

## Why the other options are incorrect

Bounds such as min(50,30)=30 apply only when key or uniqueness constraints restrict matching. No such constraint is given here. Twenty and fifty likewise underestimate the many-to-many matching possible when y is repeated in both relations.
