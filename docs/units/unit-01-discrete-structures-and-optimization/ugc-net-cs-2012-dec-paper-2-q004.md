# Question 4

*UGC NET CS · 2012 Dec Paper 2 · Sets and Relations · Power Set*

The power set of the set {empty set} is:

- **1.** {empty set}
- **2.** {empty set, {empty set}}
- **3.** {0}
- **4.** {0, empty set, {empty set}}

> [!TIP]
> **Correct answer: 2. {empty set, {empty set}}**

## Solution

The set {empty set} is not empty: it contains exactly one element, namely the empty set. A one-element set has 2^1=2 subsets. They are the empty subset and the whole set {empty set}. Hence its power set is {empty set, {empty set}}.

## Key Points

- Distinguish the empty set from a set containing it: |empty set|=0, but |{empty set}|=1, so the latter has two subsets.

## Why the other options are incorrect

Option 1 lists only the empty subset and misses the whole set. Option 3 replaces the empty set with the number 0; these are different objects. Option 4 wrongly introduces 0 and consequently has the wrong members and cardinality.
