# Question 17

*UGC NET CS · 2016 July Paper 2 · Database System Concepts and Architecture · Centralized and Client/Server DBMS Architectures*

Which of the following statement(s) is/are FALSE in the context of Relational DBMS ? I. Views in a database system are important because they help with access control by allowing users to see only a particular subset of the data in the database. II. E-R diagrams are useful to logically model concepts. III. An update anomaly is when it is not possible to store information unless some other, unrelated information is stored as well. IV. SQL is a procedural language.

- **1.** I and IV only
- **2.** III and IV only
- **3.** I, II and III only
- **4.** II, III and IV only

> [!TIP]
> **Correct answer: 2. III and IV only**

## Solution

Statements III and IV are false. III actually defines an insertion anomaly: a fact cannot be inserted without also inserting unrelated data. An update anomaly occurs when the same fact is duplicated and must be changed in several rows, risking inconsistency. IV is false because ordinary SQL is declarative/nonprocedural: a query states the desired result, while the DBMS chooses an execution plan.

## Key Points

- Insertion anomaly blocks independent insertion; update anomaly requires repeated synchronized changes; SQL states what, not how.

## Why the other options are incorrect

Statement I is true because a view can expose selected rows/columns while hiding base data. Statement II is acceptable: ER diagrams model entities, attributes, and relationships at the conceptual/logical design stage. Therefore answer codes containing I or II as false are incorrect.
