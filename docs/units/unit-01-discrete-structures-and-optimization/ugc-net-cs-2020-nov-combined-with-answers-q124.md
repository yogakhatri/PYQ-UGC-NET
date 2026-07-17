# Question 124

*UGC NET CS · 2020 Nov With Answers · Discrete Structures · Lexicographic Ordering of Bit Strings*

Find the lexicographic order, using 0<1, of the bit strings 001, 010, 011, 0001, and 0101.

- **1.** 001 < 010 < 011 < 0001 < 0101
- **2.** 0001 < 001 < 010 < 0101 < 011
- **3.** 0001 < 0101 < 001 < 010 < 011
- **4.** 001 < 010 < 0001 < 0101 < 011

> [!TIP]
> **Correct answer: 2. 0001 < 001 < 010 < 0101 < 011**

## Solution

Compare strings left to right using 0<1; if one string is a prefix of another, the shorter string comes first. First, 0001<001 because the first difference is the third bit, 0<1. Next 001<010 because their second bits are 0 and 1. Since 010 is a prefix of 0101, 010<0101. Finally 0101<011 because their third bits are 0 and 1. Thus 0001<001<010<0101<011, option 2.

## Key Points

- Stop at the first differing symbol; only when no difference appears before one string ends does the shorter prefix come first.

## Why the other options are incorrect

The other choices treat the strings as binary numbers, sort partly by length, or place an extension before its prefix. Lexicographic order is dictionary order, not numeric order.
