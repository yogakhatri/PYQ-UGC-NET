# Question 99

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Normalization for Relational Databases · Object and Object-Relational Databases*

Which of the following database model, we have a parent-child relationship? A. hierarchical databases B. network databases C. relational databases Choose the correct answer from the options below:

- **1.** A, B
- **2.** A, C
- **3.** B. C
- **4.** A, B, C

> [!TIP]
> **Correct answer: 1. A, B**

## Solution

The hierarchical model explicitly organizes records as a parent-child tree. The network model generalizes this using owner-member (parent-child-like) set relationships and permits a record to participate in multiple such sets. The relational model instead represents associations through keys and joins. Thus A and B apply.

## Key Points

- Hierarchical and network databases are navigational; relational databases connect tables through values and keys.

## Why the other options are incorrect

Any option containing C treats the relational model as a navigational parent-child model, which it is not.
