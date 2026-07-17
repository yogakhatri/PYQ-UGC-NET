# Question 89

*UGC NET CS · 2018 July Paper 2 · Sets and Relations · Equivalence Relations on Function Spaces*

Which is an equivalence relation on the set of all functions from Z to Z?

- **1.** {(f,g) | f(x)-g(x)=1 for all x in Z}
- **2.** {(f,g) | f(0)=g(0) or f(1)=g(1)}
- **3.** {(f,g) | f(0)=g(1) and f(1)=g(0)}
- **4.** {(f,g) | f(x)-g(x)=k for some k in Z}

> [!TIP]
> **Correct answer: 4. {(f,g) | f(x)-g(x)=k for some k in Z}**

## Solution

Option 4 relates f and g when their pointwise difference is one integer constant k independent of x. It is reflexive with k=0; symmetric because f−g=k implies g−f=−k; and transitive because f−g=k1 and g−h=k2 imply f−h=k1+k2. Therefore it is an equivalence relation.

## Key Points

- Functions are equivalent here when they differ only by an additive integer constant; constants negate under reversal and add under composition.

## Why the other options are incorrect

Option 1 is not reflexive because f−f=0, not 1. Option 2 can fail transitivity: one pair may agree only at 0 and the next only at 1. Option 3 is not reflexive for a function with f(0)≠f(1).
