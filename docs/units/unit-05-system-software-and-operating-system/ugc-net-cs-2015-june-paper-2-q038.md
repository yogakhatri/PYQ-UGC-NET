# Question 38

*UGC NET CS · 2015 June Paper 2 · Memory Management · LRU Page Replacement*

A LRU page replacement is used with four page frames and eight pages. How many page faults will occur with the reference string 0172327103 if the four frames are initially empty ?

- **1.** 6
- **2.** 7
- **3.** 5
- **4.** 8

> [!TIP]
> **Correct answer: 2. 7**

## Solution

Trace LRU through `0 1 7 2 3 2 7 1 0 3` with four empty frames. The first four references `0,1,7,2` cause four faults. Reference `3` evicts least-recently-used page 0, giving fault 5. References `2,7,1` are hits. Reference `0` then evicts page 3, giving fault 6; the final `3` evicts the now least-recently-used page 2, giving fault 7. Thus there are seven page faults.

## Key Points

- LRU replaces the page whose most recent use is furthest in the past; hits must also refresh recency.

## Why the other options are incorrect

Counts 5 or 6 miss one or both faults near the end, while 8 incorrectly counts a hit as a fault. Updating recency on every hit—especially for 2, 7, and 1—is essential to choosing the later victims correctly.
