# Question 135

*UGC NET CS · 2018 Dec Paper 1 And 2 · File Organization and Indexing · Clustering Index on an Ordering Non-Key Field*

A clustering index is defined on fields which are of type:

- **1.** non-key and ordering
- **2.** non-key and non-ordering
- **3.** key and ordering
- **4.** key and non-ordering

> [!TIP]
> **Correct answer: 1. non-key and ordering**

## Solution

A clustering index is built when the data file is physically ordered on a field whose value may repeat. Because duplicate ordering-field values can identify a cluster of records rather than one record, this field is non-key; because it determines physical order, it is an ordering field. Therefore option 1—non-key and ordering—is correct.

## Key Points

- Primary index: ordering key; clustering index: ordering non-key; secondary index: non-ordering field.

## Why the other options are incorrect

A non-ordering field cannot define how records are clustered physically, eliminating option 2. If the ordering field is a unique key, the corresponding primary index is used rather than the textbook clustering-index category, eliminating option 3. Option 4 is neither the ordering nor clustering case.
