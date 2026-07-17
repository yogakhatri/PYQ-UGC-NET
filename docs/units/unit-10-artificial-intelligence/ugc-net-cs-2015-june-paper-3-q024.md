# Question 24

*UGC NET CS · 2015 June Paper 3 · Knowledge Representation and Logic · Horn Clauses and Resolution*

Which one of the following is true ?

- **1.** The resolvent of two Horn clauses is not a Horn clause
- **2.** The resolvent of two Horn clauses is a Horn clause
- **3.** If we resolve a negated goal G against a fact or rule A to get clause C then C has positive literal or non-null goal
- **4.** If we resolve a negated goal G against a fact or rule A to get clause C then C has positive literal or null goal

> [!TIP]
> **Correct answer: 2. The resolvent of two Horn clauses is a Horn clause**

## Solution

A Horn clause contains at most one positive literal. Resolution deletes one complementary literal from each parent and combines the remainder. When both parents are Horn, this operation cannot leave two positive literals, so any non-tautological resolvent is also Horn. Hence option 2 is true.

## Key Points

- Horn clauses are closed under binary resolution, which is why resolution works naturally for logic programming.

## Why the other options are incorrect

Option 1 states the opposite of closure under resolution. Resolving a negated goal with a fact or rule produces another goal clause, possibly the empty goal on success; it does not generally create the positive-literal alternatives asserted in options 3 and 4.
