# Question 75

*UGC NET CS · 2014 Dec Paper 3 · Distributed Systems · Distributed versus Parallel Computing Models*

Which computing model is not inherently an example of a distributed-computing environment?

- **A.** Cloud computing
- **B.** Parallel computing
- **C.** Cluster computing
- **D.** Peer-to-peer computing

> [!TIP]
> **Correct answer: B. Parallel computing**

## Solution

Cloud, cluster, and peer-to-peer computing inherently coordinate autonomous networked machines and are standard distributed-computing environments. Parallel computing means executing multiple operations simultaneously; it can occur inside one tightly coupled shared-memory computer with multiple cores and therefore is not inherently distributed. Under that distinction, B is the requested model.

## Key Points

- Parallel describes simultaneous execution; distributed describes coordination across separate networked computers.
- One system may be both, but neither term guarantees the other.

## Why the other options are incorrect

Cloud resources are distributed across infrastructure, clusters connect multiple computers, and peer-to-peer systems consist of networked peers. Parallel programs can certainly run on distributed systems, so the categories overlap; the question asks which model is not necessarily a distributed environment, making B the intended choice.
