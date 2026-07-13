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

This guide contains all **178 question blocks currently recoverable and assigned to Unit 4** from the local UGC NET archive. Questions are arranged chapter-wise and numbered continuously through the unit.

**Important:** a question-specific correct option is included only after reliable key matching or independent derivation. Unverified answers are never guessed.

Use each entry in three passes: revise the basics, attempt the question, and compare your method with the exam route. Full source paths and PDF pages remain in the structured data for auditing.

## Unit-wide exam playbook

- **Core idea:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.
- **Method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.
- **Rules/formulas:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.
- **Frequent traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

## Chapter-wise concepts and PYQs

<a id="chapter-1"></a>

### 1. Database System Concepts and Architecture (35 questions)

**What to master:** Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

---

#### Question 1

*UGC NET Dec 2009, Paper II, original Q47*

> Analysis of large database to retrieve information is ca lled (A) OLTP (B) OLAP (C) OLDP (D) OLPP

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 2

*UGC NET June 2012, Paper II, original Q7*

> In multiuser database if two users wish to update the same record at the same time, they are prevented from doing so by (A) Jamming (B) Password (C) Documentation (D) Record lock

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 3

*UGC NET June 2012, Paper II, original Q12*

> A Transaction Manager is which of the following ? (A) Maintains a log of transactions (B) Maintains before and after database images (C) Maintains appropriate concurrency control (D) All of the above

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 4

*UGC NET Dec 2014, Paper III, original Q8*

> Which of the following is correct ? I. Two phase locking is an optimistic protocol. II. Two phase locking is pessimistic protocol III. Time stamping is an optimistic protocol. IV. Time stamping is pessimistic protocol. (A) I and III (B) II and IV (C) I and IV (D) II and III 9. __________ rules used to limit the volume of log information that has to be handled and processed in the event of system failure involving the loss of volatile information. (A) Write-ahead log (B) Check-pointing (C) Log buffer (D) Thomas

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 5

*UGC NET Dec 2015, Paper II, original Q14*

> Match the following database terms to their functions List - I List - II (a) Normalization (i) Enforces match of primary key to foreign key (b) Data Dictionary (ii) Reduces data redundancy in a database (c) Referential Integrity (iii) Defines view (s) of the database for particular users) (d) External Schema (iv) Contains metadata describing database structure Codes: (a) (b) (c) (d) (1) (iv) (iii) (i) (ii) (2) (ii) (iv) (i) (ili)

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 6

*UGC NET Dec 2015, Paper II, original Q19*

> Data which improves the performance and accessibility of the database are called : (1) Indexes (2) User Data (3) Application Metadata (4) Data Dictionary

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 7

*UGC NET Dec 2015, Paper III, original Q59*

> Consider the following database table: Create table test one integer, two integer, primary key(one), unique(two), check(one>=1 and <=10), check(two>=1 and <=5) How many data records/tuples atmost can this table contain ? (1) 5 (2) 10 (3) 15 (4) 50

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 8

*UGC NET June 2015, Paper II, original Q16*

> An Assertion is a predicate expressing a condition we wish database to always satisfy. The correct syntax for Assertion is : (1) CREATE ASSERTION 'ASSERTION Name' CHECK 'Predicaté' (2) CREATE ASSERTION 'ASSERTION Name' (3) CREATE ASSERTION, CHECK Predicate (4) SELECT ASSERTION

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 9

*UGC NET June 2015, Paper II, original Q19*

> Database applications were built directly on top of file system to overcome the following drawbacks of using file-systems : (a) Data redundancy and inconsistency (b) Difficulty in accessing Data (c) Data isolation (d) Integrity problems (1) (a) (2) (a) and (d) (3) (a), (b) and (c) (4) (a), (b), (c) and (d)

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 10

*UGC NET July 2016, Paper II, original Q17*

> Which of the following statement(s) is/are FALSE in the context of Relational DBMS ? I. Views in a database system are import ant because they help with access control by allowing users to see only a particular subset of the data in the database. II. E-R diagrams are useful to logically model concepts. III. An update anomaly is when it is not possible to store information unless some other, unrelated information is stored as well. IV. SQL is a procedural language. (1) I and IV only (2) III and IV only (3) I, II and III only (4) II, III and IV only

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 11

*UGC NET July 2016, Paper II, original Q20*

> Consider the following database table having A, B, C and D as its four attributes and four possible candidate keys (I, II, III and IV) for this table : A B C D a1 b 1 c 1 d 1 a2 b 3 c 3 d 1 a1 b 2 c 1 d 2 I : {B} II : {B, C} III : {A, D} IV : {C, D} If different symbols stand for diffe rent values in the table (e.g., d1 is definitely not equal to d2), then which of the above could not be the candidate key for the database table ? (1) I and III only (2) III and IV only (3) II only (4) I only

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 12

*UGC NET July 2016, Paper III, original Q10*

> Which of the following statements is TRUE ? D 1 : The decomposition of the schema R(A, B, C) into R 1(A, B) and R2 (A, C) is always lossless. D 2 : The decomposition of the schema R(A, B, C, D, E) having AD → B, C → DE, B → AE and AE → C, into R1 (A, B, D) and R2 (A, C, D, E) is lossless. (1) Both D 1 and D2 (2) Neither D 1 nor D2 (3) Only D 1 (4) Only D 2

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 13

*UGC NET July 2016, Paper III, original Q12*

> Semi-join strategies are techniques for query processing in distributed database system. Which of the following is a semi-join technique ? (1) Only the joining attributes are sent from one site to another and then all of the rows are returned. (2) All of the attributes are sent from one s ite to another and then only the required rows are returned. (3) Only the joining attributes are sent from one site to another and then only the required rows are returned. (4) All of the attributes are sent from one s ite to another and then only the required rows are returned.

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 14

*UGC NET Jan 2017, Paper III, original Q10*

> For a database relation R(A, B, C, D) wher e the domains of A, B, C and D include only atomic values, only the following functional de pendencies and those that can be inferred from them are : A → C B → D The relation R is in _______. (1) First normal form but not in second normal form. (2) Both in first normal form as well as in second normal form. (3) Second normal form but not in third normal form. (4) Both in second normal form as well as in third normal form.

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 15

*UGC NET Dec 2018, original Q133*

> Consider the following sequence of two transactions on a bank account (A) with initial balance 20,000 that transfers 5,000 to another account (B) and then apply 10% interest. (i) T1 start (i) T1 A old = 20,000 new 15,000 (i) T1 B old = 12,000 new = 17,000 (iv) T1 commit (v) T2 start (vi) T2 A old = 15,000 new = 16,500 (vil) 12 commit Suppose the database system crashes just before log record (vii) is written. When the system is restarted, which one statement is true of the recovery process? . We must redo log record (vi) to set A to 16,500. 91394342530. We must redo log record (vi) to set A to 16,500 and then redo log records (ii) and (i). 91394342531. We need not redo log records (ii) and (il) because transaction T1 has committed. We can apply redo and undo operations in arbitrary order because they are idempotent. 91394342532.

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 16

*UGC NET Dec 2018, original Q140*

> Suppose that everyone in a group of N people wants to communicate secretly with (N- 1) other people using symmetric key cryptographic system. The communication between any two persons should not be decodable by the others in the group. The number of keys required in the system as a whole to satisfy the confidentiality requirement is Options:

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 17

*UGC NET July 2018, Paper II, original Q63*

> In a Hierachical database, a hashing function is used to locate the _ _______. (1) Collision (2) Root (3) Foreign Key (4) Records

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 18

*UGC NET July 2018, Paper II, original Q66*

> For a database relation R(a, b, c, d) where the domains of a, b, c and d inclu de only atomic values, and only the following functional dependencies and those tha t can be inferred from them hold : a → c b → d The relation is in _________. (1) First normal form but not in second normal form (2) Second normal form but not in third normal form (3) Third normal form (4) BCNF

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 19

*UGC NET July 2018, Paper II, original Q68*

> Database systems that store each relation in a separate operating sys tem file may use the operating system’s authorization scheme, instead of defining a spec ial scheme themselves. In this case, which of the following is false ? (1) The administrator enjoys more control on the grant option. (2) It is difficult to differentiate among the update, delete and insert aut horizations. (3) Cannot store more than one relation in a file. (4) Operations on the database are speeded up as the authorization procedu re is carried out at the operating system level.

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 20

*UGC NET Dec 2019, original Q70*

> Which of the component module of DBMS does rearrangement and possible ordering of operations, eliminate redundancy in query and use efficient algorithms and indexes during the exceution of a query? (1) query compiler (2) query optimizer (3) Stored data manager (4) Database processor 61547540978. 2 61547540979. 3 61547540980.4

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 21

*UGC NET Dec 2019, original Q114*

> The order of schema ?10?101? and ?2?0?21 are — and respectively. (1) 5.3 (2) 5.2 (3) 7.5 (4) 8.7 61547541154.2 61547541155.3 61547541156.4

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 22

*UGC NET Dec 2019, original Q123*

> Two concurrent executing transactions I, and T, are allowed to update same stock item say 'A' in an uncontrolled manner. In such scenario, following problems may occur : (a) Dirty read problem (b) Lost update problem (c) Transaction failure (d) Inconsistent database state Which of the following option is correct if database system has no concurrency module and allows concurrent execution of above two transactions? (1) (a). (b) and (c) only (2) (c) and (d) only (3) (a) and (b) only (4) (a). (b) and (d) only 61547541190.2 61547541191. 3 61547541192. 4

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 23

*UGC NET Dec 2019, original Q150*

