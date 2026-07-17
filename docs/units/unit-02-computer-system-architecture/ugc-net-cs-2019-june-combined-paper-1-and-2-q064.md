# Question 64

*UGC NET CS · 2019 June Paper 1 And 2 · Microprogrammed Control · Diagnostic Tracing*

The fault can be easily diagnosed in the micro-program control unit using diagnostic tools by maintaining the contents of

- **1.** flags and counters ›ona
- **2.** registers and counters
- **3.** flags and registers
- **4.** flags, registers and counters

> [!TIP]
> **Correct answer: 4. flags, registers and counters**

## Solution

Diagnostic tracing of a microprogrammed control unit preserves the machine's important state across microinstructions. Flags reveal condition outcomes, registers hold operands and intermediate values, and counters track sequencing or repeated operations. Maintaining all three lets a diagnostic tool reconstruct where control or data first diverged from the expected execution. Therefore flags, registers and counters are all included.

## Key Points

- Microprogram diagnostics work by tracing control state and datapath state together: flags, registers and counters.

## Why the other options are incorrect

Options 1-3 each omit one category of state needed for a complete diagnostic trace: register data, condition flags or sequencing counts.
