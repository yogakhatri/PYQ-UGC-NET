# Question 59

*UGC NET CS · 2019 June Paper 1 And 2 · Sets and Relations · Transitive closure of a relation*

Find the zero-one matrix of the transitive closure of the relation represented by A=[[1,0,1],[0,1,0],[1,1,0]].

- **1.** [[1,1,1],[0,1,0],[1,1,1]]
- **2.** [[1,0,1],[0,1,0],[1,1,0]]
- **3.** [[1,0,1],[0,1,0],[1,0,1]]
- **4.** [[1,1,1],[0,1,0],[1,0,1]]

> [!TIP]
> **Correct answer: 1. [[1,1,1],[0,1,0],[1,1,1]]**

## Solution

The original relation has 1→3 and 3→2, so transitivity requires 1→2. It also has 3→1 and 1→3, so 3 can reach itself; combining the paths from 3 also reaches 2. Vertex 2 reaches only itself. Thus the reachability rows are [1,1,1], [0,1,0] and [1,1,1], which is option 1.

## Key Points

- A transitive closure contains (i,j) whenever any directed path from i to j exists, not only when a direct edge exists.

## Why the other options are incorrect

- **Option 2:** is just the original matrix and omits paths of length greater than one.
- **Option 3:** omits 1→2 and 3→2.
- **Option 4:** omits the path 3→2.