> Assume that given table R is decomposed in two tables R, (A. B. C) with functional dependency set fi = (A → B. A → C; and R,(A. D. E) with FD set F2 = {A → D. D → E). Which of the following option is true w.r.t. given decomposition? (1) Dependency preservation property is followed (2) R, and R, are both in 2 NF (3) R, is in 2 NF and R3 is in 3 NF (4) R, is in 3 NF and R, is in 2 NF 61547541298. 2 61547541299.3 61547541300. 4 Question Label: Comprehension Answer question (96-100) based on the problem statement given below : An organization needs to maintain database having five attributes A. B. C. D. E. These attributes are functionally dependent on each other for which functionally dependency set F is given as : F:{A→BC.D→E. BC→D. A→D}. Consider a universal relation R(A. B. C. D. E) with functional dependency set F. Also all attributes are simple and take atomic values only. Sub questions

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 24

*UGC NET June 2019, original Q102*

> The M components in MVC are responsible for 1. user interface 2. security of the system 3. business logic and domain objects + translating between user interface actions/events and operations on the domain objects 64635085744. 2 64635085745.3 64635085746.4

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 25

*UGC NET Nov 2021, original Q12*

> potential customers at the developer's location The V components in MVC are responsible for: 1. User interface. 2. Security of the system. 3. Business logic and domain objects. 4. Translating between user interface actions/events and operations on the domain objects.

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 26

*UGC NET Nov 2021, original Q61*

> 6000 Which of the DBMS component ensures that concurrent execution of multiple operations on the database results into a consistent database state? 1. Logs 2. Buffer manager 3. File manager 4. Transaction processing system

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 27

*UGC NET Nov 2021, original Q62*

> Logs Consider following two statements: Statement I: Relational database schema represents the logical design of the database. Statement II: Current snapshot of a relation only provides the degree of the relation. In the context to the above statements, choose the correct option from the options given below: 1. Statement I is TRUE but Statement II is FALSE 2. Statement I is FALSE but Statement II is TRUE 3. Both Statement I and Statement II are FALSE 4. Both Statement I and Statement II are TRUE

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 28

*UGC NET Nov 2021, original Q68*

> C only A company is consuming parts in the manufacturing of other products. Each of the part is either manufactured within the company or purchased from the external suppliers or both. For each part, partnumber, partname is maintained. Attribute batchnumber is maintained if the consumed part is manufactured in the company. If part is purchased from external supplier, then supplier name is maintained. Which of the following constraints need to be considered when modelling class/subclass concepts in ERD for the given problem. 1. Total specialization and overlapping constraints 2. Disjoint constraint only 3. Partial participation 4. Partial participation and disjoint constraints

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 29

*UGC NET Nov 2021, original Q70*

> A only Which of the following is used to create a database schema? 1. DML 2. DDL 3. HTML 4. XML

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 30

*UGC NET Oct 2022, original Q1*

> In a database, a rule is defined as (P1 and P2) or P3? R1 (0.8) and R2 (0.3), where P1. P2. PS are premises and R1. R2 are conclusions of rules with certainty factors: (CF) 0.8 and 0.3 respectively. If any running program has produced P1. P2. P3 with CF as 0.5. 0.8. 0.2 respectively, find the CF of results on the basis of premises. 1. CF (R1 = 0.8), CF (R2 = 0.3) 2. CF (R1 = 0.40), CF (R2 = 0.15) 3. CF (R1 = 0.15), CF (R2 = 0.35) 4. CF (R1 = 0.8). CF (R2 = 0.35)

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 31

*UGC NET Oct 2022, original Q52*

> A trigger is 1. A statement that enables to start DBMS. 2. A statement that is executed by the user when debugging an application program. 3. A condition the system tests for the validity of the database user. 4. A statement that is executed automatically by the system as a side effect of modification to the database.

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 32

*UGC NET June 2023, Paper II, original Q23*

> Which of the following scenario may lead to an irrecoverable error in a (+2) database system? a. A transaction writes a data item after it is read by an uncommitted transaction b. A transaction reads a data item after it is read by an uncommitted transaction c. A transaction reads a data item after it is written by a committed transactions d. A transaction reads a data item after it is written by an uncommitted transaction.

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 33

*UGC NET Dec 2022 session, 15 Mar 2023 Shift 1, original Q1*

> No.9 Use the following schema of the academic institution relational database: student (rollne, name, degree, year, sex, deptno, advisor) department (deptid, name, hod, phone) professor (empid, name, sex, startyear, deptno, phone) course (courseid, cname, credits, deptno) enrollment (rollne, courseid, sem year, grade) teaching (empid, courseid, sem, year, classroom) prerequisite (precourseid, courseid) deptno is foreign key in the student, professor and course relations referring to deptid of department relation; advisor is a foreign key in the student relation referring to empid of professor relation; hod is a foreign key in the department relation referring to empid of professor relation; rollno is a foreign key in the enrollment relation referring to rollno of student relation; courseid is a foreign key in the enrollment, teaching relations referring to courseid of course relation; empid is a foreign key of the teaching relation referring to empid of professor relation; precourseid and courseid are foreign keys in the prerequisite relation referring to courseid of the course relation;

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 34

*UGC NET Dec 2022 session, 15 Mar 2023 Shift 1, original Q4*

> Select s.rollno, s.name From student s Where EXISTS (select * prerequisite p where p.courseid = "324") and EXISTS (select * from enrollment e where e.courseid = p.precourseid and e.rollno = s.rollno)) (1) 1 (2) 2 (3) 3 (4) 4 2 1 department (deptid, name, hod, phone) professor (empid, name, sex, startyear, deptno, phone) | course (courseid, cname, credits, deptno) enrollment (rollne, courseid, sem, year, grade) teaching (empid, courseid, sem, year, classroom) prerequisite (precourseid, courseid) deptno is foreign key in the student, professor and course relations referring to deptid of department relation; advisor is a foreign key in the student relation referring to empid of professor relation; hod is a foreign key in the department relation referring to empid of professor relation; rollno is a foreign key in the enrollment relation referring to rollno of student relation; courseid is a foreign key in the enrollment, teaching relations referring to courseid of course relation; empid is a foreign key of the teaching relation referring to empid of professor relation; precourseid and courseid are foreign keys in the prerequisite relation referring to courseid of the course relation;

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 35

*UGC NET June 2025, original Q51*

> In a group of 120 people: 65 eat Rice, 45 eat bread, 42 eat curd, 20 eat both Rice and bread, 25 eat both Rice and curd, 15 eat both bread and curd, and 8 eat all three items. Which of the following is the number of people who eat at least one of the three items: (1) 56 (2) 100 (3) 92 (4) 65 42558919257.2 42558919258.3 42558919259.4 Mandatory: No

**Basics to understand**

This question belongs to the ideas covered by **Database System Concepts and Architecture**. Revise these foundations: Data Models, Schemas and Instances; Three-Schema Architecture and Data Independence; Database Languages and Interfaces; Centralized and Client/Server DBMS Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Database System Concepts and Architecture questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-2"></a>

### 2. Data Modeling (21 questions)

**What to master:** Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

---

#### Question 36

*UGC NET Dec 2009, Paper II, original Q16*

> The E-R model is expressed in term of I. Entities II. The relationship among entities. III. The attributes of the entities. IV. Functional relationship. (A) I, II (B) I, II, IV (C) II, II, IV (D) I, II, III

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 37

*UGC NET June 2010, Paper II, original Q1*

> “ x1 is a clone of x” means x1 is identical to x in terms of the physical attributes namely, height, weight and complexion. Given, height, weight and complexion only form a complete set of attributes for an entity, cloning is an equivalence relation. What is your impression about this statement ? (A) The statement is true (B) The statement is false (C) The truth value of the statement cannot be computed (D) None of these 2. ‘R is a robot of M’ means R can perform some of the tasks that otherwise M would do and R is unable to do anything else. Which of the following is the most appropriate representation to model this situation ? (A) (B) (C) (D) None of these

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 38

*UGC NET June 2010, Paper II, original Q16*

> An entity instance is a single occurrence of an _______. (A) entity type (B) relationship type (C) entity and relationship type (D) None of these

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 39

*UGC NET Dec 2013, Paper II, original Q11*

> The student marks should not be greater than 100. This is (A) Integrity constraint (B) Referential constraint (C) Over-defined constraint (D) Feasible constraint

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 40

*UGC NET Dec 2013, Paper II, original Q13*

> An ER Model includes I. An ER diagram portraying entity types. II. Attributes for each entity type III. Relationships among entity types. IV. Semantic integrity constraints that reflects the business rules about data not captured in the ER diagram. (A) I, II, III & IV (B) I & IV (C) I, II & IV (D) I & III

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 41

*UGC NET Dec 2013, Paper II, original Q14*

> Based on the cardinality ratio and participation ________ associated with a relationship type, choose either the Foreign Key Design, the Cross Referencing Design or Mutual Referencing Design. (A) Entity (B) Constraints (C) Rules (D) Keys

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 42

*UGC NET Dec 2013, Paper III, original Q62*

> Which of the following statement(s) is (are) true ? I. Two successive translations are additive. II. Two successive rotations are additive. III. Two successive scaling operations are multiplicative. (A) I and II (B) I and III (C) II and III (D) All the above

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 43

*UGC NET June 2013, Paper III, original Q47*

> Match the following : a. Foreign keys i. Domain constraint b. Private key ii. Referential integrity c. Event control action model iii. Encryption d. Data security iv. Trigger Codes : a b c d (A) iii ii i iv (B) ii i iv iii (C) iii iv i ii (D) i ii iii iv

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 44

*UGC NET Dec 2014, Paper II, original Q18*

> What kind of mechanism is to be taken into account for converting a weak entity set into strong entity set in entity-relationship diagram ? (A) Generalization (B) Aggregation (C) Specialization (D) Adding suitable attributes

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 45

*UGC NET Dec 2015, Paper III, original Q63*

> Consider the following three tables R, S and T. In this question, all the join operations are natural joins (A). (m) is the projection operation of a relation : R S T A B A 2 6 2 7 1 3 2 2 1 2 5 6 8 1 9 3 7 8 8 3 5 4 8 2 5 Possible answer tables for this question are also given as below : A B C 2 4 1 2 5 3 2 4 3 2 5 A B CA B 6 2 1 2 2 1 6 2 8 1 3 2 5 3 2 B 7 8 3 4 2 3 2 5 8 1 7 8 1 7 8 7 8 1 9 8 3 9 8 3 9 8 3 9 8 3 (a) (b) (c) (d) What is the resulting table of TA, B (RosI) A TB,C(SmaI)? (1) (2) (b) (4) (d) D-8715 12 Paper-III

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 46

*UGC NET June 2015, Paper II, original Q18*

