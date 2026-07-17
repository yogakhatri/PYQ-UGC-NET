# Question 114

*UGC NET CS · 2019 Dec Paper 1 And 2 · Genetic Algorithms · Schema Order and Defining Length*

In genetic algorithms, what are the orders of the schemata ?10?101? and ???0??1, respectively?

- **1.** 5, 3
- **2.** 5, 2
- **3.** 7, 5
- **4.** 8, 7

> [!TIP]
> **Correct answer: 2. 5, 2**

## Solution

A schema's order is the number of fixed positions—0s and 1s—not the total length and not the number of wildcards. In ?10?101?, five positions are fixed: 1,0,1,0,1. In ???0??1, only two positions are fixed: 0 and 1. The orders are therefore 5 and 2, option 2.

## Key Points

- Schema order o(H) = count of non-wildcard symbols in H.

## Why the other options are incorrect

The pair 5,3 miscounts one wildcard in the second schema as fixed. The pairs 7,5 and 8,7 confuse order with length or with the number of nonleading positions. Every '?' can match either bit and contributes zero to schema order.
