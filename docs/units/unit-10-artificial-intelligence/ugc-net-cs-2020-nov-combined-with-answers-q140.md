# Question 140

*UGC NET CS · 2020 Nov With Answers · Search and Optimization · Genetic Algorithms and AND–OR Search*

Statement I: A genetic algorithm is a stochastic hill-climbing search in which a population of states is maintained. Statement II: In nondeterministic environments, agents can use AND–OR search to generate contingent plans that reach the goal regardless of which outcome occurs during execution. Choose the correct evaluation.

- **1.** Both Statement I and Statement II are true
- **2.** Both Statement I and Statement Il are false
- **3.** Statement I is correct but Statement II is false
- **4.** Statement I is incorrect but Statement II is true

> [!TIP]
> **Correct answer: 1. Both Statement I and Statement II are true**

## Solution

A genetic algorithm performs stochastic population-based search: selection favours fitter states while crossover and mutation generate new candidates, making the hill-climbing characterization reasonable. Statement I is true. In a nondeterministic problem, one action can have several possible outcomes. An AND–OR search tree uses OR nodes for the agent's choice and AND nodes for the outcomes that the plan must handle, thereby representing a contingent plan that succeeds for every possible result. Statement II is also true, so option 1 follows.

## Key Points

- Genetic algorithms search with a stochastic population; AND–OR search builds plans with a branch for every nondeterministic outcome.

## Why the other options are incorrect

Options 2–4 reject at least one standard AI characterization. Ordinary single-path search is insufficient for nondeterministic outcomes, while genetic algorithms differ from deterministic hill climbing precisely through random variation and a maintained population.