> Drop Table cannot be used to drop a Table referenced by - . constraint. (a) Primary key (b) Sub key (c) Super key (d) Foreign key (1) (a) (2) (a), (b) and (c) 3) (d) (4) (a) and (d)

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 47

*UGC NET June 2015, Paper II, original Q49*

> Which of the following statements is FALSE about weak entity set? (1) Weak entities can be deleted automatically when their strong entity is deleted. (2) Weak entity set avoids the data duplication and consequent possible inconsistencies caused by duplicating the key of the strong entity. (3) A weak entity set has no primary keys unless attributes of the strong entity set on which it depends are included. (4) Tuples in a weak entity set are not partitioned according to their relationship with tuples in a strong entity set.

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 48

*UGC NET June 2015, Paper III, original Q11*

> The relation schemas Ry and R, form a Lossless join decomposition of R if and only if : (a) RynR2 → (Ry-R2) (c) RInR2 » (R2-Ry) (d) R2→RjnR2 Codes : (1) (a) and (b) happens (2) (a) and (d) happens (3) (a) and (c) happens (4) (b) and (c) happens

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 49

*UGC NET July 2016, Paper II, original Q16*

> In RDBMS, the constraint that no key attri bute (column) may be NULL is referred to as : (1) Referential integrity (2) Multi-valued dependency (3) Entity Integrity (4) Functional dependency

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 50

*UGC NET Jan 2017, Paper II, original Q17*

> Integrity constraints ensure that changes made to the database by authorized users do not result into loss of data consistency. Which of the following stateme nt(s) is (are) true w.r.t. the examples of integrity constraints ? (A) An instructor Id. No. cannot be null, provided Intructor Id No. being primary key. (B) No two citizens have same Adhar-Id. (C) Budget of a company must be zero. (1) (A), (B) and (C) are true. (2) (A) false, (B) and (C) are true. (3) (A) and (B) are true; (C) false. (4) (A), (B) and (C) are false.

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 51

*UGC NET Nov 2017, Paper II, original Q18*

> Match the following with respect to RDBMS : (a) Entity integrity (i) enforces some specific business rule that do not fall into entity or domain (b) Domain integrity (ii) Rows can’t be deleted which are used by other records (c) Referential integrity (iii) enforces valid entries for a column (d) Userdefined integrity (iv) No duplicate rows in a table Code : (a) (b) (c) (d) (1) (iii) (iv) (i) (ii) (2) (iv) (iii) (ii) (i) (3) (iv) (ii) (iii) (i) (4) (ii) (iii) (iv) (i)

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 52

*UGC NET July 2018, Paper II, original Q64*

> Relations produced from E - R Model will always be in ________. (1) 1 NF (2) 2 NF (3) 3 NF (4) 4 NF

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 53

*UGC NET July 2018, Paper II, original Q67*

> A many-to-one relationship exists between entity sets r 1 and r 2. How will it be represented using functional depedencies if Pk(r) denotes the primary key attrib ute of relation r ? (1) Pk(r1) → Pk(r2) (2) Pk(r2) → Pk(r1) (3) Pk(r2) → Pk(r1) and Pk(r 1) → Pk(r2) (4) Pk(r2) → Pk(r1) or Pk(r 1) → Pk(r2)

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 54

*UGC NET June 2019, original Q82*

> Which of the following features is supported in the relational database model? Complex data-types Multivalued attributes Associations with multiplicities 4. Generalization relationships Options : Exam Guide 64635085663.1 64635085664. 2 64635085665.3 64635085666.4

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 55

*UGC NET Aug 2024, original Q75*

> How does a relational database ensure data integrity ? (1) By encrypting all data stored (2) By enforcing rules defined in the schema (3) By compressing data for efficient storage (4) By allowing unrestricted access to all users

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 56

*UGC NET Dec 2025 session (Jan 2026), original Q71*

> Question Number : 71

**Basics to understand**

This question belongs to the ideas covered by **Data Modeling**. Revise these foundations: Entity-Relationship Diagrams; Relational Model - Constraints, Languages, Design and Programming; Relational Database Schemas; Update Operations and Constraint Violations; Relational Algebra and Calculus; Codd Rules.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Modeling questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-3"></a>

### 3. SQL (16 questions)

**What to master:** Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

---

#### Question 57

*UGC NET Dec 2012, Paper II, original Q22*

> In DML, RECONNCT command key mod 13, with linear probing is cannot be used with used to insert keys 55, 58, 68, 91, 27,

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 58

*UGC NET Dec 2013, Paper III, original Q58*

> Consider the table Student (stuid, name, course, marks). Which one of the following two queries is correct to find the highest marks student in course 5 ? Q.1. Select S.stuid From student S Where not exists (select ∗ from student e where e course = ‘5’ and e marks ≥ s marks) Q.2. Select s.stu.id From student S Where s ⋅ marks > any (select distinct marks from student S where s ⋅ course = 5) (A) Q. 1 (B) Q. 2 (C) Both Q. 1 and Q. 2 (D) Neither Q. 1 nor Q. 2

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 59

*UGC NET June 2013, Paper III, original Q8*

> The employee information of an Organization is stored in the relation : Employee (name, sex, salary, deptname) Consider the following SQL query Select deptname from Employee Where sex = ‘M’ group by deptname having avg (salary) > {select avg (salary) from Employee} Output of the given query corresponds to (A) Average salary of employee more than average salary of the organization. (B) Average salary less than average salary of the organization. (C) Average salary of employee equal to average salary of the organization. (D) Average salary of male employees in a department is more than average salary of the organization.

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 60

*UGC NET Dec 2014, Paper II, original Q16*

> Division operation is ideally suited to handle queries of the type : (A) customers who have no account in any of the branches in Delhi. (B) customers who have an account at all branches in Delhi. (C) customers who have an account in atleast one branch in Delhi. (D) customers who have only joint account in any one branch in Delhi

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 61

*UGC NET Dec 2015, Paper II, original Q13*

> Consider a "CUSTOMERS" database table having a column "CITY" filled with all the names of Indian cities (in capital letters). The SQL statement that finds all cities that have "GAR" somewhere in its name, is : (1) Select * from customers where city = '%GAR%; (2) Select * from customers where city = '$GAR$'; (3) Select * from customers where city like '%GAR%'; (4) Select * from customers where city as '%GAR';

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 62

*UGC NET Dec 2015, Paper III, original Q60*

> Suppose ORACLE relation R(A, B) currently has tuples {(1, 2), (1, 3), (3, 4)} and relation S(B, C) currently has ((2, 5), (4, 6), (7, 8)). Consider the following two SQL queries SQ1 and SQ2 : SQ1 : Select * From R Full Join S On R.B = S.B; SQ2 : Select * From R Inner Join S On R.B = S.B; The numbers of tuples in the result of the SQL query SQ1 and the SQL query SQ2 are given by : (1) 2 and 6 respectively (2) 6 and 2 respectively (3) 2 and 4 respectively (4) 4 and 2 respectively D-8715 11 Paper-II

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 63

*UGC NET Dec 2015, Paper III, original Q61*

> Consider the following three SQL queries (Assume the data in the people table) : (a) Select Name from people where Age>21; (b) Select Name from people where Height>180; (c) Select Name from people where (Age>21) or (Height>180); If the SQL queries (a) and (b) above, return 10 rows and 7 rows in the result set respectively, then what is one possible number of rows returned by the SQL query (c) ? (1) (2) 7 (3) 10 (4) 21

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 64

*UGC NET June 2015, Paper III, original Q8*

> The STUDENT information in a university stored in the relation STUDENT (Name, SEX, Marks, DEPT_Name) Consider the following SQL Query SELECT DEPT_Name from STUDENT where SEX = M' group by DEPT_Name having avg (Marks)>SELECT avg (Marks) from STUDENT. It Returns the Name of the Department for which : (1) The Average marks of Male students is more than the average marks of students in the same Department (2) The average marks of male students is more than the average marks of students in the University (3) The average marks of male students is more than the average marks of male students in the University (4) The average marks of students is more than the average marks of male students in the University

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 65

*UGC NET July 2016, Paper II, original Q19*

> Consider the following two commands C1 and C2 on the relation R from an SQL database : C1 : drop table R; C2 : delete from R; Which of the following statements is TRUE ? I. Both C1 and C2 delete the schema for R. II. C2 retains relation R, but deletes all tuples in R. III. C1 deletes not only all tuples of R, but also the schema for R. (1) I only (2) I and II only (3) II and III only (4) I, II and III

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 66

*UGC NET July 2016, Paper III, original Q11*

> Consider the following ORACLE relations : R (A, B, C) = {<1, 2, 3>, <1, 2, 0>, <1, 3, 1>, <6, 2, 3>, <1, 4, 2>, <3, 1, 4> } S (B, C, D) = {<2, 3, 7>, <1, 4, 5>, <1, 2, 3>, <2, 3, 4>, <3, 1, 4>}. Consider the following two SQL queries SQ 1 and SQ2 : SQ 1 : SELECT R⋅B, AVG (S⋅B) FROM R, S WHERE R ⋅A = S⋅C AND S⋅D < 7 GROUP BY R ⋅B; SQ 2 : SELECT DISTINCT S⋅B, MIN (S⋅C) FROM S GROUP BY S ⋅B HAVING COUNT (DISTINCT S ⋅D) > 1; If M is the number of tuples returned by SQ 1 and N is the number of tuples returned by SQ2 then (1) M = 4, N = 2 (2) M = 5, N = 3 (3) M = 2, N = 2 (4) M = 3, N = 3

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 67

*UGC NET Jan 2017, Paper III, original Q11*

> Consider the following relation : Works (emp_name, company_name, salary) Here, emp_name is primary key. Consider the following SQL query Select emp_name From works T where salary > (select avg (salary) from works S where T.company _ name = S.company _ name) The above query is for following : (1) Find the highest paid employee who earns more than the average salary of all employees of his company. (2) Find the highest paid employee who earns more than the average salary of all the employees of all the companies. (3) Find all employees who earn more than the average salary of all employees of all the companies. (4) Find all employees who earn mo re than the average salary of all employees of their company.

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 68

