# Question 78

*UGC NET CS · 2019 June Paper 1 And 2 · 2-D Geometrical Transforms and Viewing · Reflection and rotation matrices*

Consider the following statements regarding 2D transforms in computer graphics. S1: The matrix [[1,0],[0,-1]] reflects a 2D point about the X-axis. S2: A 2x2 matrix which mirrors any 2D point about the X-axis is a rotation matrix. What can you say about S1 and S2?

- **1.** Both S1 and S2 are true
- **2.** Only S1 is true
- **3.** Only S2 is true
- **4.** Both S1 and S2 are false

> [!TIP]
> **Correct answer: 2. Only S1 is true**

## Solution

Multiplying (x,y) by [[1,0],[0,-1]] produces (x,-y), which is reflection about the x-axis, so S1 is true. A proper 2D rotation matrix has determinant +1. This reflection matrix has determinant -1 and reverses orientation, so it is not a rotation matrix. Hence S2 is false.

## Key Points

- Both rotations and reflections preserve lengths, but a rotation has determinant +1 whereas a reflection has determinant -1.

## Why the other options are incorrect

- **Option 1:** incorrectly classifies a reflection as a rotation.
- **Option 3:** rejects the correct coordinate effect in S1.
- **Option 4:** also rejects S1.
