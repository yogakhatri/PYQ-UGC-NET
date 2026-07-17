# Question 22

*UGC NET CS · 2018 July Paper 2 · Data Structures · BUILD-MAX-HEAP and Array Representation*

For A=⟨4,1,3,2,16,9,10,14,8,7⟩, after BUILD-MAX-HEAP, what are the heap depth and the root's right child, respectively? The root is at level 0.

- **1.** 3, 14
- **2.** 3, 10
- **3.** 4, 14
- **4.** 4, 10

> [!TIP]
> **Correct answer: 2. 3, 10**

## Solution

Ten heap elements occupy levels 0 through ⌊log₂10⌋=3, so the depth is 3. Bottom-up BUILD-MAX-HEAP transforms the array into one valid result ⟨16,14,10,8,7,9,3,2,4,1⟩. The root is 16 and its right child, at array index 3 in 1-based representation, is 10. Hence the pair is (3,10), option 2.

## Key Points

- A complete heap with n nodes has edge-depth ⌊log₂n⌋; in a 1-indexed array the root's children are positions 2 and 3.

## Why the other options are incorrect

Options 3 and 4 count four levels as depth 4, despite the explicit root-at-level-0 convention. Options 1 and 3 choose 14, which is the root's left child after heap construction, not its right child.
