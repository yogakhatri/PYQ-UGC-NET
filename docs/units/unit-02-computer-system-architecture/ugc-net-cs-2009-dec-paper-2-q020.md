# Question 20

*UGC NET CS · 2009 Dec Paper 2 · Data Representation · Data Types*

Which of the following statement is wrong ? I. 2-phase locking protocol suffer from dead lock. II. Time stamp protocol suffer from more aborts. III. A block hole in a DFD is a data store with only inbound flow s. IV. Multivalued dependency among attribute is checked at 3 NF level. V. An entity-relationship diagram is a tool to represent eve nt model.

- **A.** I, II, II
- **B.** II, III, IV
- **C.** III, IV, V
- **D.** I I, IV, V

> [!TIP]
> **Correct answer: C. III, IV, V**

## Solution

I is true because basic 2PL can deadlock. II is generally true because timestamp ordering avoids waiting but may abort conflicting transactions. III is wrong: a DFD black hole is a process that consumes inputs without producing output, not a data store definition. IV is wrong because nontrivial multivalued dependencies are handled by 4NF, not 3NF. V is wrong because an ER diagram represents a data/conceptual model, not an event model. Thus III, IV, and V are wrong.

## Key Points

- Distinguish transaction-control properties, DFD process errors, normalization levels, and data modeling.

## Why the other options are incorrect

The other groups mark statement I or II wrong even though those are recognized properties of the respective concurrency-control protocols, or omit one of III–V.
