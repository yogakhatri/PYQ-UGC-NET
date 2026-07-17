# Question 145

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Database System Concepts and Architecture · Database Languages and Interfaces*

Use the following schema of the academic institution relational database: student (rollno, name, degree, year, sex, deptno, advisor) department (deptid, name, hod, phone) professor (empid, name, sex, startyear, deptno, phone) course (courseid, cname, credits, deptno) enrollment (rollno, courseid, sem, year, grade) teaching (empid, courseid, sem, year, classroom) prerequisite (precourseid courseid) deptno is foreign key in the student, professor and course relations referring to deptid of department relation; advisor is a foreign key in the student relation referring to empid of professor relation; hod is a foreign key in the department relation referring to empid of professor relation; rollno is a foreign key in the enrollment relation referring to rollno of student relation; courseid is a foreign key in the enrollment, teaching relations referring to courseid of course relation; empid is a foreign key of the teaching relation referring to empid of professor relation; precourseid and courseid are foreign keys in the prerequisite relation referring to courseid of the course relation; Given query: select s.rollno, s.name from student s where EXISTS (select c.courseid from course c Where c.deptno=5 and EXISTS (select e.* from enrollemnt e where e.courseid = c.courseid and e.rollno = s.rollno)): Which one of the following statements is correct with respect to the given query?

- **1.** It retrieves the roll number and names of students who have not enrolled for all course offered by department
- **2.** It retrieves the roll number and names of students who have enrolled for all course offered by department number 5.
- **3.** It retrieves the roll number and names of students who have enrolled for at least one course offered by department
- **4.** It retrieves the roll number and names of students who are such that there exists at least one course offered by department number 5 which is not enrolled by the student.

> [!TIP]
> **Correct answer: 3. It retrieves the roll number and names of students who have enrolled for at least one course offered by department**

## Solution

For each student, the outer EXISTS succeeds if there is some course c with c.deptno=5 for which the inner EXISTS finds that student's enrollment in c. The query therefore selects students enrolled in at least one course offered by department 5.

## Key Points

- Nested positive EXISTS expresses 'there exists at least one matching course and enrollment.'

## Why the other options are incorrect

Universal 'all courses' logic requires double NOT EXISTS, not nested positive EXISTS. The query contains no NOT condition, so options 1 and 4 describe logic it does not perform. Option 2 also incorrectly changes existential qualification into universal qualification.
