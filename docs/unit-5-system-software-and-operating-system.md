# Unit 5: System Software and Operating System

[Project home](../README.md) · [All units](README.md) · [Official syllabus](syllabus.md)

## Contents

- [How to use this guide](#status-and-use)
- [Unit-wide exam playbook](#unit-wide-exam-playbook)
- [1. System Software](#chapter-1)
- [2. Basics of Operating Systems](#chapter-2)
- [3. Process Management](#chapter-3)
- [4. Threads](#chapter-4)
- [5. CPU Scheduling](#chapter-5)
- [6. Deadlocks](#chapter-6)
- [7. Memory Management](#chapter-7)
- [8. Storage Management](#chapter-8)
- [9. File and Input/Output Systems](#chapter-9)
- [10. Security](#chapter-10)
- [11. Virtual Machines](#chapter-11)
- [12. Linux Operating Systems](#chapter-12)
- [13. Windows Operating Systems](#chapter-13)
- [14. Distributed Systems](#chapter-14)
- [Coverage and quality notes](#coverage-and-quality-notes)

## Status and use

This guide contains all **182 question blocks currently recoverable and assigned to Unit 5** from the local UGC NET archive. Questions are arranged chapter-wise and numbered continuously through the unit.

> [!WARNING]
> This is a working extraction inventory, not a complete solved guide. **0 answers are validated and 182 remain pending** in this unit. Some unit and chapter placements use fallback routing, and OCR or missing figures can make questions incomplete.

Use this file for question discovery and broad chapter revision. The chapter notes and exam methods are general, not question-specific solutions. Full source paths, PDF pages and classification states remain in the structured data for auditing.

## Unit-wide exam playbook

- **Core idea:** Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.
- **Method:** Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.
- **Rules/formulas:** Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.
- **Frequent traps:** Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.

## Chapter-wise concepts and PYQs

<a id="chapter-1"></a>

### 1. System Software (10 questions)

**What to master:** Machine, Assembly and High-Level Languages; Compilers and Interpreters; Loading, Linking and Relocation; Macros; Debuggers.

**Exam lens:** Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.

**Reusable method:** Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.

**High-yield rules:** Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.

**Common traps:** Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.

---

#### Question 1

*UGC NET Dec 2009, Paper II, original Q31*

> In an absolute loading scheme which loader function is accomplishe d by assembler ?

**Options**

- **A.** re-allocation
- **B.** allocation
- **C.** linking
- **D.** loading

**Chapter foundations**

This question belongs to the ideas covered by **System Software**. Revise these foundations: Machine, Assembly and High-Level Languages; Compilers and Interpreters; Loading, Linking and Relocation; Macros; Debuggers.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For System Software questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 2

*UGC NET June 2010, Paper II, original Q31*

> In an absolute loading scheme, which loader function is accomplished by a loader ?

**Options**

- **A.** Re-allocation
- **B.** Allocation
- **C.** Linking
- **D.** Loading

**Chapter foundations**

This question belongs to the ideas covered by **System Software**. Revise these foundations: Machine, Assembly and High-Level Languages; Compilers and Interpreters; Loading, Linking and Relocation; Macros; Debuggers.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For System Software questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 3

*UGC NET June 2010, Paper II, original Q45*

> Applications-software

**Options**

- **A.** is used to control the operating system
- **B.** includes programs designed to help programmers
- **C.** performs a specific task for computer users
- **D.** all of the above

**Chapter foundations**

This question belongs to the ideas covered by **System Software**. Revise these foundations: Machine, Assembly and High-Level Languages; Compilers and Interpreters; Loading, Linking and Relocation; Macros; Debuggers.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For System Software questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 4

*UGC NET Dec 2011, Paper III, original Q7*

> Can a system detect that some of its processes are starving ? If yes, then explain how it can ? If no, then explain how the system can deal with starvation problem. _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________

**Chapter foundations**

This question belongs to the ideas covered by **System Software**. Revise these foundations: Machine, Assembly and High-Level Languages; Compilers and Interpreters; Loading, Linking and Relocation; Macros; Debuggers.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For System Software questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 5

*UGC NET Dec 2015, Paper II, original Q17*

> In C+t, which system - provided function is called when no handler is provided to deal with an exception ?

**Options**

1. terminate ( )
2. unexpected ()
3. abort ()
4. kill ()

**Chapter foundations**

This question belongs to the ideas covered by **System Software**. Revise these foundations: Machine, Assembly and High-Level Languages; Compilers and Interpreters; Loading, Linking and Relocation; Macros; Debuggers.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For System Software questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 6

*UGC NET July 2016, Paper III, original Q68*

> Which of the following statement is not corr ect with reference to cron daemon in UNIX O.S. ?

**Options**

1. The cron daemon is the standard tool for running commands on a pre-determined schedule.
2. It starts when the system boots and runs as long as the system is up.
3. Cron reads configuration files that contain list of co mmand lines and the times at which they invoked.
4. Crontab for individua l users are not stored.

**Chapter foundations**

This question belongs to the ideas covered by **System Software**. Revise these foundations: Machine, Assembly and High-Level Languages; Compilers and Interpreters; Loading, Linking and Relocation; Macros; Debuggers.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For System Software questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 7

*UGC NET Jan 2017, Paper II, original Q35*

> Which of the following statement(s) regarding a linker software is/are true ? I. A function of a linker is to combine several object modules int o a single load module. II A function of a linker is to replace absolute references i n an object module by symbolic references to locations in other modules.

**Options**

1. Only I
2. Only II
3. Both I and II
4. Neither I nor II

**Chapter foundations**

This question belongs to the ideas covered by **System Software**. Revise these foundations: Machine, Assembly and High-Level Languages; Compilers and Interpreters; Loading, Linking and Relocation; Macros; Debuggers.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For System Software questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 8

*UGC NET Dec 2019, original Q78*

> Suppose a system has 12 magnetic tape drives and at time to. three processes are allotted tape drives out of their need as given below : Maximum Needs Current Needs Po 10 5 P1 4 2 P2 9 2 At time to. the system is in safe state. Which of the following is safe sequence so that deadlock is avoided?
>
> **Additional extracted choices — check the source page:**
>
> 1. _Missing in extracted text_
> 2. Pr. Po: P2)
> 3. (P2• P1. Po)
> 4. (Po: P2. P1) 61547541010. 2 61547541011.3 61547541012.4

**Chapter foundations**

This question belongs to the ideas covered by **System Software**. Revise these foundations: Machine, Assembly and High-Level Languages; Compilers and Interpreters; Loading, Linking and Relocation; Macros; Debuggers.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For System Software questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 9

*UGC NET Nov 2020, original Q66*

> Consider a disk system having 60 cylinders. Disk requests are received by a disk drive for cylinders 10. 22. 20. 2. 40, 6 and 38, in that order. Assuming the disk head is currently at cylinder 20, what is the time taken to satisfy all the requests if it takes 2 milliseconds to move from one cylinder to adjacent one and Shortest Seek Time First (SSTF) algorithm is used?

**Options**

1. 240 milliseconds
2. 96 milliseconds
3. 120 milliseconds
4. 112 milliseconds 53622816762.2 53622816763.3 53622816764.4

**Chapter foundations**

This question belongs to the ideas covered by **System Software**. Revise these foundations: Machine, Assembly and High-Level Languages; Compilers and Interpreters; Loading, Linking and Relocation; Macros; Debuggers.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For System Software questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 10

*UGC NET Oct 2022, original Q57*

> Consider the following: List I List II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Activation record (1) Linking Loader
> - **B.** Location counter (II) Garbage Collection
> - **C.** Reference count (III) Subroutine Call
> - **D.** Address relocation (IV) Assembler Which of the following is correct matching? 1.
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(I).
> - **B.** -(IV).
> - **C.** -I).
> - **D.** -(IL) 2.
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(IV).
> - **B.** -(III,
> - **C.** -I.
> - **D.** -(I) 3.
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(IV).
> - **B.** -(II,
> - **C.** -II.
> - **D.** -(D 4.

**Options**

- **A.** -I.
- **B.** -I).
- **C.** -(L).
- **D.** -(IV)

**Chapter foundations**

This question belongs to the ideas covered by **System Software**. Revise these foundations: Machine, Assembly and High-Level Languages; Compilers and Interpreters; Loading, Linking and Relocation; Macros; Debuggers.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For System Software questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-2"></a>

### 2. Basics of Operating Systems (0 questions)

**What to master:** Structure, Operations and Services; System Calls; Design and Implementation; Booting.

**Exam lens:** Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.

**Reusable method:** Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.

**High-yield rules:** Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.

**Common traps:** Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.

_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._

<a id="chapter-3"></a>

### 3. Process Management (25 questions)

**What to master:** Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam lens:** Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.

**Reusable method:** Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.

**High-yield rules:** Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.

**Common traps:** Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.

---

#### Question 11

*UGC NET Dec 2009, Paper II, original Q36*

> In the process management Round-robin method is essentially the pre -emptive version of _________

**Options**

- **A.** FILO
- **B.** FIFO
- **C.** SSF
- **D.** Longest time first

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 12

*UGC NET June 2010, Paper II, original Q39*

> In order to allow only one process to enter its critical section, binary semaphore are initialized to

**Options**

- **A.** 0
- **B.** 1
- **C.** 2
- **D.** 3

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 13

*UGC NET June 2012, Paper II, original Q21*

> Key process areas of CMM level 4 are also classified by a process which is

**Options**

- **A.** CMM level 2
- **B.** CMM level 3
- **C.** CMM level 5
- **D.** All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 14

*UGC NET June 2012, Paper II, original Q31*

> Resources are allocated to the process on non-sharable basis is

**Options**

- **A.** mutual exclusion
- **B.** hold and wait
- **C.** no pre-emption
- **D.** circular wait

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 15

*UGC NET Dec 2013, Paper II, original Q29*

> The process of assigning load addresses to the va rious parts of the program and adjusting the code and data in the program to reflect the assigned addresses is called _______.

**Options**

- **A.** Symbol resolution
- **B.** Parsing
- **C.** Assembly
- **D.** Relocation

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 16

*UGC NET Dec 2013, Paper III, original Q74*

> Which of the following commands would return process_id of sleep command ?

**Options**

- **A.** Sleep 1 and echo $?
- **B.** Sleep 1 and echo $#
- **C.** Sleep 1 and echo $ ×
- **D.** Sleep 1 and echo $!

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 17

*UGC NET June 2013, Paper III, original Q60*

> Suppose S and Q are two semaphores initialized to 1. P1 and P2 are two processes which are sharing resources. P1 has statements P2 has statements wait(S) ; wait(Q) ; wait(Q) ; wait(S) ; critical- section 1; critical- section 2; signal(S) ; signal(Q) ; signal(Q) ; signal(S) ; Their execution may sometimes lead to an undesirable situation called

**Options**

- **A.** Starvation
- **B.** Race condition
- **C.** Multithreading
- **D.** Deadlock

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 18

*UGC NET June 2013, Paper III, original Q69*

> If we convert ∃u ∀v ∀x ∃y (P(f(u),v, x, y) → Q(u,v,y)) to ∀v ∀x (P(f(a),v, x, g(v,x)) → Q(a,v,g(v,x))) This process is known as

**Options**

- **A.** Simplification
- **B.** Unification
- **C.** Skolemization
- **D.** Resolution

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 19

*UGC NET Dec 2014, Paper II, original Q38*

> Which of the following conditions does not hold good for a solution to a cri tical section problem ?

**Options**

- **A.** No assumptions may be made about speeds or the number of CPUs.
- **B.** No two processes may be simultaneously inside their critical secti ons.
- **C.** Processes running outside its critical section may block other process es.
- **D.** Processes do not wait forever to enter its critical section.

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 20

*UGC NET Dec 2015, Paper III, original Q39*

> Consider a system with twelve magnetic tape drives and three processes P1, P2 and P3. Process Py requires maximum ten tape drives, process P2 may need as many as four tape drives and Pz may need upto nine tape drives. Suppose that at time ty, process P, is holding five tape drives, process P2 is holding two tape drives and process Pz is holding three tape drives. At time ty, system is in :

**Options**

1. safe state
2. unsafe state
3. deadlocked state
4. starvation state

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 21

*UGC NET June 2015, Paper III, original Q15*

> The process of dividing an analog signal into a string of discrete outputs, each of constant amplitude, is called :

**Options**

1. Strobing
2. Amplification
3. Conditioning
4. Quantization

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 22

*UGC NET July 2016, Paper II, original Q37*

> Suppose there are four proce sses in execution with 12 inst ances of a Resource R in a system. The maximum need of each process a nd current allocation are given below : Process Max. Need Current Allocation P1 8 3 P2 9 4 P3 5 2 P4 3 1 With reference to current allocation, is system safe ? If so, what is the safe sequence ?

**Options**

1. No
2. Yes, P 1P2P3P4
3. Yes, P 4P3P1P2
4. Yes, P 2P1P3P4

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 23

*UGC NET Jan 2017, Paper III, original Q52*

> Some of the criteria for calcula tion of priority of a process are : a. Processor utilization by an individual process. b. Weight assigned to a user or group of users. c. Processor utilization by a user or group of processes In fair share scheduler, priority is calculated based on :

**Options**

1. only (a) and (b)
2. only (a) and (c)
3. (a), (b) and (c)
4. only (b) and (c)

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 24

*UGC NET Jan 2017, Paper III, original Q53*

> One of the disadvantages of user level thre ads compared to Kernel level threads is

**Options**

1. If a user level thread of a process execu tes a system call, all threads in that process are blocked.
2. Scheduling is application dependent.
3. Thread switching doesn’t re quire kernel mode privileges.
4. The library procedures invoked for thr ead management in us er level threads are local procedures.

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 25

*UGC NET Jan 2017, Paper III, original Q54*

> Which statement is not correct about “init” process in Unix ?

**Options**

1. It is generally the pa rent of the login shell.
2. It has PID 1.
3. It is the first process in the system.
4. Init forks and execs a ‘getty’ process at every port connected to a terminal.

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 26

*UGC NET Nov 2017, Paper II, original Q40*

> Two atomic operations permissible on Semaphores are __________ and ___ _______.

**Options**

1. wait, stop
2. wait, hold
3. hold, signal
4. wait, signal

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 27

*UGC NET Dec 2018, original Q120*

> Suppose a system has 12 instances of some resource with n processes competing for that resource. Each process may require 4 instances of the resource. The maximum value of n for which the system never enters into deadlock is 91394342478. 4 91394342479 5 91394342480. 6

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 28

*UGC NET Dec 2018, original Q124*

> Sure po, and are co prating pales gaging Mutual Exclusion condition. Then, . Both P' and 'R' execute in critical section. 91394342494. Neither 'P' nor 'R' executes in their critical section. 91394342495. 'P' executes in critical section. 91394342496. 'R' executes in critical section. uestion Number: 125

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 29

*UGC NET June 2019, original Q93*

> Consider that a process has been allocated 3 frames and has a sequence of page referencing as 1, 2, 1, 3, 7, 4, 5, 6, 3, 1. What shall be the difference in page faults for the above string using the algorithms of LRU and optimal page replacement for referencing the string? 1. 2 0 1 3 64635085708. 2 64635085709.3 64635085710. 4

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 30

*UGC NET June 2019, original Q98*

> A computer has six tape drives with n processes competing for them. Each process may need two drives. What is the maximum value of n for the system to be deadlock free?

**Options**

1. 5 O
2. 4
3. 3
4. 6 64635085728. 2 64635085729.3 64635085730. 4

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 31

*UGC NET Aug 2024, original Q112*

> Which of the following statements are TRUE about mutual exclusion in concurrent programming?

**Options**

- **A.** Mutual exclusion ensures that only one process can be in a critical section at any given time.
- **B.** Mutual exclusion are designed to prevent conflicts and ensure that only one process can access shared resources at a time.
- **C.** Mutual exclusion can use various algorithms to ensure that processes do not enter the critical section simultaneously.
- **D.** Mutual exclusion allows multiple processes to access the critical section simultaneously to improve performance. Choose the correct answer from the options given below : (1) (A), (B), (C) Only (2) (B), (C), (D) Only 3) B)D, (A) Only (4) (A), (C), (D) Only

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 32

*UGC NET Aug 2024, original Q145*

> Which of the following is/are the application area(s) of ANN ?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Natural Language Processing
> - **B.** Image Processing
> - **C.** Pattern Recognition
> - **D.** Speech Recognition Choose the correct answer from the options given below : (1) (A) and (B) Only (2) (B) and (C) Only (3) (A), (B) and (C) Only (4)

**Options**

- **A.** ,
- **B.** ,
- **C.** and
- **D.** Sub-Section Number : 3 Sub-Section Id : 533072154 Question Shuffling Allowed : No Question Label: Comprehension Read the below passage and answer the questions. The Banker's Algorithm is a critical deadlock avoidance method in operating systems, designed to facilitate resource allocation without causing deadlock. It operates by maintaining information about the maximum resources. Each process may require, the current allocated resources and the available resources in the system. The algorithm checks each resource request to determine, if granting it would leave the system in a safe state, meaning that there is always a sequence in which all processes can complete their execution without getting stuck due to resource unavailability. Each process must specify its maximum demand for each resource type before it starts execution. When a process requests additional resources, the algorithm checks if granting the request will keep the system in a safe state. If so, the resources are allocated otherwise the process must wait until its request can be safely fulfilled. Sub questions

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 33

*UGC NET June 2024, original Q112*

> IP is responsible for communication.

**Options**

1. Node-to-node, Host-to-host
2. Process-to process, Host-to-host
3. Socket-to-socket, Host-to-node
4. Host-to-Host, Process-to-process

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 34

*UGC NET June 2025, original Q113*

> Identify the correct statement(s) from the followings with respect to Spinlock Semaphores
>
> **Additional extracted choices — check the source page:**
>
> - **A.** The name refers to busy waiting semaphores.
> - **B.** They are not useful when the locks are to be held for a short duration of time.
> - **C.** It may require multiple context switches when a process waits on a lock.
> - **D.** They are often employed on Unprocessor systems. Choose the correct answer from the options given below:

**Options**

1. A Only
2. D Only
3. B, D Only
4. A, C and D Only 42558919505.2 42558919506. 3 42558919507.4

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 35

*UGC NET Dec 2025 session (Jan 2026), original Q82*

> Question Number : 82

**Chapter foundations**

This question belongs to the ideas covered by **Process Management**. Revise these foundations: Scheduling and Operations; IPC; Client-Server Communication; Synchronization; Critical-Section Problem; Peterson's Solution; Semaphores.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Process Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-4"></a>

### 4. Threads (0 questions)

**What to master:** Multicore Programming; Multithreading Models; Thread Libraries; Implicit Threading; Threading Issues.

**Exam lens:** Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.

**Reusable method:** Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.

**High-yield rules:** Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.

**Common traps:** Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.

_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._

<a id="chapter-5"></a>

### 5. CPU Scheduling (24 questions)

**What to master:** Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam lens:** Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.

**Reusable method:** Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.

**High-yield rules:** Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.

**Common traps:** Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.

---

#### Question 36

*UGC NET June 2010, Paper II, original Q36*

> Match the following : (a) Disk scheduling

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 37

*UGC NET Dec 2012, Paper II, original Q20*

> The problem of indefinite blockage of other people. Some people do this, low-priority jobs in general priority while some do not send any letter. scheduling algorithm can be solved How many people have seen the letter, using: including the first person, if no one

**Options**

- **A.** Parity bit receives more than one letter and if the
- **B.** Aging chain letter ends after there have been
- **C.** Compaction 100 people who read it but did not send it out? Also find how many people
- **D.** Timer sent out the letter? (A) 122 & 22

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 38

*UGC NET June 2012, Paper II, original Q29*

> Pre-emptive scheduling is the strategy of temporarily suspending a gunning process

**Options**

- **A.** before the CPU time slice expires
- **B.** to allow starving processes to run
- **C.** when it requests I/O
- **D.** to avoid collision

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 39

*UGC NET June 2012, Paper II, original Q30*

> In round robin CPU scheduling as time quantum is increased the average turn around time

**Options**

- **A.** increases
- **B.** decreases
- **C.** remains constant
- **D.** varies irregularly

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 40

*UGC NET June 2013, Paper III, original Q58*

> Consider the following processes with time slice of 4 milliseconds (I/O requests are ignored) : Process A B C D Arrival time 0 1 2 3 CPU cycle 8 4 9 5 The average turn around time of these processes will be

**Options**

- **A.** 19.25 milliseconds
- **B.** 18.25 milliseconds
- **C.** 19.5 milliseconds
- **D.** 18.5 milliseconds

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 41

*UGC NET June 2013, Paper III, original Q65*

> A thread is usually defined as a light weight process because an Operating System (OS) maintains smaller data structure for a thread than for a process. In relation to this, which of the following statement is correct ?

**Options**

- **A.** OS maintains only scheduling and accounting information for each thread.
- **B.** OS maintains only CPU registers for each thread.
- **C.** OS does not maintain a separate stack for each thread.
- **D.** OS does not maintain virtual memory state for each thread.

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 42

*UGC NET June 2015, Paper II, original Q32*

> The translator which performs macro calls expansion is called :

**Options**

1. Macro processor
2. Micro pre - processor
3. Macro pre - processor
4. Dynamic Linker

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 43

*UGC NET July 2016, Paper II, original Q40*

> A scheduling Algorithm assigns priority propor tional to the waiting time of a process. Every process starts with priority zero (low est priority). The scheduler reevaluates the process priority for every ‘T’ time units and decides next pr ocess to be scheduled. If the process have no I/O operations and all arrive at time zero, th en the scheduler implements _________ criteria.

**Options**

1. Priority scheduling
2. Round Robin Scheduling
3. Shortest Job First
4. FCFS

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 44

*UGC NET Jan 2017, Paper II, original Q39*

> Which of the following scheduling algorithms may cause starvation ?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** First-come-first-served
> - **B.** Round Robin
> - **C.** Priority
> - **D.** Shortest process next e. Shortest remaining time first

**Options**

1. a, c and e
2. c, d and e
3. b, d and e
4. b, c and d

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 45

*UGC NET Nov 2017, Paper II, original Q37*

> In __________ disk scheduling algorithm, the disk head moves from one end to other end of the disk, serving the requests along the way. When the head reaches the other end , it immediately returns to the beginning of the disk without serving any requests on t he return trip.

**Options**

1. LOOK
2. SCAN
3. C - LOOK
4. C - SCAN

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 46

*UGC NET Dec 2018, original Q123*

> Consider the following set of processes and the length of CPU burst time given in milliseconds: Process CPU Burst time (ms) P1 5 P2 7 Pз 6 PA 4 Assume that processes being scheduled with Round-Robin Scheduling Algorithm with time quantum 4 ms. Then the waiting time for Pa is ms.

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 47

*UGC NET July 2018, Paper II, original Q59*

> Consider the following three processes with the arrival time and CPU bur st time given in milliseconds : Process Arrival Time Burst Time P1 0 7 P2 1 4 P3 2 8 The Gantt Chart for preemptive SJF scheduling algorithm is _________.
>
> **Additional extracted choices — check the source page:**
>
> 1. _Missing in extracted text_
> 2. _Missing in extracted text_
> 3. _Missing in extracted text_
> 4. _Missing in extracted text_

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 48

*UGC NET July 2018, Paper II, original Q60*

> In which of the following scheduling criteria, context switching will never take place ?

**Options**

1. ROUND ROBIN
2. Preemptive SJF
3. Non-preemptive SJF
4. Preemptive priority

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 49

*UGC NET Dec 2019, original Q76*

> Which of the following CPU scheduling algorithms is/are supported by LINUX operating system?

**Options**

1. Non-preemptive priority scheduling
2. Preemptive priority scheduling and time sharing CPU scheduling
3. Time sharing scheduling only
4. Priority scheduling only 61547541002.2 61547541003.3 61547541004.4

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 50

*UGC NET Dec 2019, original Q80*

> Given CPU time slice of 2ms and following list of processes. Process Burst time Arrival time (ms) PI 3 0 dersonal P2 4 2 5 Find average turnaround time and average waiting time using round robin CPU scheduling?

**Options**

1. 4.0
2. 5.66. 1.66
3. 5.66, 0
4. 7.2 61547541018.2 61547541019.3 61547541020.4 Single Line Ouestion Option : No Ontion Orientation: Vertical Duestion Number: 80 Ouestion Id: 61547510520 Ouestion Type: MCO

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 51

*UGC NET Dec 2019, original Q124*

> Identify the circumstances under which pre-emptive CPU scheduling is used : (a) A process switches from Running state to Ready state (b) A process switches from Waiting state to Ready state (c) A process completes its execution d) A process switches from Ready to Waiting state Choose the correct

**Options**

1. (a) and (b) only
2. (a) and (d) only
3. (c) and (d) only
4. (a). (b). (c) only 61547541194.2 61547541195. 3 61547541196.4

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 52

*UGC NET June 2019, original Q95*

> Consider three CPU intensive processes, which require 10, 20 and 30 units of time and arrive at times 0, 2 and 6 respectively. How many context switches are needed if the operating system implements a shortest remaining time first scheduling algorithm? Do not count the context switches at time zero and at the end. 1. 4 2 3. 3 1 Guide 64635085716.2 xam. 64635085717.3 64635085718.4

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 53

*UGC NET Oct 2022, original Q76*

> Consider the following: List I List II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Stack algorithm I Deadlock
> - **B.** Elevator algorithm (I) Disk scheduling
> - **C.** Priority scheduling algorithm (III) Page replacement
> - **D.** Havender's algorithm (IV) CPU scheduling Which of the following is correct matching? 1. (A)-III), (B)-(II. (C)-(IV). (D-(I 2. (A)-(I). (B)-III, (C-(IV). (D)-(D) 4.

**Options**

- **A.** -(I,
- **B.** -III,
- **C.** -(D.
- **D.** -(IV)

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 54

*UGC NET Aug 2024, original Q140*

> Match List - I with List - II. List - I List - II (Algorithms) (Characteristics)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** First Come First Served (FCFS) (I) Each process is assigned a priority.
> - **B.** Shortest Job First (SJF) (LI) Ensures fair allocation of CPU time by assigning time slice.
> - **C.** Round Robin (RR) (III) Processes are executed in the order they arrive.
> - **D.** Priority Scheduling (IV) Select the process for execution with smallest next Burst time. Choose the correct answer from the options given below : (1)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(LI),
> - **B.** -(III),
> - **C.** -(IV),
> - **D.** -(I) (2)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(II,
> - **B.** -(IV),
> - **C.** -(III,
> - **D.** -(t) (3)

**Options**

- **A.** -(III),
- **B.** -(IV),
- **C.** -(II),
- **D.** -(I) (4) (А)-(I), (B)-(IV), (C)-(I), (D)-(II) Sub-Section Number : 2 Sub-Section Id : 533072153 Question Shuffling Allowed : No Question Label: Comprehension 95/101

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 55

*UGC NET Aug 2024, original Q146*

> What information is used to determine if a resource request can be granted ?

**Options**

1. Available resources and current allocation of each process
2. CPU utilization of each process
3. Number of processes waiting for resources
4. Arrival time of each process

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 56

*UGC NET June 2024, original Q114*

> In windows scheduling, which of the following option is correct? (1) 4 non-real-time priorities (3) 12 non-real-time priorities (2) 8 non-real-time priorities (4) 16 non-real-time priorities 115 TH.1I0

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 57

*UGC NET June 2025, original Q68*

> Consider the following table about processes, their burst time and arrival time Process Burst Time Arrival Time 09 0 P2 30 0 04 PA 08 2 Now which of the process shall finish second last as per the respective GANT charts for the non- preemptive SJF and Round Robin (time quantum = 10) scheduling methods.

**Options**

1. SJF : PA; RR: P4
2. SJF : Ps; RR: P4
3. SJF : PA; RR: Ps
4. SJF : Ps; RR: Ps 42558919325.2 42558919326.3 42558919327.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 58

*UGC NET Dec 2025 session (Jan 2026), original Q81*

> Question Number : 81 using priority scheduling.

**Options**

1. 8
2. 8.2
3. 8.3
4. 8.4 6119878722.2 6119878723.3 6119878724.4

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 59

*UGC NET Dec 2025 session (Jan 2026), original Q86*

> Question Number : 86

**Chapter foundations**

This question belongs to the ideas covered by **CPU Scheduling**. Revise these foundations: Criteria and Algorithms; Thread Scheduling; Multiple-Processor Scheduling; Real-Time Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For CPU Scheduling questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-6"></a>

### 6. Deadlocks (1 questions)

**What to master:** Characterization; Handling; Prevention; Avoidance; Detection; Recovery.

**Exam lens:** Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.

**Reusable method:** Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.

**High-yield rules:** Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.

**Common traps:** Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.

---

#### Question 60

*UGC NET Aug 2024, original Q147*

> What is the primary goal of the Banker's Algorithm?

**Options**

1. To allocate resources optimally
2. To prevent processes from requesting resources
3. To detect and recover from deadlocks
4. To maximise CPU utilization

**Chapter foundations**

This question belongs to the ideas covered by **Deadlocks**. Revise these foundations: Characterization; Handling; Prevention; Avoidance; Detection; Recovery.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Deadlocks questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-7"></a>

### 7. Memory Management (27 questions)

**What to master:** Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam lens:** Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.

**Reusable method:** Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.

**High-yield rules:** Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.

**Common traps:** Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.

---

#### Question 61

*UGC NET Dec 2009, Paper II, original Q37*

> A page fault

**Options**

- **A.** is an error specific page.
- **B.** is an access to the page not currently in memory.
- **C.** occur when a page program occur in a page memory.
- **D.** page used in the previous page reference.

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 62

*UGC NET Dec 2011, Paper III, original Q19*

> Why are segmentation and paging sometimes combined into one scheme ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ ______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ ____________

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 63

*UGC NET Dec 2012, Paper II, original Q30*

> Which of the following memory allocation scheme suffers from external

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 64

*UGC NET Dec 2012, Paper II, original Q34*

> The maximum number of keys stored fragmentation? in a B-tree of order m and depth d is
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Segmentation (A) md+1-1
> - **B.** md+1 - 1 (B) Pure demand paging m - 1
> - **C.** Swapping (C) (m- 1) (md + 1 - 1)
> - **D.** Paging (D) md - 1 m - 1

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 65

*UGC NET June 2012, Paper II, original Q33*

> Consider the following page trace : 4,3, 2, 1, 4, 3, 5, 4, 3, 2, 1, 5 Percentage of page fault that would occur if FIFO page replacement algorithm is used with number of frames for the JOB m = 4 will be

**Options**

- **A.** 8
- **B.** 9
- **C.** 10
- **D.** 12

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 66

*UGC NET June 2013, Paper III, original Q63*

> Working set model is used in memory management to implement the concept of

**Options**

- **A.** Swapping
- **B.** Principal of Locality
- **C.** Segmentation
- **D.** Thrashing

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 67

*UGC NET Dec 2014, Paper II, original Q36*

> Consider the following justifications for commonly using the two-level CPU sc heduling : I. It is used when memory is too small to hold all the ready processes. II. Because its performance is same as that of the FIFO. III. Because it facilitates putting some set of processes into memory and a choice is made from that. IV. Because it does not allow to adjust the set of in-core processes. Which of the following is true ?

**Options**

- **A.** I, III and IV
- **B.** I and II
- **C.** III and IV
- **D.** I and III

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 68

*UGC NET Dec 2014, Paper II, original Q39*

> For the implementation of a paging scheme, suppose the average p rocess size be x bytes, the page size be y bytes, and each page entry requires z bytes . The optimum page size that minimizes the total overhead due to the page table and the interna l fragmentation loss is given by

**Options**

- **A.** x 2
- **B.** xz 2
- **C.** 2xz
- **D.** xz 2

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 69

*UGC NET Dec 2014, Paper II, original Q40*

> In a demand paging memory system, page table is held in regi sters. The time taken to service a page fault is 8 m.sec. if an empty frame is availabl e or if the replaced page is not modified, and it takes 20 m.secs., if the replaced page is modified. W hat is the average access time to service a page fault assuming that the page to be replaced is modified 70% of the time ?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** 11.6 m.sec.
> - **B.** 16.4 m.sec.
> - **C.** 28 m.sec.
> - **D.** 14 m.sec. 41. __________ are applied throughout the software process.

**Options**

- **A.** Framework activities
- **B.** Umbrella activities
- **C.** Planning activities
- **D.** Construction activities

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 70

*UGC NET Dec 2015, Paper II, original Q26*

> A virtual memory has a page size of 1K words. There are eight pages and four blocks. The associative memory page table contains the following entries: Page Block 0 3 2 1 5 2 7 Which of the following list of virtual addresses (in decimal) will not cause any page fault if referenced by the CPU?

**Options**

1. 1024, 3072, 4096, 6144
2. 1234, 4012, 5000, 6200
3. 1020, 3012, 6120, 8100
4. 2021, 4050, 5112, 7100

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 71

*UGC NET Dec 2015, Paper II, original Q27*

> Suppose that the number of instructions executed between page fault is directly proportional to the number of page frames allocated to a program. If the available memory is doubled, the mean interval between page faults is also doubled. Further, consider that a normal instruction takes one microsecond, but if a page fault occurs, it takes 2001 microseconds. If a program takes 60 sec to run, during which time it gets 15,000 page faults, how long would it take to

**Options**

1. 60 sec
2. 30 sec
3. 45 sec
4. 10 sec

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 72

*UGC NET Dec 2015, Paper II, original Q45*

> The . memory. transfers the executable image of a Ct+ program from hard disk to main

**Options**

1. Compiler
2. Linker
3. Debugger
4. Loader

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 73

*UGC NET June 2015, Paper II, original Q37*

> Let P; and P; be two processes, R be the set of variables read from memory, and W be the set of variables written to memory. For the concurrent execution of two processes P; and P; which of the following conditions is not true ? (1) R(Pi) ^ W(P;) =$ (3) R(Pi) ~ R(P;) =Ф 38. faults will occur with the reference string 0172327103 if the four frames are initially empty? A LRU page replacement is used with four page frames and eight pages. How many page

**Options**

1. 6
2. 7
3. 5
4. 8

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 74

*UGC NET June 2015, Paper III, original Q18*

> Match the following : List - I List - II

**Options**

- **A.** Flood Gun (i) An electron gun designed to flood the entire screen with electrons.
- **B.** Collector (ii) Partly energised by flooding gun, stores the charge generated by the writing gun.
- **C.** Ground (i) Used to discharge the collector.
- **D.** Phosphorus grains (iv) Used in memory - tube display and similar to those used in standard CRT. (e) Writing Gun System (v) Used in memory - tube display and basically the same as the electron gun used in a conventional CRT. Codes: (a) (b)(c) (d) (e) (1) (i) (li) (ili) (iv) (v) (2) (ii) (ill) (i) (iv) (v) (3) (iii (1) (ii) (V) (iv)

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 75

*UGC NET July 2016, Paper II, original Q36*

> Consider the reference string 012301401234 If FIFO page replacement algorithm is used, then the number of page faults with three page frames and four page frames are _______ and ______ respectively.

**Options**

1. 10, 9
2. 9, 9
3. 10, 10
4. 9, 10

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 76

*UGC NET July 2018, Paper II, original Q57*

> Page information in memory is also called as Page Table. The essential contents in each entry of a page table is/are _________.

**Options**

1. Page Access information
2. Virtual Page number
3. Page Frame number
4. Both virtual page number and Page Frame Number

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 77

*UGC NET July 2018, Paper II, original Q58*

> Consider a virtual page reference string 1, 2, 3, 2, 4, 2, 5, 2, 3, 4. Suppose LRU page replacement algorithm is implemented with 3 page frames in main memory. Then the num ber of page faults are_________.

**Options**

1. 5
2. 7
3. 9
4. 10

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 78

*UGC NET June 2019, original Q97*

> The minimum number of page frames that must be allocated to a running process in a virtual memory environment is determined by page size 2. physical size of memory the instruction set architecture 4. number of processes in memory Guide 64635085724.2 64635085725.3 64635085726.4

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 79

*UGC NET Nov 2020, original Q65*

> Consider a hypothetical machine with 3 pages of physical memory, 5 pages of virtual memory, and < A,B,C, D,A, B,E,A, B,C, D,E,B,A, B > as the stream of page references by an application. If P and Q are the number of page faults that the application would incur with FIFO and LEU page replacement algorithms respectively, then (P.Q) = (Assuming enough space for storing 3 page frames)

**Options**

1. (11, 10)
2. (12, 11)
3. (10, 11)
4. (11, 12) 53622816758.2 53622816759.3 53622816760.4

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 80

*UGC NET Nov 2021, original Q71*

> Given memory access time as p nanoseconds and additional q nanoseconds for handling the page fault. What is the effective memory access time if a page fault occurs once for every 100 instructions? 1. 2. 3. 4.

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 81

*UGC NET Oct 2022, original Q53*

> For the following page reference string 4, 8, 2, 1. 4, 3, 5. 4, 3, 2,

**Options**

1. 5. the number of page faults that oceur in Least Recently Used (LU) page replacement algorithm with frame size
2. 8
3. 10
4. 12

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 82

*UGC NET June 2023, Paper II, original Q46*

> Given below are two statements: one is labelled as Assertion A and the other is (+2) labelled as Reason R. A virtual memory system uses first-in first-out page replacement policy and allocates a fixed number of frames to a process Assertion A: Increasing number of page frames allocated to a process sometimes increases the page fault rate. Reason R: Some programs do not exhibit locality of reference. In the light of the above statements, choose the correct answer from the options given below.

**Options**

- **A.** Both A and Rare true and R is the correct explanation of A
- **B.** Both A and R are true but R is NOT the correct explanation of A
- **C.** A is true but R is false
- **D.** A is false but R is true Gui

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 83

*UGC NET Aug 2024, original Q110*

> Which of the following statements are TRUE about Process Control Block (PCB)?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** The PCB contains information about the process state, such as whether it is running, waiting or terminated
> - **B.** The PCB includes the program code and data segments of the process
> - **C.** The PCB stores the process's memory management information, such as page tables and segment tables
> - **D.** The PCB is used to track process scheduling information and CPU registers for process execution Choose the correct answer from the options given below :

**Options**

1. (A), (B) and (C) Only
2. (B), (C) and (D) Only
3. (A), (C) and (D) Only
4. (A) and (B) Only

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 84

*UGC NET Aug 2024, original Q111*

> Which of the following statements are TRUE about Privileged Instructions?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** It can only be executed by the Operating System kernel and not by user applications.
> - **B.** It is designed to perform operations that can directly affect the hardware or system state such as I/O operations or changing memory management setting.
> - **C.** User applications can execute privileged instructions if they have to correct permissions, set by the Operating System.
> - **D.** It usually executed in user mode to ensure the safety and security of the system. Choose the correct answer from the options given below :

**Options**

1. (A) and (B) Only
2. (A), (B) and (C) Only
3. (B) and (C) Only
4. (B), (C) and (D) Only

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 85

*UGC NET June 2024, original Q103*

> Which of the following is not correct about the virtual memory segmentation?

**Options**

1. It is not necessary to load all of the segments of a process.
2. It has no internal fragmentation.
3. It has large virtual address space.
4. It provides lower degree of multiprogramming.

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 86

*UGC NET June 2025, original Q131*

> Match List I with List I! List List I
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Clustered Page Table I. Generally considered inappropriate for 64 bit architectures.
> - **B.** Hierarchical Page Table lI. Has only entry for each real page (or frame) of memory.
> - **C.** Segmentation I. Useful for Sparse address spaces.
> - **D.** Inverted Page Table IV. Supports a user view of the system. Choose the correct answer from the options given below:

**Options**

1. A→III, B→IV, C→II, D→I
2. A>III, B→I, C→IV, D>|I
3. A→II, B→III, C→I, D→IV
4. A→IV, B→III, C→II, D→I 42558919577.2 42558919578. 3 42558919579.4

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 87

*UGC NET June 2025, original Q132*

> Match List I with List I! List I List
>
> **Additional extracted choices — check the source page:**
>
> - **A.** RAID Level 2 1. Block interleaved distribution parity
> - **B.** RAID Level 3 lI. Also known as P+Q redundancy Scheme
> - **C.** RAID Level 5 IlI. Bit interleaved parity
> - **D.** RAID Level 6 IV. Also known as Memory style error correcting code organization Choose the correct answer from the options given below:

**Options**

1. A→IV, B→III, C→I, D>/I
2. A→III, B→IV, C→I, D>II
3. A→I, B→III, C→IV, D→>II
4. A→II, B→IV, C→I, D→III 42558919581.2 42558919582. 3 42558919583.4 Mandary Ner: 132

**Chapter foundations**

This question belongs to the ideas covered by **Memory Management**. Revise these foundations: Contiguous Allocation; Swapping; Paging; Segmentation; Demand Paging; Page Replacement; Frame Allocation; Thrashing; Memory-Mapped Files.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-8"></a>

### 8. Storage Management (3 questions)

**What to master:** Mass-Storage Structure; Disk Structure, Scheduling and Management; RAID.

**Exam lens:** Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.

**Reusable method:** Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.

**High-yield rules:** Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.

**Common traps:** Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.

---

#### Question 88

*UGC NET June 2013, Paper III, original Q10*

> Match the following :
>
> **Additional extracted choices — check the source page:**
>
> - **A.** RAID 0 i. Bit interleaved parity
> - **B.** RAID 1 ii. Non redundant stripping
> - **C.** RAID 2 iii. Mirrored disks
> - **D.** RAID 3 iv. Error correcting codes Codes : a b c d

**Options**

- **A.** iv i ii iii
- **B.** iii iv i ii
- **C.** iii i iv ii
- **D.** iii ii iv i

**Chapter foundations**

This question belongs to the ideas covered by **Storage Management**. Revise these foundations: Mass-Storage Structure; Disk Structure, Scheduling and Management; RAID.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Storage Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 89

*UGC NET Aug 2024, original Q149*

> What is the significance of the Banker's algorithm in terms of resource management?

**Options**

1. It enures that all processes can finish their execution without deadlock.
2. It eliminates the need for processes to request resources.
3. It accelerates the execution of critical sections in processes.
4. It minimizes the number of context switches between processes.

**Chapter foundations**

This question belongs to the ideas covered by **Storage Management**. Revise these foundations: Mass-Storage Structure; Disk Structure, Scheduling and Management; RAID.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Storage Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 90

*UGC NET June 2024, original Q75*

> Match List-l with ise-lt List - 1 List - 11 A. RAID level2 Hock-ass/haved RAID level-3 error-cortreting-code C. RAID level4 reed solomont codes D. RAID level-s bit-interlated Choose the correct answer from the options given below

**Options**

1. A-L B-III, C-IV, D-I1
2. A-IL B-IV, C-L, D-II
3. A-IV, B-L C-IL D-II
4. A-IL BILL, C-IV, D-I

**Chapter foundations**

This question belongs to the ideas covered by **Storage Management**. Revise these foundations: Mass-Storage Structure; Disk Structure, Scheduling and Management; RAID.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Storage Management questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-9"></a>

### 9. File and Input/Output Systems (40 questions)

**What to master:** Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam lens:** Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.

**Reusable method:** Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.

**High-yield rules:** Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.

**Common traps:** Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.

---

#### Question 91

*UGC NET Dec 2009, Paper II, original Q40*

> The Unix command used to find out the number of characters in a file is

**Options**

- **A.** nc
- **B.** wc
- **C.** chcnt
- **D.** lc

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 92

*UGC NET Dec 2012, Paper II, original Q42*

> Which of the following mode (D) 20,12,14 declaration is used in Ctt to open a file for input?

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 93

*UGC NET June 2012, Paper II, original Q9*

> What deletes the entire file except the file structure ?

**Options**

- **A.** ERASE
- **B.** DELETE
- **C.** ZAP
- **D.** PACK

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 94

*UGC NET June 2012, Paper II, original Q10*

> Which command is the fastest among the following ?

**Options**

- **A.** COPY TO <NEW FILE>
- **B.** COPY STRUCTURE TO <NEW FILE>
- **C.** COPY FILE <FILE 1> <FILE 2>
- **D.** COPY TO MFILE-DAT DELIMITED

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 95

*UGC NET Dec 2013, Paper III, original Q71*

> Simplest way of deadlock recovery is

**Options**

- **A.** Roll back
- **B.** Preempt resource
- **C.** Lock one of the processes
- **D.** Kill one of the processes

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 96

*UGC NET Dec 2013, Paper III, original Q72*

> The directory structure used in Unix file system is called

**Options**

- **A.** Hierarchical directory
- **B.** Tree structured directory
- **C.** Directed acyclic graph
- **D.** Graph structured directory

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 97

*UGC NET June 2013, Paper III, original Q64*

> A UNIX file system has 1 KB block size and 4-byte disk addresses. What is the maximum file size if the inode contains ten direct block entries, one single indirect bl ock entry, one double indirect block entry and one triple indirect block entry ?

**Options**

- **A.** 30 GB
- **B.** 64 GB
- **C.** 16 GB
- **D.** 1 GB

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 98

*UGC NET Dec 2014, Paper II, original Q23*

> The directory can be viewed as ________ that translates filenames into their directory entries.

**Options**

- **A.** Symbol table
- **B.** Partition
- **C.** Swap space
- **D.** Cache

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 99

*UGC NET Dec 2014, Paper III, original Q51*

> Consider an imaginary disk with 40 cylinders. A request come to rea d a block on cylinder

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 100

*UGC NET Dec 2015, Paper II, original Q28*

> Consider a disk with 16384 bytes per track having a rotation time of 16 msec and average seek time of 40 msec. What is the time in msec to read a block of 1024 bytes from this disk ?

**Options**

1. 57 msec
2. 49 msec
3. 48 msec
4. 17 msec D-8715 Paper-Il

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 101

*UGC NET Dec 2015, Paper II, original Q30*

> In Unix, the login prompt can be changed by changing the contents of the file -

**Options**

1. contrab
2. init
3. gettydefs
4. inittab

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 102

*UGC NET Dec 2015, Paper II, original Q49*

> A unix file system has 1-KB blocks and 4-byte disk addresses. What is the maximum file size if i-nodes contain 10 direct entries and one single, double and triple indirect entry each ?
>
> **Additional extracted choices — check the source page:**
>
> 1. 32 GB
> 2. 64 GB
> 3. 16 GB
> 4. 1GB uses electronic means to transfer funds directly from one account to another rather than by cheque or cash.

**Options**

1. M-Banking
2. E-Banking
3. O-Banking
4. C-Banking - 000- D-8715 11 Paper-Il

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 103

*UGC NET Dec 2015, Paper III, original Q40*

> In Unix operating system, special files are used to :

**Options**

1. buffer data received in its input from where a process reads
2. provide a mechanism to map physical device to file names
3. store list of file names plus pointers associated with i-nodes
4. store information entered by a user application program or utility program

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 104

*UGC NET Dec 2015, Paper III, original Q41*

> Match the following in Unix file system : List - I List - II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Boot block (i) Information about file system
> - **B.** Super block (ii) Information about file
> - **C.** Inode table (iii) Storage space
> - **D.** Data block (iv) Code for making OS ready Codes: (a) (b) (c) (d)

**Options**

1. (iv) (i) (i) (iti)
2. (i) (iii) (i) (iv)
3. (iii) (i) (ii) (iv)
4. (iv) (ii) (i) (iii) D-8715 8 Paper-III

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 105

*UGC NET Dec 2015, Paper III, original Q56*

> In Unix, the command to enable execution permission for file "mylife" by all is

**Options**

1. Chmod ugo + X myfile
2. Chmod a + X myfile
3. Chmod +X myfile
4. All of the above D-8715 10 Paper-III

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 106

*UGC NET Dec 2015, Paper III, original Q57*

> What will be the output of the following Unix command? $rm chap0\ [1 - 3\1

**Options**

1. Remove file chap0|1 - 3]
2. Remove file chap01, chap02, chap03
3. Remove file chap\[1 - 3\1
4. None of the above

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 107

*UGC NET Dec 2015, Paper III, original Q62*

> The distributed system is a collection of (P) and communication is achieved in distributed system by _ (Q) where (P) and (Q) are :

**Options**

1. Loosely coupled hardware on tightly coupled software and disk sharing, respectively.
2. Tightly coupled hardware on loosely coupled software and shared memory, respectively.
3. Tightly coupled software on loosely coupled hardware and message passing, respectively.
4. Loosely coupled software on tightly coupled hardware and file sharing, respectively.

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 108

*UGC NET June 2015, Paper II, original Q25*

> To determine the efficiency of an algorithm the time factor is measured by :

**Options**

1. Counting micro seconds
2. Counting number of key operations
3. Counting number of statements
4. Counting kilobytes of algorithm

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 109

*UGC NET June 2015, Paper II, original Q36*

> A disk drive has 100 cyclinders, numbered 0 to 99. Disk requests come to the disk driver for cyclinders 12, 26, 24, 4, 42, 8 and 50 in that order. The driver is currently serving a request at cyclinder 24. A seek takes 6 msec per cyclinder moved. How much seek time is needed for shortest seek time first (SSTF) algorithm? 0.984 sec (2) 0.396 sec (3) 0.738 sec (4) 0.42 sec

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 110

*UGC NET June 2015, Paper II, original Q39*

> What does the following command do? grep - vn "abc" x

**Options**

1. It will print all of the lines in the file x that match the search string "abc".
2. It will print all of the lines in file x that do not match the search string "abc".
3. It will print the total number of lines in the file x that match the string "abc".
4. It will print the specific line numbers of the file x in which there is a match for string "abc"

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 111

*UGC NET June 2015, Paper III, original Q3*

> Both files can be edited using 'mv' command to move between the file: (4) Edits filel first, saves it and then edits file2 - 000- J-8715 15 Paper-III

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 112

*UGC NET June 2015, Paper III, original Q52*

> Dining Philosopher's problem is a :
>
> **Additional extracted choices — check the source page:**
>
> 1. Producer - consumer problem
> 2. Classical IPC problem
> 3. Starvation problem
> 4. Synchronization primitive allocation method for disk block allocation in a file system, insertion and deletion of blocks in a file is easy.

**Options**

1. Index
2. Linked
3. Contiguous
4. Bit Map

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 113

*UGC NET June 2015, Paper III, original Q54*

> A unix file may be of the type:

**Options**

1. Regular file
2. Directory file
3. Device file
4. Any one of the above

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 114

*UGC NET June 2015, Paper III, original Q73*

> Match the following for unix system calls: List - I List - II

**Options**

- **A.** exec (i) Creates a new process
- **B.** brk (ii) Invokes another program overlaying memory space with a copy of an executable file
- **C.** wait (iii) To increase or decrease the size of data region
- **D.** fork (iv) A process synchronizes with termination of child process Codes: (a) (b) (c) (d) (1) (i) (il) (iv) (i) (2) (iii) (ii) (iv) (i) (3) (iv)

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 115

*UGC NET June 2015, Paper III, original Q74*

> WOW32 is a : Win 32 API library for creating processes and threads. (2) Special kind of file system to the NT name space. (3) Kernel - mode objects accessible through Win 32 API (4) Special execution environment used to run 16 bit Windows applications on 32 - bit machines.

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 116

*UGC NET June 2015, Paper III, original Q75*

> The unix command : $ vi file1 file2 (1) Edits filel and stores the contents of filel in file2 (2) oth files i.e. file1 and file2 can be edited using 'ex' command to travel between the file.

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 117

*UGC NET July 2016, Paper III, original Q51*

> Which of the following information about the UNIX file system is not correct ?

**Options**

1. Super block contains the number of i-nodes, the number of disk blocks, and the start of the list of free disk blocks.
2. An i-node contains accounting information as well as enough information to locate all the disk blocks that holds the file’s data.
3. Each i-node is 256-bytes long.
4. All the files and directorie s are stored in data blocks.

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 118

*UGC NET July 2016, Paper III, original Q54*

> Suppose that the time to do a null remote procedure call (R PC) (i.e. 0 data bytes) is 1.0 msec, with an additional 1.5 msec for every 1K of data. How long does it take to read 32 K from the file server as 32 1K RPCs ?

**Options**

1. 49 msec
2. 80 msec
3. 48 msec
4. 100 msec

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 119

*UGC NET July 2016, Paper III, original Q67*

> What is the function of following UNIX command ? WC – l <a > b &

**Options**

1. It runs the word count program to count the number of lines in its input, a, writing the result to b, as a foreground process.
2. It runs the word count program to count the number of lines in its input, a, writing the result to b, but does it in the background.
3. It counts the errors during the executi on of a process, a, and puts the result in process b.
4. It copies the ‘ l’ numbers of lines of program from file, a, and stores in file b.

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 120

*UGC NET Jan 2017, Paper II, original Q36*

> There are three processes P 1, P 2 and P 3 sharing a semaphore for synchronizing a variable. Initial value of semaphore is one. Assume that negative value of semaphore tells us how many processes are waiting in queue. Processes access the s emaphore in following order :
>
> **Additional extracted choices — check the source page:**
>
> - **A.** P2 needs to access
> - **B.** P1 needs to access
> - **C.** P3 needs to access
> - **D.** P2 exits critical section (e) P1 exits critical section The final value of semaphore will be :

**Options**

1. 0
2. 1
3. –1
4. –2

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 121

*UGC NET Jan 2017, Paper III, original Q51*

> Match the following for Unix file system : List – I List – II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Boot block i. Information about file system, free block list, free inode list etc.
> - **B.** Super block ii. Contains operati ng system files as well as program and data files created by users.
> - **C.** Inode block iii. Contains boot program and partition table.
> - **D.** Data block iv. Contains a table fo r every file in the file system. Attributes of files are stored here. Codes : a b c d

**Options**

1. iii i ii iv
2. iii i iv ii
3. iv iii ii i
4. iv iii i ii

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 122

*UGC NET Jan 2017, Paper III, original Q74*

> Unix command to change the case of first three lines of file “shortlist” from lower to upper

**Options**

1. $ tr ‘[a – z]’ ‘[A – Z]’ shortlist ¦ head-3
2. $ head-3 shortlist ¦ tr ‘[a – z]’ ‘[A – Z]’
3. $ tr head -3 shor tlist ‘[A – Z]’ ‘[a – z]’
4. $ tr shortlist head -3 ‘[a – z]’ ‘[A – Z]’

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 123

*UGC NET Jan 2017, Paper III, original Q75*

> Match the following vi commands in Unix : List – I List – II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** : w i. saves the file and quits editing mode
> - **B.** : x ii. escapes unix shell
> - **C.** : q iii. saves file and remains in editing mode
> - **D.** : sh iv. quits editing mode and no changes are saved to the file Codes : a b c d

**Options**

1. ii iii i iv
2. iv iii ii i
3. iii iv i ii
4. iii i iv ii ___________

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 124

*UGC NET July 2018, Paper II, original Q51*

> At a particular time of computation, the value of a counting semapho re is 10. Then 12 P operations and “ x” V operations were performed on this semaphore. If the final value of semaphore is 7, x will be :

**Options**

1. 8
2. 9
3. 10
4. 11

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 125

*UGC NET Dec 2019, original Q74*

> A counting semaphore is initialized to 8. 3 wait () operations and 4 signal () operations are applied. Find the current value of semaphore variable.
>
> **Additional extracted choices — check the source page:**
>
> 1. 9
> 2. _Missing in extracted text_
> 3. 1
> 4. 4 61547540994. 2 61547540995. 3 61547540996.4

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 126

*UGC NET June 2019, original Q96*

> At a particular time of computation, the value of a counting semaphore is 7. Then 20 P (wait) operations and 15 V (signal) operations are completed on this semaphore. What is the resulting value of the semaphore? 28 12 3. 2 4. 42 Guide 64635085720.2 64635085721.3 64635085722.4

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 127

*UGC NET Nov 2020, original Q67*

> Suppose you have a Linux file system where the block size is 2K bytes, a disk address is 32 bits, and an i-node contains the disk addresses of the first 12 direct blocks of file, a single indirect block, and a double indirect block. Approximately, what is the largest file that can be represented by an i node?

**Options**

1. 513 Kbytes
2. 513 MBytes
3. 537 Mbytes
4. 537 KBytes 53622816766. 2 53622816767.3 53622816768.4

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 128

*UGC NET Nov 2021, original Q63*

> Given a fixed‐length record file that is ordered on the key field. The file needs B disk blocks to store R number of records. Find the average access time needed to access any record of the given file using binary search. 1. 2. B + R 3. B 4.

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 129

*UGC NET Aug 2024, original Q94*

> Arrange the following steps of file handling in C in the correct order :
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Close the file
> - **B.** Read from or write to the file
> - **C.** Open the file
> - **D.** Check for error Choose the correct answer from the options given below :

**Options**

1. (A), (C), (D), (B)
2. (D), (B), (C), (A)
3. (C), (D), (B), (A)
4. (B), (D), (A), (C)

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 130

*UGC NET Dec 2025 session (Jan 2026), original Q80*

> Question Number: 80

**Chapter foundations**

This question belongs to the ideas covered by **File and Input/Output Systems**. Revise these foundations: Access Methods; Directory and Disk Structure; Mounting; Sharing; File-System Structure and Implementation; Allocation; Free-Space Management; Efficiency, Performance and Recovery; I/O Hardware and Interfaces; Kernel I/O; Transforming Requests to Hardware Operations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For File and Input/Output Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-10"></a>

### 10. Security (1 questions)

**What to master:** Protection; Access Matrix and Control; Revocation; Program, System and Network Threats; Cryptography; Authentication; Defences.

**Exam lens:** Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.

**Reusable method:** Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.

**High-yield rules:** Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.

**Common traps:** Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.

---

#### Question 131

*UGC NET Nov 2017, Paper II, original Q38*

> Suppose there are six files F1, F2, F3, F4, F5, F6 with corresponding sizes 150 KB, 225 KB , 75 KB, 60 KB, 275 KB and 65 KB respectively. The files are to be stored on a sequential device in such a way that optimizes access time. In what order should the files b e stored ?

**Options**

1. F5, F2, F1, F3, F6, F4
2. F4, F6, F3, F1, F2, F5
3. F1, F2, F3, F4, F5, F6
4. F6, F5, F4, F3, F2, F1

**Chapter foundations**

This question belongs to the ideas covered by **Security**. Revise these foundations: Protection; Access Matrix and Control; Revocation; Program, System and Network Threats; Cryptography; Authentication; Defences.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Security questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-11"></a>

### 11. Virtual Machines (5 questions)

**What to master:** Types; Implementations; Virtualization.

**Exam lens:** Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.

**Reusable method:** Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.

**High-yield rules:** Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.

**Common traps:** Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.

---

#### Question 132

*UGC NET June 2010, Paper II, original Q49*

> At any given time Parallel Virtual Machine (PVM) has ________ send buffer and ________ receive buffer.

**Options**

- **A.** one-one
- **B.** one-two
- **C.** two-two
- **D.** two-one

**Chapter foundations**

This question belongs to the ideas covered by **Virtual Machines**. Revise these foundations: Types; Implementations; Virtualization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Virtual Machines questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 133

*UGC NET June 2015, Paper II, original Q47*

> Which of the following statements is incorrect for Parallel Virtual Machine (PVM) ? The PVM communication model provides asynchronous blocking send, asynchronou locking receive, and non-blocking receive functior (2) Message buffers are allocated dynamically.

**Chapter foundations**

This question belongs to the ideas covered by **Virtual Machines**. Revise these foundations: Types; Implementations; Virtualization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Virtual Machines questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 134

*UGC NET Dec 2019, original Q82*

> Java Virtual Machine (JVM) is used to execute architectural neutral byte code. Which of the following is needed by the JVM for execution of Java Code?

**Options**

1. Class loader only
2. Class loader and Java Interpreter
3. Class loader, Java Interpreter and API
4. Java Interpreter only 61547541026.2 61547541027.3 61547541028. 4

**Chapter foundations**

This question belongs to the ideas covered by **Virtual Machines**. Revise these foundations: Types; Implementations; Virtualization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Virtual Machines questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 135

*UGC NET Nov 2020, original Q108*

> Which of the following cloud concept/s is/are related to pooling and sharing of resources? (A) Virtual Memory (B) Service (C) Virtualization Choose the correct answer from the options given below:

**Options**

1. (C) only
2. (A) and (B) only
3. (A) only
4. (B) only 53622816930.2 53622816931.3 53622816932. 4

**Chapter foundations**

This question belongs to the ideas covered by **Virtual Machines**. Revise these foundations: Types; Implementations; Virtualization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Virtual Machines questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 136

*UGC NET June 2025, original Q103*

> Mandatory: No Arrange the process of virtualization in cloud environments.
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Hypervisor installed on physical server
> - **B.** Virtual machines created
> - **C.** Resources allocated to Virtual machines
> - **D.** Virtual machines run isolated workloads Choose the correct answer from the options given below:

**Options**

1. B, C, A, D
2. A, B, C, D
3. A, C, B, D
4. B, C, D, A 42558919465.2 42558919466. 3 42558919467.4

**Chapter foundations**

This question belongs to the ideas covered by **Virtual Machines**. Revise these foundations: Types; Implementations; Virtualization.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Virtual Machines questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-12"></a>

### 12. Linux Operating Systems (7 questions)

**What to master:** Design Principles; Kernel Modules; Process Management and Scheduling; Memory; File Systems; I/O; IPC; Network Structure.

**Exam lens:** Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.

**Reusable method:** Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.

**High-yield rules:** Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.

**Common traps:** Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.

---

#### Question 137

*UGC NET Dec 2013, Paper II, original Q50*

> Linux operating system uses

**Options**

- **A.** Affinity Scheduling
- **B.** Fair Preemptive Scheduling
- **C.** Hand Shaking
- **D.** Highest Penalty Ratio Next

**Chapter foundations**

This question belongs to the ideas covered by **Linux Operating Systems**. Revise these foundations: Design Principles; Kernel Modules; Process Management and Scheduling; Memory; File Systems; I/O; IPC; Network Structure.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Linux Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 138

*UGC NET Dec 2018, original Q118*

> In Linux operating system environment. command is used to print a file. . print Guide 91394342470. ptr 91394342471. pr ional Exam 91394342472. Ipr

**Chapter foundations**

This question belongs to the ideas covered by **Linux Operating Systems**. Revise these foundations: Design Principles; Kernel Modules; Process Management and Scheduling; Memory; File Systems; I/O; IPC; Network Structure.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Linux Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 139

*UGC NET July 2018, Paper II, original Q55*

> Which UNIX/Linux command is used to make all files and sub-direct ories in the directory “progs” executable by all users ?

**Options**

1. chmod− R a +x progs
2. chmod −R 222 progs
3. chmod−X a +x progs
4. chmod −X 222 progs

**Chapter foundations**

This question belongs to the ideas covered by **Linux Operating Systems**. Revise these foundations: Design Principles; Kernel Modules; Process Management and Scheduling; Memory; File Systems; I/O; IPC; Network Structure.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Linux Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 140

*UGC NET June 2019, original Q100*

> Which of the following UNIX/Linux pipes will count the number of lines in all the files having • c and h as their extension in the current working directory? 1. cat*•ch| wc-1 2. cat*•[c-h]| wc-1 3. cat*•[ch]; ls-1 cat *. [ch] wc-1 64635085736.2 64635085737.3 64635085738. 4 Ouestion Number: 101 Ouestion Id : 64635021842 Ouestion Type: MCO

**Chapter foundations**

This question belongs to the ideas covered by **Linux Operating Systems**. Revise these foundations: Design Principles; Kernel Modules; Process Management and Scheduling; Memory; File Systems; I/O; IPC; Network Structure.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Linux Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 141

*UGC NET Oct 2022, original Q23*

> What is called Journalling in Linux operating system

**Options**

1. Process scheduling
2. File saving as transaction
3. A type of thread
4. An editor

**Chapter foundations**

This question belongs to the ideas covered by **Linux Operating Systems**. Revise these foundations: Design Principles; Kernel Modules; Process Management and Scheduling; Memory; File Systems; I/O; IPC; Network Structure.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Linux Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 142

*UGC NET Aug 2024, original Q138*

> Match List - I with List - II. List - I List - II (operating system concepts) (characteristics)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Paging (D) Evicts least recently used process
> - **B.** LRU (Least Recently Used) (LI) Extends physical memory
> - **C.** C-SCAN (III) Logical to physical mapping
> - **D.** Virtual Memory (IV) Circular disk access Choose the correct answer from the options given below : (1)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -II),
> - **B.** -(IV),
> - **C.** -(I,
> - **D.** -(LI) 2)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(II),
> - **B.** -(I),
> - **C.** -(IV),
> - **D.** -(II) (3)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(I),
> - **B.** -(III),
> - **C.** -(IV),
> - **D.** -(II) (4)

**Options**

- **A.** -(I),
- **B.** -(IV),
- **C.** -(III),
- **D.** -(II) 93/101

**Chapter foundations**

This question belongs to the ideas covered by **Linux Operating Systems**. Revise these foundations: Design Principles; Kernel Modules; Process Management and Scheduling; Memory; File Systems; I/O; IPC; Network Structure.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Linux Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 143

*UGC NET June 2025, original Q69*

> Which of the following statement is correct for threads?

**Options**

1. It refers to POSIX standard (IEEE 1002.1c)
2. This standard defines API for thread creation only
3. This is a specification only for thread behavior and not its implementation
4. Operating systems like Solaris, Linux & Mac OS X, except Tru64 UNIX, implement threads 42558919328. 1 42558919330.3 42558919331.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Linux Operating Systems**. Revise these foundations: Design Principles; Kernel Modules; Process Management and Scheduling; Memory; File Systems; I/O; IPC; Network Structure.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Linux Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-13"></a>

### 13. Windows Operating Systems (26 questions)

**What to master:** Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam lens:** Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.

**Reusable method:** Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.

**High-yield rules:** Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.

**Common traps:** Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.

---

#### Question 144

*UGC NET Dec 2011, Paper III, original Q5*

> (a) Describe briefly six windows functions usually called while creating a window. (b) What is the difference between UNIX and Windows Navigat ion and directory control commands ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 145

*UGC NET Dec 2012, Paper II, original Q15*

> What is the size of the Unicode (B) 64 character in Windows Operating (C) 128 System? (D) 160 (A) 8-Bits (B) 16-Bits

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 146

*UGC NET Dec 2013, Paper III, original Q68*

> In windows 2000 operating system all the processor-dep endent code is isolated in a dynamic link library called

**Options**

- **A.** NTFS file system
- **B.** Hardware abstraction layer
- **C.** Microkernel
- **D.** Process Manager

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 147

*UGC NET Dec 2013, Paper III, original Q69*

> To place a sound into a word document, following feature of windows is used :

**Options**

- **A.** Clip board
- **B.** Task switching
- **C.** C Win App
- **D.** OLE

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 148

*UGC NET Dec 2013, Paper III, original Q73*

> Which statement is not true about process O in the Unix operating system ?

**Options**

- **A.** Process O is called init process.
- **B.** Process O is not created by fork system call.
- **C.** After forking process 1, process O becomes swapper process.
- **D.** Process O is a special process created when system boots.

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 149

*UGC NET Dec 2013, Paper III, original Q75*

> Possible thread states in Windows 2000 operating system include :

**Options**

- **A.** Ready, running and waiting
- **B.** Ready, standby, running, waiting, transition and terminated
- **C.** Ready, running, waiting, transition and terminated
- **D.** Standby, running, transition and terminated

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 150

*UGC NET June 2013, Paper III, original Q61*

> An operating system using banker’s algorithm for deadlock avoidance has ten dedicated devices (of same type) and has three processes P1, P2 and P3 with maximum resource requirements of 4, 5 and 8 respectively. There are two states of allocation of devices as follows : State 1 Processes P1 P2 P3 Devices allocated 2 3 4 State 2 Processes P1 P2 P3 Devices allocated 0 2 4 Which of the following is correct ?

**Options**

- **A.** State 1 is unsafe and state 2 is safe.
- **B.** State 1 is safe and state 2 is unsafe.
- **C.** Both, state 1 and state 2 are safe.
- **D.** Both, state 1 and state 2 are unsafe.

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 151

*UGC NET June 2013, Paper III, original Q62*

> Let the time taken to switch between user mode and kernel mode of execution be T1 while time taken to switch between two user processes be T2. Which of the following is correct ?

**Options**

- **A.** T1 < T2
- **B.** T1 > T2
- **C.** T1 = T2
- **D.** Nothing can be said about the relation between T1 and T2.

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 152

*UGC NET June 2013, Paper III, original Q66*

> The versions of windows operating system like windows XP and window Vista uses following file system :

**Options**

- **A.** FAT-16
- **B.** FAT-32
- **C.** NTFS (NT File System)
- **D.** All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 153

*UGC NET Dec 2014, Paper III, original Q52*

> An operating system has 13 tape drives. There are three processe s P1, P2 & P3. Maximum requirement of P1 is 11 tape drives, P2 is 5 tape drives and P3 is 8 t ape drives. Currently, P1 is allocated 6 tape drives, P2 is allocated 3 tape drives and P3 is allocated 2 tape drives. Which of the following sequences represent a safe state ?

**Options**

- **A.** P2 P1 P3
- **B.** P2 P3 P1
- **C.** P1 P2 P3
- **D.** P1 P3 P2

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 154

*UGC NET Dec 2014, Paper III, original Q73*

> Which of the following versions of Windows O.S. contain built-in partiti on manager which allows us to shrink and expand pre-defined drives ?

**Options**

- **A.** Windows Vista
- **B.** Windows 2000
- **C.** Windows NT
- **D.** Windows 98

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 155

*UGC NET Dec 2014, Paper III, original Q74*

> A Trojan horse is

**Options**

- **A.** A program that performs a legitimate function that is know n to an operating system or its user and also has a hidden component that can be used for nef arious purposes like attacks on message security or impersonation.
- **B.** A piece of code that can attach itself to other programs in the system and spread to other systems when programs are copied or transferred.
- **C.** A program that spreads to other computer systems by exploi ting security holes like weaknesses in facilities for creation of remote processes
- **D.** All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 156

*UGC NET Dec 2015, Paper III, original Q42*

> In an operating system, indivisibility of operation means :

**Options**

1. Operation is interruptable
2. Race - condition may occur
3. Processor can not be pre-empted
4. All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 157

*UGC NET Dec 2015, Paper III, original Q55*

> The character set used in Windows 2000 operating system is

**Options**

1. 8 bit ASCII
2. Extended ASCI
3. 16 bit UNICODE
4. 12 bit UNICODE

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 158

*UGC NET June 2015, Paper III, original Q49*

> Match the following for operating system techniques with the most appropriate advantage : List - I List - II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Spooling (i) Allows several jobs in memory to improve CPU utilization
> - **B.** Multiprogramming (ii) Access to shared resources among geographically dispersed computers in a transparent way
> - **C.** Time sharing (iii) Overlapping I/O and computations
> - **D.** Distributed computing (iv) Allows many users to share a computer simultaneously by switching processor frequently Codes : (a) (b) (c) (d) (1) (ili)

**Options**

1. (ii) (iv)
2. (iii) (i) (iv) (ii)
3. (iv) (ill) (i)
4. (ii) (iii) (iv) (i)

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 159

*UGC NET July 2016, Paper III, original Q52*

> Which of the following option with referen ce to UNIX operating system is not correct ?

**Options**

1. INT signal is sent by the terminal driv er when one types <Cont rol-C> and it is a request to terminate the current operation.
2. TERM is a request to terminate execu tion completely. The receiving process will clean up its state and exit.
3. QUIT is similar to TERM, except that it defaults to producing a core dump if not caught.
4. KILL is a blockable signal.

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 160

*UGC NET Jan 2017, Paper III, original Q66*

> Names of some of the Operating Systems are given below : (a) MS-DOS (b) XENIX (c) OS/2 In the above list, following operating systems didn’t provide multiuser facility.

**Options**

1. (a) only
2. (a) and (b) only
3. (b) and (c) only
4. (a), (b) and (c)

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 161

*UGC NET Dec 2018, original Q114*

> Suppose a cloud contains software stack such as Operating systems, Application softwares, etc. This model is referred as _ model. Saas 91394342454. Paas 91394342455. Iaas 91394342456. Maas

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 162

*UGC NET Dec 2018, original Q117*


**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 163

*UGC NET July 2018, Paper II, original Q53*

> In a multi-user operating system, 30 requests are made to use a particul ar resource per hour, on an average. The probability that no requests are made in 40 minutes, when arr ival pattern is a poisson distribution, is _________.

**Options**

1. e−15
2. 1−e−15
3. 1−e−20
4. e−20

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 164

*UGC NET July 2018, Paper II, original Q54*

> Normally user programs are prevented from handling I/O directly by I/O instructions in them. For CPUs having explicit I/O instructions, such I/O protecti on is ensured by having the I/O instructions privileged. In a CPU with memory mapped I/O, there i s no explicit I/O instruction. Which one of the following is true for a CPU with mem ory mapped I/O ?

**Options**

1. I/O protection is ensured by operating system routines.
2. I/O protection is ensured by a hardware trap.
3. I/O protection is ensured during system configuration.
4. I/O protection is not possible.

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 165

*UGC NET Dec 2019, original Q128*

> Guid Consider the following statements: (a) Windows Azure is a cloud-based operating system. (b) Google App Engine is an integrated set of online services for consumers to communicate and share with others. (c) Amazon Cloud Front is a web service for content delivery. Which of the statements is (are) correct?

**Options**

1. Only (a) and (b)
2. Only (a) and (c)
3. Only (b) and (c)
4. (a), (b) and (c) 61547541210.2 61547541211.3 61547541212. 4

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 166

*UGC NET Nov 2020, original Q94*

> Which of the following statements with respect to multiprocessor system are true? (A) Multiprocessor system is controlled by one operating system. (B) In Multiprocessor system, multiple computers are connected by the means of communication lines. (C) Multiprocessor system is classified as multiple instruction stream and multiple data stream system. Choose the correct answer from the options given below:

**Options**

1. (A) only
2. (A) and (B) only
3. (A) and (C) only
4. (B) and (C) only 53622816874.2 53622816875.3 53622816876.4

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 167

*UGC NET Oct 2022, original Q22*

> If an operating system does not allow a child process to exist when the parent process has been terminated, this phenomenon is called as -

**Options**

1. Threading
2. Cascading termination
3. Zombie termination
4. Process killing

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 168

*UGC NET Dec 2022 session, 11 Mar 2023 Shift 2, original Q4*

> Virtual, Services
>
> **Additional extracted choices — check the source page:**
>
> 1. 1
> 2. 2
> 3. 3
> 4. 4 1 2 . If FCFS is replaced by shortest seek time first (SSTF) and the vendor claims 50% better benchmark results. What is the expected improvement in the VO performance of user programs?
>
> **Additional extracted choices — check the source page:**
>
> 1. 50%
> 2. 100%
> 3. 25%
> 4. 0%
>
> **Additional extracted choices — check the source page:**
>
> 1. 1
> 2. 2
> 3. 3
> 4. 4 i Option 10-3924 P2 P1 15 P3 1.8 2. 16 3.32 4. 48

**Options**

1. 1
2. 2
3. 3
4. 4 [Option ID=39371 3[Option ID=393791 Option ID=39378

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 169

*UGC NET June 2025, original Q96*

> Which of the followings shows the correct hierarchy of a layered file system in an operating system

**Options**

- **A.** Logical File System
- **B.** File Organization Module
- **C.** Basic File System
- **D.** I/O Control E. Application Programs Choose the correct answer from the options given below: 1.A →B→D → C→ E 2.D →E →C→A→B 3.E→A→ →B → C → D 4. E →C→B →A→D 42558919437.2 42558919438.3 42558919439.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Windows Operating Systems**. Revise these foundations: Design Principles; Components; Terminal Services and Fast User Switching; File System; Networking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Windows Operating Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-14"></a>

### 14. Distributed Systems (13 questions)

**What to master:** Network-Based OS Types; Network, Communication and Protocol Structures; Robustness; Design Issues; Distributed File Systems.

**Exam lens:** Draw the system state: ready queue, allocation graph, page table, disk head, semaphore values, or file blocks.

**Reusable method:** Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test.

**High-yield rules:** Turnaround = completion - arrival; waiting = turnaround - burst. Effective access time is a probability-weighted latency. Banker's algorithm needs an executable safe sequence.

**Common traps:** Distinguish deadlock prevention, avoidance and detection; page number from offset; response time from waiting time; starvation from deadlock.

---

#### Question 170

*UGC NET Dec 2009, Paper II, original Q38*

> A semaphore count of negative n means (s = – n) that the queue cont ains ________ waiting processes.

**Options**

- **A.** n + 1
- **B.** n
- **C.** n – 1
- **D.** 0

**Chapter foundations**

This question belongs to the ideas covered by **Distributed Systems**. Revise these foundations: Network-Based OS Types; Network, Communication and Protocol Structures; Robustness; Design Issues; Distributed File Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Distributed Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 171

*UGC NET June 2010, Paper II, original Q14*

> Match the following : (a) Garbage collection in

**Chapter foundations**

This question belongs to the ideas covered by **Distributed Systems**. Revise these foundations: Network-Based OS Types; Network, Communication and Protocol Structures; Robustness; Design Issues; Distributed File Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Distributed Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 172

*UGC NET Dec 2012, Paper II, original Q21*

> Which API is used to draw a circle ? (B) 111 & 11
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Circle ()
> - **B.** Ellipse ()
> - **C.** 133 & 33 (C) Round Rect ()
> - **D.** 144 & 44 (D) Pie ()

**Chapter foundations**

This question belongs to the ideas covered by **Distributed Systems**. Revise these foundations: Network-Based OS Types; Network, Communication and Protocol Structures; Robustness; Design Issues; Distributed File Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Distributed Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 173

*UGC NET June 2015, Paper II, original Q50*

> Which of the following is not valid with reference to Message Passing Interface (MPI)?

**Options**

1. MPI can run on any hardware platform.
2. The programming model is a distributed memory model.
3. All parallelism is implicit.
4. MPI - Comm - Size returns the total number of MPI processes in specified communication. - 000- J-8715 11 Paper-II

**Chapter foundations**

This question belongs to the ideas covered by **Distributed Systems**. Revise these foundations: Network-Based OS Types; Network, Communication and Protocol Structures; Robustness; Design Issues; Distributed File Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Distributed Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 174

*UGC NET July 2016, Paper II, original Q39*

> In UNIX, _________ creates three subdirectorie s : ‘PIS’ and two subdirectories ‘progs’ and ‘data’ from just created subdirectory ‘PIS’.

**Options**

1. mkdir PIS/progs PIS/data PIS
2. mkdir PIS progs data
3. mkdir PIS PIS/progs PIS/data
4. mkdir PIS/progs data

**Chapter foundations**

This question belongs to the ideas covered by **Distributed Systems**. Revise these foundations: Network-Based OS Types; Network, Communication and Protocol Structures; Robustness; Design Issues; Distributed File Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Distributed Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 175

*UGC NET July 2016, Paper III, original Q49*

> In UNIX, processes that have finished executi on but have not yet had their status collected are known as _________.

**Options**

1. Sleeping processe s
2. Stopped processes
3. Zombie processe s
4. Orphan processes

**Chapter foundations**

This question belongs to the ideas covered by **Distributed Systems**. Revise these foundations: Network-Based OS Types; Network, Communication and Protocol Structures; Robustness; Design Issues; Distributed File Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Distributed Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 176

*UGC NET Jan 2017, Paper II, original Q40*

> Distributed operating systems consist of :

**Options**

1. Loosely coupled O.S. software on a loosely coupled hardware.
2. Loosely coupled O.S. software on a tightly coupled hardware.
3. Tightly coupled O.S. software on a loosely coupled hardware.
4. Tightly coupled O.S. software on a tightly coupled hardware.

**Chapter foundations**

This question belongs to the ideas covered by **Distributed Systems**. Revise these foundations: Network-Based OS Types; Network, Communication and Protocol Structures; Robustness; Design Issues; Distributed File Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Distributed Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 177

*UGC NET Nov 2017, Paper II, original Q36*

> In Distributed system, the capacity of a system to adapt the increased service load is called __________ .

**Options**

1. Tolerance
2. Scalability
3. Capability
4. Loading

**Chapter foundations**

This question belongs to the ideas covered by **Distributed Systems**. Revise these foundations: Network-Based OS Types; Network, Communication and Protocol Structures; Robustness; Design Issues; Distributed File Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Distributed Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 178

*UGC NET Nov 2017, Paper II, original Q46*

> Which of the following Super Computers is the fastest Super Computer ?

**Options**

1. Sun-way TaihuLight
2. Titan
3. Piz Daint
4. Sequoia

**Chapter foundations**

This question belongs to the ideas covered by **Distributed Systems**. Revise these foundations: Network-Based OS Types; Network, Communication and Protocol Structures; Robustness; Design Issues; Distributed File Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Distributed Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 179

*UGC NET July 2018, Paper II, original Q49*

> To guarantee correction of upto t errors, the minimum Hamming distan ce d min in a block code must be ________.

**Options**

1. t+1
2. t−2
3. 2t−1
4. 2t+1

**Chapter foundations**

This question belongs to the ideas covered by **Distributed Systems**. Revise these foundations: Network-Based OS Types; Network, Communication and Protocol Structures; Robustness; Design Issues; Distributed File Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Distributed Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 180

*UGC NET July 2018, Paper II, original Q99*

> Simplify the following using K-map : F (A, B, C, D) = Σ (0, 1, 2, 8, 9, 12, 13) d (A, B, C, D) = Σ (10, 11, 14, 15) d stands for don’t care condition.

**Options**

1. A B D BC+ +
2. A B D B C+ +
3. A B C+
4. A B C B D+ +

**Chapter foundations**

This question belongs to the ideas covered by **Distributed Systems**. Revise these foundations: Network-Based OS Types; Network, Communication and Protocol Structures; Robustness; Design Issues; Distributed File Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Distributed Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 181

*UGC NET June 2019, original Q105*

> Which of the following terms best describes Git? Exam Guide

**Options**

1. Issue Tracking System
2. Integrated Development Environment
3. Distributed Version Control System
4. Web-based Repository Hosting Service 64635085756. 2 64635085757.3 64635085758.4

**Chapter foundations**

This question belongs to the ideas covered by **Distributed Systems**. Revise these foundations: Network-Based OS Types; Network, Communication and Protocol Structures; Robustness; Design Issues; Distributed File Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Distributed Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 182

*UGC NET Nov 2021, original Q55*

> Consider the sentence below. There is a country that borders both India and Pakistan. Which of the following logical expressions express the above sentence correctly when the predicate Country(x) represents that x is a country and Borders(x, y) represents that the countries x and y share the border?

**Options**

1. ∃c Country(c) ∧ Border (c, India) ∧ Border (c,Pakistan)
2. ∃c Country(c) ⇒ [Border (c, India) ∧ Border (c,Pakistan)]
3. [∃c Country(c)] ⇒ [Border (c, India) ∧ Border (c,Pakistan)]
4. ∃c Border (Country(c), India ∧ Pakistan)

**Chapter foundations**

This question belongs to the ideas covered by **Distributed Systems**. Revise these foundations: Network-Based OS Types; Network, Communication and Protocol Structures; Robustness; Design Issues; Distributed File Systems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Distributed Systems questions: Simulate events in timestamp order. For scheduling write the Gantt chart; for paging record every reference; for deadlock run the safety or detection test. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

## Coverage and quality notes

- Recovered question blocks in this unit: **182**
- Chapter placements with direct keyword support: **173**
- Chapter placements needing manual review: **9**
- Questions with validated answers in this guide: **0**
- OCR may flatten mathematical notation, tables, code indentation, and figures. Full audit references are retained in the structured data.
- Some combined Paper 1/Paper 2 scans and older papers lack a trustworthy embedded key. Such questions remain pending rather than receiving guessed answers.

---

[Back to contents](#contents) · [All units](README.md) · [Project home](../README.md)

