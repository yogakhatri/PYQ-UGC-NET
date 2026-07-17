# Question 100

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Database System Concepts and Architecture · Centralized and Client/Server DBMS Architectures*

I. No.5 BID:8705 Consider the relation Student(stuid, dept, cisroll) The following functional dependencies are given: FD1: stuid → dept FD2: dept - stuid FD3: stuid → cisroll FD4: clsroll → stuid FD5: dept → clsroll Which functional dependencies should be removed to obtain the canonical cover of the set? A. FD2 and FD3 B. FD1 and FD5 C. FD5 D. FD1 Choose the correct answer from the options given below:

- **1.** A. B only
- **2.** A, Conly
- **3.** B, C only
- **4.** A, B, C only

> [!TIP]
> **Correct answer: 2. A, Conly**

## Solution

FD2 (dept→stuid) and FD3 (stuid→clsroll) are jointly recoverable after removing them because dept→clsroll (FD5), clsroll→stuid (FD4), and stuid→dept (FD1) form the needed cycle. FD5 alone is also redundant since dept→stuid→clsroll via FD2 and FD3. Thus proposals A and C identify removable dependencies; B does not.

## Key Points

- Test an FD for redundancy by computing its left-side closure using the other dependencies.

## Why the other options are incorrect

Removing FD1 and FD5 loses the ability to derive stuid→dept, so B is not a valid redundancy removal.
