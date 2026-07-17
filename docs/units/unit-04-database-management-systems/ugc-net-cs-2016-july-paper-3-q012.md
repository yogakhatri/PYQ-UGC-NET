# Question 12

*UGC NET CS · 2016 July Paper 3 · Distributed Databases · Semijoin Query-Processing Strategy*

Semi-join strategies are techniques for query processing in distributed database system. Which of the following is a semi-join technique ?

- **1.** Only the joining attributes are sent from one site to another and then all of the rows are returned.
- **2.** All of the attributes are sent from one site to another and then only the required rows are returned.
- **3.** Only the joining attributes are sent from one site to another and then only the required rows are returned.
- **4.** All of the attributes are sent from one site to another and then only the required rows are returned.

> [!TIP]
> **Correct answer: 3. Only the joining attributes are sent from one site to another and then only the required rows are returned.**

## Solution

A distributed semijoin reduces communication by first projecting and sending only join-attribute values to the remote site. Those values identify matching tuples, and only the required matching rows are sent back. This is exactly option 3.

## Key Points

- Semijoin reduction sends join keys outward and returns only matching rows, minimizing network transfer.

## Why the other options are incorrect

Option 1 sends all rows back and loses the main communication-saving benefit. Options 2 and 4 send all attributes to the other site before filtering; they are identical in the source and are not semijoin reduction. An old key listing option 1 conflicts with the standard semijoin algorithm.
