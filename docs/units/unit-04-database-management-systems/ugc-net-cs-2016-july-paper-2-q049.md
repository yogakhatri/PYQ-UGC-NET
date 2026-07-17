# Question 49

*UGC NET CS · 2016 July Paper 2 · Data Warehousing and Data Mining · Data Scrubbing before Warehouse Loading*

Consider the following statements: (A) Data scrubbing is a process to improve data quality before data is moved into a data warehouse. (B) Data scrubbing is a process of rejecting data from a data warehouse to create indexes. Which option is correct?

- **1.** (A) is true, (B) is false.
- **2.** (A) is false, (B) is true.
- **3.** Both (A) and (B) are false.
- **4.** Both (A) and (B) are true.

> [!TIP]
> **Correct answer: 1. (A) is true, (B) is false.**

## Solution

Data scrubbing (data cleansing) detects and repairs or removes inaccurate, inconsistent, duplicate, malformed, or incomplete data. In an ETL pipeline it is performed before or during loading so the warehouse receives higher-quality data; therefore A is true. Creating indexes is a physical database-design task, not the purpose of rejecting warehouse data, so B is false.

## Key Points

- Data scrubbing improves data quality before warehouse use; indexing improves retrieval performance after storage.

## Why the other options are incorrect

Options 2 and 4 make statement B true even though indexing and cleansing are different operations. Option 3 also rejects the correct description in A. Scrubbing improves the data itself; indexing improves access paths to stored data.
