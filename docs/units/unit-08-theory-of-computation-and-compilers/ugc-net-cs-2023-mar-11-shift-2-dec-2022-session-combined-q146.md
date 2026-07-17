# Question 146

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Turing Machines · Recursive and Recursively Enumerable Languages*

A Turing Machine for the language L=(a'bc | n21. m≥l) is designed. The resultant model is M= (190.91•92-93.94.95.96.97.9f), (a,b,c.d), {a,b,c,d,Xy,X2, Y1, Y21.0, 90, B, (9f)) and part of 'ổ is given in the transition table. You need to write the following questions based on design of Turing Machine for the given language. Note that, while designing the Turing Machine Xy and X2 are used to work with 'a's and'e's and Y1 and Yo are used to handle 'b's and 'd's of the given string. d x= YI 90 M2 91 (g).a, R) (g1,b, R) 91.X2, R) MI 92 (42,a. L) (92.b. L) (g2X2, IL) (92-X1, R) M3 (96X2, R) 93 94. Y, R 94 MS (94.b, R) (g5, Y 2. L) (94. 2, R) 95 (gs.X,, L) M4 (45.b.L) (93. Y2. L) 96 (97.Y2, R) K96X,, R) 97 (9=. Y≥, R) (9.B, R) What is the Move in the cell with number 'MI' of the resultant Table?

- **1.** (92.42,R)
- **2.** (92.X2,L)
- **3.** (q3.X2.L)
- **4.** Error Entry

> [!TIP]
> **Correct answer: 2. (92.X2,L)**

## Solution

State q1 scans right after marking an a as X1. On the first unmatched c it must mark that c as X2 and move left into q2 so the head can return toward the corresponding X1. Therefore M1=(q2,X2,L).

## Key Points

- The machine pairs each a with a c by marking c as X2, then returning left.

## Why the other options are incorrect

Moving right fails to return for the next phase; entering q3 is premature; the transition is required and is not an error.
