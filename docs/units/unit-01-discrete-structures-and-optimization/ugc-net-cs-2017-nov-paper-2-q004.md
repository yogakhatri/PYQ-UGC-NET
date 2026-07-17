# Question 4

*UGC NET CS · 2017 Nov Paper 2 · Counting, Mathematical Induction and Discrete Probability · Permutations and Combinations*

How many distinguishable permutations of the letters in the word BANANA are there ?

- **1.** 720
- **2.** 120
- **3.** 60
- **4.** 360

> [!TIP]
> **Correct answer: 3. 60**

## Solution

BANANA has 6 letters, but the three A's are indistinguishable and the two N's are indistinguishable; B occurs once. Divide the 6! arrangements of labeled positions by 3! for the A permutations and 2! for the N permutations: 6!/(3!2!)=720/(6×2)=60. Therefore option 3 is correct.

## Key Points

- For n objects with repetition counts n₁,n₂,…, the number of distinguishable permutations is n!/(n₁!n₂!…).

## Why the other options are incorrect

720 treats all six letters as distinct. Dividing by only one repetition factor produces values such as 120 or 360. Every repeated-letter factorial must be included in the denominator.
