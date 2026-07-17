# Question 92

*UGC NET CS · 2018 July Paper 2 · Digital Logic Circuits and Components · RS Flip-Flop Hold State*

For an active-high RS flip-flop, when does the output after a clock pulse remain equal to its previous value?

- **1.** S= R= 1
- **2.** S= 0, R = 1
- **3.** S= 1, R = 0
- **4.** S= R= 0

> [!TIP]
> **Correct answer: 4. S= R= 0**

## Solution

For the standard active-high RS latch/clocked RS flip-flop, S=0 and R=0 assert neither set nor reset. The stored state is therefore preserved: Q(t+1)=Q(t). Hence option 4 is correct.

## Key Points

- Active-high RS memory: 00 hold, 10 set, 01 reset, 11 invalid.

## Why the other options are incorrect

S=0,R=1 resets Q; S=1,R=0 sets Q. S=R=1 is the forbidden/indeterminate combination for the active-high NOR implementation. Active-low NAND inputs reverse the asserted levels, but the exam uses the standard active-high truth table.
