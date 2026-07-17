# Question 32

*UGC NET CS · 2012 Dec Paper 2 · Network Database Model · User Work Area*

The User Work Area (UWA) is a set of program variables declared in the host program to communicate the contents of individual records between:

- **1.** DBMS and the host record
- **2.** Host program and host record
- **3.** Host program and DBMS
- **4.** Host program and host language

> [!TIP]
> **Correct answer: 3. Host program and DBMS**

## Solution

In a network DBMS, the User Work Area is a collection of host-program variables whose record layouts correspond to database record types. Retrieved record contents are delivered by the DBMS into this area, and updates prepared by the program are passed back through it. It is therefore the communication area between the host program and the DBMS.

## Key Points

- Treat the UWA as the record exchange buffer at the host program-DBMS boundary.

## Why the other options are incorrect

A 'host record' is not the second communicating software system, so options 1 and 2 misstate the interface. The host language provides the environment in which the variables are declared, but the data transfer is between the executing host program and the DBMS, not between a program and its language.
