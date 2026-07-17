# Question 1

*UGC NET CS · 2018 July Paper 2 · Web Programming · Well-Formed versus Valid XML*

The definitions in an XML document are said to be __________ when the tagging system and definitions in the DTD are all in compliance.

- **1.** well-formed
- **2.** reasonable
- **3.** valid
- **4.** logical

> [!TIP]
> **Correct answer: 3. valid**

## Solution

A well-formed XML document obeys the basic XML syntax rules, such as proper nesting and one root element. A valid XML document is well-formed and also conforms to the declarations/grammar supplied by its DTD (or another schema language). Because the question explicitly requires compliance with the DTD, the correct term is `valid`, option 3.

## Key Points

- Well-formed = syntactically legal XML; valid = well-formed plus conformity to the declared DTD/schema.

## Why the other options are incorrect

Well-formedness alone does not require a DTD and does not prove conformance to one. `Reasonable` and `logical` are ordinary adjectives, not the formal XML classification requested.
