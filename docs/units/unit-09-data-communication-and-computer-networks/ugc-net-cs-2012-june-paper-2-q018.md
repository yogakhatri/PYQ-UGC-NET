# Question 18

*UGC NET CS · 2012 June Paper 2 · Data Communication · M-ary PSK and Baud Rate*

A 16-level phase-shift-keying signal carries 9600 bit/s. What is its modulation rate?

- **A.** 2400 bauds
- **B.** 1200 bauds
- **C.** 4800 bauds
- **D.** 9600 bauds

> [!TIP]
> **Correct answer: A. 2400 bauds**

## Solution

An M-ary signal carries log2(M) bits per symbol. With M=16, each phase symbol represents log2(16)=4 bits. Symbol rate (baud)=bit rate/bits per symbol=9600/4=2400 symbols per second, so the modulation rate is 2400 baud.

## Key Points

- For M-ary modulation, baud=bit rate/log2(M).

## Why the other options are incorrect

1200 baud would imply 8 bits per symbol (256 levels); 4800 would imply 2 bits per symbol (4 levels); 9600 would be binary signalling with 1 bit per symbol.
