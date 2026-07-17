# Question 10

*UGC NET CS · 2016 July Paper 2 · Digital Logic Circuits and Components · JK flip-flop behavior*

In a positive-edge-triggered JK flip-flop, if J and K both are high then the output will be _____ on the rising edge of the clock.

- **1.** No change
- **2.** Set
- **3.** Reset
- **4.** Toggle

> [!TIP]
> **Correct answer: 4. Toggle**

## Solution

The JK next-state equation is Q⁺=JQ̄+K̄Q. With J=K=1, this becomes Q⁺=Q̄: on each active rising edge, a current 0 becomes 1 and a current 1 becomes 0. The output therefore toggles.

## Key Points

- JK inputs 00 hold, 10 set, 01 reset, 11 toggle.

## Why the other options are incorrect

J=K=0 gives no change, J=1,K=0 sets, and J=0,K=1 resets. Those are the other three rows of the JK characteristic table, not the J=K=1 case.
