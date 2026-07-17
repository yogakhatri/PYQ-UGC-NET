# Question 93

*UGC NET CS · 2019 Dec Paper 1 And 2 · Context-Free Grammars · Grammar Equivalence and Redundant Productions*

Consider the grammars G1: S→aSb | bSa | aa; G2: S→aSb | bSa | SS | epsilon; G3: S→aSb | bSa | SS | a; G4: S→aSb | bSa | SS | SSS | epsilon. Which pair is equivalent?

- **1.** G1 and G3 are equivalent
- **2.** G2 and G3 are equivalent
- **3.** G2 and G4 are equivalent
- **4.** G3 and G4 are equivalent

> [!TIP]
> **Correct answer: 3. G2 and G4 are equivalent**

## Solution

G2 and G4 have the same base and wrapping/concatenation rules: aSb, bSa, SS, and epsilon. G4 additionally has S→SSS, but that rule adds no power because G2 can derive three copies using S⇒SS⇒SSS by expanding either one of the two S symbols with S→SS. Conversely every G2 rule is already in G4. Thus L(G2)=L(G4), option 3.

## Key Points

- A production is redundant if every use of it can be simulated by other productions; S→SSS is simulated by applying S→SS twice.

## Why the other options are incorrect

G3 has base a rather than epsilon, so it does not generate epsilon and produces strings with surplus a's. G1 has base aa and no concatenation/epsilon rule, so it is not equivalent to G3. These base-language differences eliminate options 1, 2, and 4.
