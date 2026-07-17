# Question 33

*UGC NET CS · 2010 June Paper 2 · Semantic Analysis · Evaluation Order*

Consider left-associative operators in decreasing precedence: − (subtraction), * (multiplication), and $ (exponentiation). Evaluate 3−2*4 $ 1*2 $ 3.

- **A.** – 61
- **B.** 64
- **C.** 512
- **D.** 4096

> [!TIP]
> **Correct answer: D. 4096**

## Solution

Apply the unusual stated precedence, not ordinary arithmetic. Highest: 3−2=1. Next, multiplication forms 1*4=4 and 1*2=2. Lowest, the two left-associative exponentiations give (4 $ 2) $ 3=(4²)³=16³=4096.

## Key Points

- First group by declared precedence, then use left associativity within each level.

## Why the other options are incorrect

64 and 512 come from different exponent associativity/grouping; −61 results from applying familiar precedence rather than the explicitly supplied order. The scan renders the second $ poorly, but 4096 and the declared operator set determine the intended expression.
