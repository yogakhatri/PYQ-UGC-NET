# Question 7

*UGC NET CS · 2014 Dec Paper 3 · Distributed Databases · Location Transparency*

Location transparency allows : I. Users to treat the data as if it is done at one location. II. Programmers to treat the data as if it is at one location. III. Managers to treat the data as if it is at one location. Which one of the following is correct ?

- **A.** I, II and III
- **B.** I and II only
- **C.** II and III only
- **D.** II only

> [!TIP]
> **Correct answer: A. I, II and III**

## Solution

Location transparency hides the physical sites that store distributed data. Users issue the same logical queries, programmers write applications against one global schema, and managers can reason about the data service as one logical database rather than coordinating site-specific names. All three groups may treat the data as if it were at one location.

## Key Points

- Location transparency presents one logical database while the DBMS resolves physical site locations.

## Why the other options are incorrect

B and C arbitrarily exclude one stakeholder group, while D restricts the benefit to programmers alone. Location transparency is a property of the distributed database interface, not of one job role.
