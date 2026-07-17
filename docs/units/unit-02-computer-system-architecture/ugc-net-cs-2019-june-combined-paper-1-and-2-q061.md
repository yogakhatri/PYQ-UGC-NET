# Question 61

*UGC NET CS · 2019 June Paper 1 And 2 · Central Processing Unit · Addressing Modes*

In which type of addressing mode are fewer memory references required?

- **1.** Immediate
- **2.** Implied
- **3.** Register
- **4.** Indexed

> [!TIP]
> **Correct answer: 3. Register**

## Solution

If a single option must be selected, register addressing is the most defensible: the instruction names a CPU register, and the operand is read from that register without an extra data-memory access. Indexed addressing must calculate an effective address and then access memory, so it clearly requires more. However, the item is not uniquely worded: an immediate operand is also contained in the instruction, and many implied instructions operate on an implicit register, so they too may avoid an extra data-memory reference.

## Key Points

- Register operands avoid data-memory access, but count instruction fetch separately and watch for ambiguous wording about immediate or implied operands.

## Why the other options are incorrect

Indexed addressing definitely requires an operand-memory access. Immediate and implied addressing cannot be rejected universally, which is precisely why this exam item is defective rather than a clean single-answer comparison.

## Additional Information

This question was excluded from evaluation in published discussions of the June 2019 paper because more than one option can satisfy the wording. The displayed answer is a forced-choice teaching convention, not a claim that the item is uniquely valid.
