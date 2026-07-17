# Question 7

*UGC NET CS · 2017 Jan Paper 2 · Digital Logic Circuits and Components · Logic Families and ECL*

ECL is the fastest of all logic families. High speed in ECL is possible because transistors are used in difference amplifier configuration, in which they are never driven into ____.

- **1.** Race condition
- **2.** Saturation
- **3.** Delay
- **4.** High impedance

> [!TIP]
> **Correct answer: 2. Saturation**

## Solution

Emitter-coupled logic uses a differential-amplifier arrangement whose transistors switch current between branches without being driven into saturation. Avoiding saturation eliminates the storage time needed to remove excess charge from a saturated transistor, producing very small propagation delay. Therefore the blank is saturation, option 2.

## Key Points

- ECL is fast because its transistors remain in the active region and avoid saturation-storage delay.

## Why the other options are incorrect

Race condition is a timing interaction between signals or processes, not a transistor operating region. Delay is the quantity ECL reduces, not a state into which the transistor is driven. High impedance is associated with tri-state outputs and does not explain ECL's differential switching speed.
