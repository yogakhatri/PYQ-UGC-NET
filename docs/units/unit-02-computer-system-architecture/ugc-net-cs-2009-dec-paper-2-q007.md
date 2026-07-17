# Question 7

*UGC NET CS · 2009 Dec Paper 2 · Digital Logic Circuits and Components · Logic Gates*

Identify the logic function performed by the circuit shown

- **A.** exclusive OR
- **B.** exclusive NOR
- **C.** NAND
- **D.** NOR

> [!TIP]
> **Correct answer: B. exclusive NOR**

## Solution

All gates shown are NOR gates. Let a=¬(x+y). The two middle outputs are b=¬(x+a) and c=¬(a+y), and the final output is f=¬(b+c). Evaluating the four input pairs gives f=1 for 00 and 11, but f=0 for 01 and 10. That is the XNOR (equivalence) truth table.

## Key Points

- Name intermediate gate outputs, then evaluate or algebraically simplify the NOR network.

## Why the other options are incorrect

XOR has the complementary truth table. NAND is zero only at 11, and NOR is one only at 00; neither matches the circuit's two equal-input cases.
