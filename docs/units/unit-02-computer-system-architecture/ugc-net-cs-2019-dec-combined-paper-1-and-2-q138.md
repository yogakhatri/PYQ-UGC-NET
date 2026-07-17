# Question 138

*UGC NET CS · 2019 Dec Paper 1 And 2 · Microprogrammed Control · Microoperations and Microinstructions*

Match List I with List II. List I: A. Microoperation; B. Microprogrammed control unit; C. Interrupts; D. Microinstruction. List II: I. specifies microoperations; II. improves CPU utilization; III. uses control memory; IV. is an elementary operation performed on data stored in registers.

- **1.** A-IV, B-III, C-II, D-I
- **2.** A-IV, B-III, C-I, D-II
- **3.** A-III, B-IV, C-I, D-II
- **4.** A-III, B-IV, C-II, D-I

> [!TIP]
> **Correct answer: 1. A-IV, B-III, C-II, D-I**

## Solution

A microoperation is an elementary operation—transfer, shift, arithmetic, or logic—performed on data in registers, so A-IV. A microprogrammed control unit stores its control program in control memory, so B-III. Interrupts let the processor perform other useful work instead of continuously polling or waiting for a device, improving CPU utilization, so C-II. A microinstruction is a control word that specifies the microoperations to be activated in a microcycle, so D-I. Therefore A-IV, B-III, C-II, D-I is option 1.

## Key Points

- Microoperations do the register-level work; microinstructions specify that work; a microprogrammed controller stores them in control memory.

## Why the other options are incorrect

Options 2–4 confuse an interrupt with a microinstruction or swap control memory with the elementary register operation. The pair microoperation/elementary operation and microinstruction/specification should be fixed first; the remaining two then follow directly.
