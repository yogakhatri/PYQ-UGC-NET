# Question 4

*UGC NET CS · 2017 Jan Paper 2 · Counting, Mathematical Induction and Discrete Probability · Counting Multiples in Open Intervals*

How many multiples of 6 are there between the following pairs of numbers ? 0 and 100 and –6 and 34

- **1.** 16 and 6
- **2.** 17 and 6
- **3.** 17 and 7
- **4.** 16 and 7

> [!TIP]
> **Correct answer: 1. 16 and 6**

## Solution

Interpret 'between' as excluding both endpoints. Between 0 and 100, the multiples are 6,12,…,96, so their count is floor(99/6)=16. Between −6 and 34, they are 0,6,12,18,24,30, giving 6 values. Therefore the pair is 16 and 6, option 1.

## Key Points

- Before counting integer multiples, translate 'between' into explicit inequalities and decide whether endpoints are included.

## Why the other options are incorrect

Counts of 17 arise only when an endpoint that is itself a multiple of 6 is included: including 0 in the first interval gives 17, and including −6 in the second gives 7. That is not the strict-between convention used by the question.

## Additional Information

The English word 'between' can be used inclusively in informal speech. If both endpoints were included, the answer would be 17 and 7 (option 3); the exam's intended mathematical reading is the open interval in option 1.
