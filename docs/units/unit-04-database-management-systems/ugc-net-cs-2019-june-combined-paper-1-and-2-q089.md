# Question 89

*UGC NET CS · 2019 June Paper 1 And 2 · Data Modeling · Cascading foreign keys*

A table has attributes Employee_id and Manager_id. Employee_id is the primary key and Manager_id is a foreign key referencing Employee_id with ON DELETE CASCADE. Its tuples are (20,40), (25,40), (30,35), (35,20), (40,45), (45,25). On deleting tuple (20,40), which other tuples must be deleted to maintain referential integrity?

- **1.** (30,35) only
- **2.** (30,35) and (35,20) only
- **3.** (35,20) only
- **4.** (40,45) and (25,40) only

> [!TIP]
> **Correct answer: 2. (30,35) and (35,20) only**

## Solution

Deleting employee 20 activates ON DELETE CASCADE for every row whose Manager_id is 20, so tuple (35,20) is deleted. That deletion then cascades again because employee 30 references manager 35, deleting (30,35). No listed tuple references employee 30, so the chain stops. The additional deleted tuples are therefore (35,20) and (30,35).

## Key Points

- A cascading self-referential foreign key must be followed recursively through every dependent row.

## Why the other options are incorrect

- **Option 1:** misses the direct deletion of employee 35.
- **Option 3:** misses the second-level cascade to employee 30.
- **Option 4:** those rows reference manager 40 and are not dependents of employee 20.
