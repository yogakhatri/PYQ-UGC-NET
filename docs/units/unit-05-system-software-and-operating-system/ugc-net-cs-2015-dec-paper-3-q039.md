# Question 39

*UGC NET CS · 2015 Dec Paper 3 · Deadlocks · Safety-State Analysis*

Consider a system with twelve magnetic tape drives and three processes P1, P2 and P3. Process P1 requires maximum ten tape drives, process P2 may need as many as four tape drives and P3 may need upto nine tape drives. Suppose that at time t1, process P1 is holding five tape drives, process P2 is holding two tape drives and process P3 is holding three tape drives. At time t1, system is in :

- **1.** safe state
- **2.** unsafe state
- **3.** deadlocked state
- **4.** starvation state

> [!TIP]
> **Correct answer: 2. unsafe state**

## Solution

Ten of the 12 drives are allocated, leaving Work=2. Remaining needs are P1:10−5=5, P2:4−2=2, and P3:9−3=6. P2 can finish first and release its current two drives, making Work=4. Neither P1 (needs 5) nor P3 (needs 6) can then finish, so no complete safe sequence exists. The state is unsafe.

## Key Points

- Unsafe means no guaranteed safe completion sequence; it does not necessarily mean deadlock has already occurred.

## Why the other options are incorrect

It is not safe because the safety algorithm gets stuck. It is not necessarily already deadlocked: P2 can still obtain its remaining drives and finish. Starvation concerns indefinite postponement, which the snapshot does not establish.
