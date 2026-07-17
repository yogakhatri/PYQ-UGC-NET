# Question 112

*UGC NET CS · 2020 Nov With Answers · Knowledge Representation and Logic · Entailment, Soundness and Horn Inference*

Which statements are true? (A) A sentence α entails β if β is true in only a few worlds where α is true. (B) Forward and backward chaining are natural reasoning algorithms for Horn-form knowledge bases. (C) Sound inference algorithms derive all sentences that are entailed. (D) Propositional logic does not scale to environments of unbounded size.

- **1.** (A) and (B) only
- **2.** (B) and (C) only
- **3.** (C) and (D) only
- **4.** (B) and (D) only

> [!TIP]
> **Correct answer: 4. (B) and (D) only**

## Solution

Entailment α⊨β requires β to be true in every model in which α is true, not merely a few, so A is false. Horn clauses naturally support forward chaining from known facts and backward chaining from a goal, so B is true. Soundness means every derived conclusion is entailed; deriving every entailed conclusion is completeness, so C is false. A finite propositional vocabulary cannot naturally represent arbitrarily many objects in an unbounded environment, so D is true. Therefore B and D only, option 4.

## Key Points

- Entailment uses all models, Horn rules suit chaining, and soundness is ‘only entailed,’ not ‘all entailed.’

## Why the other options are incorrect

Options 1–3 include the incorrect entailment definition or confuse soundness with completeness. Remember: sound means no false positives; complete means no entailed conclusion is missed.
