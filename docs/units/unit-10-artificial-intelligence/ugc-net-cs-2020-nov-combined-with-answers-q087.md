# Question 87

*UGC NET CS · 2020 Nov With Answers · Knowledge Representation and Logic · First-Order Logic Translation*

If f(x) means ‘x is my friend’ and p(x) means ‘x is perfect’, then the correct logical translation of the statement ‘Some of my friends are not perfect’ is

- **1.** ∀x (f(x) ∧ ¬p(x))
- **2.** ∃x (f(x) ∧ ¬p(x))
- **3.** ¬∃x (f(x) ∧ ¬p(x))
- **4.** ∃x (¬f(x) ∧ ¬p(x))

> [!TIP]
> **Correct answer: 2. ∃x (f(x) ∧ ¬p(x))**

## Solution

The word ‘some’ introduces an existential quantifier: there is at least one object x. That same object must satisfy both conditions: it is my friend, f(x), and it is not perfect, ¬p(x). Joining the conditions with conjunction gives ∃x(f(x)∧¬p(x)), option 2.

## Key Points

- Translate ‘some A are not B’ as ∃x(A(x)∧¬B(x)).

## Why the other options are incorrect

A universal quantifier would claim every object is a non-perfect friend. Negating the existential says no friend is imperfect, the opposite of the sentence. Using ¬f(x) describes someone who is not a friend and therefore fails the required meaning.
