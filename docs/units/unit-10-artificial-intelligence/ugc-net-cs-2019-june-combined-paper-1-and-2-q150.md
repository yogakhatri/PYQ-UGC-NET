# Question 150

*UGC NET CS · 2019 June Paper 1 And 2 · Artificial Neural Networks · Unsupervised and Reinforcement Learning*

Reinforcement learning can be formalized using ______, in which the agent initially knows only the set of possible ______ and the set of possible actions.

- **1.** Markov decision processes, objects
- **2.** Hidden states, objects
- **3.** Markov decision processes, states
- **4.** objects, states

> [!TIP]
> **Correct answer: 3. Markov decision processes, states**

## Solution

Reinforcement learning is commonly formalized as a Markov decision process (MDP). An MDP describes states, actions, transition behaviour, rewards and a discount or horizon model. In the stated starting situation, the agent knows the possible states and actions and must learn useful behaviour from reward-bearing interaction. The blanks are therefore 'Markov decision processes' and 'states'.

## Key Points

- An RL agent selects actions in states and learns from rewards; the standard mathematical framework is an MDP.

## Why the other options are incorrect

Objects are not the basic MDP alternative to actions, so options 1, 2 and 4 fail the second blank. 'Hidden states' points toward partial observability but does not name the standard formalism requested here.
