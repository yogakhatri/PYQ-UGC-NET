# Question 7

*UGC NET CS · 2010 June Paper 2 · Software Configuration Management · Change and Version Control*

Advantage of synchronous sequential circuits over asynchronous ones is

- **A.** faster operation
- **B.** ease of avoiding problems due to hazard
- **C.** lower hardware requirement
- **D.** better noise immunity

> [!TIP]
> **Correct answer: B. ease of avoiding problems due to hazard**

## Solution

A clock constrains when state changes may occur in a synchronous circuit. Designers can analyze signals relative to clock edges and allow combinational paths to settle between them, making races and hazards substantially easier to control than in asynchronous circuits.

## Key Points

- Clocked state transitions make timing behavior predictable and hazard control easier.

## Why the other options are incorrect

Asynchronous circuits may be faster because they need not wait for clocks and may use less clocking hardware. Noise immunity is primarily a logic-family/electrical property, not the defining synchronous advantage.
