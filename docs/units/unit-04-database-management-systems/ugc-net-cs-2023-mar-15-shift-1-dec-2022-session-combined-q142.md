# Question 142

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Database System Concepts and Architecture · Database Languages and Interfaces*

No: 87092 Use the following schema of the academic institution relational database: student (rollno, name, degree, year, sex, deptno, advisor) department (deptid, name, hod, phone) professor (empid, name, sex, startyear, deptno, phone) course (courseid, chame, credits, deptno) enrollment (rollno, courseid, sem, year, grade) teaching (empid, courseid, sem, year, classroom) prerequisite (precourseid courseid) deptno is foreign key in the student, professor and course relations referring to deptid of department relation; advisor is a foreign key in the student relation referring to empid of professor relation; hod is a foreign key in the department relation referring to empid of professor relation; rollno is a foreign key in the enrollment relation referring to rollno of student relation; courseid is a foreign key in the enrollment, teaching relations referring to courseid of course relation; empid is a foreign key of the teaching relation referring to empid of professor relation; precourseid and courseid are foreign keys in the prerequisite relation referring to courseid of the course relation; Given query: select s.rollno from students where s.sex = ALL (select f.sex from professor f where fempid = s.advisor) Consider the following statements about the given query that retrieves the set of all students whose gender is same as the gender of their advisor: S1. It has a correlated subquery S2. It has an uncorrelated subquery S3. If we replace ALL by ANY in the above query, its result will be different S4. If we replace ALL by ANY in the above query, its result will be same. Identify all the statement that are TRUE:

- **1.** 51 and S3 are true
- **2.** S1 and S4 are true
- **3.** S2 and S3 are true
- **4.** S2 and S4 are true

> [!TIP]
> **Correct answer: 2. S1 and S4 are true**

## Solution

The inner query refers to s.advisor from the outer student row, so it is correlated: S1 is true and S2 false. Because advisor references the professor primary key empid, the subquery returns at most one advisor-sex value for a student. Comparing with ALL or ANY over that one value gives the same result, so S4 is true and S3 false.

## Key Points

- ALL and ANY coincide for a singleton subquery result; an outer-row reference makes a subquery correlated.

## Why the other options are incorrect

Options 1 and 3 claim the result changes, while options 3 and 4 incorrectly call the subquery uncorrelated.
