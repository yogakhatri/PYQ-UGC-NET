# Question 35

*UGC NET CS · 2013 June Paper 3 · Programming-Language Design · Parameter-Passing Semantic Modes*

Which of the following is/are the fundamental semantic model(s) of parameter passing ?

- **A.** in mode
- **B.** out mode
- **C.** in-out mode
- **D.** all of the above

> [!TIP]
> **Correct answer: D. all of the above**

## Solution

Parameter passing can be classified by the direction in which information crosses the call boundary. In mode carries an initial value from caller to callee; out mode returns a value from callee to caller; and in-out mode does both. These are all fundamental semantic models, regardless of whether a language implements them by copying, references or another mechanism.

## Key Points

- Parameter modes describe information flow: in, out, or both directions.

## Why the other options are incorrect

A, B and C each name a genuine model but omit the other two. Because the question asks which models apply, the complete choice is 'all of the above.'
