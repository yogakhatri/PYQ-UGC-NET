# Question 24

*UGC NET CS · 2021 Nov With Answers · Counting · Pigeonhole Principle*

Warehouse bins are specified by aisle, horizontal location within the aisle, and shelf. There are 50 aisles, 85 horizontal locations per aisle, and 5 shelves. What is the least number of products that guarantees at least two products are stored in the same bin?

- **1.** 251
- **2.** 426
- **3.** 4251
- **4.** 21251

> [!TIP]
> **Correct answer: 4. 21251**

## Solution

The number of distinct bins is 50 aisles ×85 locations per aisle ×5 shelves =21,250. With at most one product per bin, 21,250 products can still avoid a collision. The next product forces some bin to contain at least two by the pigeonhole principle. Therefore the least guaranteed number is 21,251, option 4.

## Key Points

- For N bins, N+1 objects guarantee a shared bin.

## Why the other options are incorrect

Options 1–3 multiply only some dimensions or stop at the number of bins. A guarantee requires one more product than the total number of available bins.
