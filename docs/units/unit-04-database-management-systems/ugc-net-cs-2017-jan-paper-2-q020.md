# Question 20

*UGC NET CS · 2017 Jan Paper 2 · Database Indexing · B+ Tree Degree from Block Size*

The order of a leaf node in a B+ tree is the maximum number of children it can have. Suppose that block size is 1 kilobytes, the child pointer takes 7 bytes long and search field value takes 14 bytes long. The order of the leaf node is ________.

- **1.** 16
- **2.** 63
- **3.** 64
- **4.** 65

> [!TIP]
> **Correct answer: No listed option — the stated sizes allow 48 leaf entries (or 49 internal children), not 16, 63, 64, or 65**

## Solution

A B+ tree leaf stores search-key/data-pointer pairs and normally one pointer to the next leaf. Each pair here needs 14+7=21 bytes. Even ignoring every other overhead, floor(1024/21)=48 pairs fit; reserving a 7-byte next-leaf pointer still gives floor((1024−7)/21)=48. If the question instead intended an internal-node order p, its size equation would be 7p+14(p−1)≤1024, yielding p≤49. Neither standard interpretation produces any listed option.

## Key Points

- Derive B+ tree capacity from a byte inequality; do not choose an option merely because that many entries would fit.

## Why the other options are incorrect

16 is merely a smaller number that would fit, not the maximum. Values 63, 64, and 65 would require at least 1323, 1344, and 1365 bytes respectively for 21-byte entries, already exceeding a 1 KiB block before overhead.

## Additional Information

The stem is also terminologically loose: leaf nodes have data pointers/entries and a sibling pointer, whereas 'number of children' conventionally describes internal-node fan-out. This item is defective as printed.

## References

- [University of Cape Town — B+ tree internal and leaf-node structure](https://www.cs.uct.ac.za/mit_notes/database/htmls/chp11.html)
