# Question 150

*UGC NET CS · 2020 Nov With Answers · SQL · UPDATE with a Filtering Subquery*

The university gives every employee in the SCIENCE department a 20% salary rise. Which query or queries compute the result? A. UPDATE EMPLOYEE SET SALARY=SALARY*1.20 WHERE DEPTNO IN (SELECT DID FROM DEPARTMENT WHERE DNAME='SCIENCE'); B. UPDATE TABLE EMPLOYEE SET SALARY=SALARY*1.20 WHERE DNAME='SCIENCE'; C. ALTER TABLE EMPLOYEE SET SALARY=SALARY-1.20 WHERE DEPTNO IN (SELECT DNAME FROM DEPARTMENT WHERE DNAME='SCIENCE').

- **1.** A and B only
- **2.** A only
- **3.** B and C only
- **4.** C only

> [!TIP]
> **Correct answer: 2. A only**

## Solution

Query A is valid DML: it identifies the DID of the SCIENCE department, selects employees whose DEPTNO matches it, and replaces each salary by 1.20 times its current value. Query B is invalid because SQL uses UPDATE EMPLOYEE, not UPDATE TABLE EMPLOYEE, and DNAME is not an EMPLOYEE column. Query C uses ALTER TABLE, which changes a schema rather than row values; it also compares numeric DEPTNO with DNAME and subtracts 1.20 instead of granting a 20% rise. Thus A only is correct, option 2.

## Key Points

- Use UPDATE…SET for data changes; use a subquery to translate the department name into the department key stored in EMPLOYEE.

## Why the other options are incorrect

Option 1 includes invalid B, while options 3 and 4 include invalid C. A salary increase is a row update, not a table-alteration operation.
