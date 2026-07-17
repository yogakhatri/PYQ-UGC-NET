# Question 60

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Programming in C · Multidimensional arrays and pointer notation*

9B10:89010 Given int arr[3][4]12] = (12,4), 7, 8), 3,4)(5, 6))(7,6)(34){5,3), 2,31 (8.9) 7,2) 3,4 (5, 1)»; Which one of the following can be used to refer to element 1 in the above 3-d array?

- **1.** arr[3][4][2]
- **2.** *(*(*(arr+2)+3)+ 1)
- **3.** *(arr+2) +*(arr +3) +*(arr+1)
- **4.** arr[2][3][2]

> [!TIP]
> **Correct answer: 2. *(*(*(arr+2)+3)+ 1)**

## Solution

The final initializer value 1 occupies arr[2][3][1] using zero-based indices. Pointer form *(*(*(arr+2)+3)+1) dereferences exactly that element.

## Key Points

- a[i][j][k] equals *(*(*(a+i)+j)+k).

## Why the other options are incorrect

Options 1 and 4 use out-of-range indices 3/4/2 for dimensions [3][4][2]; option 3 adds pointer expressions instead of indexing one scalar.
