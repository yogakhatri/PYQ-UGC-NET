# Question 41

*UGC NET CS · 2016 July Paper 2 · Software Metrics · Prior-Processing Dependence Ratio*

In the Design Structure Quality Index (DSQI), S₁ is the total number of modules and S₃ is the number whose correct function depends on prior processing. Which expression measures the normalized proportion of modules not dependent on prior processing?

- **1.** 1 + S₃/S₁
- **2.** 1 − S₃/S₁
- **3.** 1 + S₁/S₃
- **4.** 1 − S₁/S₃

> [!TIP]
> **Correct answer: 2. 1 − S₃/S₁**

## Solution

Of the S₁ total modules, S₃ are dependent on prior processing, so S₁−S₃ are not dependent. Normalize by the total: (S₁−S₃)/S₁ = 1−S₃/S₁. Therefore option 2 is the DSQI component D₃.

## Key Points

- Complement proportion =1−(dependent part/total); here D₃=1−S₃/S₁.

## Why the other options are incorrect

Adding a ratio can exceed 1, so options 1 and 3 cannot be proportions. Option 4 reverses the ratio and can be negative when S₁>S₃. The source says 'number', but its fractional choices ask for a normalized proportion; the literal unnormalized count would be S₁−S₃.
