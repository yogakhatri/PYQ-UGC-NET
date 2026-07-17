# Question 32

*UGC NET CS · 2013 June Paper 3 · Programming in C · Multidimensional Arrays and Row-Major Storage*

Arrays in C language can have _________ with reference to memory representation.

- **A.** n-subscripts
- **B.** two-subscripts
- **C.** only one subscript
- **D.** three subscripts only

> [!TIP]
> **Correct answer: A. n-subscripts**

## Solution

C supports multidimensional arrays, conceptually as arrays whose elements are themselves arrays. An array may therefore be declared with one, two, three or more subscripts, subject to implementation limits. Its elements occupy contiguous storage, and C lays multidimensional arrays out in row-major order, so the rightmost subscript changes fastest.

## Key Points

- A C array can have n dimensions; multidimensional arrays are contiguous arrays of arrays in row-major order.

## Why the other options are incorrect

Two and three subscripts are valid examples but are not exclusive limits. 'Only one subscript' ignores C declarations such as int a[3][4] and higher-dimensional arrays.
