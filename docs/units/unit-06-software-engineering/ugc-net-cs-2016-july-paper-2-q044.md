# Question 44

*UGC NET CS · 2016 July Paper 2 · Software Testing · Cyclomatic Complexity from Predicate Nodes*

The cyclomatic complexity of a flow graph V(G), in terms of predicate nodes is :

- **1.** P+1
- **2.** P–1
- **3.** P–2
- **4.** P+2

> [!TIP]
> **Correct answer: 1. P+1**

## Solution

For a connected control-flow graph, cyclomatic complexity equals the number of independent paths. Each binary predicate introduces one additional branch and therefore one additional independent path beyond the initial path. With P predicate nodes, V(G)=P+1, so option 1 is correct.

## Key Points

- For connected structured flow graphs with binary decisions, cyclomatic complexity V(G)=P+1.

## Why the other options are incorrect

Subtracting 1 or 2 would make complexity too small—for example, a graph with no predicate would incorrectly have negative complexity. P+2 adds an extra path without a corresponding decision. The baseline for straight-line connected code is 1.
