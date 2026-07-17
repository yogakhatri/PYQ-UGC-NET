# Question 62

*UGC NET CS · 2018 July Paper 2 · SQL · Correlated Subqueries and Ranking*

Consider a relation book(title, price) containing book titles and prices, with no two books having the same price. What does this SQL query list? SELECT title FROM book AS B WHERE (SELECT COUNT(*) FROM book AS T WHERE T.price > B.price) < 7

- **1.** Titles of the six most expensive books.
- **2.** Title of the sixth most expensive books.
- **3.** Titles of the seven most expensive books.
- **4.** Title of the seventh most expensive books.

> [!TIP]
> **Correct answer: 3. Titles of the seven most expensive books.**

## Solution

For each candidate book B, the correlated subquery counts books T with a strictly greater price. With distinct prices, the most expensive book has count 0, the second has count 1, and the seventh has count 6. The condition count<7 therefore accepts ranks 1 through 7. The query lists the titles of the seven most expensive books, option 3.

## Key Points

- When prices are unique, `COUNT(prices greater than B.price)+1` is B's descending rank.

## Why the other options are incorrect

The strict inequality is applied to the number of more-expensive books, not directly to the rank. Counts 0–6 give seven rows, not six. The query is not restricted to a single sixth- or seventh-ranked row.
