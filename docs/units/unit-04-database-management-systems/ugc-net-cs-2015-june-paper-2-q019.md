# Question 19

*UGC NET CS · 2015 June Paper 2 · Database System Concepts and Architecture · Drawbacks of File-Based Systems*

Database applications were built directly on top of file system to overcome the following drawbacks of using file-systems : (a) Data redundancy and inconsistency (b) Difficulty in accessing Data (c) Data isolation (d) Integrity problems

- **1.** (a)
- **2.** (a) and (d)
- **3.** (a), (b) and (c)
- **4.** (a), (b), (c) and (d)

> [!TIP]
> **Correct answer: 4. (a), (b), (c) and (d)**

## Solution

Traditional file-based applications commonly duplicate the same facts in separate files, making redundancy and inconsistent copies likely. Each new query may require a special program, so ad-hoc access is difficult. Data is scattered across files and formats, creating isolation, while integrity rules are buried in application code and are hard to enforce uniformly. A DBMS was introduced to address all four listed weaknesses.

## Key Points

- DBMSs centralize data and rules to reduce redundancy, improve access, integrate isolated data, and enforce integrity.

## Why the other options are incorrect

Options 1–3 each omit at least one genuine file-system problem. Data isolation and integrity enforcement are as central to the database motivation as redundancy and access difficulty, so only the all-inclusive option is complete.
