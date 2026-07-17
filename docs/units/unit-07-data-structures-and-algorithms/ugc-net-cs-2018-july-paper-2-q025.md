# Question 25

*UGC NET CS · 2018 July Paper 2 · Greedy Algorithms · Huffman Coding and Average Length*

Characters A,B,C,D,E occur with probabilities 0.08,0.40,0.25,0.15,0.12, respectively. What average codeword length is achieved by optimal binary prefix coding?

- **1.** 2.4
- **2.** 1.87
- **3.** 3.0
- **4.** 2.15

> [!TIP]
> **Correct answer: 4. 2.15**

## Solution

Huffman coding repeatedly combines the two smallest probabilities: .08+.12=.20, then .15+.20=.35, then .25+.35=.60, then .40+.60=1. The resulting code lengths can be B:1, C:2, D:3, A:4, E:4. Average length is .40(1)+.25(2)+.15(3)+.08(4)+.12(4)=2.15 bits/symbol. Hence option 4 is correct.

## Key Points

- Huffman minimizes expected prefix-code length by repeatedly merging the two least probable symbols/subtrees.

## Why the other options are incorrect

The other averages do not correspond to the weighted external path length of the optimal Huffman tree. The most probable character must receive a short code; simply averaging code lengths without probability weights is incorrect.
