# Question 28

*UGC NET CS · 2014 Dec Paper 3 · Data Communication · Propagation Delay and Unit Consistency*

What is the propagation time if the distance between two points is 48,000 (the source omits the distance unit)? Assume a propagation speed of 2.4 × 10⁸ metres/second in the cable.

- **A.** 0.5 ms
- **B.** 20 ms
- **C.** 50 ms
- **D.** 200 ms

> [!TIP]
> **Correct answer: The printed question is incomplete. If 48,000 km was intended, option D: 200 ms; if 48,000 m was intended, 0.2 ms, which is not listed.**

## Solution

Propagation delay is distance/propagation speed, but the source gives 48,000 without a unit. Interpreting it as 48,000 km gives 48,000,000 m ÷ (2.4×10⁸ m/s) = 0.2 s = 200 ms, matching D. Interpreting it as 48,000 m gives 2×10⁻⁴ s = 0.2 ms, matching no option. The options reveal the examiner's likely intended unit, but dimensional analysis shows that the printed item has no unique answer.

## Key Points

- Propagation delay d/v is meaningful only when units are specified and converted consistently; answer choices cannot repair a missing unit, though they may reveal intent.

## Why the other options are incorrect

With the likely kilometre interpretation, 0.5 ms, 20 ms, and 50 ms do not equal 0.2 s. More importantly, choosing D without stating the missing-unit assumption would conceal the defect. Always convert distance to metres before dividing by a speed in metres per second.
