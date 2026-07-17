# Question 31

*UGC NET CS · 2017 Jan Paper 2 · Lexical Analysis · Regular-Expression String Matching*

Which strings match the regular expression p+[3−5]*[xyz]? I. p443y; II. p6y; III. 3xyz; IV. p35z; V. p353535x; VI. ppp5.

- **1.** I, III and VI only
- **2.** IV, V and VI only
- **3.** II, IV and V only
- **4.** I, IV and V only

> [!TIP]
> **Correct answer: 4. I, IV and V only**

## Solution

Read the expression in three parts: p+ requires one or more p characters; [3−5]* permits zero or more digits chosen only from 3,4,5; and [xyz] requires exactly one final x, y, or z. I, p443y, satisfies all three parts. IV, p35z, and V, p353535x, also satisfy them. II contains forbidden digit 6, III does not start with p, and VI ends in 5 rather than x/y/z. Thus I, IV, and V only—option 4—match.

## Key Points

- Parse a regular expression by quantifier scope: p+ · [3−5]* · [xyz].

## Why the other options are incorrect

Every other answer set includes at least one invalid string or omits a valid one. The plus applies only to p, the star only to the digit class, and the final character class is mandatory.
