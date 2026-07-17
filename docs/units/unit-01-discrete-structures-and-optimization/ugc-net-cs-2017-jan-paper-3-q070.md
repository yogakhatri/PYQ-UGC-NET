# Question 70

*UGC NET CS · 2017 Jan Paper 3 · Optimization · Linear-Programming Standard Form*

Consider the following LPP : Min. Z = x1 + x2 + x3 Subject to 3x1 + 4x3 ≤ 5 5x1 + x2 + 6x3 = 7 8x1 + 9x3 ≥ 2, x1, x2, x3 ≥ 0 The standard form of this LPP shall be :

- **1.** Min. Z = x1 + x2 + x3 + 0x4 + 0x5 Subject to 3x1 + 4x3 + x4 = 5; 5x1 + x2 + 6x3 = 7; 8x1 + 9x3 – x5 = 2; x1, x2, x3, x4, x5 ≥ 0
- **2.** Min. Z = x1 + x2 + x3 + 0x4 + 0x5 – 1(x6) – 1(x7) Subject to 3x1 + 4x3 + x4 = 5; 5x1 + x2 + 6x3 + x6 = 7; 8x1 + 9x3 – x5 + x7 = 2; x1 to x7 ≥ 0
- **3.** Min. Z = x1 + x2 + x3 + 0x4 + 0x5 + 0x6 Subject to 3x1 + 4x3 + x4 = 5; 5x1 + x2 + 6x3 = 7; 8x1 + 9x3 – x5 + x6 = 2; x1 to x6 ≥ 0
- **4.** Min. Z = x1 + x2 + x3 + 0x4 + 0x5 + 0x6 + 0x7 Subject to 3x1 + 4x3 + x4 = 5; 5x1 + x2 + 6x3 + x6 = 7; 8x1 + 9x3 − x5 + x7 = 2; x1 to x7 ≥ 0

> [!TIP]
> **Correct answer: 1. Min. Z = x1 + x2 + x3 + 0x4 + 0x5 Subject to 3x1 + 4x3 + x4 = 5; 5x1 + x2 + 6x3 = 7; 8x1 + 9x3 – x5 = 2; x1, x2, x3, x4, x5 ≥ 0**

## Solution

To convert inequalities to equality standard form, add a nonnegative slack variable x4 to the ≤ constraint: 3x1+4x3+x4=5. Subtract a nonnegative surplus variable x5 from the ≥ constraint: 8x1+9x3−x5=2. The middle constraint is already an equality. Give x4 and x5 zero objective coefficients and require all variables nonnegative. This is exactly option 1.

## Key Points

- ≤ gets +slack; ≥ gets −surplus; equality stays unchanged.
- Artificial variables belong to a solution-start procedure, not the basic standard-form conversion.

## Why the other options are incorrect

Options 2–4 introduce artificial variables x6 or x7. Those may be used to construct an initial basis for Big-M or two-phase simplex, but they are not required merely to express the LPP in equality standard form. Option 2 also gives artificial variables inappropriate negative unit objective coefficients.
