# Question 44

*UGC NET CS · 2012 Dec Paper 2 · Regular Languages and Finite Automata · NFA-to-DFA Subset Construction*

Let L be accepted by a nondeterministic finite automaton with |Q| states. The maximum number of states in an equivalent deterministic finite automaton accepting L is:

- **1.** Q
- **2.** 2|Q
- **3.** 2^|Q|-1
- **4.** 2^|Q

> [!TIP]
> **Correct answer: 4. 2^|Q**

## Solution

The subset construction represents each DFA state by a subset of the NFA's state set Q. A set with |Q| elements has 2^|Q| subsets, including the empty subset, so an equivalent DFA may require as many as 2^|Q| states in the worst case.

## Key Points

- NFA-to-DFA conversion uses states that are subsets of Q; the power set has 2^|Q| members.

## Why the other options are incorrect

|Q| and 2|Q| grow only linearly and cannot represent every possible subset. Subtracting one wrongly removes the empty subset, which may be needed as the dead DFA state when no NFA state is reachable.
