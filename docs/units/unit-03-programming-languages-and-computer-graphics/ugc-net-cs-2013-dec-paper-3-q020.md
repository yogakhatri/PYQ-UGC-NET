# Question 20

*UGC NET CS · 2013 Dec Paper 3 · Logic Programming in Prolog · Unification and Backtracking Strategies*

Match the following control strategies of prolog : List – I List – II a. Forward movement i. Variable can be done with a constant, another variable or a function. b. Unifica- tion ii. The entire conjunctive goal is executed. c. Deep back- tracking iii. Previous sub goal to find alternative solutions. d. Shallow back- tracking iv. Chooses sub goal with possible unifier. Codes : a b c d

- **A.** iv i ii iii
- **B.** ii iv i iii
- **C.** iii i iv ii
- **D.** ii iii iv i

> [!TIP]
> **Correct answer: A. iv i ii iii**

## Solution

Forward movement selects a subgoal that has a possible unifier (iv). Unification binds a variable to a constant, variable or term (i). Deep backtracking restarts/reconsiders the conjunctive goal more broadly (ii), whereas shallow backtracking returns to a previous subgoal to try another solution (iii). Thus iv,i,ii,iii.

## Key Points

- Prolog uses unification for bindings and backtracking to explore alternative clauses/subgoals.

## Why the other options are incorrect

The other codes confuse unification with search movement or interchange deep and shallow backtracking. Variable binding is the direct anchor for unification.