*UGC NET Nov 2017, Paper II, original Q17*

> In SQL, __________ is an Aggregate function. (1) SELECT (2) CREATE (3) AVG (4) MODIFY

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 69

*UGC NET Nov 2017, Paper II, original Q19*

> In RDBMS, different classes of relations are created using _________ _ technique to prevent modification anomalies. (1) Functional Dependencies (2) Data integrity (3) Referential integrity (4) Normal Forms 20. __________ SQL command changes one or more fields in a record. (1) LOOK-UP (2) INSERT (3) MODIFY (4) CHANGE

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 70

*UGC NET Dec 2018, original Q129*

> command is used to remove a relation from an SQL database. . Drop table 91394342514 Delete table

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 71

*UGC NET July 2018, Paper II, original Q62*

> Consider a relation book (title, price) which contains the titles and prices of different books. Assuming that no two books have the same price, what does the followin g SQL query list ? Select title from book as B where (select count ( *) from book as T where T.price > B.price) < 7 (1) Titles of the six most expensive books. (2) Title of the sixth most expensive books. (3) Titles of the seven most expensive books. (4) Title of the seventh most expensive books.

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 72

*UGC NET July 2018, Paper II, original Q69*

> Let R1(a, b, c) and R2(x, y, z) be two relations in which a is the foreign key of R 1 that refers to the primary key of R 2. Consider following four options. (a) Insert into R 1 (b) Insert into R 2 (c) Delete from R 1 (d) Delete from R 2 Which of the following is correct about the referential integrity co nstraint with respect to above ? (1) Operations (a) and (b) will cause violation. (2) Operations (b) and (c) will cause violation. (3) Operations (c) and (d) will cause violation. (4) Operations (d) and (a) will cause violation.

**Basics to understand**

This question belongs to the ideas covered by **SQL**. Revise these foundations: Data Definition and Types; Constraints; Queries; Insert, Delete and Update; Views; Stored Procedures and Functions; Triggers; SQL Injection.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For SQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-4"></a>

### 4. Normalization for Relational Databases (43 questions)

**What to master:** Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

---

#### Question 73

*UGC NET Dec 2009, Paper II, original Q19*

> A function that has no partial functional dependencies is in __________ form. (A) 3 NF (B) 2 NF (C) 4 NF (D) BCNF

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 74

*UGC NET June 2010, Paper II, original Q18*

> Match the following : I. 2 NF (a) transitive dependencies eliminated II. 3 NF (b) multivalued attribute removed III. 4 NF (c) contain no partial functional dependencies IV. 5 NF (d) contains no join dependency Codes : I II III IV (A) (a) (c) (b) (d) (B) (d) (a) (b) (c) (C) (c) (d) (a) (b) (D) (d) (b) (a) (c)

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 75

*UGC NET Dec 2011, Paper III, original Q11*

> Find the Normalization transformation that maps a windows whose lowe r left is at (1,1) and Upper right (3, 5) onto a view port that has lower left corner at (0, 0) and Upper right corner at (½, ½). _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 76

*UGC NET Dec 2011, Paper III, original Q14*

> What is the basic difference between optimistic concurrency contr ol and other concurrency control technique. Describe the different phases of an optim istic concurrency control scheme. _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 77

*UGC NET Dec 2013, Paper II, original Q6*

> FAN IN of a component A is defined as (A) Number of components that can call or pass control to component A. (B) Number of components that are called by component A. (C) Number of components related to component A. (D) Number of components dependent on component A.

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 78

*UGC NET Dec 2013, Paper III, original Q59*

> Armstrong (1974) proposed systematic approach to derive functional dependencies. Match the following w.r.t. functional dependencies : List – I List – II a. Decom- position rule i. If X → Y and Z → W then {X, Z} → {Y, W} b. Union rule ii. If X → Y and {Y, W}→ Z then {X, W} → Z c. Com- position rule iii. If X → Y and X → Z then X → {Y, Z} d. Pseudo transitivity rule iv. If X → {Y, Z} then X → Y and X → Z Codes : a b c d (A) iii ii iv i (B) i iii iv ii (C) ii i iii iv (D) iv iii i ii

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 79

*UGC NET Dec 2013, Paper III, original Q60*

> Match the following : List – I List – II a. Secondary Index i. Functional Dependency b. Non- procedural Query Language ii. B-Tree c. Closure of set of Attributes iii. Relational Algebraic Operation d. Natural JOIN iv. Domain Calculus Codes : a b c d (A) i ii iv iii (B) ii i iv iii (C) i iii iv ii (D) ii iv i iii

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 80

*UGC NET June 2013, Paper III, original Q7*

> The “PROJECT” operator of a relational algebra creates a new table that has always (A) More columns than columns in original table (B) More rows than original table (C) Same number of rows as the original table (D) Same number of columns as the original table

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 81

*UGC NET Dec 2014, Paper II, original Q17*

> Which of the following is true ? I. Implementation of self-join is possible in SQL with table alias. II. Outer-join operation is basic operation in relational algebra. III. Natural join and outer join operations are equivalent. (A) I and II are correct. (B) II and III are correct. (C) Only III is correct. (D) Only I is correct.

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 82

*UGC NET Dec 2014, Paper II, original Q19*

> The best normal form of relation scheme R(A, B, C, D) along with the set of functional dependencies F = {AB → C, AB → D, C → A, D → B} is (A) Boyce-Codd Normal form (B) Third Normal form (C) Second Normal form (D) First Normal form

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 83

*UGC NET Dec 2014, Paper II, original Q20*

> Identify the minimal key for relational scheme R(A, B, C, D, E ) with functional dependencies F = {A → B, B → C, AC → D} (A) A (B) AE (C) BE (D) CE

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 84

*UGC NET Dec 2014, Paper III, original Q10*

> Let R = ABCDE is a relational scheme with function al dependency set F = {A → B, B → C, AC → D}. The attribute closures of A and E are (A) ABCD, φ (B) ABCD, E (C) Φ, φ (D) ABC, E

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 85

*UGC NET Dec 2014, Paper III, original Q12*

> Which of the following is false ? (A) Every binary relation is never be in BCNF. (B) Every BCNF relation is in 3NF. (C) 1 NF, 2 NF, 3 NF and BCNF are based on functional dependencies. (D) Multivalued Dependency (MVD) is a special case of Join Dependency (JD) .

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 86

*UGC NET Dec 2014, Paper III, original Q37*

> Which methods are utilized to control the access to an object in m ulti-threaded programming ? (A) Asynchronized methods (B) Synchronized methods (C) Serialized methods (D) None of the above

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 87

*UGC NET Dec 2015, Paper II, original Q20*

> A relation R = {A, B, C, D, E, F,G) is given with following set of functional dependencies : F = {AD → E, BE → F, B → C, AF → G} Which of the following is a candidate key ? (1) A (2) AB (3) ABC (4) ABD

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 88

*UGC NET Dec 2015, Paper III, original Q58*

> Which of the following statements regarding the features of the object-oriented approach to databases are true ? (a) The ability to develop more realistic models of the real world. (b) The ability to represent the world in a non-geometric way. (c) The ability to develop databases using natural language approaches. (d) The need to split objects into their component parts. (e) The ability to develop database models based on location rather than state and behaviour. Codes: (1) (a), (b) and (c) (2) (b), (c) and (d) (3) (a), (d) and (e) (4) (c), (d) and (e)

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 89

*UGC NET July 2016, Paper III, original Q7*

> Which of the following statements concer ning Object-Oriented databases is FALSE ? (1) Objects in an object-oriented database contain not only data but also methods for processing the data. (2) Object-oriented databases store computational instructions in the same place as the data. (3) Object-oriented databases are more adap t at handling structur ed (analytical) data than relational databases. (4) Object-oriented databases store more types of data than relational databases and access that data faster.

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 90

*UGC NET July 2016, Paper III, original Q9*

> Consider the relations R(A, B) and S(B, C) and the fo llowing four relational algebra queries over R and S : I. ΠA, B (R S) II. R ΠB(S) III. R ∩ (ΠA(R) × ΠB(S)) IV. ΠA,R.B (R × S) where R⋅B refers to the column B in table R. One can determine that : (1) I, III and IV are the same query. (2) II, III and IV are the same query. (3) I, II and IV are the same query. (4) I, II and III are the same query.

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 91

*UGC NET Jan 2017, Paper II, original Q19*

> Consider a schema R(MNPQ) and functional dependencies M → N, P → Q. Then the decomposition of R into R 1(MN) and R 2(PQ) is ________. (1) Dependency preserving but not lossless join (2) Dependency preserving and lossless join (3) Lossless join but not dependency preserving (4) Neither dependency preserving nor lossless join.

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 92

*UGC NET Dec 2018, original Q132*

> Consider a relation schema R = (A, B, C, D, E, F) on which the following functional dependencies hold : A →B B, C →D E→C D→A What are the candidate keys of R? . AE and BE Guide 91394342526. AE, BE and DE rsonal Exam | 91394342527. AEF, BEF and BCF AEF, BEF and DEF 91394342528. Single Dine Question pion: No Opion Orientation: Vernaype: MCQ

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 93

*UGC NET Dec 2019, original Q73*

> Find minimum number of tables required for converting the following entity relationship diagram into relational database? 1 M R12 R2 (1) 2 (2) onal Exam Guide. 4 (3) (4) 5 61547540990.2 61547540991.3 61547540992.4

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 94

*UGC NET June 2019, original Q81*

> Which of the following has same expressive power with regard to relational query language? (a) Relational algebra and domain relational calculus (b) Relational algebra and tuples relational calculus (c) Relational algebra and domain relational calculus restricted to safe expression (d) Relational algebra and tuples relational calculus restricted to safe expression repp 1. (a) and (b) only Your 2. (c) and (d) only 3. (a) and (c) only 4. (b) and (d) only 64635085660. 2 64635085661.3 64635085662.4

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 95

*UGC NET June 2019, original Q84*

> In relational databases, if relation R is in BCNF, then which of the following is true about relation R? 1. Ris in 4NF 2. R is not in INF 3. Ris in 2NF and not in 3NF 4. R is in 2NF and 3NF 64635085672.2 64635085673.3 64635085674.4

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 96

