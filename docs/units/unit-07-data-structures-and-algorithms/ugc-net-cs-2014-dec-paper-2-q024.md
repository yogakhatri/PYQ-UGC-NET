# Question 24

*UGC NET CS · 2014 Dec Paper 2 · Data Structures · Row-Major Array Address Calculation*

Consider an array A[20,10] stored in row-major order, with 4 addressable words per array element and base address 100. What is the address of A[11,5]?

- **A.** 560
- **B.** 565
- **C.** 570
- **D.** 575

> [!TIP]
> **Correct answer: A. 560**

## Solution

For row-major A[20,10], the zero-based linear index of A[11,5] is 11·10+5=115. Each element occupies 4 addressable words, so the displacement is 115·4=460. Adding base address 100 gives 560. The answer choices therefore imply the usual zero-based indexing assumption.

## Key Points

- Row-major address = base + ((row·column_count)+column)·element_size for zero-based indices.

## Why the other options are incorrect

565, 570 and 575 add incorrect displacements after the row-major calculation. A one-based interpretation would produce a value absent from the options, confirming the indexing convention intended by the item.
