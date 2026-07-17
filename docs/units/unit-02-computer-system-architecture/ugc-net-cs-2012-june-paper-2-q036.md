# Question 36

*UGC NET CS · 2012 June Paper 2 · Digital Logic Circuits and Components · Logic Families and ECL*

Which of the following logic families is well suited for high-speed operations ?

- **A.** TTL
- **B.** ECL
- **C.** MOS
- **D.** CMOS

> [!TIP]
> **Correct answer: B. ECL**

## Solution

Emitter-Coupled Logic keeps its bipolar transistors out of saturation and steers current between branches. Avoiding saturation storage delay gives ECL very small propagation delay, making it the traditional logic family best known for high-speed operation, though at high power consumption and with smaller noise margins.

## Key Points

- Classic ECL gains speed by using nonsaturating current-steering transistor operation.

## Why the other options are incorrect

TTL is fast but generally slower than ECL. Traditional MOS is slower, while CMOS is valued especially for low static power and density; modern CMOS can be extremely fast, but the classic logic-family comparison asked here selects ECL.
