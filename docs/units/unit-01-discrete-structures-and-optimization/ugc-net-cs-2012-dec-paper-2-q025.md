# Question 25

*UGC NET CS · 2012 Dec Paper 2 · Graph Theory · Full m-ary Trees*

A chain letter asks each recipient to send it to four other people. Some do so and some send none. No one receives more than one letter. If the chain ends after 100 people read it but do not send it, how many people saw the letter including the first person, and how many sent it?

- **1.** 122 and 22
- **2.** 111 and 11
- **3.** 133 and 33
- **4.** 144 and 44

> [!TIP]
> **Correct answer: 3. 133 and 33**

## Solution

Model the chain as a full rooted 4-ary tree. A person who sends the letter is an internal vertex with exactly four children; a person who does not send it is a leaf. If I people send and L=100 do not, the number of edges is both 4I and (I+L)-1. Thus 4I=I+100-1, so 3I=99 and I=33. The total number who saw the letter is I+L=33+100=133.

## Key Points

- For a full m-ary tree, L=(m-1)I+1 and total vertices are I+L.
- Here 100 leaves imply 33 internal senders and 133 readers.

## Why the other options are incorrect

The other pairs do not satisfy the full m-ary tree relation L=(m-1)I+1. For m=4 and L=100, the only possible sender count is 33 and the first person is already included as the root.
