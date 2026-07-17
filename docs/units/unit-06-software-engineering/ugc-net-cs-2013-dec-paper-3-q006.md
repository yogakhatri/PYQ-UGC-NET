# Question 6

*UGC NET CS · 2013 Dec Paper 3 · Software Design · Types of Module Coupling*

Match the following : List – I List – II a. Data coupling i. Module A and Module B have shared data b. Stamp coupling ii. Dependency between modules is based on the fact they communicate by only passing of data c. Common coupling iii. When complete data structure is passed from one module to another d. Content coupling iv. When the control is passed from one module to the middle of another Codes : a b c d

- **A.** iii ii i iv
- **B.** ii iii i iv
- **C.** ii iii iv i
- **D.** iii ii iv i

> [!TIP]
> **Correct answer: B. ii iii i iv**

## Solution

Data coupling passes only the needed data (ii). Stamp coupling passes an entire composite structure (iii). Common coupling occurs when modules share global data (i). Content coupling is the strongest form listed, where one module transfers control into or depends on the internals of another (iv). Thus a-ii,b-iii,c-i,d-iv.

## Key Points

- Coupling quality generally worsens from data to stamp to common to content coupling.

## Why the other options are incorrect

The other codes swap the distinguishing definitions. Use 'stamp' for a whole record/structure, 'common' for shared globals and 'content' for intrusion into another module's implementation.
