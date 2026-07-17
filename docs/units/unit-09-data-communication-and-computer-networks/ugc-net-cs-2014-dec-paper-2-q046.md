# Question 46

*UGC NET CS · 2014 Dec Paper 2 · Mobile and Wireless Networks · Hard versus Soft Handover*

Consider the following statements S1 and S2 : S1 : A hard handover is one in which the channel in the source cell is retained and used for a while in parallel with the channel in the target cell. S2 : A soft handover is one in which the channel in the source cell is released and only then the channel in the target cell is engaged.

- **A.** S1 is true and S2 is not true.
- **B.** S1 is not true and S2 is true.
- **C.** Both S1 and S2 are true.
- **D.** Both S1 and S2 are not true.

> [!TIP]
> **Correct answer: D. Both S1 and S2 are not true.**

## Solution

A hard handover is break-before-make: the source-cell channel is released before the target-cell channel is established, so S1's parallel use is not hard handover. A soft handover is make-before-break: source and target links overlap for a time, so S2's release-first description is not soft handover. Both statements reverse the definitions and are false.

## Key Points

- Hard=break before make; soft=make before break with overlapping links.

## Why the other options are incorrect

A treats S1 as true; B treats S2 as true; C accepts both reversed descriptions. Only D marks both false.
