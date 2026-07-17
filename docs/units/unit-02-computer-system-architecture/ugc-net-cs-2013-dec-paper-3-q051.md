# Question 51

*UGC NET CS · 2013 Dec Paper 3 · Basic Computer Organization and Design · Clock Generator and Timing Pulses*

Synchronization is achieved by a timing device called a ________ which generates a periodic train of ________.

- **A.** clock generator, clock pulse
- **B.** master generator, clock pulse
- **C.** generator, clock
- **D.** master clock generator, clock pulse

> [!TIP]
> **Correct answer: D. master clock generator, clock pulse**

## Solution

Synchronous digital components coordinate state changes with a master clock generator. That timing device produces a periodic train of clock pulses; the active edge or level of each pulse tells registers and control circuits when an operation may occur. Therefore the complete pair is master clock generator, clock pulse.

## Key Points

- The master clock generator is the timing source; its periodic clock pulses synchronize digital operations.

## Why the other options are incorrect

A omits the standard qualifier master, B uses the nonstandard term master generator, and C reverses the roles into an imprecise generator/clock pair. D supplies both standard names.