*UGC NET June 2019, original Q85*

> Which of the following key constraints is required for functioning of foreign key in the context of relational databases? 1. Unique key 2. Primary key Candidate key 4. Check key 64635085676. 2 64635085677.3 64635085678. 4 Single Lie Question pios: No bon Orenza neVer Type: MCQ Option Shufling : No

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 97

*UGC NET June 2019, original Q86*

> In relational database management, which of the following is/are property/properties of candidate key? P: Uniqueness Q: Irreducibility 1. P only 2. Q only Both Pand Q 4. Neither P nor Q 64635085680. 2 64635085681. 3 64635085682.4 Single Dine Onestion 6 Dion: No 0ibion Sent onesertzape: MCQ

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 98

*UGC NET Nov 2020, original Q64*

> Consider a relational schema S = (U.V.W,X,Y,Z) on which the following functional dependencies hold: [U → V.VW → X.Y → W, → U} Which are the candidate keys among following options? (1) UY. VY (2) UY. VY. XY (3) UYZ. VYZ. VWZ (4) UYZ, VYZ, XYZ 53622816754.2 53622816755.3 53622816756.4

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 99

*UGC NET Nov 2021, original Q65*

> A and B only Given the following STUDENT‐COURSE scheme: STUDENT (Rollno, Name, Courseno) COURSE (Courseno, Coursename, Capacity), where Rollno is the primary key of relation STUDENT and Courseno is the primary key of relation COURSE. Attribute Coursename of COURSE takes unique values only. The number of records in COURSE and STUDENT tables are 3 and 5 respectively. Following relational algebra query is executed: R=STUDENT X COURSE Match List I with List II in context to the above problem statement. List I List II A. Degree of table R I. 15 B. Cardinality of table R II. NIL C. Foreign key of relation STUDENT III. 6 D. Foreign key of relation COURSE IV. Courseno Choose the correct answer from the options given below: 1. A ‐III , B ‐I , C ‐IV , D ‐ II 2. A ‐I , B ‐III , C ‐IV , D ‐ II 3. A ‐I , B ‐III , C ‐IV , D ‐ II (options 2 and 4 are same) 4. A ‐I , B ‐III, C ‐II , D ‐ IV

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 100

*UGC NET Nov 2021, original Q67*

> (57, 53) Given a relation scheme R(x,y,z,w) with functional dependencies set F={x y, z w}. All attributes take single and atomic values only. A. Relation R is in First Normal FORM B. Relation R is in Second Normal FORM C. Primary key of R is xz Choose the correct answer from the options given below: 1. C only 2. B and C only 3. A and C only 4. B only

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 101

*UGC NET Nov 2021, original Q69*

> Total specialization and overlapping constraints A transaction may be in one of the following states during its execution life cycle in concurrent execution environment. A. FAILED B. TERMINATED C. PARTIALLY COMMITTED D. COMMITTED E. ACTIVE Given a transaction in active state during its execution, find its next transitioned state from the options given below: 1. A only 2. Either A or C only 3. C only 4. D only

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 102

*UGC NET Oct 2022, original Q51*

> Let R (ABCDEFGH) be a relation of functional dependencies is 1. 4→B,ACD → E,EF →G, and EF → H 2. A →B,ACD →E,EF →G,EF → Hand ACDF →G 3. A→ B,ACD→E,EF →G, EF → H and ACDF → E 4. LA → B.ABCD→ E.EF → H and EF →G

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 103

*UGC NET Oct 2022, original Q91*

> Read the following and Answer the questions: Consider the relational schema of sailors S. Reserves R and Boats B. Table 1: Sailors S Table 2 : Reserves R Sid Sname Ratting Age Sid Bid day 22 Dustin 7 45.0 22 101 10/10/98 29 Brutus 1 33.0 22 102 10/10/98 31 8 55.5 22 103 10/8/98 32 8 25.5 22 104 10/7/98 58 10 35.0 31 102 11/10/98 64 35.0 31 103 11/6/98 71 10 16.0 81 104 11/12/98 74 9 35.0 64 101| 9/5/98 85 3 25.5 64 102 918/98 95 3 63.5 74 103 9/8/98 Table 3: Boats B Bid Bname Color 101 Interlake blue 102 Interlake red 103 Clipper green 104 Marine red Which of the following relational algebra query computes the Sid's of sailors with age over 20 who have not reserved a red boat? 1. 7 sia (6 age - 20 Sailors) - I sid (6 color = red Boats) A Reserves Mr Sailors) 2. sia ((5 color = red A age - 20 (Boats M Sailors MReserves))) 3. sid ( age « 20 Sailors) - T sia ((Ô color = red Boats) D4 Reserves Sailors) 4. sia (6 age - 20 Sailors) ^ Tsia (Cô color = red Boats) M Reserves M Sailors)

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 104

*UGC NET Oct 2022, original Q92*

> Read the following and Answer the questions: Consider the relational schema of sailors S. Reserves R and Boats B. Table 1: Sailors S Table 2 : Reserves R Sid Sname Ratting Age Sid Bid day 22 Dustin 7 45.0 22 101 10/10/98 29 Brutus 1 33.0 22 102 10/10/98 31 Lubber 8 55.5 22 103 10/8/98 32 Andy 8 25.5 22 104 10/7/98 58 Rusty 10 35.0 31 102 11/10/98 64 Horatio 35.0 31 103 11/6/98 71 Zorba 10 16.0 81 104 11/12/98 74 Horatio 9 35.0 64 101| 9/5/98 85 3 25.5 64 102 918/98 95 3 63.5 74 103 9/8/98 Table 3: Boats B Bid Bname Color 101 Interlake blue 102 Interlake red 103 Clipper green 104 Marine red Which of the following relational algebra query/queries computes/compute the names of sailors who have reserved a red boat? Q1 It same ( color = red Boats) A Reserves Sailors) Q2 T sname (T sia ((Tbid 6 color = red Boats) M Reserves) ASailors) Q3 sname ((D color = red Reserves) Boats MSailors) 1. Both Q1 and Q2 2. Both Q2 and Q3 3. Only Q1 4. Only Q2

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 105

*UGC NET Oct 2022, original Q93*

> Read the following and Answer the questions: Consider the relational schema of sailors S. Reserves R and Boats B. Table 1: Sailors S Table 2 : Reserves R Sid Sname Ratting Age Sid Bid day 22 Dustin 7 8.85...... 22 101 10/10/98 29 Brutus 1 22 102 10/10/98 31 8 22 103 10/8/98 32 8 22 104 10/7/98 58 10 31 102 11/10/98 64 31 103 11/6/98 71 10 81 104 11/12/98 74 9 64 101| 9/5/98 85 3 64 102 918/98 95 3 74 103 9/8/98 Table 3: Boats B Bid Bname Color 101 Interlake blue 102 Interlake red 103 Clipper green 104 Marine red Which of the following relational algebra query/queries computes/compute the name of sailors who have reserved boat 1032 QI sname ((Ô bid = 103 Boats) M Sailors) Q2 sname (6 bid = 103 (Reserves» Sailors)) Q3 T sname (6 bid - 103 Reserves) Sailors) 1. Both Q1 and Q3 2. Both Q2 and Q3 3. Only Q3 4. Only Q2

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 106

*UGC NET Oct 2022, original Q94*

> Read the following and Answer the questions: Consider the relational schema of sailors S. Reserves R and Boats B. Table 1: Sailors S Table 2 : Reserves R Sid Sname Ratting Age Sid Bid day 22 Dustin 7 45.0 22 101 10/10/98 29 Brutus 1 33.0 22 102 10/10/98 31 Lubber 8 55.5 22 103 10/8/98 32 111L12 8 25.5 22 104 10/7/98 58 10 35.0 31 102 11/10/98 64 35.0 31 103 11/6/98 71 10 16.0 81 104 11/12/98 74 9 35.0 64 101| 9/5/98 85 3 25.5 64 102 918/98 95 63.5 74 103 9/8/9S Table 3: Boats B Bid Bname Color 101 Interlake blue 102 Interlake red 103 Clipper green 104 Marine red Which of the following relational algebra query computes the names of sailor who have reserved all boats? | 1. p. (Tempsids, (bid Reserves) / Thia Boats) I same (Tempsids) M Sailors) 2. p (Tempsids, (sid, hid Reserves) / T bid Boats) sname ((Tempsids) M Sailors) 3. p (Tempsids. (Jad Sailors) / Iba Boats) Taname (Tempsids) M Sailors) 4. p (Tempsids. (sid Reserves) / bid Boats) I sname ((Tempsids) A Boats)

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 107

*UGC NET Oct 2022, original Q95*

