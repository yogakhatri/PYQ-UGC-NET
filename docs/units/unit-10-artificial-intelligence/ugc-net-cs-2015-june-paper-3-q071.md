# Question 71

*UGC NET CS · 2015 June Paper 3 · Fuzzy Sets · Fuzzy Addition by the Extension Principle*

Let A={(1,0.3),(2,0.6),(3,1),(4,0.7),(5,0.2)} and B={(10,0.5),(11,1),(12,0.5)}. Using μ_(A+B)(z)=max_(x+y=z) min(μ_A(x),μ_B(y)), find A+B.

- **1.** {(11, 0.8), (13, 1), (15,1)}
- **2.** {(11, 0.3), (12, 0.5), (13, 1), (14, 1), (15, 1), (16, 0.5), (17, 0.2)}
- **3.** {(11, 0.3), (12, 0.5), (13, 0.6), (14, 1), (15, 1), (16, 0.5), (17, 0.2)}
- **4.** {(11, 0.3), (12, 0.5), (13, 0.6), (14, 1), (15, 0.7), (16, 0.5), (17, 0.2)}

> [!TIP]
> **Correct answer: 4. {(11, 0.3), (12, 0.5), (13, 0.6), (14, 1), (15, 0.7), (16, 0.5), (17, 0.2)}**

## Solution

For each sum z, take the maximum over all pairs x+y=z of the smaller input membership. This gives: 11→0.3; 12→max(0.3,0.5)=0.5; 13→max(0.3,0.6,0.5)=0.6; 14→max(0.5,1,0.5)=1; 15→max(0.5,0.7,0.2)=0.7; 16→max(0.5,0.2)=0.5; 17→0.2. The resulting set is exactly option 4.

## Key Points

- Fuzzy addition by the extension principle uses max across decompositions and min within each contributing pair.

## Why the other options are incorrect

Options 1–3 assign excessive memberships to one or more sums, especially z=13 or z=15. For z=15, no generating pair has minimum membership above 0.7, so a value of 1 is impossible.
