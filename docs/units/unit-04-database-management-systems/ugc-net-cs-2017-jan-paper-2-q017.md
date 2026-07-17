# Question 17

*UGC NET CS · 2017 Jan Paper 2 · Data Modeling · Entity-Integrity and Uniqueness Constraints*

Integrity constraints ensure that changes made to the database by authorized users do not result into loss of data consistency. Which of the following statement(s) is (are) true w.r.t. the examples of integrity constraints ? (A) An instructor Id. No. cannot be null, provided Intructor Id No. being primary key. (B) No two citizens have same Adhar-Id. (C) Budget of a company must be zero.

- **1.** (A), (B) and (C) are true.
- **2.** (A) false, (B) and (C) are true.
- **3.** (A) and (B) are true; (C) false.
- **4.** (A), (B) and (C) are false.

> [!TIP]
> **Correct answer: 3. (A) and (B) are true; (C) false.**

## Solution

A primary-key column is subject to entity integrity, so an instructor identifier chosen as the primary key cannot be NULL; A is true. Aadhaar ID is intended to identify one citizen uniquely, so a uniqueness constraint expresses B; B is true. There is no general database-integrity rule that a company's budget must equal zero; a sensible domain rule might require it to be nonnegative instead. Thus C is false and option 3 is correct.

## Key Points

- Primary key means unique and not NULL; other domain constraints must reflect a valid business rule rather than an arbitrary value.

## Why the other options are incorrect

Options 1 and 2 incorrectly accept C. Option 2 also rejects the NOT NULL property of a primary key. Option 4 rejects both standard key constraints.
