# Question 38

*UGC NET CS · 2017 Nov Paper 2 · File and Input/Output Systems · Optimal Sequential File Ordering*

Suppose there are six files F1, F2, F3, F4, F5, F6 with corresponding sizes 150 KB, 225 KB, 75 KB, 60 KB, 275 KB and 65 KB respectively. The files are to be stored on a sequential device in such a way that optimizes access time. In what order should the files be stored ?

- **1.** F5, F2, F1, F3, F6, F4
- **2.** F4, F6, F3, F1, F2, F5
- **3.** F1, F2, F3, F4, F5, F6
- **4.** F6, F5, F4, F3, F2, F1

> [!TIP]
> **Correct answer: 2. F4, F6, F3, F1, F2, F5**

## Solution

On a sequential device, reaching a later file requires passing all earlier file contents. With equal access probabilities, the average retrieval time is minimized by placing the shortest files first (the shortest-processing-time rule). Sorting the sizes gives F4=60, F6=65, F3=75, F1=150, F2=225, F5=275 KB. This is option 2.

## Key Points

- For equally likely sequential files, ascending file size minimizes the sum—and hence the mean—of completion/access times.

## Why the other options are incorrect

Option 1 uses descending size, which maximizes rather than minimizes the accumulated waiting time. Options 3 and 4 are not ordered by increasing size. If access probabilities differed, a weighted ordering would be needed; none are supplied, so equal likelihood is the intended assumption.
