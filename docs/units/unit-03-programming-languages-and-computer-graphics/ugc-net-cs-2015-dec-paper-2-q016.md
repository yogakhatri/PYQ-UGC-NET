# Question 16

*UGC NET CS · 2015 Dec Paper 2 · Programming in C · Multidimensional Arrays and Row-Major Addressing*

A three-dimensional array in C is declared as int A[x][y][z]. How is the address of A[p][q][r] computed if w is the word length of an integer?

- **1.** &A[0][0][0] + w(yzq + zp + r)
- **2.** &A[0][0][0] + w(yzp + zq + r)
- **3.** &A[0][0][0] + w(xyp + zq + r)
- **4.** &A[0][0][0] + w(xyq + zp + r)

> [!TIP]
> **Correct answer: 2. &A[0][0][0] + w(yzp + zq + r)**

## Solution

C stores multidimensional arrays in row-major order, so the rightmost index changes fastest. One complete p-slice contains y·z integers, giving offset p·y·z. Within that slice, q complete rows contribute q·z, and r selects the element within the row. The element offset is pyz+qz+r, so the byte address is &A[0][0][0] + w(pyz+qz+r), which is option 2.

## Key Points

- Row-major offset for A[p][q][r] in A[x][y][z] is p(yz)+qz+r.

## Why the other options are incorrect

Option 1 interchanges p and q. Options 3 and 4 incorrectly use x, the number of top-level slices, as a stride inside the array. Address calculation uses the sizes of dimensions to the right of each index.
