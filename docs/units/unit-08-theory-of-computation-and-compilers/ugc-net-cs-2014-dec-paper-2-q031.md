# Question 31

*UGC NET CS · 2014 Dec Paper 2 · Parsing and Syntax Analysis · Shift-Reduce Operations*

Shift-Reduce parsers perform the following :

- **A.** Shift step that advances in the input stream by K(K > 1) s ymbols and Reduce step that applies a completed grammar rule to some recent parse tree s, joining them together as one tree with a new root symbol.
- **B.** Shift step that advances in the input stream by one symbol and Reduce step that applies a completed grammar rule to some recent parse trees, joining them together as one tree with a new root symbol.
- **C.** Shift step that advances in the input stream by K(K = 2) s ymbols and Reduce step that applies a completed grammar rule to form a single tree.
- **D.** Shift step that does not advance in the input stream and Reduce s tep that applies a completed grammar rule to form a single tree.

> [!TIP]
> **Correct answer: B. Shift step that advances in the input stream by one symbol and Reduce step that applies a completed grammar rule to some recent parse trees, joining them together as one tree with a new root symbol.**

## Solution

A shift action consumes exactly one next input symbol and pushes the corresponding state/symbol information onto the parser stack. A reduce action recognizes a handle matching the right side of a completed production, removes the handle's parse fragments and replaces them with their left-side nonterminal, forming one tree with a new root. Option B states both operations correctly.

## Key Points

- Shift consumes one terminal; reduce replaces a recognized right-hand side by its production's left-hand nonterminal.

## Why the other options are incorrect

A and C incorrectly say one shift consumes multiple input symbols. D says shifting does not advance input at all. A reduction may combine several recent trees, so the more complete description in B is also preferable to C and D.
