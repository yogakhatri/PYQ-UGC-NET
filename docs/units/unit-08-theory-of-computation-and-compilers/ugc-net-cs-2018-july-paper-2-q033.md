# Question 33

*UGC NET CS · 2018 July Paper 2 · Pushdown Automata · Two-Stack PDA Equivalence to a Turing Machine*

A pushdown automaton has the power of a Turing machine when the number of auxiliary stacks is:

- **1.** 0
- **2.** 1
- **3.** 1 or more
- **4.** 2 or more

> [!TIP]
> **Correct answer: 4. 2 or more**

## Solution

One stack gives an ordinary pushdown automaton, which recognizes context-free languages and is weaker than a Turing machine. Two stacks are sufficient to simulate a Turing tape: one stores the tape portion left of the head and the other stores the current/right portion, with pushes and pops simulating head movement. Therefore a PDA-like machine with two or more auxiliary stacks has Turing-machine power, option 4.

## Key Points

- Finite control + one stack = PDA; finite control + two stacks = Turing-equivalent computation.

## Why the other options are incorrect

With zero stacks the device is finite-state; with one stack it remains a standard PDA. Option 3 incorrectly includes the one-stack case, which cannot recognize all Turing-recognizable languages.
