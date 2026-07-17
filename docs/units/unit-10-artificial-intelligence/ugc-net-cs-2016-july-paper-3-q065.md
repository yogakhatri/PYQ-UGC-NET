# Question 65

*UGC NET CS · 2016 July Paper 3 · Fuzzy Sets · Fuzzy Addition by the Extension Principle*

Add the fuzzy integers A = {(0.3, 1), (0.6, 2), (1, 3), (0.7, 4), (0.2, 5)} and B = {(0.5, 11), (1, 12), (0.5, 13)}, where μ_(A+B)(z) = max over x+y=z of min(μ_A(x), μ_B(y)). Then A + B is

- **1.** {(0.5, 12), (0.6, 13), (1, 14), (0.7, 15), (0.7, 16), (1, 17), (1, 18)}
- **2.** {(0.5, 12), (0.6, 13), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18)}
- **3.** {(0.3, 12), (0.5, 13), (0.5, 14), (1, 15), (0.7, 16), (0.5, 17), (0.2, 18)}
- **4.** {(0.3, 12), (0.5, 13), (0.6, 14), (1, 15), (0.7, 16), (0.5, 17), (0.2, 18)}

> [!TIP]
> **Correct answer: 4. {(0.3, 12), (0.5, 13), (0.6, 14), (1, 15), (0.7, 16), (0.5, 17), (0.2, 18)}**

## Solution

Apply the extension principle separately to each possible sum z. For z=12 only 1+11 contributes, giving min(0.3,0.5)=0.3. For z=13 take max{min(0.3,1),min(0.6,0.5)}=0.5. Continuing in the same way gives memberships μ(14)=0.6, μ(15)=1, μ(16)=0.7, μ(17)=0.5, and μ(18)=0.2. Thus A+B={(0.3,12),(0.5,13),(0.6,14),(1,15),(0.7,16),(0.5,17),(0.2,18)}, exactly option 4.

## Key Points

- For fuzzy addition, enumerate all pairs with x+y=z, take min for each pair, then take the maximum of those minima.

## Why the other options are incorrect

Options 1 and 2 incorrectly retain membership 1 at several sums even when no pair producing that sum has both memberships equal to 1. Option 3 underestimates z=14: the pair 2+12 has minimum membership min(0.6,1)=0.6, which dominates the other pairs.

## Additional Information

The printed formula shows μ_B(x) in the minimum, but the constraint x+y=z makes μ_B(y) the mathematically intended term; the computation above uses that standard extension-principle definition.
