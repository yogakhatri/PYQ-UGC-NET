# Question 59

*UGC NET CS · 2015 Dec Paper 3 · Data Modeling · PRIMARY KEY, UNIQUE and CHECK Constraints*

Consider the intended table definition: CREATE TABLE test(one INTEGER, two INTEGER, PRIMARY KEY(one), UNIQUE(two), CHECK(one >= 1 AND one <= 10), CHECK(two >= 1 AND two <= 5)); Assuming the constrained values are non-NULL as intended by the question, what is the maximum number of tuples the table can contain?

- **1.** 5
- **2.** 10
- **3.** 15
- **4.** 50

> [!TIP]
> **Correct answer: 1. 5**

## Solution

Under the question's intended constraints, column one may take the ten values 1 through 10 and is a primary key; column two may take only the five values 1 through 5 and is UNIQUE. Because each non-NULL value of two can appear only once, column two is the tighter limit, so at most five tuples can be stored. Option 1 is the intended answer.

## Key Points

- With two non-NULL unique finite domains, maximum rows = the smaller domain size: min(10,5)=5.

## Why the other options are incorrect

Ten counts the possible primary-key values but ignores the tighter UNIQUE column, while 15 and 50 do not follow from either domain. Two SQL caveats are important: the source prints incomplete CHECK expressions such as 'one >= 1 AND <= 10', which are invalid unless the column name is repeated; and a standard UNIQUE column permits NULLs while CHECK accepts UNKNOWN, so without NOT NULL on two the literal repaired schema could hold up to ten rows by using NULL. The stated five-row answer requires the exam's intended non-NULL finite-domain assumption.
