# Unit 4: Database Management Systems

[Project home](../README.md) · [All units](README.md) · [Official syllabus](syllabus.md)

## Contents

- [How to use this guide](#status-and-use)
- [Unit-wide exam playbook](#unit-wide-exam-playbook)
- [1. Database System Concepts and Architecture](#chapter-1)
- [2. Data Modeling](#chapter-2)
- [3. SQL](#chapter-3)
- [4. Normalization for Relational Databases](#chapter-4)
- [5. Enhanced Data Models](#chapter-5)
- [6. Data Warehousing and Data Mining](#chapter-6)
- [7. Big Data Systems](#chapter-7)
- [8. NoSQL](#chapter-8)
- [Coverage and quality notes](#coverage-and-quality-notes)

## Status and use

This guide contains all **10 question blocks currently recoverable and assigned to Unit 4** from the local UGC NET archive. Questions are arranged chapter-wise and numbered continuously through the unit.

> [!WARNING]
> This is a working extraction inventory, not a complete solved guide. **0 answers are validated and 10 remain pending** in this unit. Some unit and chapter placements use fallback routing, and OCR or missing figures can make questions incomplete.

Use this file for question discovery and broad chapter revision. The chapter notes and exam methods are general, not question-specific solutions. Full source paths, PDF pages and classification states remain in the structured data for auditing.

## Unit-wide exam playbook

- **Core idea:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.
- **Method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.
- **Rules/formulas:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.
- **Frequent traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

## Chapter-wise concepts and PYQs

<a id="chapter-1"></a>

### 1. Database System Concepts and Architecture (4 questions)

**What to master:** Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

---

#### Question 1

*UGC NET Nov 2021, original Q61*

> Which of the DBMS component ensures that concurrent execution of multiple operations on the database results into a consistent database state?

**Options**

1. Logs
2. Buffer manager
3. File manager
4. Transaction processing system

**Chapter foundations**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 2

*UGC NET Nov 2021, original Q62*

> Consider following two statements: Statement I: Relational database schema represents the logical design of the database. Statement II: Current snapshot of a relation only provides the degree of the relation. In the context to the above statements, choose the correct option from the options given below:

**Options**

1. Statement I is TRUE but Statement II is FALSE
2. Statement I is FALSE but Statement II is TRUE
3. Both Statement I and Statement II are FALSE
4. Both Statement I and Statement II are TRUE

**Chapter foundations**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 3

*UGC NET Nov 2021, original Q70*

> Which of the following is used to create a database schema?

**Options**

1. DML
2. DDL
3. HTML
4. XML

**Chapter foundations**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 4

*UGC NET Nov 2021, original Q72*

> In a file allocation system, the following allocation schemes are used: A. Contiguous B. Indexed C. Linked allocation Which of the allocation scheme(s) given above will not suffer from external fragmentation? Choose the correct answer from the options given below:

**Options**

1. A only
2. B and C only
3. A and B only
4. C only

**Chapter foundations**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-2"></a>

### 2. Data Modeling (0 questions)

**What to master:** Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._

<a id="chapter-3"></a>

### 3. SQL (0 questions)

**What to master:** Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._

<a id="chapter-4"></a>

### 4. Normalization for Relational Databases (3 questions)

**What to master:** Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

---

#### Question 5

*UGC NET Nov 2021, original Q65*

> Given the following STUDENT‐COURSE scheme: STUDENT (Rollno, Name, Courseno) COURSE (Courseno, Coursename, Capacity), where Rollno is the primary key of relation STUDENT and Courseno is the primary key of relation COURSE. Attribute Coursename of COURSE takes unique values only. The number of records in COURSE and STUDENT tables are 3 and 5 respectively. Following relational algebra query is executed: R=STUDENT X COURSE Match List I with List II in context to the above problem statement. List I List II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Degree of table R I. 15
> - **B.** Cardinality of table R II. NIL
> - **C.** Foreign key of relation STUDENT III. 6
> - **D.** Foreign key of relation COURSE IV. Courseno Choose the correct answer from the options given below:

**Options**

1. A ‐III , B ‐I , C ‐IV , D ‐ II
2. A ‐I , B ‐III , C ‐IV , D ‐ II
3. A ‐I , B ‐III , C ‐IV , D ‐ II (options 2 and 4 are same)
4. A ‐I , B ‐III, C ‐II , D ‐ IV

**Chapter foundations**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 6

*UGC NET Nov 2021, original Q67*

> Given a relation scheme R(x,y,z,w) with functional dependencies set F={x y, z w}. All attributes take single and atomic values only. A. Relation R is in First Normal FORM B. Relation R is in Second Normal FORM C. Primary key of R is xz Choose the correct answer from the options given below:

**Options**

1. C only
2. B and C only
3. A and C only
4. B only

**Chapter foundations**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 7

*UGC NET Nov 2021, original Q69*

> A transaction may be in one of the following states during its execution life cycle in concurrent execution environment.
>
> **Additional extracted choices — check the source page:**
>
> - **A.** FAILED
> - **B.** TERMINATED
> - **C.** PARTIALLY COMMITTED
> - **D.** COMMITTED E. ACTIVE Given a transaction in active state during its execution, find its next transitioned state from the options given below:

**Options**

1. A only
2. Either A or C only
3. C only
4. D only

**Chapter foundations**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-5"></a>

### 5. Enhanced Data Models (0 questions)

**What to master:** Temporal, Multimedia, Deductive, XML and Internet Databases; Mobile Databases; GIS; Genome Data Management; Distributed Databases; Client-Server Architectures.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._

<a id="chapter-6"></a>

### 6. Data Warehousing and Data Mining (0 questions)

**What to master:** Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._

<a id="chapter-7"></a>

### 7. Big Data Systems (0 questions)

**What to master:** Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._

<a id="chapter-8"></a>

### 8. NoSQL (3 questions)

**What to master:** NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

---

#### Question 8

*UGC NET Nov 2021, original Q30*

> Consider the following linear optimization problem: Maximize Z = 6x+5y Subject to 2x ‐ 3y <= 5 x+3y <= 11 4x + y <=15 and x>=0, y >= 0. The optimal solution of the problem is:

**Options**

1. 15
2. 25
3. 31.72
4. 41.44

**Chapter foundations**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 9

*UGC NET Nov 2021, original Q41*

> The postfix form of the expression (A + B) * (C * D ‐ E) * F / G is _______ .

**Options**

1. A B + C D * E – F G / * *
2. A B + C D * E – F * * G /
3. A B + C D * E – * F * G /
4. A B + C D E * – * F * G /

**Chapter foundations**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 10

*UGC NET Nov 2021, original Q64*

> Given the following STUDENT‐COURSE scheme: STUDENT (Rollno, Name, courseno) COURSE (courseno, coursename, capacity), where Rollno is the primary key of relation STUDENT and courseno is the primary key of relation COURSE. Attribute coursename of COURSE takes unique values only. Which of the following query(ies) will find total number of students enrolled in each course, along with its coursename. A. SELECT coursename, count(*) 'total' from STUDENT natural join COURSE group by coursename; B. SELECT C.coursename, count(*) 'total' from STUDENT S, COURSE C where S.courseno=C.courseno group by coursename; C. SELECT coursename, count(*) 'total' from COURSE C where courseno in (SELECT courseno from STUDENT);

**Options**

1. A and B only
2. C only
3. A only
4. B only

**Chapter foundations**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

## Coverage and quality notes

- Recovered question blocks in this unit: **10**
- Chapter placements with direct keyword support: **9**
- Chapter placements needing manual review: **1**
- Questions with validated answers in this guide: **0**
- OCR may flatten mathematical notation, tables, code indentation, and figures. Full audit references are retained in the structured data.
- Some combined Paper 1/Paper 2 scans and older papers lack a trustworthy embedded key. Such questions remain pending rather than receiving guessed answers.

---

[Back to contents](#contents) · [All units](README.md) · [Project home](../README.md)

