# Question 65

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Data Modeling · Foreign-key identification*

Consider the two relations below. The primary keys are underlined. Identify all possible foreign keys) from the options based only on the two relations. EMP (eid, ename, did DEPT (did, dname)

- **1.** eid
- **2.** did
- **3.** eid, did
- **4.** eid, did, ename

> [!TIP]
> **Correct answer: 2. did**

## Solution

DEPT.did is the primary key of DEPT. The EMP relation contains an attribute with the same role, EMP.did, which can reference DEPT.did and thereby associate each employee with a department. Thus did is the possible foreign key indicated by the two schemas.

## Key Points

- A foreign key in one relation references a candidate/primary key in another; matching names are suggestive, but the referenced key constraint is decisive.

## Why the other options are incorrect

EMP.eid identifies employees and has no matching referenced key in DEPT. The name ename is not shown as a key in either relation. Options that include eid or ename therefore add attributes unsupported as foreign keys by the given schemas.
