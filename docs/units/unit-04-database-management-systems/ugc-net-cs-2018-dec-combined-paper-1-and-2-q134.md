# Question 134

*UGC NET CS · 2018 Dec Paper 1 And 2 · SQL · JOIN, GROUP BY and Aggregate Rows*

Consider the following relations. Students(Roll-No, Name): (18CS101, Ramesh), (18CS102, Mukesh), (18CS103, Ramesh), with Roll-No as the primary key. Performance(Roll-No, Course, Marks): (18CS101, DBMS, 60), (18CS101, Compiler Design, 65), (18CS102, DBMS, 80), (18CS103, DBMS, 85), (18CS102, Compiler Design, 75), (18CS103, Operating System, 70), with (Roll-No, Course) as the composite primary key. Consider the query: SELECT S.Name, SUM(P.Marks) FROM Students S, Performance P WHERE S.Roll-No = P.Roll-No GROUP BY S.Name. The number of rows returned by the query is:

- **1.** 0
- **2.** 1
- **3.** 2
- **4.** 3

> [!TIP]
> **Correct answer: 3. 2**

## Solution

The join pairs every Performance row with the matching Students row. GROUP BY S.Name then creates one group per distinct name, not per roll number. The joined names are only Ramesh and Mukesh, so there are two groups and hence two result rows. Ramesh's group combines both students named Ramesh (marks 60+65+85+70=280), while Mukesh's group totals 80+75=155. Therefore option 3 is correct.

## Key Points

- GROUP BY controls result cardinality: equal grouping values merge even when their primary keys differ.

## Why the other options are incorrect

The result is not empty because every performance roll number matches a student. It is not one row because two distinct names occur. It is not three rows because the two different Ramesh roll numbers collapse into one group when grouping only by Name.
