# Question 146

*UGC NET CS · 2019 Dec Paper 1 And 2 · Relational Database Design · Functional Dependencies, Keys and Normalization*

Which of the following is a minimal cover F′ of the functional-dependency set F?

- **1.** F′={A→B, A→C, BC→D, D→E}
- **2.** F′={A→BC, B→D, D→E}
- **3.** F′={A→B, A→C, A→D, D→E}
- **4.** F′={A→B, A→C, B→D, C→D, D→E}

> [!TIP]
> **Correct answer: 1. F′={A→B, A→C, BC→D, D→E}**

## Solution

Start by splitting the multiattribute right side A→BC into A→B and A→C. This gives A→B, A→C, D→E, BC→D, and A→D. The dependency A→D is redundant: from A→B and A→C we obtain A→BC, and BC→D then yields A→D transitively. Remove it. Neither B nor C is extraneous in BC→D because B alone and C alone cannot determine D under the remaining dependencies. The minimal cover is therefore {A→B, A→C, BC→D, D→E}, option 1.

## Key Points

- Minimal cover: split right sides, remove extraneous left-side attributes, then remove dependencies implied by the rest.

## Why the other options are incorrect

Option 2 wrongly replaces BC→D by B→D and also keeps a nonsingleton right side. Option 3 drops the necessary BC→D, so it is not equivalent to F. Option 4 asserts both B→D and C→D, neither of which follows from the original set.
