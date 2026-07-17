# Question 26

*UGC NET CS · 2021 Nov With Answers · Graph Theory · Regularity of Wheel Graphs*

For which value of n is Wheel graph W regular?

- **1.** 2
- **2.** 3
- **3.** 4
- **4.** 5

> [!TIP]
> **Correct answer: 2. 3**

## Solution

Using the convention intended here, W_n=K1+C_n: it has an n-vertex rim plus a hub. Every rim vertex has degree 3—two rim neighbours and the hub—while the hub has degree n. The graph is regular exactly when n=3, at which point W_3 is K4 and every vertex has degree 3. Therefore option 2.

## Key Points

- Equate hub degree with rim degree: n=3 under the cycle-size convention.

## Why the other options are incorrect

For n>3 the hub degree n differs from the rim degree 3; n=2 does not give the ordinary simple wheel construction. A notation caveat matters: some references define W_n as the wheel on n total vertices, K1+C_(n−1); under that alternate convention the same K4 is called W_4. The question is ambiguous unless its convention is specified.

## References

- [Wheel Graph — MathWorld (documents both numbering conventions)](https://mathworld.wolfram.com/WheelGraph.html)
- [NetworkX wheel_graph documentation (alternate total-vertex convention)](https://networkx.org/documentation/stable/reference/generated/networkx.generators.classic.wheel_graph.html)
