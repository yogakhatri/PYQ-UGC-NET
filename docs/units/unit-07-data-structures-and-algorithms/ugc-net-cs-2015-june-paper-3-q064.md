# Question 64

*UGC NET CS · 2015 June Paper 3 · Greedy Algorithms · Huffman Weighted Path Length*

Symbols A, B, C, D, E, F, G, and H have probabilities 1/30, 1/30, 1/30, 2/30, 3/30, 5/30, 5/30, and 12/30 respectively. What is the average Huffman code size in bits per symbol?

- **1.** 67/30
- **2.** 70/34
- **3.** 76/30
- **4.** 78/30

> [!TIP]
> **Correct answer: 3. 76/30**

## Solution

Huffman merging uses the two smallest weights repeatedly. With integer weights over denominator 30, one valid merge sequence is `1+1=2`, `1+2=3`, `2+3=5`, `3+5=8`, `5+5=10`, `8+10=18`, and `12+18=30`. The weighted external path length equals the sum of all merge weights: `2+3+5+8+10+18+30 = 76`. Dividing by total weight 30 gives average length `76/30` bits per symbol.

## Key Points

- For a Huffman tree, average code length = sum of merge weights / total source weight.

## Why the other options are incorrect

The other fractions do not equal the Huffman weighted path length for these weights. Tie choices may change which equal-weight symbols receive particular codes, but they do not change the optimal average cost here.
