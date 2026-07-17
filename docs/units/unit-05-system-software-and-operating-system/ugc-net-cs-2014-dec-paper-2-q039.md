# Question 39

*UGC NET CS · 2014 Dec Paper 2 · Memory Management · Optimal Page Size*

For a paging scheme, let average process size be x bytes, page size be y bytes and each page-table entry require z bytes. The optimum page size minimizing page-table overhead plus internal fragmentation is

- **A.** x/2
- **B.** xz/2
- **C.** √(2xz)
- **D.** √(xz)/2

> [!TIP]
> **Correct answer: C. √(2xz)**

## Solution

A process of size x uses about x/y page-table entries, costing xz/y bytes. Average internal fragmentation is approximately y/2. Total overhead is H(y)=xz/y+y/2. Differentiate: H′(y)=−xz/y²+1/2. Setting this to zero gives y²=2xz, so the minimizing page size is y=√(2xz). The second derivative 2xz/y³ is positive, confirming a minimum.

## Key Points

- Optimize page size by minimizing page-table overhead xz/y plus expected fragmentation y/2.

## Why the other options are incorrect

x/2 and xz/2 do not balance the inverse page-table term against linear fragmentation. √(xz)/2 has the wrong constant factor; solving the derivative gives √2 times √(xz), not half of it.
