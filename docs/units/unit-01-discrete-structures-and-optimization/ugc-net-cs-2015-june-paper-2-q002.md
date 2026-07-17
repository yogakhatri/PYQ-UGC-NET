# Question 2

*UGC NET CS · 2015 June Paper 2 · Counting, Mathematical Induction and Discrete Probability · Divisibility Events on Ordered Dice*

Two fair dice, one black and one red, are tossed. What is the probability that the number on the black die divides the number on the red die?

- **1.** 22/36
- **2.** 12/36
- **3.** 14/36
- **4.** 6/36

> [!TIP]
> **Correct answer: 3. 14/36**

## Solution

The dice are distinguishable, so there are 36 ordered pairs (black,red). Count red values divisible by each black value: black 1 gives 6; 2 gives 3 (2,4,6); 3 gives 2 (3,6); and 4, 5, 6 each give 1. The favorable count is 6+3+2+1+1+1=14, so the probability is 14/36.

## Key Points

- With distinguishable dice, count ordered pairs; for divisor b, favorable red faces are its multiples not exceeding 6.

## Why the other options are incorrect

6/36 counts only equal faces. 12/36 and 22/36 come from incomplete or double-counted divisibility pairs. Listing multiples separately for each possible black die avoids both errors.
