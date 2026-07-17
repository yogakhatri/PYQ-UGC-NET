# Question 111

*UGC NET CS · 2019 Dec Paper 1 And 2 · Fuzzy Sets · Additive Fuzzy Rule Models*

Consider M1: the Mamdani model, M2: the Takagi–Sugeno–Kang (TSK) model, and M3: Kosko's standard additive model (SAM). Which are examples of additive rule models?

- **1.** Only M1 and M2
- **2.** Only M2 and M3
- **3.** Only M1 and M3
- **4.** M1, M2 and M3

> [!TIP]
> **Correct answer: 2. Only M2 and M3**

## Solution

An additive rule model combines the contributions of fired rules by summation or a normalized weighted sum. A TSK system computes a weighted average of its rules' crisp consequent functions, so M2 is additive. Kosko's SAM explicitly adds scaled consequent-set contributions and then normalizes/defuzzifies, so M3 is additive by definition. The conventional Mamdani model uses fuzzy implication followed by set aggregation—typically max aggregation—and is not placed in this additive-rule category. Therefore only M2 and M3 are correct, option 2.

## Key Points

- TSK and SAM form outputs from weighted/additive rule contributions; conventional Mamdani inference aggregates fuzzy output sets instead.

## Why the other options are incorrect

Options 1, 3, and 4 all include the conventional Mamdani model in the additive-rule class. Mamdani rules may certainly be aggregated, but that fact alone does not make the standard max–min Mamdani architecture an additive rule model in this classification.

## References

- [Kosko: Additive Fuzzy Systems—TSK systems as special additive fuzzy systems](https://sipi.usc.edu/~kosko/IJIS-galley-proof-5-Add-Fuzz-Sys-11December2017.pdf)
