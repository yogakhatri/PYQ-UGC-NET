# Question 41

*UGC NET CS · 2017 Nov Paper 2 · Software Maintenance · Software Evolution and Change-Induced Deterioration*

Software does not wear-out in the traditional sense of the term, but software does tend to deteriorate as it evolves, because :

- **1.** Software suffers from exposure to hostile environments.
- **2.** Defects are more likely to arise after software has been used often.
- **3.** Multiple change requests introduce errors in component interactions.
- **4.** Software spare parts become harder to order.

> [!TIP]
> **Correct answer: 3. Multiple change requests introduce errors in component interactions.**

## Solution

Software has no physical parts that fatigue from repeated execution, so ordinary use does not wear it out. It can nevertheless deteriorate as successive maintenance changes accumulate: modifications introduce new faults, disturb interfaces, and increase structural complexity, especially in component interactions. This is exactly option 3.

## Key Points

- Software failure rate changes mainly because the software is modified, not because executing unchanged code physically ages it.

## Why the other options are incorrect

Hostile physical environments and unavailable spare parts explain hardware failure, not software behavior. Simply running a correct program often does not create new defects; defects arise from design/code faults or changes, even though repeated use may reveal them.
