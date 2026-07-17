# Question 58

*UGC NET CS · 2017 Jan Paper 3 · Game Playing · Heuristic Search and Evaluation*

What is the best method to go for the game playing problem ?

- **1.** Optimal Search
- **2.** Random Search
- **3.** Heuristic Search
- **4.** Stratified Search

> [!TIP]
> **Correct answer: 3. Heuristic Search**

## Solution

Game trees usually grow too rapidly to search exhaustively to terminal positions. Practical game playing therefore searches selectively to a cutoff depth and applies a heuristic evaluation function to estimate the desirability of nonterminal positions; minimax and alpha-beta pruning are commonly used around this evaluation. Among the choices, heuristic search is the appropriate method, so option 3 is correct.

## Key Points

- Large game trees require heuristic evaluation at cutoff states, usually combined with minimax/alpha-beta search.

## Why the other options are incorrect

An exact optimal search is generally infeasible for large games, random search does not use strategic information, and 'stratified search' is not the standard game-playing approach represented here.
