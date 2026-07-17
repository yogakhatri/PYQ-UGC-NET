# Question 33

*UGC NET CS · 2015 June Paper 2 · Formal Languages and Grammars · Context-Free Production Rules*

If all the production rules have single non - terminal symbol on the left side, the grammar defined is :

- **1.** context free grammar
- **2.** context sensitive grammar
- **3.** unrestricted grammar
- **4.** phrase grammar

> [!TIP]
> **Correct answer: 1. context free grammar**

## Solution

A context-free grammar requires every production to have the form `A → α`, where the left side is exactly one nonterminal and the right side is any string of terminals and nonterminals. The condition in the question is precisely this defining restriction, so the grammar is context-free.

## Key Points

- One nonterminal alone on every production's left side characterizes a context-free grammar.

## Why the other options are incorrect

A context-sensitive grammar has the more general contextual form and also imposes a noncontracting condition. An unrestricted grammar permits a broader left side containing at least one nonterminal. `Phrase grammar` is a broad informal label, not the specific class defined by a single nonterminal on every left side.
