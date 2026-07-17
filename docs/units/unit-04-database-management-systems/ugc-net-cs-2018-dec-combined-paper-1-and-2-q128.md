# Question 128

*UGC NET CS · 2018 Dec Paper 1 And 2 · Data Warehousing and Data Mining · Summary Data in Warehouses*

Data warehouse contains data that is never found in operational environment.

- **1.** Summary
- **2.** Encoded
- **3.** Encrypted
- **4.** Scripted

> [!TIP]
> **Correct answer: 1. Summary**

## Solution

A data warehouse commonly stores derived and aggregated data—daily totals, monthly averages, regional summaries, and other rollups—created from detailed operational records. Such summary data may never exist as stored rows in the operational environment, whose job is transaction processing. Therefore option 1 is correct.

## Key Points

- Operational systems capture current transactions; warehouses add historical integration and summary/aggregate data for analysis.

## Why the other options are incorrect

Encoding and encryption may be applied in either operational or analytical systems and are not the distinctive warehouse-only content described. ‘Scripted data’ is not the standard warehouse category. The key contrast is detailed operational facts versus historical, integrated summaries.
