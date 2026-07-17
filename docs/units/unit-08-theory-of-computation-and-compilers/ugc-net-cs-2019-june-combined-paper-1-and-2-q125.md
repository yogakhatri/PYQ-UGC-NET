# Question 125

*UGC NET CS · 2019 June Paper 1 And 2 · Regular Language Models · Minimum DFA*

How many states are there in a minimum-state automaton equivalent to the regular expression a*b(a+b)?

- **1.** 1
- **2.** 2
- **3.** 3
- **4.** 4

> [!TIP]
> **Correct answer: 4. 4**

## Solution

The expression a*b(a+b) describes zero or more a's, followed by b, followed by exactly one symbol a or b. A complete DFA needs: q0 for the initial a* prefix, q1 after the required b, q2 as the accepting state after the final symbol, and a dead state for any extra or invalid symbol. These four states have different future behaviours and cannot be merged, so the minimum complete automaton has four states.

## Key Points

- Count distinguishable residual languages, including the dead state when a complete DFA is intended.

## Why the other options are incorrect

One, two or three states cannot separately represent all four distinguishable residual situations: still in a*, just after b, exactly complete and irrecoverably invalid.

## Additional Information

Transitions: q0 loops on a and goes to q1 on b; q1 goes to q2 on either a or b; q2 goes to dead on either symbol; dead loops on both.