> Read the following and Answer the questions: Consider the relational schema of sailors S. Reserves R and Boats B. Table 1: Sailors S Table 2 : Reserves R Sid Sname Ratting Age Sid Bid day 22 Dustin 7 45.0 22 101 10/10/98 29 Brutus 1 33.0 22 102 10/10/98 31 Lubber 8 55.5 22 103 10/8/98 32 Andy 8 25.5 22 104 10/7/98 58 Rusty 10 35.0 31 102 11/10/98 64 Horatio 35.0 31 103 11/6/98 71 Zorba 10 16.0 81 104 11/12/98 74 Horatio 9 35.0 64 101| 9/5/98 85 3 25.5 64 102 918/98 95 3 63.5 74 103 9/8/98 Table 3: Boats B Bid Bname Color 101 Interlake blue 102 Interlake red 103 Clipper green 104 Marine red Which of the following relational algebra query computes the names of sailors who have reserved a red and a green boat? 1. P (Tempred, i sid (Ocolor = red Boats) 1 Reserves), p (Tempereen, I sid ( color = eren" Boata) Reserves)), I sname (Tempred n Tempgreen) M Sailors 2. P (Tempboats 2. (Scar = red Boats) r (Scolor = gren Boats)) Tenme (Tempboats 2 M Reserves) i sname (18 color = red Boats) ~ (color = green Boats) (Tempboats 2M Sailors M Reserves)) 4. p (Tempboats 2. (O color = red color = green Boats) sname (Tempboats M Sailors)

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 108

*UGC NET Aug 2024, original Q76*

> What is SQL primarily used for in the context of relational databases ? (1) To design user interfaces 2) To create and manipulate databases (3) To display data on web pages (4) To format printed reports 51/101

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 109

*UGC NET Aug 2024, original Q78*

> Consider a schema R(P,Q,R,S) and the following functional dependencies P→Q. Q→R, R→S, S→Q. Then decomposition of R, (P,Q), R2 (Q,R) and Rz (QS) is : (1) Dependency Preserving and lossless join (2) Lossless Join but not dependency preserving (3) Dependency preserving but not lossless Join (4) Not dependency preserving and not lossless join

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 110

*UGC NET Aug 2024, original Q79*

> Consider a relation schema R = (U, V, W, X, Y, Z), on which the following functional dependencies hold : (U→V, VW→X, Y→W; X→U} The candidate keys of Rare : (1) UY, VY (2) UY, VY, XY (3) UYZ, VYZ, VWZ (4) UYZ, VYZ, XYZ

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 111

*UGC NET Aug 2024, original Q81*

> In a schema R(A, B, C, D, E, F, G, H), each field of R contains only atomic values. F= (CH→G, A→BC, B→CFH, E→A, F→EG) is a set of functional dependencies so that F+ is exactly the set of FDs that holds R. The relation R is : (1) In 1NF, but not in 2NF (2) In 2NF, but not in 3NF (3) In 3NF, but not in BCNF (4) In BCNF

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 112

*UGC NET June 2025, original Q64*

> Consider R (A,B,C,D,E) be relation with following dependencies: C->F, E-> A, EC ->D, A ->B. Which of the following is a key for R? (1) CD (2) EC (3) AE (4) AC 12558919308.1 42558919309.2 42558919310.3 42558919311.4 Mandinry :ber: 64 be relation with following dependencies: C->F, E-> A, EC ->D, A ->B. Which of the following is a key for R? (1) CD (2) EC (4) AC (3) AE 42558919309.2 42558919310.3 42558919311.4 Mandatory : No

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 113

*UGC NET June 2025, original Q65*

> Consider the relation T1(A,B,C,D,E) with the dependencies (EB -C,D->E, EA ->B} and T2(A,B,C,D) with the dependencies (C->A,A ->B, A->D). Which of the following is TRUE? (1) T1 is in 3NF (2) T2 is in 3NF (3) T1 is not in 3NF (4) T1 is in 2NF 42558919313.2 42558919314.3 42558919315.4 Mandatory: No

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 114

*UGC NET June 2025, original Q66*

> Mandatory: No In a relational database, which one of the following is CORRECT: (1) A relation with only two attributes is always in BCNF (2) If all attributes of a relation are prime attributes then the relation is in BCNF. (3) Every relation has at least one non-prime attribute. (4) BCNF decomposition preserves functional dependencies. 42558919317.2 42558919318.3 42558919319.4 Mandatory: No

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 115

*UGC NET June 2025, original Q67*

> Consider the following three relations Employee (eid, eName), Comp(cid, cName), Own(eid, cid). Which of the following relational algebra expression return the set of eids who own all brands: (1) eid Teid,cid(Own)/ TIcid(Comp)) (2) Heid Teid(Own) x Tcid(Comp)) (3) eid(Teid,cid(Own) x T cid(Comp)) (4) eid Teid(Own) x (I cid cName (Own)/ cid(Comp))) 42558919321.2 42558919322.3 42558919323.4 Mandatory: No

**Basics to understand**

This question belongs to the ideas covered by **Normalization for Relational Databases**. Revise these foundations: Functional Dependencies and Normalization; Query Processing and Optimization; Transaction Processing; Concurrency Control; Recovery; Object and Object-Relational Databases; Security and Authorization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Normalization for Relational Databases questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-5"></a>

### 5. Enhanced Data Models (1 questions)

**What to master:** Temporal, Multimedia, Deductive, XML and Internet Databases; Mobile Databases; GIS; Genome Data Management; Distributed Databases; Client-Server Architectures.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

---

#### Question 116

*UGC NET June 2010, Paper II, original Q19*

> Which data management language component enabled the DBA to define the schema components ? (A) DML (B) Sub-schema DLL (C) Schema DLL (D) All of these

**Basics to understand**

This question belongs to the ideas covered by **Enhanced Data Models**. Revise these foundations: Temporal, Multimedia, Deductive, XML and Internet Databases; Mobile Databases; GIS; Genome Data Management; Distributed Databases; Client-Server Architectures.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Enhanced Data Models questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-6"></a>

### 6. Data Warehousing and Data Mining (19 questions)

**What to master:** Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

---

#### Question 117

*UGC NET Dec 2009, Paper II, original Q18*

> Match the following : (1) Determinants (a) No attribute can be added (2) Candidate key (b) Uniquely identified a row (3) Non-redundancy (c) A constraint between two attribute (4) Functional dependency (d) Group of attributes on the left hand s ide of arrow of function dependency. (A) 1 – d, 2 – b, 3 – a, 4 – c (B) 2 – d, 3 – a, 1 – b, 4 – c (C) 4 – a, 3 – b, 2 – c, 1 – d (D) 3 – a, 4 – b, 1 – c, 2 – d

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 118

*UGC NET June 2010, Paper II, original Q50*

> Data Mining uses ________, ________ and ________ to build effective predictive model. (i) Data set (ii) Information set (iii) Input set (iv) Process set (v) Output set (vi) Test set (A) (i), (ii) and (iv) (B) (ii), (iv) and (v) (C) (i), (v) and (vi) (D) (ii), (iii) and (v)

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 119

*UGC NET June 2012, Paper II, original Q42*

> Identify the incorrect statement : (A) The overall strategy drives the E-Commerce data warehousing strategy. (B) Data warehousing in an E-Commerce environment should be done in a classical manner. (C) E-Commerce opens up an entirely new world of web server. (D) E-Commerce security threats can be grouped into three major categories. www.solutionsadda.in

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 120

*UGC NET Dec 2014, Paper II, original Q47*

> Fact-less fact table in a data warehouse contains (A) only measures (B) only dimensions (C) keys and measures (D) only surrogate keys

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 121

*UGC NET Dec 2014, Paper II, original Q48*

> Which e-business model allows consumers to name their own price for products and services ? (A) B2 B (B) B2 G (C) C2 C (D) C2 B 49. __________ model is designed to bring prices down by increasing the number of customers who buy a particular product at once. (A) Economic Order Quantity (B) Inventory (C) Data Mining (D) Demand-Sensitive Pricing

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 122

*UGC NET Dec 2015, Paper II, original Q32*

> Suppose that from given statistics, it is known that meningitis causes stiff neck 50% of the time, that the proportion of persons having meningitis is 50000, and that the proportion of people having stiff neck is 20• Then the percentage of people who had meningitis and complain about stiff neck is: (1) 0.01% (2) 0.02% (3) 0.04% (4) 0.05% 33. _ system is market oriented and is used for data analysis by knowledge workers including Managers, Executives and Analysts. (1) OLTP (2) OLAP (3) Data System (4) Market System 34. allows selection of the relevant information necessary for the data warehouse. (1) The Top - Down View (2) Data Warehouse View (3) Datasource View (4) Business Query View

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 123

*UGC NET June 2015, Paper II, original Q20*

> For a weak entity set to be meaningful, it must be associated with another entity set in combination with some of their attribute values, is called as : (1) Neighbour Set (2) Strong Entity Set (3) Owner Entity Set (4) Weak Set J-8715 5 Paper-Il

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 124

*UGC NET July 2016, Paper II, original Q47*

> Consider the following two statements : (A) Business intelligence and Data warehousing is used for forecasting and Data mining. (B) Business intelligence and Da ta warehousing is used for analysis of large volumes of sales data. Which one of the following options is correct ? (1) (A) is true, (B) is false. (2) Both (A) and (B) are true. (3) (A) is false, (B) is true. (4) Both (A) and (B) are false.

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 125

*UGC NET July 2016, Paper II, original Q49*

> Consider the following two statements : (A) Data scrubling is a process to upgrade th e quality of data, before it is moved into Data warehouse. (B) Data scrubling is a proce ss of rejecting data from data warehouse to create indexes. Which one of the following options is correct ? (1) (A) is true, (B) is false. (2) (A) is false, (B) is true. (3) Both (A) and (B) are false. (4) Both (A) and (B) are true.

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 126

*UGC NET Dec 2018, original Q128*

> Data warehouse contains. _ data that is never found in operational environment. . Summary 91394342510. Encoded Encrypted 91394342511. Scripted 91394342512.

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 127

*UGC NET Dec 2019, original Q146*

> Minimal cover F" of functional dependency set Fis (1) F'= (A → B. A →C, BC → D, D→ E} (2) F'= (A → BC, B → D. D → E} (3) F'= {A → B, A → C, A → D. D→ E} (4) F'= {4 → B. A →C. B→D. C→ D. D→ E} Options : Exam Guide 61547541281.1 61547541282.2 61547541283. 61547541284. 4

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 128

*UGC NET Dec 2019, original Q147*

> Identify primary key of table R with functional dependency set F (1) BC (2) AD (3) A (4) AB 61547541286. 2 61547541287.3 61547541288. 4

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 129

*UGC NET Dec 2019, original Q149*

> Identify the redundant functional dependency in F (1) BC→D (2) D→E (3) A → D (4) A → BC 61547541294.2 61547541295.3 61547541296. 4

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 130

*UGC NET Aug 2024, original Q74*

> Fifth normal form is concerned with : (1) Join Dependency (2) Domain-Key (3) Multivalued dependency (4) Functional dependency

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 131

*UGC NET Aug 2024, original Q77*

> Which of the following best describes the structure of a relational database ? (1) Data organized into tables with rows and columns (2) Data organized into files and folders (3) Data organized into a hierarchical tree structure (4) Data organized into a network of interconnected nodes

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 132

*UGC NET June 2025, original Q124*

