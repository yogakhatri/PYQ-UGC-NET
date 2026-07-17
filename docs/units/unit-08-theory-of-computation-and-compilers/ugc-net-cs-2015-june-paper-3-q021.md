# Question 21

*UGC NET CS · 2015 June Paper 3 · Finite Automata · Parity-Tracking DFA States*

For L = {w | n_a(w) and n_b(w) are both odd}, the transitions are δ(q0,a)=q1, δ(q0,b)=q2; δ(q1,a)=q0, δ(q1,b)=q3; δ(q2,a)=q3, δ(q2,b)=q0; δ(q3,a)=q2, δ(q3,b)=q1. What are the initial and final states?

- **1.** q0 and q0 respectively
- **2.** q0 and q1 respectively
- **3.** q0 and q2 respectively
- **4.** q0 and q3 respectively

> [!TIP]
> **Correct answer: 4. q0 and q3 respectively**

## Solution

Interpret each state by parity. Starting at q0, both counts are even. Reading `a` moves to q1, so q1 is odd-a/even-b; reading `b` from q0 moves to q2, so q2 is even-a/odd-b. From q1, reading `b` reaches q3, which must therefore represent odd-a/odd-b. The language accepts exactly that parity combination, so q0 is initial and q3 is final.

## Key Points

- A parity DFA uses one state for each pair: even/even, odd/even, even/odd, odd/odd.

## Why the other options are incorrect

q0 represents even/even, q1 odd/even, and q2 even/odd; none satisfies both-odd. The transition table's toggling behavior uniquely identifies q3 as the accepting state.
