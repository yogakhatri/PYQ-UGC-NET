# Question 55

*UGC NET CS · 2019 Dec Paper 1 And 2 · Sets and Relations · Equivalence Relations*

Let P be the set of all people. Let R be a binary relation on P such that (a. b) is in R if a is a brother of b. Is R symmetric transitive, an equivalence relation, a partial order relation?

- **1.** NO, NO, NO, NO
- **2.** NO, NO, YES, NO
- **3.** NO, YES, NO, NO
- **4.** NO, YES, YES, NO

> [!TIP]
> **Correct answer: 3. NO, YES, NO, NO**

## Solution

Using the usual exam model of ‘brother’ as a male sibling: the relation is not symmetric, because if a is the brother of b, b might be a sister and hence not a brother of a. It is transitive in the intended sibling model: if a is a brother of b and b is a brother of c, then a is a male sibling of c. It is not reflexive, so it cannot be an equivalence relation; it is also neither reflexive nor antisymmetric, so it is not a partial order. The pattern is NO, YES, NO, NO—option 3.

## Key Points

- Test each relation property separately; failing reflexivity alone rules out both equivalence and partial order.

## Why the other options are incorrect

Options 1 and 2 incorrectly deny the intended transitivity. Options 2 and 4 call the relation an equivalence relation even though no person is their own brother and symmetry can fail. Every option correctly rejects partial order, but only option 3 combines all four properties consistently.
