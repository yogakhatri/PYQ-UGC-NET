# Question 32

*UGC NET CS · 2014 Dec Paper 2 · LR Parsing · Canonical LR(1) and LR(k)*

Which statement is true? A. A canonical LR parser is an LR(1) parser with a single look-ahead terminal. B. Every LR(k) parser with k>1 can be transformed into an LR(1) parser.

- **A.** A only
- **B.** B only
- **C.** Both A and B
- **D.** Neither A nor B

> [!TIP]
> **Correct answer: C. Both A and B**

## Solution

Canonical LR parsing conventionally means canonical LR(1): its items carry one terminal of lookahead, so statement A is true. LR(k) for finite k≥1 does not define a larger class of deterministic context-free languages than LR(1); an LR(k) grammar/language can be transformed to an equivalent LR(1) form, although the transformed grammar and parse table need not be identical. Thus statement B is true in the intended theoretical sense, and both hold.

## Key Points

- Canonical LR uses one lookahead; extra finite lookahead beyond one does not enlarge the LR language class.

## Why the other options are incorrect

A only and B only each discard one true statement. 'Neither' contradicts both the definition of canonical LR and the equivalence theorem for finite lookahead.
