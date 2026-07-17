# Question 3

*UGC NET CS · 2014 Dec Paper 3 · Input-Output Organization · Printer Throughput and Line Time*

In a dot matrix printer the time to print a character is 6 m.s ec., time to space in between characters is 2 m.sec., and the number of characters in a line a re 200. The printing speed of the dot matrix printer in characters per second and the time to print a character line are given by which of the following options ?

- **A.** 125 chars/second and 0.8 seconds
- **B.** 250 chars/second and 0.6 seconds
- **C.** 166 chars/second and 0.8 seconds
- **D.** 250 chars/second and 0.4 seconds

> [!TIP]
> **Correct answer: No listed option is correct. The stated times give 125 characters/s and about 1.6 s for a 200-character line.**

## Solution

Each character position takes 6 ms to print plus 2 ms to move to the next position, approximately 8 ms. Throughput is 1/0.008=125 characters/s. A 200-character line therefore takes 200×0.008=1.6 s; if no spacing follows the final character, the exact time is 200×6+199×2=1598 ms, still about 1.6 s. Option A contains the correct speed but an incorrect 0.8 s line time.

## Key Points

- Check internal consistency: line time must equal character count divided by characters per second.

## Why the other options are incorrect

B and D claim 250 characters/s, which would require 4 ms per character position. C uses approximately the reciprocal of the 6 ms print time but still gives an incompatible line time. None pairs 125 with 1.6 s.
