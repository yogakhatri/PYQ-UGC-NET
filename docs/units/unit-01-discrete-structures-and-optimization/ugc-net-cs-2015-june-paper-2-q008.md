# Question 8

*UGC NET CS · 2015 June Paper 2 · Mathematical Logic · Translating Natural-Language Arguments*

If my computations are correct and I pay the electric bill, then I will run out of money. If I dont pay the electric bill, the power will be turned off. Therefore, if I dont run out of money and the power is still on, then my computations are incorrect. Convert this argument into logical notations using the variables c, b, r, p for propositions of computations, electric bills, out of money and the power respectively. (Where Ø means NOT)

- **1.** If (c∧b)→r and ¬b→¬p, then (¬r∧p)→¬c
- **2.** If (c∨b)→r and ¬b→¬p, then (r∧p)→c
- **3.** If (c∧b)→r and ¬p→¬b, then (¬r∨p)→¬c
- **4.** If (c∨b)→r and ¬b→¬p, then (¬r∧p)→¬c

> [!TIP]
> **Correct answer: 1. If (c∧b)→r and ¬b→¬p, then (¬r∧p)→¬c**

## Solution

Translate each sentence directly. 'Computations correct and bill paid implies run out' is (c∧b)→r. 'Bill not paid implies power off' is ¬b→¬p. The conclusion 'not run out and power still on implies computations incorrect' is (¬r∧p)→¬c. Option 1 contains exactly these two premises and conclusion.

## Key Points

- Translate phrase by phrase: 'and'→∧, 'if…then'→→, and 'not'→¬; never reverse an implication silently.

## Why the other options are incorrect

Options 2 and 4 replace the premise's conjunction c∧b with a disjunction. Option 2 also changes the conclusion. Option 3 reverses the second implication and replaces the concluding conjunction with a disjunction. Only 1 preserves every connective and direction.
