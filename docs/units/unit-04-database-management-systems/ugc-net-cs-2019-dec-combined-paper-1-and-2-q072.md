# Question 72

*UGC NET CS · 2019 Dec Paper 1 And 2 · SQL · GROUP BY and HAVING*

What does this query return? SELECT COUNT(*) AS total FROM EMPLOYEE WHERE DEPTNO IN (D1,D2) GROUP BY DEPTNO HAVING COUNT(*)>5;

- **1.** Total number of employees in each department D1 and D2
- **2.** Total number of employees of department D1 and D2 if their total is >5
- **3.** Display total number of employees in both departments D1 and D2
- **4.** The output of the query must have atleast two rows

> [!TIP]
> **Correct answer: 2. Total number of employees of department D1 and D2 if their total is >5**

## Solution

WHERE first keeps only employees in D1 or D2. GROUP BY then forms a separate group for each department, COUNT(*) counts that department's employees, and HAVING retains only a department whose count exceeds 5. Thus the result reports the employee total for each of D1 and D2 that individually has more than five employees, which is the intended meaning of option 2.

## Key Points

- WHERE filters rows before grouping; HAVING filters completed groups after aggregate values are computed.

## Why the other options are incorrect

Option 1 omits the HAVING condition. Option 3 suggests one combined total, but GROUP BY DEPTNO produces separate counts. Option 4 is false because the query may return zero, one, or two rows depending on which department groups exceed five.
