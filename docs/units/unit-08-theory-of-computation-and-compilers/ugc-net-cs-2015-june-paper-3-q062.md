# Question 62

*UGC NET CS · 2015 June Paper 3 · Turing Machines and Language Classes · Closure and Countability of Recursively Enumerable Languages*

Consider two statements. S1: If L1 and L2 are recursively enumerable languages over Σ, then L1 ∪ L2 and L1 ∩ L2 are recursively enumerable. S2: The set of recursively enumerable languages is countable. Which is correct?

- **1.** S1 is correct and S2 is not correct
- **2.** S1 is not correct and S2 is correct
- **3.** Both S1 and S2 are not correct
- **4.** Both S1 and S2 are correct

> [!TIP]
> **Correct answer: 4. Both S1 and S2 are correct**

## Solution

Recursively enumerable languages are closed under union: dovetail recognizers for L1 and L2 and accept when either accepts. They are also closed under intersection: dovetail both and accept after both accept. Hence S1 is true. Turing machines have finite descriptions over a finite alphabet, so there are only countably many machines and therefore at most countably many languages they recognize. Thus S2 is also true.

## Key Points

- Finite machine descriptions make RE languages countable; dovetailing proves union and intersection closure.

## Why the other options are incorrect

Options 1–3 reject at least one true statement. Note the contrast: the collection of all languages over a nonempty alphabet is uncountable, but only countably many have Turing-machine recognizers.
