# Question 70

*UGC NET CS · 2019 Dec Paper 1 And 2 · Query Processing and Optimization · Role of the Query Optimizer*

Which of the component module of DBMS does rearrangement and possible ordering of operations, eliminate redundancy in query and use efficient algorithms and indexes during the exceution of a query?

- **1.** query compiler
- **2.** query optimizer
- **3.** Stored data manager
- **4.** Database processor

> [!TIP]
> **Correct answer: 2. query optimizer**

## Solution

The query optimizer transforms a logical query into an efficient execution plan. It can reorder joins and other operations, remove redundant work, choose access paths such as indexes, and select physical algorithms using estimated costs. These are exactly the tasks described, so option 2 is correct.

## Key Points

- The optimizer decides how to execute a query; the execution/storage components carry out that chosen plan.

## Why the other options are incorrect

A query compiler/parser checks and translates the query but optimization is the component responsible for plan alternatives and cost choices. The stored-data manager carries out low-level data access. ‘Database processor’ is a broad, non-specific label rather than the module performing the listed optimizations.
