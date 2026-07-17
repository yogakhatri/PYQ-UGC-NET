# Question 61

*UGC NET CS · 2015 June Paper 3 · Context-Free Language · CFG for Unequal Symbol Counts*

Which context-free grammar generates L = {w | n_0(w) > n_1(w)}?

- **1.** S → 0 | 0S | 1SS
- **2.** S → 0S | 1S | 0SS | 1SS | 0 | 1
- **3.** S → 0 | 0S | 1SS | S1S | SS1
- **4.** S → 0S | 1S | 0 | 1

> [!TIP]
> **Correct answer: 3. S → 0 | 0S | 1SS | S1S | SS1**

## Solution

Every derivation in option 3 has more zeros than ones. `0` supplies one excess zero; `0S` adds another zero to a valid string. Each of `1SS`, `S1S`, and `SS1` inserts one `1` but combines two strings that each already have at least one excess zero, leaving total excess at least one. The three placements of `1` allow the grammar to construct valid strings with the unmatched zero appearing around arbitrary substructures.

## Key Points

- Maintain the invariant `#0−#1 ≥ 1`; a production with one new 1 must combine two positive-excess subwords.

## Why the other options are incorrect

Option 1 lacks productions for enough placements of an internal or trailing 1 and does not generate the entire language. Options 2 and 4 directly generate `1`, where zeros do not outnumber ones; they also permit repeated `1S` constructions that violate the invariant.
