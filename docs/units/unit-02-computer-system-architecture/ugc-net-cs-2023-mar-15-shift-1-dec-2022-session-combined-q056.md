# Question 56

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Digital Logic Circuits and Components · Karnaugh-map simplification*

option TD=457291 5. 0:87006 Simplify the following using K-Map. F(A, B,C,D) = 2(3,4,5,6,7,11, 15)

- **1.** AB+CD
- **2.** A'B+CD
- **3.** AC+BD
- **4.** A'B+B'C

> [!TIP]
> **Correct answer: 2. A'B+CD**

## Solution

Minterms 4,5,6,7 form the implicant A′B. Minterms 3,7,11,15 form CD. Their union is exactly the given set, so F=A′B+CD.

## Key Points

- A four-cell K-map group eliminates the two variables that change within it.

## Why the other options are incorrect

The other products cover minterms outside the set or fail to cover required minterms.
