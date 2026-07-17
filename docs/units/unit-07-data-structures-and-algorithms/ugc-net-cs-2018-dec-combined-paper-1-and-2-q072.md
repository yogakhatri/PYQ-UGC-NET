# Question 72

*UGC NET CS · 2018 Dec Paper 1 And 2 · Data Structures · Max-Heap Insertion*

The elements 42, 25, 30, 40, 22, 35, 26 are inserted one by one in the given order into a max-heap. The resultant max-heap is stored in an array implementation as

- **1.** <42, 40, 35, 25, 22, 30, 26>
- **2.** <42, 35, 40, 22, 25, 30, 26>
- **3.** <42, 40, 35, 25, 22, 26, 30>
- **4.** <42, 35, 40, 22, 25, 26, 30>

> [!TIP]
> **Correct answer: 1. <42, 40, 35, 25, 22, 30, 26>**

## Solution

Insert each key at the next array position and bubble it upward while it exceeds its parent. After 42,25,30 the heap is <42,25,30>. Inserting 40 swaps it with 25, giving <42,40,30,25>. Inserting 22 changes nothing. Inserting 35 swaps with 30, giving <42,40,35,25,22,30>. Finally 26 is no larger than its parent 35, so the result is <42,40,35,25,22,30,26>, option 1.

## Key Points

- Heap insertion appends at the next leaf and performs only parent swaps along that new node’s ancestor path.

## Why the other options are incorrect

Options 2 and 4 incorrectly place 35 above 40 even though their insertion paths do not require that swap. Option 3 reverses the final siblings 30 and 26; insertion preserves 30 at index 6 and places 26 at index 7.
