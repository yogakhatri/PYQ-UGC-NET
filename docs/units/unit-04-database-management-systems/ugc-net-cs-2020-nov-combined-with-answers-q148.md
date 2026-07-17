# Question 148

*UGC NET CS · 2020 Nov With Answers · SQL · ALL Quantifier and Multirow Subqueries*

Which query returns the EID and NAME of employees whose salary is greater than the salary of every employee in department 20, ordered by EID? A. SELECT EID, NAME FROM EMPLOYEE WHERE SALARY>(SELECT SALARY FROM EMPLOYEE WHERE DEPTNO=20) ORDER BY EID; B. SELECT EID, NAME FROM EMPLOYEE WHERE SALARY>(SELECT SALARY FROM EMPLOYEE WHERE DEPTNO=20); C. SELECT EID, NAME FROM EMPLOYEE WHERE SALARY>ALL(SELECT SALARY FROM EMPLOYEE WHERE DEPTNO=20) ORDER BY EID;

- **1.** (A) and (B) only
- **2.** (A) and (C) only
- **3.** (B) only
- **4.** (C) only

> [!TIP]
> **Correct answer: 4. (C) only**

## Solution

The requirement is salary greater than every salary returned for department 20. SQL expresses that universal comparison as SALARY > ALL (subquery), and query C also includes the required ORDER BY EID. Queries A and B compare a scalar value with a subquery that can return many rows—one per department-20 employee—so they fail with a multirow scalar-subquery error in the general case. Only C is correct, giving option 4.

## Key Points

- Use >ALL(subquery) for 'greater than every returned value'; a bare scalar comparison requires the subquery to return at most one row.

## Why the other options are incorrect

Options 1 and 2 include A, and option 3 includes B; neither scalar comparison represents a general multirow 'greater than all' test. B additionally omits the required ordering.
