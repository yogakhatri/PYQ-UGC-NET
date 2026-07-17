# Question 68

*UGC NET CS · 2019 Dec Paper 1 And 2 · 2-D Geometrical Transforms and Viewing · Line and Polygon Clipping*

Which of the following algorithms is not used for line clipping?

- **1.** Cohen-Sutherland algorithm
- **2.** Southerland-Hodgeman algorithm
- **3.** Liang-Barsky algorithm
- **4.** Nicholl-Lee-Nicholl algorithm

> [!TIP]
> **Correct answer: 2. Southerland-Hodgeman algorithm**

## Solution

Cohen–Sutherland, Liang–Barsky, and Nicholl–Lee–Nicholl are line-clipping algorithms for rectangular windows. Sutherland–Hodgman instead clips a polygon by successively processing its vertices and edges against each clipping boundary. It is therefore the algorithm not used for line clipping, option 2.

## Key Points

- Sutherland–Hodgman is for polygon clipping; Cohen–Sutherland is for line clipping.

## Why the other options are incorrect

Options 1, 3, and 4 are established line-clipping methods: region-code subdivision, parametric inequalities, and region-based case reduction respectively. The similar Sutherland name in option 2 should not be confused with Cohen–Sutherland.
