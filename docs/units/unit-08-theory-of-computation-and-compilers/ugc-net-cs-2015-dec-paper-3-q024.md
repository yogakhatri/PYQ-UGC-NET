# Question 24

*UGC NET CS · 2015 Dec Paper 3 · Context-Free Language · Ambiguity and Parse-Tree Counting*

For the grammar S→aS | Sa | a, how many different parse trees generate the word a³?

- **1.** Two
- **2.** Three
- **3.** Four
- **4.** Five

> [!TIP]
> **Correct answer: 3. Four**

## Solution

First note that `aa` has two parse trees: S→aS→aa and S→Sa→aa. To generate `aaa`, the root can use S→aS and the remaining S can use either `aa` tree, giving two trees; or the root can use S→Sa and its child S can use either `aa` tree, giving two more. Total=2+2=4 distinct parse trees.

## Key Points

- Count parse trees by conditioning on the root production, then recurse on the remaining nonterminal.

## Why the other options are incorrect

Two counts only one root-production family. Three misses one symmetric derivation, and five adds a structure not licensed by the grammar. Different left/right derivations count because their parse-tree shapes differ.
