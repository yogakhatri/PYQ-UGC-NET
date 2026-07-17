# Question 58

*UGC NET CS · 2019 Dec Paper 1 And 2 · Sets and Relations · Representation and Properties of Relations*

How many reflexive relations are there on a set with 4 elements?

- **1.** 2^4
- **2.** 2^12
- **3.** 4^2
- **4.** 2

> [!TIP]
> **Correct answer: 2. 2^12**

## Solution

A relation on a four-element set is a subset of A×A, which has 4²=16 ordered pairs. Reflexivity forces the four diagonal pairs (a,a) to be present. Each of the remaining 16−4=12 off-diagonal pairs may independently be included or omitted. Therefore there are 2^12 reflexive relations, option 2.

## Key Points

- For n elements, reflexivity fixes n of the n² pairs and leaves 2^(n²−n) possible relations.

## Why the other options are incorrect

2^4 counts choices for only four pairs, but the diagonal pairs are compulsory, not optional. 4²=16 is the number of possible ordered pairs, not the number of relations. The count is far greater than 2 because twelve independent binary choices remain.
