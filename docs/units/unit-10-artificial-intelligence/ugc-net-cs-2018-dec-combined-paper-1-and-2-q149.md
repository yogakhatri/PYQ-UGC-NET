# Question 149

*UGC NET CS · 2018 Dec Paper 1 And 2 · Knowledge Representation · First-Order Logic Translation*

Consider the sentence: 'There is a country that borders both India and Nepal.' Which representation is correct?

- **1.** exists c: Country(c) AND Border(c, India) AND Border(c, Nepal)
- **2.** exists c: Country(c) => [Border(c, India) AND Border(c, Nepal)]
- **3.** [exists c: Country(c)] => [Border(c, India) AND Border(c, Nepal)]
- **4.** exists c: Border(Country(c), India AND Nepal)

> [!TIP]
> **Correct answer: 1. exists c: Country(c) AND Border(c, India) AND Border(c, Nepal)**

## Solution

“There is” introduces an existentially quantified object c. The same c must satisfy all three requirements: it is a country, it borders India, and it borders Nepal. The faithful formula is therefore ∃c[Country(c)∧Border(c,India)∧Border(c,Nepal)], which is option 1.

## Key Points

- Translate “there exists an object with properties P, Q and R” as ∃x(P(x)∧Q(x)∧R(x)).

## Why the other options are incorrect

In option 2, putting an implication inside an existential allows any non-country to make the implication true vacuously, so it does not assert the required country's existence. Option 3 leaves c free in the consequent and makes the existential only the antecedent of an implication. Option 4 uses malformed predicate arguments and treats India∧Nepal as though it were an object.
