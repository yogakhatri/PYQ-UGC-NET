# Question 19

*UGC NET CS · 2015 Dec Paper 2 · Database Indexing · Indexes and Query Access*

Data which improves the performance and accessibility of the database are called :

- **1.** Indexes
- **2.** User Data
- **3.** Application Metadata
- **4.** Data Dictionary

> [!TIP]
> **Correct answer: 1. Indexes**

## Solution

An index is an auxiliary access structure—commonly a B-tree or hash index—that maps search-key values to row locations. It can avoid scanning the whole relation and can also support ordered access, thereby improving query performance and accessibility. Hence the described data structures are indexes.

## Key Points

- Indexes trade extra storage and update cost for faster data access.

## Why the other options are incorrect

User data is the primary stored content. Application metadata describes an application, and a data dictionary describes database objects. Neither is primarily an access path for speeding row retrieval.
