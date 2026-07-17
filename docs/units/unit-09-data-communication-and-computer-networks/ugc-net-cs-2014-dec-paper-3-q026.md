# Question 26

*UGC NET CS · 2014 Dec Paper 3 · Data Communication · Asynchronous Character Framing*

How many characters per second can be transmitted over a 3200 bps line using asynchronous transfer if each character has 7 data bits, 1 parity bit, 1 start bit, and 1 stop bit?

- **A.** 300
- **B.** 320
- **C.** 360
- **D.** 400

> [!TIP]
> **Correct answer: B. 320**

## Solution

Each asynchronous character occupies 7 data bits + 1 parity bit + 1 start bit + 1 stop bit = 10 transmitted bits. At 3200 bits per second, the character rate is 3200/10 = 320 characters per second. The framing overhead must be included even though it is not payload.

## Key Points

- For asynchronous transmission, throughput in characters/s equals line rate divided by all bits in one framed character.

## Why the other options are incorrect

400 would divide by only the 8 data-plus-parity bits and ignore start/stop framing. 300 and 360 do not result from the stated 10-bit frame at 3200 bps. Option B performs the required bits-per-character conversion.