> Considering the following statements: A. Data transformation is involved in Datamining process. B. Online database is used in Data warehouse. C. Classification is a measure of accuracy. D. K-means clustering algorithm is based on the concept of minimizing the within-cluster variance. E. Pattern evaluation is a process to identify knowledge based on interestingness measure. Choose the correct answer from the options given below: 1. B, C, E Only B, D, E Only 3. A, C, E Only 4. A, C, D Only 42558919549.2 42558919550.3 42558919551.4 Mandatory: No

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 133

*UGC NET Dec 2025 session (Jan 2026), original Q72*

> Question Number: 72 mode, then which of the following is true for another transaction to? 1. to can lock d in shared (s) mode 2. to can lock d in exclusive (X) mode 3. to can lock d in intention-exclusive (IX) mode 4. to can lock d in intention-shared (IS) mode 6119878686. 2 6119878687.3 6119878688.4 uestion Number: 73

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 134

*UGC NET Dec 2025 session (Jan 2026), original Q73*

> Question Number : 73

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 135

*UGC NET Dec 2025 session (Jan 2026), original Q123*

> Question Number : 123

**Basics to understand**

This question belongs to the ideas covered by **Data Warehousing and Data Mining**. Revise these foundations: Warehouse Data Modeling; Concept Hierarchy; OLAP and OLTP; Association Rules; Classification; Clustering; Regression; SVM; K-Nearest Neighbour; HMM; Summarization; Dependency Modeling; Link, Sequence and Social-Network Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Warehousing and Data Mining questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-7"></a>

### 7. Big Data Systems (17 questions)

**What to master:** Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

---

#### Question 136

*UGC NET Dec 2009, Paper II, original Q45*

> The name of the transaction file shall be provided by the opera tor and the file that contains the edited transactions ready for execution shall be called (A) Batch. Exe (B) Trans. Exe (C) Opt. Exe (D) Edit.Exe

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 137

*UGC NET Dec 2013, Paper II, original Q12*

> GO BOTTOM and SKIP-3 commands are given one after another in a databa se file of 30 records. It shifts the control to (A) 28 th record (B) 27 th record (C) 3 rd record (D) 4 th record

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 138

*UGC NET Dec 2013, Paper II, original Q15*

> Data Integrity control uses _______ (A) Upper and lower limits on numeric data. (B) Passwords to prohibit unauthorised access to files. (C) Data dictionary to keep the data (D) Data dictionary to find last access of data

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 139

*UGC NET Dec 2013, Paper III, original Q31*

> Consider the formula in image processing R D = 1 – 1 CR Where C R = n1 n2 C R is called as compression ratio n1 and n 2 denotes the number of information carrying units in two datasets that represent the same information. In this situation R D is called as relative _________ of the first data set. (A) Data Compression (B) Data Redundancy (C) Data Relation (D) Data Representation

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 140

*UGC NET Dec 2014, Paper III, original Q7*

> Location transparency allows : I. Users to treat the data as if it is done at one location. II. Programmers to treat the data as if it is at one location. III. Managers to treat the data as if it is at one location. Which one of the following is correct ? (A) I, II and III (B) I and II only (C) II and III only (D) II only

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 141

*UGC NET Dec 2015, Paper II, original Q18*

> Which of the following provides the best description of an entity type? (1) A specific concrete object with a defined set of processes (eg. Jatin with diabetes) (2) A value given to a particular attribute (e.g. height - 230 cm) (3) A thing that we wish to collect data about zero or more, possibly real world examples of it may exist (4) A template for a group of things with the same set of characteristics that may exist in the real world

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 142

*UGC NET July 2016, Paper III, original Q69*

> In Unix, files can be protected by assigning e ach one a 9-bit mode called rights bits. Now, consider the following two statements: I. A mode of 641 (octal) means that the owner can read and write the file, other members of the owner’s group can read it, and users can execute only. II. A mode of 100 (octal) allo ws the owner to execute the file, but prohibits all other access. Which of the following options is correct with reference to above statements ? (1) Only I is correct. (2) Only II is correct. (3) Both I and II are correct. (4) Both I and II are incorrect.

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 143

*UGC NET Jan 2017, Paper III, original Q67*

> From the given data below : a b b a a b b a a b which one of the following is not a word in the dictionary create d by LZ-coding (the initial words are a, b) ? (1) a b (2) b b (3) b a (4) b a a b

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 144

*UGC NET June 2019, original Q88*

> Hadoop (a big data tool) works with number of related tools. Choose from the following, the common tools included into Hadoop : 1. MySQL, Google API and Map reduce 2. Map reduce, Scala and Hummer 3. Map reduce, H Base and Hive 4. Map reduce, Hummer and Heron 64635085688.2 64635085689. 3 Guide 64635085690.4

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 145

*UGC NET Nov 2020, original Q63*

> The data node and name node in HADOOP are (1) Worker Node and Master Node respectively (2) Master Node and Worker Node respectively (3) Both Worker Nodes (4) Both Master Nodes 53622816750. 2 53622816751.3 53622816752.4

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 146

*UGC NET Nov 2020, original Q98*

> In the context of concurrency control, a given pair of operations in a schedule is called conflict schedule if (A) At least one of the operations is write operation. (B) Both the operations are performed on the same data item. (C) Both the operations are performed by different transactions. (D) Both the operations are performed on different data items. Choose the correct answer from the options given below: (1) (A) and (B) only (2) (A). (B) and (C) only (3) (A). (C) and (D) only (4) (C) and (D) only 53622816890.2 53622816891.3 53622816892.4

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 147

*UGC NET Nov 2020, original Q145*

> If one track of data can be transferred per revolution, then what is the data transfer rate? (1) 2,850 KBytes/second (2) 4,500 KBytes/second (3) 5,700 KBytes/second (4) 2,250 KBytes/second 53622817078.2 53622817079.3 53622817080.4

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 148

*UGC NET Oct 2022, original Q65*

> In reference to Big data, consider the following database: (A) Memcached (B) Couch DB (C) Infinite graph Choose the most appropriate answer from the options given below: 1. (A) and (B) only 2. (B) and (C) only 3. (C) and (A) only 4. (A). (B) and (C)

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 149

*UGC NET June 2024, original Q95*

> Which of the following is/ are true in case of free locking? A. It ensures shorter waiting times. B. It ensures freedom from deadlock. C. Transaction can lock data items earlier Choose the correct answer from the options given below : D. It does not ensure greater amount of concurrency. (1) A and B Only (2)C and D Only 3} Band COnly (4) A and D Only

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 150

*UGC NET Dec 2025 session (Jan 2026), original Q75*

> Question Number : 75 command includes the following steps. Arrange the following steps in correct sequence. A. Copy item X from the program variable named X into its correct location in the buffer. B. Store the updated block from the buffer back to disk. C. Find the address of the disk block that contains item. D. Copy that disk block into a buffer in main memory. Choose the correct answer from the options given below: 1. C, D, A, B 2. A, C, D, B 3. C, A, B, D 4. D, B, C, A 6119878698.2 6119878699.3 6119878700.4 uestion Number : 76

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 151

*UGC NET Dec 2025 session (Jan 2026), original Q76*

> Question Number: 76

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 152

*UGC NET Dec 2025 session (Jan 2026), original Q129*

> Question Number : 129

**Basics to understand**

This question belongs to the ideas covered by **Big Data Systems**. Revise these foundations: Characteristics and Types of Big Data; Architecture; MapReduce and Hadoop; Distributed File System; HDFS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Big Data Systems questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-8"></a>

### 8. NoSQL (26 questions)

**What to master:** NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam lens:** Model the data constraints first, then choose relational algebra, SQL, normalization, transaction, or data-mining machinery.

**Reusable method:** For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically.

**High-yield rules:** 2NF removes partial dependency, 3NF controls transitive dependency, and BCNF requires every nontrivial determinant to be a superkey. Support and confidence use transaction counts.

**Common traps:** Do not confuse lossless join with dependency preservation, conflict serializability with recoverability, or WHERE filtering with HAVING filtering.

---

#### Question 153

*UGC NET June 2010, Paper II, original Q20*

> The PROJECT Command will create new table that has (A) more fields than the original table (B) more rows than original table (C) both (A) & (B) (D) none of these

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 154

*UGC NET Dec 2011, Paper III, original Q12*

> Consider the following piece of Knowledge: Mary, Micky and John ar e members of rotary club. Every rotary club member who is not a swimmer is a mountain climber. Mountain climber do not like rains. Any one who does not like water is not a swimmer. Micky dislikes whatever Mary likes and likes whateve r Mary dislikes. Mary likes rain and water. (a) Represent this Knowledge as predicate statement. (b) Answer the query. Is there a member of Rotary club who is not a mountain climber but a swimmer using resolution method. _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 155

*UGC NET Dec 2012, Paper II, original Q145*

> What will be the location of 79? (A) OPTIONAL Set (B) FIXED Set (A) 1 (C) MANDATOR Set (B) 2 (D) All of the above (C) 3 (D) 4

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 156

*UGC NET June 2015, Paper II, original Q17*

> Which of the following concurrency protocol ensures both conflict serializability and freedom from deadlock ? (a) z - phase Locking (b) Time stamp - ordering (1) Both (a) and (b) (2) (a) only (3) (b) only (4) Neither (a) nor (b)

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 157

*UGC NET June 2015, Paper III, original Q22*

> The clausal form of the disjunctive normal form - A v - Bv - Cv D is: (1) АлВл С → D (2) AvBv CvD → true (3) Алв^С^D→ true 4) Ал Вл Сл D → false

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 158

*UGC NET Jan 2017, Paper III, original Q7*

> Consider following schedules involving two transactions : S 1 : r1(X); r1(Y); r2(X); r2(Y); w2(Y); w1(X) S 2 : r1(X); r2(X); r2(Y); w2(Y); r1(Y); w1(X) Which of the following statement is true ? (1) Both S 1 and S2 are conflict serializable. (2) S 1 is conflict serializable and S2 is not conflict serializable. (3) S 1 is not conflict serializable and S2 is conflict serializable. (4) Both S 1 and S2 are not conflict serializable.

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 159

*UGC NET July 2018, Paper II, original Q61*

