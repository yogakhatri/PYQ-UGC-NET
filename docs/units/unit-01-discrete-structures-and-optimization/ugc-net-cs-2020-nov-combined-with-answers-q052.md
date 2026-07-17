# Question 52

*UGC NET CS · 2020 Nov With Answers · Combinatorics · Integer Partitions and Identical Boxes*

How many ways are there to pack six copies of the same book into four identical boxes, where a box can contain as many as six books?

- **1.** 4
- **2.** 6
- **3.** 7
- **4.** 9

> [!TIP]
> **Correct answer: 4. 9**

## Solution

Because both the books and boxes are identical, an arrangement is determined only by the unordered positive occupancies of the nonempty boxes—an integer partition of 6 into at most four parts. List them: 6; 5+1; 4+2; 4+1+1; 3+3; 3+2+1; 3+1+1+1; 2+2+2; and 2+2+1+1. Empty boxes may fill the remaining positions, but identical empty boxes create no new arrangement. There are 9 ways, option 4.

## Key Points

- Identical objects in identical boxes are counted by integer partitions, here partitions of 6 with at most four parts.

## Why the other options are incorrect

Stars-and-bars would overcount because it treats boxes as distinguishable. Counts 4, 6, and 7 omit valid partitions. The capacity of six imposes no additional restriction because only six books exist.
