# Question 131

*UGC NET CS · 2018 Dec Paper 1 And 2 · Data Warehousing and Data Mining · ETL Data Scrubbing*

Data scrubbing is:

- **1.** a process to reject data from the data warehouse and create necessary indexes
- **2.** a process to load data into the data warehouse and create necessary indexes
- **3.** a process to upgrade the quality of data after it is moved into a data warehouse
- **4.** a process to upgrade the quality of data before it is moved into a data warehouse

> [!TIP]
> **Correct answer: 4. a process to upgrade the quality of data before it is moved into a data warehouse**

## Solution

Data scrubbing (data cleansing) detects and repairs problems such as invalid formats, inconsistent codes, duplicates, missing values, and impossible values. In the warehouse ETL pipeline it is normally performed during extraction/transformation before the cleaned data is loaded into the warehouse. Thus option 4 is correct.

## Key Points

- ETL order: extract source data, transform/clean it, then load trusted data into the warehouse.

## Why the other options are incorrect

Rejecting data or creating indexes is not the definition of scrubbing, eliminating option 1. Loading and indexing are load-phase tasks, not cleansing, so option 2 fails. Cleaning only after warehouse loading, as option 3 says, would let poor-quality data enter analytical tables; although later corrections can occur, the intended ETL step precedes loading.
