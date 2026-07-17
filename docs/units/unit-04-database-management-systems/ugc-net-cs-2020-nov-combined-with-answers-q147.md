# Question 147

*UGC NET CS · 2020 Nov With Answers · SQL · Aggregate Functions and Join Conditions*

To find the sum, maximum, minimum, and average salary of employees in the ENGLISH department, evaluate these queries. Statement I: SELECT SUM(SALARY), MAX(SALARY), MIN(SALARY), AVG(SALARY) FROM EMPLOYEE, DEPARTMENT WHERE DEPTNO=DID AND DNAME='ENGLISH'; Statement II: SELECT SUM(SALARY), MAX(SALARY), MIN(SALARY), AVG(SALARY) FROM EMPLOYEE, DEPARTMENT WHERE DNAME='ENGLISH';

- **1.** Both Statement I and Statement Il are true
- **2.** Both Statement I and Statement II are false
- **3.** Statement I is correct but Statement II is false
- **4.** Statement I is incorrect but Statement Il is true

> [!TIP]
> **Correct answer: 3. Statement I is correct but Statement II is false**

## Solution

Statement I joins EMPLOYEE.DEPTNO to DEPARTMENT.DID and then keeps the row whose department name is ENGLISH. Its four aggregate functions therefore summarize exactly the English-department employees. Statement II filters DEPARTMENT to ENGLISH but never joins it to EMPLOYEE. The comma-separated FROM then forms a Cartesian product; since DNAME is unique, the English row is paired with every employee, so the aggregates cover all employees rather than only the English department. Statement I is correct and Statement II false: option 3.

## Key Points

- With old-style comma joins, an explicit equality condition is essential; otherwise the result is a Cartesian product.

## Why the other options are incorrect

Options 1 and 4 accept the query with the missing join condition, while option 2 rejects the correctly joined query. A WHERE predicate on one table does not automatically connect it to another table in FROM.
