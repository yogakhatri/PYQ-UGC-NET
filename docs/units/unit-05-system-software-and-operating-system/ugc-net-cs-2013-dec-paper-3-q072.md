# Question 72

*UGC NET CS · 2013 Dec Paper 3 · File and Input/Output Systems · Unix Tree-Structured Directory*

The directory structure used in Unix file system is called

- **A.** Hierarchical directory
- **B.** Tree structured directory
- **C.** Directed acyclic graph
- **D.** Graph structured directory

> [!TIP]
> **Correct answer: Intended answer: B, tree-structured directory. 'Hierarchical directory' in A is also a descriptive synonym, so the wording is not perfectly discriminating.**

## Solution

The traditional UNIX namespace starts at one root directory, '/', and every ordinary file or directory has a path descending through parent directories. In operating-system directory classifications this is called a tree-structured directory. The term hierarchical also describes that same parent-child organization, which is why option A sounds true; B is the formal category the question is asking for.

## Key Points

- Tree structure means one root and one parent path for each node; links can make the full UNIX namespace more graph-like in practice.

## Why the other options are incorrect

A is not conceptually false, but it is a general description rather than the conventional classification intended by the options. A directed-acyclic-graph directory permits shared files/subdirectories with multiple parents, and a general graph may contain cycles; neither is the basic tree model named here.
