# Question 8

*UGC NET CS · 2013 June Paper 3 · SQL · GROUP BY, HAVING and Scalar Subqueries*

Employee information is stored as Employee(name, sex, salary, deptname). What does this query return? SELECT deptname FROM Employee WHERE sex='M' GROUP BY deptname HAVING AVG(salary) > (SELECT AVG(salary) FROM Employee);

- **A.** Average salary of employee more than average salary of the organization.
- **B.** Average salary less than average salary of the organization.
- **C.** Average salary of employee equal to average salary of the organization.
- **D.** Average salary of male employees in a department is more than average salary of the organization.

> [!TIP]
> **Correct answer: D. Average salary of male employees in a department is more than average salary of the organization.**

## Solution

WHERE sex='M' first restricts rows to male employees. GROUP BY deptname then forms one male-employee group per department. HAVING compares each group's AVG(salary) with the scalar subquery's AVG(salary), which is computed over every employee in the organization. The query outputs department names whose male employees' average salary exceeds the overall organizational average.

## Key Points

- SQL evaluation cue: WHERE filters rows, GROUP BY forms groups, HAVING filters groups, and the uncorrelated subquery supplies one global average.

## Why the other options are incorrect

A omits both the male filter and department grouping. B reverses the > condition. C changes > to equality. D alone includes all three essential details: male employees, per-department average and comparison with the organization-wide average.
