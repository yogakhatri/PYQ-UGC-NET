# Question 34

*UGC NET CS · 2016 July Paper 3 · Advanced Algorithms · Complexities of Greedy, Dynamic and Sorting Algorithms*

Match the following : (a) Huffman codes (i) O(n2) (b) Optimal polygon triangulation (ii) θ(n3) (c) Activity selection problem (iii) O(nlgn) (d) Quicksort (iv) θ(n) Codes : (a) (b) (c) (d)

- **1.** (i) (ii) (iv) (iii)
- **2.** (i) (iv) (ii) (iii)
- **3.** (iii) (ii) (iv) (i)
- **4.** (iii) (iv) (ii) (i)

> [!TIP]
> **Correct answer: 3. (iii) (ii) (iv) (i)**

## Solution

Huffman coding uses repeated priority-queue operations and takes O(n log n), so (a)→(iii). Dynamic programming for optimal polygon triangulation considers interval splits and takes Θ(n³), so (b)→(ii). Once activities are ordered by finish time, greedy activity selection scans once in Θ(n), so (c)→(iv). Quicksort has O(n²) worst-case time, so (d)→(i). The mapping is option 3.

## Key Points

- Huffman O(n log n); polygon-triangulation DP Θ(n³); greedy activity scan Θ(n); quicksort worst case O(n²).

## Why the other options are incorrect

The other codes exchange complexities among unrelated methods. Be careful that the listed quicksort bound is its worst case and that activity selection's linear scan assumes the standard preordered input.
