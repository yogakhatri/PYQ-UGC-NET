# Question 8

*UGC NET CS · 2015 June Paper 3 · SQL · GROUP BY, HAVING, and Scalar Subqueries*

STUDENT information is stored as STUDENT(Name, SEX, Marks, DEPT_Name). What does the query `SELECT DEPT_Name FROM STUDENT WHERE SEX = 'M' GROUP BY DEPT_Name HAVING AVG(Marks) > (SELECT AVG(Marks) FROM STUDENT)` return?

- **1.** The Average marks of Male students is more than the average marks of students in the same Department
- **2.** The average marks of male students is more than the average marks of students in the University
- **3.** The average marks of male students is more than the average marks of male students in the University
- **4.** The average marks of students is more than the average marks of male students in the University

> [!TIP]
> **Correct answer: 2. The average marks of male students is more than the average marks of students in the University**

## Solution

`WHERE SEX='M'` filters the outer query to male students before grouping. `GROUP BY DEPT_Name` forms one male-student group per department, and the outer `AVG(Marks)` is therefore that department's male average. The scalar subquery has no sex or department filter, so it computes the average marks of all students in the university. `HAVING` keeps departments whose male average exceeds that university-wide average.

## Key Points

- Outer filters affect only the outer aggregate; an uncorrelated scalar subquery computes its own independent global aggregate.

## Why the other options are incorrect

Option 1 incorrectly treats the subquery as department-specific. Option 3 incorrectly applies the male filter to the subquery. Option 4 reverses which average belongs on each side of the comparison.
