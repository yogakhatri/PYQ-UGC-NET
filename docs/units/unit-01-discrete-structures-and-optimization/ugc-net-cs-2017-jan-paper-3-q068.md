# Question 68

*UGC NET CS · 2017 Jan Paper 3 · Optimization · Loops in Transportation Tables*

With respect to a loop in the transportation table, which one of the following is not correct ?

- **1.** Every loop has an odd no. of cells and atleast 5.
- **2.** Closed loops may or may not be square in shape.
- **3.** All the cells in the loop that have a plus or minus sign, except the starting cell, must be occupied cells.
- **4.** Every loop has an even no. of cells and atleast four.

> [!TIP]
> **Correct answer: 1. Every loop has an odd no. of cells and atleast 5.**

## Solution

A transportation-table loop alternates horizontal and vertical moves and must return to its starting cell. Such an alternating orthogonal cycle has an even number of corner cells, with the smallest loop containing four. It need not be geometrically square, and every signed corner except the entering starting cell must be an occupied basic cell. Therefore the claim that every loop has an odd number of cells and at least five is not correct, making option 1 the answer.

## Key Points

- Transportation loop: closed, horizontal/vertical alternation, even number of corners ≥4, with nonstarting corners basic/occupied.

## Why the other options are incorrect

Options 2–4 state the standard loop properties. 'Closed' describes returning to the start, not having a square outline; irregular rectilinear loops are allowed.
