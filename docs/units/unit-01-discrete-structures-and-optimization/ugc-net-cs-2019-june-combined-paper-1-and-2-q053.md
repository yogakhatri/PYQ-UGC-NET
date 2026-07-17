# Question 53

*UGC NET CS · 2019 June Paper 1 And 2 · Counting, Mathematical Induction and Discrete Probability · Inclusion-Exclusion Principle*

How many bit strings of length ten either start with a 1 bit or end with two bits 00?

- **1.** 320
- **2.** 480
- **3.** 640
- **4.** 768

> [!TIP]
> **Correct answer: 3. 640**

## Solution

Let A be the set of length-10 strings starting with 1 and B the set ending with 00. For A, the other nine bits are free, so |A|=2^9=512. For B, the first eight bits are free, so |B|=2^8=256. Strings in both sets start with 1 and end with 00, leaving seven free bits, so |A∩B|=2^7=128. Inclusion-exclusion gives 512+256-128=640.

## Key Points

- For an either-or count, use |A∪B|=|A|+|B|-|A∩B|.

## Why the other options are incorrect

- **Option 1:** 320 does not count both overlapping conditions correctly.
- **Option 2:** 480 subtracts too much from the union.
- **Option 4:** 768 simply adds 512 and 256 and double-counts the 128 strings satisfying both conditions.
