# Question 56

*UGC NET CS · 2018 July Paper 2 · Memory Management · Internal and External Fragmentation*

Which of the following statements are true ? (a) External Fragmentation exists when there is enough total memory space t o satisfy a request but the available space is contiguous. (b) Memory Fragmentation can be internal as well as external. (c) One solution to external Fragmentation is compaction.

- **1.** (a) and (b) only
- **2.** (a) and (c) only
- **3.** (b) and (c) only
- **4.** (a), (b) and (c)

> [!TIP]
> **Correct answer: 3. (b) and (c) only**

## Solution

Read statement (a) literally: it says the available free space is contiguous. That is false—external fragmentation is precisely the case where enough total free memory exists but it is split into noncontiguous holes. Statement (b) is true because fragmentation may be internal or external. Statement (c) is true because compaction relocates allocated blocks so scattered holes merge into a larger contiguous region. Therefore only (b) and (c) are true, option 3.

## Key Points

- External fragmentation means sufficient total free space but no sufficiently large contiguous hole; compaction can combine holes.

## Why the other options are incorrect

Options 1, 2, and 4 all include the false printed statement (a). If `contiguous` were corrected to `not contiguous`, all three statements would be true, but that is not what the verified source page says.
