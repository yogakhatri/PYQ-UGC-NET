# Question 128

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Programming in C · Do-while loop execution order*

S.ND:187078 In what sequence the initialization, testing and execution of body is done while using do-while loop? A. Commenting B. Execution of the body C. Initialisation D. Testing the condition Choose the correct answer from the following

- **1.** D.B.C
- **2.** D,C,B
- **3.** C,A,B
- **4.** C,B,D

> [!TIP]
> **Correct answer: 4. C,B,D**

## Solution

A do-while loop initializes its control state (C), executes the body at least once (B), and tests the condition afterward (D). Thus C–B–D.

## Key Points

- Do-while is post-test: initialize → body → condition.

## Why the other options are incorrect

Options beginning with D incorrectly test before the first body execution; option 3 inserts the irrelevant ‘commenting’ item.
