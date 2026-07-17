# Question 59

*UGC NET CS · 2016 July Paper 3 · Greedy Algorithms · Huffman Weighted Path Length*

Consider a source with symbols A, B, C, D with probabilities 1/2, 1/4, 1/8, 1/8 respectively. What is the average number of bits per symbol for the Huffman code generated from above information ?

- **1.** 2 bits per symbol
- **2.** 1.75 bits per symbol
- **3.** 1.50 bits per symbol
- **4.** 1.25 bits per symbol

> [!TIP]
> **Correct answer: 2. 1.75 bits per symbol**

## Solution

Build the Huffman tree by repeatedly combining the two smallest probabilities. First combine 1/8 and 1/8 to obtain 1/4. Then combine that new 1/4 with the original 1/4 to obtain 1/2. Finally combine the two 1/2 nodes. The resulting code lengths are 1 for A, 2 for B, and 3 each for C and D. Hence the average length is (1/2)(1) + (1/4)(2) + (1/8)(3) + (1/8)(3) = 0.5 + 0.5 + 0.375 + 0.375 = 1.75 bits per symbol. Option 2 is correct.

## Key Points

- Huffman average length is the probability-weighted path length: sum pᵢlᵢ, not the ordinary average of the codeword lengths.

## Why the other options are incorrect

A fixed-length code for four symbols would use 2 bits per symbol, but Huffman exploits unequal probabilities. The smaller values 1.50 and 1.25 cannot be achieved by a binary prefix code for this distribution; the Huffman average also equals the source entropy here, confirming optimality.
