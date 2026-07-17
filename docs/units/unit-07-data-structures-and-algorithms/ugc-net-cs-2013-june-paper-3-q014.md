# Question 14

*UGC NET CS · 2013 June Paper 3 · Greedy Algorithms · Huffman Coding Cost*

A data file of 1,00,000 characters contains only the characters g-l, with the frequencies as indicated in table : g h i j k l Frequency in thousand 45 13 12 16 9 5 using the variable-length code by Huffman codes, the file can be encoded with

- **A.** 2,52,000 bits
- **B.** 2,64,000 bits
- **C.** 2,46,000 bits
- **D.** 2,24,000 bits

> [!TIP]
> **Correct answer: D. 2,24,000 bits**

## Solution

Build the Huffman tree by repeatedly merging the two smallest frequencies (in thousands): 5+9=14, 12+13=25, 14+16=30, 25+30=55, and 45+55=100. The resulting code lengths are 1 for frequency 45; 3 for 12, 13 and 16; and 4 for 5 and 9. Total bits, in thousands, are 45·1+12·3+13·3+16·3+9·4+5·4=224. Thus the file requires 224,000 bits.

## Key Points

- Huffman cost can be computed by summing every merge weight; here that sum is 224 thousand.

## Why the other options are incorrect

The other totals do not equal the weighted external path length of the optimal Huffman tree. A useful arithmetic check is that every merge adds its combined frequency to total cost: 14+25+30+55+100=224 thousand bits.
