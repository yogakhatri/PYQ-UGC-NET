# Question 94

*UGC NET CS · 2019 Dec Paper 1 And 2 · Context-Free Grammars · Constructing a Grammar for a Count Relation*

For L={a^n b^(n-3) | n>2} over {a,b}, which grammar generates exactly L?

- **1.** S→aA | a; A→aAb | b
- **2.** S→aaA | epsilon; A→aAb | epsilon
- **3.** S→aaaA | a; A→aAb | epsilon
- **4.** S→aaaA; A→aAb | epsilon

> [!TIP]
> **Correct answer: 4. S→aaaA; A→aAb | epsilon**

## Solution

Let k=n−3, so k≥0 and the language becomes {a^(k+3)b^k}. In option 4, S→aaaA supplies the three unmatched initial a's. Each use of A→aAb adds one a before A and one matching b after it; finally A→epsilon stops. After k recursive uses the result is a^(k+3)b^k, exactly L. Therefore option 4.

## Key Points

- For a fixed count difference, generate the unmatched prefix first, then use a recursive rule that adds one symbol to both counted blocks.

## Why the other options are incorrect

Option 3 includes an extra alternative S→a, which is not in L because n must exceed 2. Option 2 can generate epsilon and has only two fixed initial a's. Option 1 balances its generated a's and b's differently and also generates the standalone a.
