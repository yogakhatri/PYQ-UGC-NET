# Question 39

*UGC NET CS · 2018 July Paper 2 · Syntax Analysis · Bottom-Up Parsing and Reversed Rightmost Derivations*

A bottom-up parser generates :

- **1.** Left-most derivation in reverse
- **2.** Right-most derivation in reverse
- **3.** Left-most derivation
- **4.** Right-most derivation

> [!TIP]
> **Correct answer: 2. Right-most derivation in reverse**

## Solution

A bottom-up parser starts from the input string and repeatedly reduces handles until it reaches the start symbol. Those reductions undo the productions of a rightmost derivation in the reverse order. Hence it generates a rightmost derivation in reverse, option 2.

## Key Points

- LR means scan Left-to-right and construct a Rightmost derivation in reverse.

## Why the other options are incorrect

Options 3 and 4 give forward derivations even though bottom-up parsing reduces input toward the root. Option 1 names the derivation associated with top-down LL parsing, not shift-reduce/LR parsing.
