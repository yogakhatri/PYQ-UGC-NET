# Question 69

*UGC NET CS · 2014 Dec Paper 3 · Optimization · Assignment-Problem Minimum Cost*

Assign men P,Q,R,S,T to jobs I–V, one job each, to minimize total hours. Cost rows (I,II,III,IV,V) are P=(2,9,2,7,1), Q=(6,8,7,6,1), R=(4,6,5,3,1), S=(4,2,7,3,1), T=(5,3,9,5,1). What is the minimum total time?

- **A.** 5
- **B.** 11
- **C.** 13
- **D.** 15

> [!TIP]
> **Correct answer: C. 13**

## Solution

An optimal assignment is P→III (2), Q→V (1), R→I (4), S→IV (3), and T→II (3), totaling 2+1+4+3+3=13 hours. A matching lower-bound certificate is given by row potentials (−4,1,−1,−1,0) and column potentials (5,3,6,4,0): every row-plus-column potential is at most its table cost, their total is 13, and every chosen assignment attains equality. Therefore no assignment can cost below 13, and the displayed one is optimal.

## Key Points

- An assignment solution needs one distinct column per row; prove optimality with the Hungarian method or equivalent row/column potentials.

## Why the other options are incorrect

5 is impossible despite every entry in column V being 1 because only one man may take that job. 11 is below the certified lower bound. 15 is feasible for some assignments but not minimal. Option C is both attainable and proven optimal.
