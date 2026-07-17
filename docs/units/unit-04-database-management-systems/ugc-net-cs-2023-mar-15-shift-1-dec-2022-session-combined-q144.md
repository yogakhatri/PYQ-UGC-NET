# Question 144

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Database System Concepts and Architecture · Database Languages and Interfaces*

S.ID:87094 Use the following schema of the academic institution relational database: student (rollno, name, degree, year, sex, deptno, advisor) department (deptid, name, hod, phone) professor (empid, name, sex, startyear, deptno, phone) course (courseid, cname, credits, deptno) enrollment (rollno, courseid, sem, year, grade) teaching (empid, courseid, sem, year, classroom) prerequisite (precourseid courseid) deptno is foreign key in the student, professor and course relations referring to deptid of department relation; advisor is a foreign key in the student relation referring to empid of professor relation; hod is a foreign key in the department relation referring to empid of professor relation; rollno is a foreign key in the enrollment relation referring to rollno of student relation; courseid is a foreign key in the enrollment, teaching relations referring to courseid of course relation; empid is a foreign key of the teaching relation referring to empid of professor relation; precourseid and courseid are foreign keys in the prerequisite relation referring to courseid of the course relation; Which of the following queries would retrieve the dept id and name of all the departments that are such that the total of the credits of all the offered courses by the department is strictly greater than 40?

- **1.** select deptid, name, sum(credits) as totalcredits from department, course where totalcredits ≥ 40 group by deptid, name having deptid = deptno
- **2.** select deptid, name, sum(credits) as totalcredits from department, course where deptid = deptno and totalcredits > 40 group by deptid, name
- **3.** select deptid, name, sum(credits) as totalcredits from department, course group by deptid, name having deptid = deptno and totalcredits > 40
- **4.** select deptid, name, sum (credits) as totalcredits from department, course where deptid = deptno group by deptid, name having totalcredits > 40

> [!TIP]
> **Correct answer: 4. select deptid, name, sum (credits) as totalcredits from department, course where deptid = deptno group by deptid, name having totalcredits > 40**

## Solution

The department-course join belongs in WHERE, rows are then grouped by department, and the condition on the aggregate total belongs in HAVING. Option 4 has this logical SQL order and filters groups whose SUM(credits), aliased totalcredits, is greater than 40.

## Key Points

- WHERE filters rows before grouping; HAVING filters groups after aggregation.

## Why the other options are incorrect

Options 1 and 2 try to use an aggregate result in WHERE. Option 3 delays the ordinary join predicate until HAVING and groups a Cartesian product. Although alias use in HAVING varies by SQL dialect, option 4 is clearly the intended query.
