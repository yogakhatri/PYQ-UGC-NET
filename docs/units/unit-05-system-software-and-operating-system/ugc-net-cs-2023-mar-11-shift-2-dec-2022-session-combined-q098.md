# Question 98

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · File and Input/Output Systems · Transforming Requests to Hardware Operations*

What are the drawbacks of using file systems to store data? A. Data inconsistency B. Difficulty in accessing data C. Data isolation D. Atomicity of updates Choose the correct answer from the options given below:

- **1.** A. B. only
- **2.** B. C, D only
- **3.** A, B, C only
- **4.** A. B, C, D

> [!TIP]
> **Correct answer: 4. A. B, C, D**

## Solution

Traditional application-managed files commonly produce redundant inconsistent data, awkward access logic, isolated incompatible files, and difficulty guaranteeing that a multi-step update is atomic. A DBMS is designed to address all four problems.

## Key Points

- Core DBMS motivations include controlled redundancy, data independence, integrated access, and transaction guarantees.

## Why the other options are incorrect

Options 1–3 omit one or more genuine file-system drawbacks, especially isolation or failure atomicity.
