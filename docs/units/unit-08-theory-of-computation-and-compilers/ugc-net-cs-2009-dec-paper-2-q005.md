# Question 5

*UGC NET CS · 2009 Dec Paper 2 · Unsolvable Problems and Computational Complexity · Complexity Measurement and Classification*

In a MIU puzzle, either of the letters M, I or U could go as a start symbol. Production rules are given below : R 1 : U → IU R 2 : M. x → M. x.x where . .. is string concatenation operator. Given this, which of the following holds for (i) MIUIUIUIUIU (ii) MIUIUIUIUIUIUIUIU

- **A.** Either (i) or (ii) but not both of these are valid words .
- **B.** Both (i) and (ii) are valid words and they take identical number of transformations for the production.
- **C.** Both (i) and (ii) are valid words but they involve differe nt number of transformations in the production.
- **D.** None of these

> [!TIP]
> **Correct answer: A. Either (i) or (ii) but not both of these are valid words .**

## Solution

Starting from MU, rule R2 doubles the suffix after M, so the number of U symbols can become 1,2,4,8,… . Applying U→IU to every U then produces M followed by that many IU blocks. String (i) contains five IU blocks and cannot arise by repeated doubling, while string (ii) contains eight IU blocks and can. Exactly one is valid.

## Key Points

- R2 doubles the post-M suffix; target repetition counts must follow powers of two.

## Why the other options are incorrect

Because five is not a power of two, the two strings cannot both be generated, so B and C fail. Since the eight-block string is generable, D also fails.
