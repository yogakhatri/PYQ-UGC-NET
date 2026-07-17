# Question 142

*UGC NET CS · 2018 Dec Paper 1 And 2 · Intelligent Agents · Static, Dynamic and Semi-Dynamic Environments*

Which of the following is true for semi-dynamic environment?

- **1.** The environment may change while the agent is deliberating.
- **2.** The environment itself does not change with the passage of time but the agent's performance score does.
- **3.** Even if the environment changes with the passage of time while deliberating, the performance score does not change.
- **4.** Environment and performance score, both change simultaneously.

> [!TIP]
> **Correct answer: 2. The environment itself does not change with the passage of time but the agent's performance score does.**

## Solution

An environment is dynamic if it can change while the agent is deliberating. It is static if neither the relevant state nor the performance measure changes during deliberation. The intermediate, semi-dynamic case occurs when the environment itself stays fixed but the agent's performance score changes with time—for example, a chess board with a running clock. This is exactly option 2.

## Key Points

- Semi-dynamic means fixed world state during deliberation, but a time-sensitive performance measure.

## Why the other options are incorrect

Option 1 describes a dynamic environment. Option 3 also allows the environment to change and therefore is not the defining semi-dynamic case. Option 4 makes both state and score change, which is fully dynamic rather than semi-dynamic.
