# Question 13

*UGC NET CS · 2015 Dec Paper 2 · SQL · LIKE Operator and Wildcards*

A CUSTOMERS table has a CITY column containing Indian city names in uppercase. Which SQL statement finds every city whose name contains the substring ‘GAR’ anywhere?

- **1.** SELECT * FROM customers WHERE city = '%GAR%';
- **2.** SELECT * FROM customers WHERE city = '$GAR$';
- **3.** SELECT * FROM customers WHERE city LIKE '%GAR%';
- **4.** SELECT * FROM customers WHERE city AS '%GAR';

> [!TIP]
> **Correct answer: 3. SELECT * FROM customers WHERE city LIKE '%GAR%';**

## Solution

SQL pattern matching uses LIKE. Within a LIKE pattern, `%` matches any sequence of zero or more characters, so `CITY LIKE '%GAR%'` accepts any value containing GAR at the beginning, middle, or end. The two percent signs allow arbitrary text on both sides.

## Key Points

- Use `LIKE '%substring%'` for a substring search in SQL.

## Why the other options are incorrect

With `=`, `%` is treated as an ordinary character rather than a wildcard pattern. `$` is not the SQL wildcard shown here. `AS` creates aliases and is not a comparison operator.
