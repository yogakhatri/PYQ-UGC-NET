# Question 10

*UGC NET CS · 2016 July Paper 3 · Normalization for Relational Databases · Binary Lossless-Join Decomposition Test*

Which of the following statements is TRUE ? D1 : The decomposition of the schema R(A, B, C) into R1(A, B) and R2 (A, C) is always lossless. D2 : The decomposition of the schema R(A, B, C, D, E) having AD → B, C → DE, B → AE and AE → C, into R1 (A, B, D) and R2 (A, C, D, E) is lossless.

- **1.** Both D1 and D2
- **2.** Neither D1 nor D2
- **3.** Only D1
- **4.** Only D2

> [!TIP]
> **Correct answer: 4. Only D2**

## Solution

For a binary decomposition into R₁ and R₂, losslessness requires the common attributes R₁∩R₂ to functionally determine R₁ or R₂. In D1 the intersection is {A}, but no functional dependency is given that makes A determine AB or AC, so it is not always lossless. In D2 the intersection is {A,D}; the given AD→B implies AD→ABD=R₁, so D2 is lossless. Only D2 is true.

## Key Points

- Binary lossless join test: (R₁∩R₂)→R₁ or (R₁∩R₂)→R₂ must follow from the FDs.

## Why the other options are incorrect

Options 1 and 3 incorrectly call D1 always lossless merely because the components share A. A common attribute alone is insufficient. Option 2 overlooks that AD functionally determines all of R₁ through AD→B.