> In RDBMS, which type of Join returns all rows that satisfy the join condition ? (1) Inner Join (2) Outer Join (3) Semi Join (4) Anti Join

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 160

*UGC NET July 2018, Paper II, original Q65*

> Consider the following schedules involving two transactions. S1 : r 1(X) ; r 1(Y) ; r 2(X) ; r 2(Y) ; w 2(Y) ; w 1(X) S2 : r 1(X) ; r 2(X) ; r 2(Y) ; w 2(Y) ; r 1(Y) ; w 1(X) Which one of the following statements is correct with respect to abov e ? (1) Both S1 and S2 are conflict serializable. (2) Both S1 and S2 are not conflict serializable. (3) S1 is conflict serializable and S2 is not conflict serializable. (4) S1 is not conflict serializable and S2 is conflict serializable.

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 161

*UGC NET Dec 2019, original Q71*

> Given two tables R1(x. y) and R2 (y, z) with 50 and 30 number of tuples respectively. Find maximum number of tuples in the output of natural join between tables R1 and R2 i.e. R1 * R2? (* - Natural Join) (1) 30 (2) 20 (3) 50 (4) 1500 61547540982.2 61547540983.3 61547540984.4

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 162

*UGC NET Dec 2019, original Q72*

> Given two tables EMPLOYEE (EID, ENAME, DEPTNO) DEPARTMENT (DEPTNO. DEPTNAME) Guide Find the most appropriate statement of the given query : Select count (*) 'total xam from EMPLOYEE ona where DEPTNO IN (D1. D2) S group by DEPTNO having count (*) >5 (1) Total number of employees in each department D1 and D2 (2) Total number of employees of department D1 and D2 if their total is >5 (3) Display total number of employees in both departments D1 and D2 (4) The output of the query must have atleast two rows 61547540986. 2 61547540987. 3 61547540988. 4

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 163

*UGC NET Dec 2019, original Q148*

> Identify the normal form in which relation R belong to (1) 1 NF (2) 2 NF (3) 3 NF (4) BCNF 61547541290. 2 61547541291. 3 61547541292. 4

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 164

*UGC NET June 2019, original Q56*

> Which of the following is principal conjunctive normal form for [(pVg)^7P→]9]? pvlg 2. pva 3. 1pvg 4. 64635085560. 2 64635085561.3

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 165

*UGC NET Nov 2020, original Q88*

> What kind of clauses are available in conjunctive normal form? (1) Disjunction of literals (2) Disjunction of variables (3) Conjunction of literals (4) Conjunction of variables. 53622816850.2 53622816851. 3 53622816852. 4

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 166

*UGC NET Nov 2020, original Q97*

> Concerning phong shading and Gouraud shading in a SD scene. which of the following statements are true? (A) Gouraud shading requires more computation than phong shading. (B) Gouraud shading linearly interpolates the color of an interior pixel from the color at the vertices. (C) Phong shading interpolates over the normal vectors specified at the vertices. Choose the correct answer from the options given below: (1) (A) and (B) only (2) (A) and (C) only (3) (B) and (C) only (4) (A), (B) and (C) 53622816886.2 53622816887.3 53622816888.4

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 167

*UGC NET Nov 2020, original Q147*

> Given below are two statements to find the sum of salaries of all employees of the English department as well as the maximum, minimum and average salary in English department. STATEMENT I: SELECT SUM (SALARY). MAX (SALARY, MIN (SALARY). AVG (SALARY) FROM EMPLOYEE, DEPARTMENT WHERE DEPTNO=DID AND DNAME-'ENGLISH: STATEMENT II: SELECT SUM (SALARY), MAX (SALARY), MIN (SALARY). AVG (SALARY) FROM EMPLOYEE, DEPARTMENT WHERE DNAME-'ENGLISH: In the light of the above statements, choose the correct answer from the options given below (1) Both Statement I and Statement Il are true (2) Both Statement I and Statement II are false (3) Statement I is correct but Statement II is false (4) Statement I is incorrect but Statement Il is true 53622817086.2 53622817087.3 53622817088.4

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 168

*UGC NET Nov 2021, original Q24*

> 1024 A company stores products in a warehouse. Storage bins in this warehouse are specified by their aisle, location in the aisle, and self. There are 50 aisles, 85 horizontal locations in each aisle, and 5 shelves throughout the warehouse. What is the least number of products the company can have so that at least two products must be stored in the same bin? 1. 251 2. 426 3. 4251 4. 21251

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 169

*UGC NET Nov 2021, original Q64*

> Given the following STUDENT‐COURSE scheme: STUDENT (Rollno, Name, courseno) COURSE (courseno, coursename, capacity), where Rollno is the primary key of relation STUDENT and courseno is the primary key of relation COURSE. Attribute coursename of COURSE takes unique values only. Which of the following query(ies) will find total number of students enrolled in each course, along with its coursename. A. SELECT coursename, count(*) 'total' from STUDENT natural join COURSE group by coursename; B. SELECT C.coursename, count(*) 'total' from STUDENT S, COURSE C where S.courseno=C.courseno group by coursename; C. SELECT coursename, count(*) 'total' from COURSE C where courseno in (SELECT courseno from STUDENT); 1. A and B only 2. C only 3. A only 4. B only

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 170

*UGC NET Oct 2022, original Q78*

> Consider the following statements: Statement I: Conservative 2 PL is a deadlock-free protocol. Statement II: Thomas's write rule enforces conflict serializability. Statement III: Timestamp ordering protocol ensures serializability based on the order of transaction timestamps. Which of the following is correct? 2. Statement I, Statement II true and Statement II false 3. Statement I, Statement II false and Statement III true 4. Statement I, Statement II and Statement III true

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 171

*UGC NET Oct 2022, original Q79*

> Consider the following statements: Statement I: Composite attributes cannot be divided into smaller subparts. Statement II: Complex attribute is formed by nesting composite attributes and multi- valued attributes in an arbitrary way. Statement III: A derived attribute is an attribute whose values are computed from other attribute. Which of the following is correct? 1. Statement I. Statement II and Statement III are true 2. Statement I true and Statement II. Statement III false Statement I, Statement II true and Statement III false 4. Statement I false and Statement II. Statement III true

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 172

*UGC NET Dec 2022 session, 11 Mar 2023 Shift 2, original Q2*

> A candidate key for which no proper subset is also a candidate key is called a super key.

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 173

*UGC NET Dec 2022 session, 15 Mar 2023 Shift 1, original Q2*

> Select s.rollno, s.name From student s, enrollment e Where e.rollno = s.rollno and e.courseid = ALL (select precourseid from prerequisite p where p.courseid = "324")

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 174

*UGC NET Dec 2022 session, 15 Mar 2023 Shift 1, original Q3*

> Select s.rollno, s.name From student s Where NOT EXISTS (select * prerequisite p where p.courseid = "324") and NOT EXISTS (select * from enrollment e where e.courseid = p.precourseid and e.rollno = s.rollno))

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 175

*UGC NET Aug 2024, original Q82*

> Consider the transactions Ty, Tz, Tz and the schedules Sy and S2 given below. T2: 12(y); 12(Z); W2(z) Тз : [з(У); Із(x); W3(У) S1 : 1,(x); "z(У); Tz(x); Iz(Y); T2(Z); W3(Y); W3(z); "(z); w1(x); w,(z) S2: 11(x); 13(y); 12(y); [3(x); rj(z); 1½(z); W3(y); w, (x); W2(z); w,(z) Which one of the following statements about the schedules is TRUE? (1) Only S, is conflict-serializable (2) Only S2 is conflict-serializable (3) Both S, and 52 are conflict-serializable Neither S, nor S, is conflict-serializable

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 176

*UGC NET June 2025, original Q89*

> Given that n refers to learning rate and x; refers to the i input to the neuron, Which of the followings most suitably describes the weight updation rule of a Kohonen SOM? (where 'I' refers to the j" neuron in the lattice) 1. Wi (new) = (1-n)*w;(old) + n*x; 2. Wij (new) = n*wi(old) + (1-n)*x; 3. Wij (new) = (1-n)*wij(old) + xi 4. Wij (new) = wi(old) + n*x; 42558919408.1 42558919410. 3 42558919411.4

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 177

*UGC NET June 2025, original Q125*

> Considering the following statements: A. A non-serial schedule is said to be conflict serializable, if it is conflict-equivalent to some serial schedule. B. A non-serial schedule is said to be view serializable if it is view-equivalent to some serial schedule. C. A schedule is said to be serial, if instructions of participating transactions are chronologically interleaved with each other. D. A conflict-serializable schedule will be view-serializable also but vice-versa may not be true. Choose the correct answer from the options given below: 1. A, B, C, D 2. A, B, C Only 3. A, B, D Only 4. B, C, D Only 42558919553.2 42558919554. 3 42558919555.4

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 178

*UGC NET Dec 2025 session (Jan 2026), original Q52*

> Question Number : 52 divides the order of the group (Z13, x) Reason R: The order of a subgroup of a group divides the order of the group. In the light of the above statements, choose the most appropriate answer from the options given below 1. Both A and Rare correct and R is the correct explanation of A 2. Both A and R are correct but R is NOT the correct explanation of A 3. A is correct but Ris not correct 4. A is not correct but R is correct 6119878610.2 6119878611.3 6119878612.4

**Basics to understand**

This question belongs to the ideas covered by **NoSQL**. Revise these foundations: NoSQL and Query Optimization; Products; Querying and Management; Indexing and Ordering Data Sets; NoSQL in the Cloud.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For NoSQL questions: For dependencies compute closures and candidate keys; for schedules draw conflicts; for SQL evaluate FROM/WHERE/GROUP/HAVING/SELECT logically. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer and detailed explanation**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

## Coverage and quality notes

- Recovered question blocks in this unit: **178**
- Chapter placements with direct keyword support: **158**
- Chapter placements needing manual review: **20**
- OCR may flatten mathematical notation, tables, code indentation, and figures. Full audit references are retained in the structured data.
- Some combined Paper 1/Paper 2 scans and older papers lack a trustworthy embedded key. Such questions remain pending rather than receiving guessed answers.

---

[Back to contents](#contents) · [All units](README.md) · [Project home](../README.md)

