# Question 33

*UGC NET CS · 2012 June Paper 2 · Memory Management · Page Replacement*

For page trace 4,3,2,1,4,3,5,4,3,2,1,5 and four frames, how many FIFO page faults occur?

- **A.** 8
- **B.** 9
- **C.** 10
- **D.** 12

> [!TIP]
> **Correct answer: C. 10**

## Solution

Fill the four frames with 4,3,2,1: four faults. The next references 4 and 3 are hits. Reference 5 faults and evicts the oldest page 4. Then 4, 3, 2, 1 and 5 each fault in turn, evicting 3, 2, 1, 5 and 4 respectively. Total faults=4+1+5=10.

## Key Points

- FIFO evicts by arrival order, not recent use; maintain a queue of loaded pages while tracing.

## Why the other options are incorrect

Counts 8 or 9 miss one or more cascading FIFO evictions after page 5 enters. Twelve incorrectly treats both hits at positions 5 and 6 as faults.

## Additional Information

The source says 'percentage', but the options are counts. Ten faults out of twelve references would be about 83.33%.
