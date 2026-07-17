# Question 68

*UGC NET CS · 2018 July Paper 2 · Database Security · Operating-System File Authorization*

A database system stores each relation in a separate operating-system file and uses the operating system's authorization scheme instead of a special database scheme. Which statement is false?

- **1.** The administrator enjoys more control on the grant option.
- **2.** It is difficult to differentiate among update, delete, and insert authorizations.
- **3.** Cannot store more than one relation in a file.
- **4.** Database operations are speeded up because authorization is carried out at the operating-system level.

> [!TIP]
> **Correct answer: 1. The administrator enjoys more control on the grant option.**

## Solution

Operating-system file permissions are usually coarse read/write controls. They do not reproduce a DBMS's fine-grained privileges or SQL `WITH GRANT OPTION`, so saying that the administrator enjoys more control over the grant option is false. Therefore option 1 is the requested false statement.

## Key Points

- OS file permissions are efficient but coarse; DBMS authorization provides operation-level privileges and controlled delegation.

## Why the other options are incorrect

A single OS write permission cannot normally distinguish INSERT, UPDATE, and DELETE, so statement 2 is true. Under the stated one-relation-per-file arrangement, file-level authorization forces separate files, supporting statement 3. Delegating checks to the OS can reduce DBMS-level authorization work, which is the intended basis for statement 4.
