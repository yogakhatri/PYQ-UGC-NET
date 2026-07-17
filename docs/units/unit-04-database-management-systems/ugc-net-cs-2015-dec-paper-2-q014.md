# Question 14

*UGC NET CS · 2015 Dec Paper 2 · Database System Concepts · Normalization, Metadata, Integrity and External Schemas*

Match the following database terms to their functions : List - I List - II (a) Normalization (i) Enforces match of primary key to foreign key (b) Data Dictionary (ii) Reduces data redundancy in a database (c) Referential Integrity (iii) Defines view(s) of the database for particular user(s) (d) External Schema (iv) Contains metadata describing database structure Codes : (a) (b) (c) (d)

- **1.** (iv) (iii) (i) (ii)
- **2.** (ii) (iv) (i) (iii)
- **3.** (ii) (iv) (iii) (i)
- **4.** (iv) (iii) (ii) (i)

> [!TIP]
> **Correct answer: 2. (ii) (iv) (i) (iii)**

## Solution

Normalization restructures relations to reduce redundancy, so (a)–(ii). A data dictionary stores metadata describing database objects, so (b)–(iv). Referential integrity ensures that a foreign-key value matches an existing referenced primary key (or is null when permitted), so (c)–(i). An external schema defines database views for particular users or groups, so (d)–(iii). The sequence is (ii),(iv),(i),(iii).

## Key Points

- Normalization reduces redundancy, the dictionary stores metadata, referential integrity links keys, and external schemas expose user views.

## Why the other options are incorrect

The other codes confuse user views with metadata, redundancy reduction, or key consistency. Keep the levels separate: external schema is user-facing; the data dictionary describes the database itself.
