# Question 90

*UGC NET CS · 2020 Nov With Answers · Mathematical Logic · Rules of Inference and Invalid Disjunction Simplification*

Consider the argument with premise ∀x(P(x) ∨ Q(x)) and conclusion (∀xP(x)) ∧ (∀xQ(x)). The proposed proof uses: (A) ∀x(P(x) ∨ Q(x)), premise; (B) P(c) ∨ Q(c), universal instantiation; (C) P(c), simplification; (D) ∀xP(x), universal generalization; (E) Q(c), simplification; (F) ∀xQ(x), universal generalization; (G) (∀xP(x)) ∧ (∀xQ(x)), conjunction. Which assessment is correct?

- **1.** This is a valid argument.
- **2.** Steps (C) and (E) are not correct inferences
- **3.** Steps (D) and (F) are not correct inferences
- **4.** Step (G) is not a correct inference

> [!TIP]
> **Correct answer: 2. Steps (C) and (E) are not correct inferences**

## Solution

Step B is valid: universal instantiation gives P(c)∨Q(c). The error occurs next. Simplification permits deriving either conjunct from P(c)∧Q(c), but it cannot derive either disjunct from P(c)∨Q(c). The disjunction may be true because only P(c) is true or only Q(c) is true. Therefore both C and E are invalid inferences, making option 2 correct.

## Key Points

- From P∨Q one may not infer P or infer Q separately; simplification applies only to a conjunction.

## Why the other options are incorrect

The argument is invalid: a one-element model with P true and Q false satisfies ∀x(P∨Q) but not ∀xQ. Universal generalization and the final conjunction are not the first faulty rules; their premises were obtained illegitimately at C and E.
