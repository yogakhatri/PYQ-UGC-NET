# Question 70

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · CPU Scheduling · FCFS average waiting time*

10-:107020 For the following set of processes scheduled using FCFS policy. determine the average waiting time. Assume that the processes arrived in the order P1, P2, P3, P4. Process Burst Time (ms) P1 8 P2 15 P3

- **1.** 8
- **2.** 16
- **3.** 32
- **4.** 48

> [!TIP]
> **Correct answer: 2. 16**

## Solution

Under FCFS the order is P1,P2,P3,P4 with burst times 8,15,10,7 ms. Their waiting times are 0, 8, 8+15=23, and 8+15+10=33 ms. The average is (0+8+23+33)/4 = 64/4 = 16 ms.

## Key Points

- For FCFS, each process waits for the sum of all burst times before it; average those cumulative sums.

## Why the other options are incorrect

8 ms is only P2’s waiting time. The values 32 and 48 do not equal the mean of the four cumulative waiting times; they result from omitting or mis-accumulating earlier bursts.
