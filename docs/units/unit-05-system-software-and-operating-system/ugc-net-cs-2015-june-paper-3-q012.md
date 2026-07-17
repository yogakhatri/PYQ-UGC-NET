# Question 12

*UGC NET CS · 2015 June Paper 3 · File and Input/Output Systems · Indexed File Allocation*

In the indexed scheme of blocks to a file, the maximum possible size of the file depends on :

- **1.** The number of blocks used for index and the size of index
- **2.** Size of Blocks and size of Address
- **3.** Size of index
- **4.** Size of Block

> [!TIP]
> **Correct answer: 2. Size of Blocks and size of Address**

## Solution

In simple indexed allocation, one index block holds block addresses. If block size is `B` bytes and an address occupies `A` bytes, the index holds `B/A` addresses and can point to that many data blocks. Maximum file size is therefore `(B/A) × B = B²/A`, so it depends on both block size and address size.

## Key Points

- Single-level indexed maximum = pointers per index block × bytes per data block = `(B/A)×B`.

## Why the other options are incorrect

Block size alone does not tell how many pointers fit in the index; address size alone does not tell data capacity. `Size of index` is ambiguous, and option 1 refers to multiple index blocks rather than the ordinary single-index-block scheme tested. For that scheme, option 2 supplies the two needed quantities.
