# Question 90

*UGC NET CS · 2018 Dec Paper 1 And 2 · Syntax Analysis · Ambiguity and Predictive Parsing*

The grammar S→(S) | SS | ε is not suitable for predictive parsing because the grammar is:

- **1.** Right recursive
- **2.** Left recursive
- **3.** Ambiguous
- **4.** An operator grammar

> [!TIP]
> **Correct answer: The printed question has two valid choices: option 2 (left recursive) and option 3 (ambiguous).**

## Solution

The grammar is directly left recursive because S→SS has S as the leftmost symbol on its right-hand side. It is also ambiguous. For example, concatenations of balanced groups can be split through S→SS in more than one way, and ε introduces still more parse trees; `()()` has distinct derivation structures. Either property prevents this grammar from being an LL(1) predictive grammar. Therefore a single-answer question cannot uniquely choose between options 2 and 3.

## Key Points

- Predictive grammars must be unambiguous and free of left recursion; always test both when a production starts with its own left-hand nonterminal.

## Why the other options are incorrect

Right recursion is not the relevant diagnosis, and the grammar is not an operator grammar because it has adjacent nonterminals in S→SS and an ε-production. Although many answer keys select ‘ambiguous,’ ‘left recursive’ is independently and literally true.
