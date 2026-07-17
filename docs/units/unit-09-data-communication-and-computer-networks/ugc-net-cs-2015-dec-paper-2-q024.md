# Question 24

*UGC NET CS · 2015 Dec Paper 2 · Mobile Communication · Cellular Frequency Reuse*

In a typical mobile phone system with hexagonal cells, it is forbidden to reuse a frequency band in adjacent cells. If 840 frequencies are available, how many can be used in a given cell ?

- **1.** 280
- **2.** 210
- **3.** 140
- **4.** 120

> [!TIP]
> **Correct answer: 1. 280**

## Solution

The adjacency graph of the hexagonal cellular layout requires three frequency groups: three mutually adjacent cells meet around a vertex, so fewer than three groups cannot work, and a repeating three-color pattern does work. The 840 available frequencies are therefore divided among a reuse cluster of size 3, giving 840/3=280 frequencies per cell.

## Key Points

- Adjacent hexagonal cells admit a repeating three-group frequency coloring.

## Why the other options are incorrect

210, 140, and 120 correspond to dividing by 4, 6, and 7. Those larger reuse factors are unnecessary under the only restriction stated: no reuse in an adjacent cell.
