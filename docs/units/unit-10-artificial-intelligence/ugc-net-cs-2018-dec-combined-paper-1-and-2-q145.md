# Question 145

*UGC NET CS · 2018 Dec Paper 1 And 2 · Informed Search Strategies · Admissible and Consistent Heuristics*

Consider S1: A heuristic is admissible if it never overestimates the cost to reach the goal. S2: A heuristic is monotone if it satisfies the triangle-inequality property. Which is true?

- **1.** Neither S1 nor S2
- **2.** S1 is false but S2 is true
- **3.** S1 is true but S2 is false
- **4.** Both S1 and S2 are true

> [!TIP]
> **Correct answer: 4. Both S1 and S2 are true**

## Solution

S1 is the definition of admissibility: h(n) must be a lower bound on the true remaining cost h*(n), so h(n)≤h*(n). S2 is also true. A monotone, or consistent, heuristic satisfies h(n)≤c(n,n')+h(n') for every successor n'; this is a triangle-inequality condition. Therefore both statements are true, option 4.

## Key Points

- Admissible: never overestimate the goal cost.
- Consistent: estimated cost obeys a triangle inequality across every edge.

## Why the other options are incorrect

Options 1–3 require at least one false statement, but both are standard definitions. Do not confuse admissibility with consistency: consistency is the stronger local edge condition and, with h(goal)=0, implies admissibility; their distinction does not make either statement false.
