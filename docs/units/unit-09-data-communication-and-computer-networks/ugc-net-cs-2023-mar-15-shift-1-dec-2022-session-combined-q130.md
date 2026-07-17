# Question 130

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Cloud Computing and IoT · Cloud and Database Storage*

I. No.8 BID:8708 A disk has 300 cylinders (0 to 299). If the initial position of the read-write head is at cylinder 101, moving towards the higher end of the disk, calculate the total head movement following C_LOOK policy for the read request sequence: 123, 45, 197, 87, 250, 198, 280

- **1.** 456
- **2.** 450
- **3.** 458
- **4.** 445

> [!TIP]
> **Correct answer: 1. 456**

## Solution

C-LOOK moving upward serves 123,197,198,250,280, then wraps to45 and serves87. Movement is (280−101)+(280−45)+(87−45)=179+235+42=456 cylinders.

## Key Points

- C-LOOK reverses logically by wrapping from highest request directly to lowest request.

## Why the other options are incorrect

Other totals omit or mismeasure the circular wrap or an ordered segment.
