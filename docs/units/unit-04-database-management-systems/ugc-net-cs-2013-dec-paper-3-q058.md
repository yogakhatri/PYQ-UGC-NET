# Question 58

*UGC NET CS · 2013 Dec Paper 3 · SQL · EXISTS, ANY and Greatest-per-Group Queries*

Consider Student(stuid, name, course, marks). Which query correctly finds the student with the highest marks in course 5? Q1: SELECT S.stuid FROM Student S WHERE NOT EXISTS (SELECT * FROM Student e WHERE e.course='5' AND e.marks >= S.marks). Q2: SELECT S.stuid FROM Student S WHERE S.marks > ANY (SELECT DISTINCT marks FROM Student T WHERE T.course=5).

- **A.** Q. 1
- **B.** Q. 2
- **C.** Both Q. 1 and Q. 2
- **D.** Neither Q. 1 nor Q. 2

> [!TIP]
> **Correct answer: D. Neither Q. 1 nor Q. 2**

## Solution

Neither query finds the requested row as written. Q1 rejects any candidate S whenever a course-5 row e has e.marks>=S.marks. A maximum course-5 student rejects itself because equality satisfies >=; a student outside course 5 with marks above every course-5 mark could instead pass. Q2 uses >ANY, which means greater than at least one value, not greater than or equal to every value, and it also does not restrict the outer S row to course 5. A correct pattern is SELECT stuid FROM Student WHERE course=5 AND marks=(SELECT MAX(marks) FROM Student WHERE course=5).

## Key Points

- For a group maximum, compare with MAX(...) or use NOT EXISTS with a strictly greater competitor and the same group condition.

## Why the other options are incorrect

A is wrong because Q1's >= makes even the maximum fail and its outer query is unfiltered. B is wrong because >ANY can return many nonmaximum students and the outer query is unfiltered. Since neither is correct, C is also false.
