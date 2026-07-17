# Question 79

*UGC NET CS · 2018 July Paper 2 · Knowledge Representation and Reasoning · Existential Instantiation and Fresh Constants*

A knowledge base contains only ∃x AsHighAs(x,Everest). Consider existential instantiations: (a) AsHighAs(Everest,Everest), and (b) AsHighAs(Kilimanjaro,Everest). Which choice is correct?

- **1.** Both sentence (a) and sentence (b) are sound conclusions.
- **2.** Both sentence (a) and sentence (b) are unsound conclusions.
- **3.** Sentence (a) is sound but sentence (b) is unsound.
- **4.** Sentence (a) is unsound but sentence (b) is sound.

> [!TIP]
> **Correct answer: 4. Sentence (a) is unsound but sentence (b) is sound.**

## Solution

Existential instantiation must introduce a fresh constant naming the unspecified witness. `Everest` already occurs in the knowledge base, so substituting it asserts without justification that Everest itself is as high as Everest; sentence (a) is unsound. `Kilimanjaro` does not occur in the one-sentence knowledge base and is used here as the new witness symbol, so sentence (b) is a sound instantiation under the exercise's naming convention. Therefore option 4 is correct.

## Key Points

- From ∃x P(x), instantiate P(c) only with a fresh constant c that has not appeared earlier in the proof or knowledge base.

## Why the other options are incorrect

The existential sentence guarantees that some object has the property, not that any already named object does. The freshness condition prevents accidental identification of the unknown witness with an existing constant. Strictly, the fresh name is a proof symbol, not a prior real-world claim about Kilimanjaro.

## References

- [U.S. Naval Academy — First-order logic standard rules](https://www.usna.edu/Users/cs/wcbrown/courses/F23SI242/resources/fol/folrules.html)
