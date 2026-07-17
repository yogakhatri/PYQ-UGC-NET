# Question 63

*UGC NET CS · 2015 Dec Paper 3 · Data Modeling · Natural join and projection*

For the displayed relations R(A,B), S(B,C), and T(A,C), all joins are natural joins and π denotes projection. Which displayed table equals π_{A,B}(R ⋈ T) ⋈ π_{B,C}(S ⋈ T)?

- **1.** Table (a)
- **2.** Table (b)
- **3.** Table (c)
- **4.** Table (d)

> [!TIP]
> **Correct answer: 1. Table (a)**

## Solution

R and T naturally join on A. Every A in R has exactly one matching row in T, so π_{A,B}(R⋈T) is {(1,2),(3,2),(5,6),(7,8),(9,8)}. S and T naturally join on C; every C in S also has one matching T row, so π_{B,C}(S⋈T) is {(6,2),(2,4),(8,1),(8,3),(2,5)}. Joining these projections on B produces four rows for B=2, one for B=6, and four for B=8: (1,2,4),(1,2,5),(3,2,4),(3,2,5),(5,6,2),(7,8,1),(7,8,3),(9,8,1),(9,8,3). This is table (a), option 1.

## Key Points

- Natural joins pair every row sharing equal common attributes; duplicate match groups create Cartesian products within each key.

## Why the other options are incorrect

Tables (b), (c), and (d) omit valid combinations created when a B value appears multiple times on both sides. A natural join uses every matching pair: for B=2 there are 2×2=4 rows, and for B=8 there are likewise 2×2=4 rows.

## Question Figure

![Question figure](../../assets/questions/ugc-net-2015-dec-paper-3-q63.png)
