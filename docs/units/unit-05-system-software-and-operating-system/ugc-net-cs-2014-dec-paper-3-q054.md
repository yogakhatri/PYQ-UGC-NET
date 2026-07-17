# Question 54

*UGC NET CS · 2014 Dec Paper 3 · Distributed Systems · Distributed Shared Memory*

In a distributed computing environment, distributed shared memory is used which is

- **A.** Logical combination of virtual memories on the nodes.
- **B.** Logical combination of physical memories on the nodes.
- **C.** Logical combination of the secondary memories on all the nodes.
- **D.** All of the above

> [!TIP]
> **Correct answer: B. Logical combination of physical memories on the nodes.**

## Solution

Distributed shared memory presents physically separate main memories at different nodes as one logically shared address space. Reads and writes to shared locations are translated into local or remote memory operations, with the DSM system managing placement and coherence. Thus it is a logical combination of the nodes' physical memories.

## Key Points

- DSM hides physical distribution: separate node memories appear as one shared address space.

## Why the other options are incorrect

Virtual-memory mechanisms may help implement DSM, but DSM is not defined as combining each node's independent virtual memory. Secondary storage is not the shared-memory substrate described here. Because C is false, all of the above cannot be correct.
