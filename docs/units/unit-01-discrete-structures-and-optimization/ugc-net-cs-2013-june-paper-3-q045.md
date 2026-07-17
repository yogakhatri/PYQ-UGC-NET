# Question 45

*UGC NET CS · 2013 June Paper 3 · Boolean Algebra · Product-of-Sums Minimization*

The simplified function in product of sums of Boolean function F(W, X, Y, Z) = Σ(0, 1, 2, 5, 8, 9, 10) is

- **A.** (W' + X') (Y' + Z') (X' + Z)
- **B.** (W' + X') (Y' + Z') (X' + Z')
- **C.** (W' + X') (Y' + Z) (X' + Z)
- **D.** (W' + X') (Y + Z') (X' + Z)

> [!TIP]
> **Correct answer: A. (W' + X') (Y' + Z') (X' + Z)**

## Solution

For product-of-sums minimization, group the zero cells of the four-variable Karnaugh map. The zeros are minterms 3,4,6,7,11,12,13,14,15. A group with W=X=1 gives (W′+X′); a group with Y=Z=1 gives (Y′+Z′); and a group with X=1,Z=0 gives (X′+Z). Multiplying these maxterms yields (W′+X′)(Y′+Z′)(X′+Z), option A.

## Key Points

- For POS, group K-map zeros; a variable fixed at 1 appears complemented in the maxterm, while one fixed at 0 appears uncomplemented.

## Why the other options are incorrect

B complements Z in the X=1,Z=0 group, which would make required minterms fail. C uses (Y′+Z), corresponding to Y=1,Z=0 rather than the actual Y=Z=1 zero group. D similarly uses (Y+Z′), describing the wrong zero pattern.
