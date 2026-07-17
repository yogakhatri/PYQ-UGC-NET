# Question 82

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Regular Language Models · Grammars and Expressions*

SA 37032 What is the minimum and maximum number of initial, dead, unreachable and final states in a valid 'n' state finite automaton, where the language accepted is not '4'?

- **1.** Minimum: 1,1,1,1; Maximum: 1, (n-1), (n-1), n
- **2.** Minimum: 1,0,0,0; Maximum: 1, (n-1), (n-1), n
- **3.** Minimum: 1,0,0,n; Maximum: 1, n, (n-1), (n-1)
- **4.** Minimum: 1,0,0,1; Maximum: 1, (n-1), (n-1), n

> [!TIP]
> **Correct answer: 4. Minimum: 1,0,0,1; Maximum: 1, (n-1), (n-1), n**

## Solution

A valid n-state automaton has exactly one initial state. With a nonempty accepted language it needs at least one final state; dead and unreachable states may be zero. Maxima are one initial, n−1 dead, n−1 unreachable, and n final states. This matches option 4.

## Key Points

- Initial count is exactly one; reachability/deadness are optional; all states may be final.

## Why the other options are incorrect

Other choices require dead/unreachable states unnecessarily or allow zero final states despite a nonempty language.
