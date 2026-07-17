# Question 11

*UGC NET CS · 2017 Jan Paper 3 · SQL · Correlated Subqueries and Group Averages*

Consider Works(emp_name, company_name, salary), where emp_name is the primary key. What does this correlated SQL query return? SELECT emp_name FROM Works T WHERE salary > (SELECT AVG(salary) FROM Works S WHERE T.company_name = S.company_name)

- **1.** Find the highest paid employee who earns more than the average salary of all employees of his company.
- **2.** Find the highest paid employee who earns more than the average salary of all the employees of all the companies.
- **3.** Find all employees who earn more than the average salary of all employees of all the companies.
- **4.** Find all employees who earn more than the average salary of all employees of their company.

> [!TIP]
> **Correct answer: 4. Find all employees who earn more than the average salary of all employees of their company.**

## Solution

For each outer employee row T, the correlated subquery selects rows S having the same company name and computes that company's average salary. The outer predicate retains T when T.salary is greater than that company-specific average. Since there is no `MAX`, ordering, or limiting clause, every qualifying employee is returned, not only the highest paid. Option 4 precisely describes the result.

## Key Points

- A correlated subquery is reevaluated for the current outer row; here the correlation creates a per-company average.

## Why the other options are incorrect

Options 1 and 2 incorrectly introduce 'highest paid,' which the query never computes. Options 2 and 3 use a single average across all companies, but the correlation `T.company_name = S.company_name` computes a separate average for each employee's company.
