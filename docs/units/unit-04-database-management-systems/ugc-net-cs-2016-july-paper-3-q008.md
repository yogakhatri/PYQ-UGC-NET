# Question 8

*UGC NET CS · 2016 July Paper 3 · Distributed Databases · Location Transparency and Fragment Names*

In distributed databases, location transparency allows for database users, programmers and administrators to treat the data as if it is at one location. A SQL query with location transparency needs to specify :

- **1.** Inheritances
- **2.** Fragments
- **3.** Locations
- **4.** Local formats

> [!TIP]
> **Correct answer: 2. Fragments**

## Solution

Location transparency hides the physical site of each distributed fragment. At this transparency level, a query may refer to the required fragment names, but it does not state which sites hold them. Therefore it needs to specify fragments, option 2.

## Key Points

- Location transparency hides sites while allowing logical fragment references; fragmentation transparency would hide the fragments too.

## Why the other options are incorrect

Specifying locations would defeat location transparency, and local storage formats are also hidden from the user. Inheritance is an object-model concept unrelated to locating distributed relational data.
