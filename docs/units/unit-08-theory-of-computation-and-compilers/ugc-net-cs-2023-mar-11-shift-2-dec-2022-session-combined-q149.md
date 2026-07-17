# Question 149

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Turing Machines · Recursive and Recursively Enumerable Languages*

A Turing Machine for the language L=(a"bc*| n21. m≥1) is designed. The resultant model is M= (190.91.92.93.94.95.96.97.9F), (ab,c.d), (a,b,c.d,],X2, Yi, Y2),8, 90, B, (9)) and part of 'ổ is given in the transition table. You need to write the following questions based on design of Turing Machine for the given language. Note that, while designing the Turing Machine Xy and X2 are used to work with 'a's and 'c's and Y and Yo are used to handle 'b's and 'd's of the given string. (91,X1. R) 90 91 MI (91,b, R) (91.a, R) (91-2, R) 92 (92.b. L) (42,a. L) (92.X1, R) (92-X2. L) M3 93 K90.X,, R) (94. Yi. R) MS 94 (94,b, R) (94. 2, R) (95. Y2.1) (95.b. L) 95 KasX, L) MA (9s.Y, L) 96 Kg6:X2, R) (97Y2, R) 47 (grY,, R) (9r.B, R) What is the Move in the cell with number M4' of the resultant Table?

- **1.** (95. Y1.L)
- **2.** (93.Y1,R)
- **3.** (94. Y 1. L)
- **4.** (93. Y 1. L)

> [!TIP]
> **Correct answer: 4. (93. Y 1. L)**

## Solution

After q4 marks a d as Y2, q5 moves left across processed symbols until it reaches the Y1 that marks the paired b. It must then enter q3 and continue left so q3 can locate the next unmarked b. Thus M4=(q3,Y1,L).

## Key Points

- The transition at the left marker changes from the return state to the next-symbol search state.

## Why the other options are incorrect

Remaining in q5 or q4 does not restart the b-search; moving right returns toward the already processed d side.
