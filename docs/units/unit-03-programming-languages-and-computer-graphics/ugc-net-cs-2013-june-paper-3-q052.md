# Question 52

*UGC NET CS · 2013 June Paper 3 · Programming in C · Dynamic Memory Allocation Functions*

Match the following : a. calloc( ) i. Frees previously allocated space b. free( ) ii. Modifies previously allocated space c. malloc( ) iii. Allocates space for array d. realloc( ) iv. Allocates requested size of space Codes : a b c d

- **A.** iii i iv ii
- **B.** iii ii i iv
- **C.** iii iv i ii
- **D.** iv ii iii i

> [!TIP]
> **Correct answer: A. iii i iv ii**

## Solution

calloc allocates storage for an array of elements and initializes its bytes to zero, so a→iii. free releases previously allocated storage, b→i. malloc allocates a requested number of bytes, c→iv. realloc changes the size of a previously allocated block and may move it, d→ii. The sequence is iii, i, iv, ii.

## Key Points

- calloc=array allocation plus zeroing; malloc=raw allocation; realloc=resize; free=release.

## Why the other options are incorrect

B assigns 'modifies allocated space' to free and 'frees' to malloc. C swaps the roles of free, malloc and realloc. D describes calloc as a plain requested-size allocation and free as a resizing operation. Only A preserves all four standard library roles.
