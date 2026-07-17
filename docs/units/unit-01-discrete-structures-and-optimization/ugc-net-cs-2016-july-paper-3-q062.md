# Question 62

*UGC NET CS · 2016 July Paper 3 · Optimization · Revised Simplex Method*

Consider the following statements : (a) Revised simplex method requires lesser computations than the simplex method. (b) Revised simplex method automatically generates the inverse of the current basis matrix. (c) Less number of entries are needed in each table of revised simplex method than usual simplex method. Which of these statements are correct ?

- **1.** (a) and (b) only
- **2.** (a) and (c) only
- **3.** (b) and (c) only
- **4.** (a), (b) and (c)

> [!TIP]
> **Correct answer: 4. (a), (b) and (c)**

## Solution

The ordinary tableau method updates and stores the whole simplex tableau after every pivot. The revised simplex method keeps the current basis information—traditionally the basis inverse B⁻¹—and computes only the reduced-cost row, entering column, and right-hand-side information needed for the next pivot. Consequently it uses fewer stored entries and, for realistic large problems, fewer computations. In the textbook inverse-updating form it also produces the inverse for the new current basis from the old one. Therefore statements (a), (b), and (c) are all correct, giving option 4.

## Key Points

- Revised simplex performs the same pivots as simplex but stores and computes only the basis-related pieces actually needed.

## Why the other options are incorrect

Options 1, 2, and 3 each omit one valid advantage or feature. Statement (b) should be read in the classical revised-simplex sense: the algorithm updates the representation of the current basis inverse rather than recomputing a full tableau from scratch.

## Additional Information

Modern implementations often maintain an LU factorization of B instead of forming B⁻¹ explicitly; this is numerically preferable but does not change the exam's textbook answer.

## References

- [MIT — Applied Mathematical Programming, Appendix B: Linear Programming in Matrix Form](https://web.mit.edu/15.053/www/AMP-Appendix-B.pdf)
