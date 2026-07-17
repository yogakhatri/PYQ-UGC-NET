# Question 78

*UGC NET CS · 2018 July Paper 2 · Planning · Planning Graphs and Delete Relaxation*

Consider: (a) A planning-graph data structure can provide a better heuristic for a planning problem. (b) Dropping the negative effects from every action schema produces a relaxed planning problem. Which choice is correct?

- **1.** Both sentence (a) and sentence (b) are false.
- **2.** Both sentence (a) and sentence (b) are true.
- **3.** Sentence (a) is true but sentence (b) is false.
- **4.** Sentence (a) is false but sentence (b) is true.

> [!TIP]
> **Correct answer: 2. Both sentence (a) and sentence (b) are true.**

## Solution

Statement (a) is true: a planning graph records which propositions and actions become reachable at successive levels, including mutex information, and can yield stronger planning heuristics than simple goal counts. Statement (b) is also true: removing every action's negative/delete effects makes actions interfere less and creates a relaxed planning problem whose solution cost can guide the original problem. Hence option 2.

## Key Points

- Planning graphs exploit reachability/mutex structure; delete relaxation removes negative effects to obtain an easier heuristic problem.

## Why the other options are incorrect

Options 1, 3, and 4 deny one or both standard planning techniques. The relaxed problem is easier because facts, once achieved, are never deleted; it need not be a valid executable plan for the original problem.
