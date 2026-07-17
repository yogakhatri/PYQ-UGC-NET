# Question 2

*UGC NET CS · 2015 June Paper 3 · Input-Output Organization · Bus Width, Clock Rate, and Transfer Bandwidth*

Consider a 32 - bit microprocessor, with a 16 - bit external data bus, driven by an 8 MHz input clock. Assume that this microprocessor has a bus cycle whose minimum duration equals four input clock cycles. What is the maximum data transfer rate for this microprocessor ?

- **1.** 8 × 10^6 bytes/sec
- **2.** 4 × 10^6 bytes/sec
- **3.** 16 × 10^6 bytes/sec
- **4.** 4 × 10^9 bytes/sec

> [!TIP]
> **Correct answer: 2. 4 × 10^6 bytes/sec**

## Solution

An 8 MHz clock has 8 million clock cycles per second. One bus cycle requires four clocks, so at most `8×10^6 / 4 = 2×10^6` bus transfers occur per second. The external bus carries 16 bits = 2 bytes per transfer. Therefore the maximum rate is `2×10^6 × 2 = 4×10^6 bytes/s`.

## Key Points

- Bandwidth = bus cycles per second × bytes per bus cycle = `(clock/4) × 2`.

## Why the other options are incorrect

Option 1 forgets the four-clock bus-cycle duration. Option 3 incorrectly uses the processor's 32-bit internal width and also ignores timing. Option 4 is three orders of magnitude too large. External-bus width, not internal word size, determines bytes per bus transfer.
