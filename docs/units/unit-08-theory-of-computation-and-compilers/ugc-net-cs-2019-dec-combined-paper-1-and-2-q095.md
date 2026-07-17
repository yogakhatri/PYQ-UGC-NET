# Question 95

*UGC NET CS · 2019 Dec Paper 1 And 2 · Context-Free Grammars · Productive Nonterminals and Generated Language*

Consider the grammar S→0A | 0BB; A→00A | epsilon; B→1B | 11C; C→B. Which language does it generate?

- **1.** L((00)*0 + (11)*1)
- **2.** L(0(11)* + 1(00)*)
- **3.** L((00)*0)
- **4.** L(0(11)*1)

> [!TIP]
> **Correct answer: 3. L((00)*0)**

## Solution

From S→0A and A→00A | epsilon, after k repetitions of A→00A the grammar produces 0(00)^k, i.e. every positive odd-length string of zeros. The alternative S→0BB produces no terminal string: B→1B or 11C and C→B always leaves at least one B/C nonterminal, so B is nonproductive. Therefore the generated language is L((00)*0), option 3.

## Key Points

- A derivation contributes to the language only if every nonterminal can eventually disappear; B and C form a nonterminating nonproductive cycle here.

## Why the other options are incorrect

Options 1, 2, and 4 include strings containing 1, but the only branch that could introduce 1 never terminates. Grammar analysis must discard nonproductive branches rather than treating their visible terminal prefixes as completed words.
