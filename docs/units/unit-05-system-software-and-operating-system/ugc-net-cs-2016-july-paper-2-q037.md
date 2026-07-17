# Question 37

*UGC NET CS · 2016 July Paper 2 · Deadlocks · Banker's Safety Algorithm*

A system has 12 instances of resource R. For processes P₁, P₂, P₃, P₄, the (maximum need, current allocation) pairs are respectively (8,3), (9,4), (5,2), and (3,1). Is the current state safe? If so, what is a safe sequence?

- **1.** No
- **2.** Yes, P1P2P3P4
- **3.** Yes, P4P3P1P2
- **4.** Yes, P2P1P3P4

> [!TIP]
> **Correct answer: 3. Yes, P4P3P1P2**

## Solution

The current allocations total 3+4+2+1=10, so Available=12−10=2. Remaining needs are P₁:5, P₂:5, P₃:3, P₄:2. Only P₄ can finish first; it releases 1, making Available=3. Then P₃ finishes and releases 2, giving 5. P₁ can now finish and release 3, giving 8, after which P₂ finishes. Thus P₄→P₃→P₁→P₂ is a safe sequence.

## Key Points

- Banker's safety test repeatedly finds a process with Remaining Need≤Available, then adds its allocation back to Available.

## Why the other options are incorrect

The state is not unsafe because P₄'s remaining need equals the two available instances. Sequences beginning with P₁ or P₂ are impossible at the first step because each still needs 5 while only 2 are available.
