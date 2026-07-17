# Question 49

*UGC NET CS · 2015 June Paper 3 · Operating-System Concepts · Spooling, Multiprogramming, Time Sharing, and Distribution*

Match the following for operating system techniques with the most appropriate advantage : List - I List - II (a) Spooling (i) Allows several jobs in memory to improve CPU utilization (b) Multiprogramming (ii) Access to shared resources among geographically dispersed computers in a transparent way (c) Time sharing (iii) Overlapping I/O and computations (d) Distributed computing (iv) Allows many users to share a computer simultaneously by switching processor frequently Codes : (a) (b) (c) (d)

- **1.** (iii) (i) (ii) (iv)
- **2.** (iii) (i) (iv) (ii)
- **3.** (iv) (iii) (ii) (i)
- **4.** (ii) (iii) (iv) (i)

> [!TIP]
> **Correct answer: 2. (iii) (i) (iv) (ii)**

## Solution

Spooling places device work in a disk queue so slow I/O can overlap computation: (a)–(iii). Multiprogramming keeps several jobs in memory to use the CPU when one waits: (b)–(i). Time sharing switches the processor frequently to support simultaneous interactive users: (c)–(iv). Distributed computing provides transparent access to resources on geographically separated machines: (d)–(ii). The sequence is `(iii),(i),(iv),(ii)`.

## Key Points

- Spooling overlaps device work, multiprogramming raises utilization, time sharing serves users, and distribution shares remote resources.

## Why the other options are incorrect

Each other code sequence swaps at least one defining advantage. The strongest anchors are time sharing with many simultaneous users and distributed computing with geographically dispersed shared resources; these force option 2.
