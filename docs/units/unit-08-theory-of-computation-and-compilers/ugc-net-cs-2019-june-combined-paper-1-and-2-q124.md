# Question 124

*UGC NET CS · 2019 June Paper 1 And 2 · Syntax Analysis · Shift-Reduce Parsing*

A shift-reduce parser consists of: (a) input buffer; (b) stack; (c) parse table. Choose the correct combination.

- **1.** (a) and (b) only
- **2.** (a) and (c) only
- **3.** (c) only
- **4.** (a), (b) and (c)

> [!TIP]
> **Correct answer: 4. (a), (b) and (c)**

## Solution

A shift-reduce parser needs an input buffer holding the unread tokens, a stack holding grammar symbols and states, and a parsing table that selects shift, reduce, accept or error actions from the current state and lookahead. Consequently all three listed components are required.

## Key Points

- Bottom-up LR-style parsing combines input, a stack and an action/goto parse table.

## Why the other options are incorrect

Options 1-3 each omit at least one essential component. Without the stack the parser cannot maintain viable prefixes; without the input buffer it lacks lookahead; without the table it cannot choose parser actions.
