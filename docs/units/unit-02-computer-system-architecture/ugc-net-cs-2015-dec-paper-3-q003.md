# Question 3

*UGC NET CS · 2015 Dec Paper 3 · Microprocessors · 8085 Hardware Interrupt Priority*

Which of the following 8085 microprocessor hardware interrupt has the lowest priority ?

- **1.** RST 6.5
- **2.** RST 7.5
- **3.** TRAP
- **4.** INTR

> [!TIP]
> **Correct answer: 4. INTR**

## Solution

The 8085 hardware-interrupt priority from highest to lowest is TRAP, RST 7.5, RST 6.5, RST 5.5, and INTR. Therefore INTR is the lowest-priority interrupt among the choices. It is also non-vectored and maskable.

## Key Points

- Memorize 8085 priority: TRAP > 7.5 > 6.5 > 5.5 > INTR.

## Why the other options are incorrect

TRAP is the highest-priority, non-maskable interrupt. RST 7.5 outranks RST 6.5, and both outrank INTR.
