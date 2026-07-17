# Question 72

*UGC NET CS · 2016 July Paper 3 · Heuristic Search · Randomized Hill Climbing*

How does randomized hill-climbing choose the next move each time ?

- **1.** It generates a random move from the moveset, and accepts this move.
- **2.** It generates a random move from the whole state space, and accepts this move.
- **3.** It generates a random move from the moveset, and accepts this move only if this move improves the evaluation function.
- **4.** It generates a random move from the whole state space, and accepts this move only if this move improves the evaluation function.

> [!TIP]
> **Correct answer: 3. It generates a random move from the moveset, and accepts this move only if this move improves the evaluation function.**

## Solution

Randomized hill climbing samples a move from the current state's legal moveset—that is, from neighboring states—and accepts it only when it improves the evaluation value. It is still a hill-climbing method, so it does not deliberately accept a downhill move in this definition. Therefore option 3 is correct.

## Key Points

- Hill climbing is local and improvement-driven; randomization changes which neighbor is tried, not the requirement to climb.

## Why the other options are incorrect

Options 2 and 4 sample from the whole state space rather than from legal neighboring moves. Option 1 accepts every sampled move, including worse ones, which turns the procedure into a random walk rather than hill climbing.
