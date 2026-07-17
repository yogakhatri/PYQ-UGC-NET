# Question 144

*UGC NET CS · 2019 June Paper 1 And 2 · Fuzzy Sets · Fuzzy Conjunction and Disjunction*

A fuzzy conjunction t(x,y) and fuzzy disjunction s(x,y) form a dual pair under standard negation when which condition holds?

- **1.** t(x,y)=1-s(x,y)
- **2.** t(x,y)=s(1-x,1-y)
- **3.** t(x,y)=1-s(1-x,1-y)
- **4.** t(x,y)=s(1+x,1+y)

> [!TIP]
> **Correct answer: 3. t(x,y)=1-s(1-x,1-y)**

## Solution

Dual fuzzy conjunction and disjunction operators obey De Morgan's law with the standard negation N(x)=1-x. Therefore t(x,y)=N(s(N(x),N(y)))=1-s(1-x,1-y). For example, min and max are dual because min(x,y)=1-max(1-x,1-y).

## Key Points

- Duality under standard fuzzy negation complements both inputs and the output.

## Why the other options are incorrect

Option 1 fails to complement the inputs. Option 2 complements the inputs but not the output. Option 4 moves values outside the usual [0,1] membership interval and is not a De Morgan duality condition.
