# Question 147

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Turing Machines · Recursive and Recursively Enumerable Languages*

A Turing Machine for the language L={a"b*| n21, m≥1) is designed. The resultant model is M= (190. 91-92:93:94.95•96-97:9f). fa.b,c.d), fa,b.c.d.,,X2.Y,. Yzi.8, 90, B, (96)) and part of t is given in the transition table. You need to write the following questions based on design of Turing Machine for the given language. Note that, while designing the Turing Machine Xy and X2 are used to work with 'a's and 'c's and Y and Yo are used to handle 'b's and 'd's of the given string. d a X2 X1 M2 91 (91.b. R) (gi.a. R) (91-42. R) 92 (a2,a, L) (42.b. L) (qz.X1, R) (qz.Xz. L) M3 93 (96-42. R) (41,b, R) 94 (94. Y2, R) (gs. Y1,L) 95 (9s,b, L) (qs.Yz. L) (qs.Xz, L) M+ 96 (90:42, R) (97. Y2, R) 97 (97.Y2, R) (g.B. R) What is the Move in the cell with number 'M2' of the resultant Table?

- **1.** (91.X1.R)
- **2.** (91,a,R)
- **3.** (92.41. R)
- **4.** Error Entry

> [!TIP]
> **Correct answer: 4. Error Entry**

## Solution

M2 is the q0 transition on X1. To search past already marked a symbols, the logical move is (q0,X1,R). None of options 1–3 gives that transition, so the table entry represented by the supplied alternatives is an error entry/no matching listed move.

## Key Points

- When scanning for the next unmarked symbol, remain in the scan state while passing its markers.

## Why the other options are incorrect

The listed q1/q2 moves switch to a later matching phase instead of retaining q0 while skipping a processed marker.
