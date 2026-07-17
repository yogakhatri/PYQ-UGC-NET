# Question 83

*UGC NET CS · 2018 Dec Paper 1 And 2 · Languages and Strings · Counting Nonempty Substrings*

The number of substrings that can be formed from the string 'adefbghnmp' is:

- **1.** 10
- **2.** 45
- **3.** 55
- **4.** 56

> [!TIP]
> **Correct answer: 3. 55**

## Solution

The string `adefbghnmp` has n=10 characters. A nonempty substring is determined by choosing a start position i and an end position j with i≤j. The count is 10+9+⋯+1=10·11/2=55. Because all ten characters are distinct, no two different intervals produce the same substring, so the number of distinct nonempty substrings is also 55. Therefore option 3.

## Key Points

- A length-n string has n(n+1)/2 nonempty substring occurrences; add one only when the empty string is explicitly included.

## Why the other options are incorrect

10 counts only length-one substrings. 45 equals C(10,2) and misses the ten single-character substrings. 56 includes the empty string, which the question’s ordinary use of ‘substrings formed from the string’ does not count here.
