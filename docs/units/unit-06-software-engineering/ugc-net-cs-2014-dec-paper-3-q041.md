# Question 41

*UGC NET CS · 2014 Dec Paper 3 · Software Design · UML Stereotypes and Profiles*

What is true about UML stereotypes ?

- **A.** Stereotype is used for extending the UML language.
- **B.** Stereotyped class must be abstract
- **C.** The stereotype indicates that the UML element cannot be changed
- **D.** UML profiles can be stereotyped for backward compatibility

> [!TIP]
> **Correct answer: A. Stereotype is used for extending the UML language.**

## Solution

A stereotype is a UML extension mechanism. It gives an existing UML metaclass a domain-specific meaning and may add tagged values or constraints, commonly inside a UML profile. It extends how a UML element is interpreted without changing the UML metamodel arbitrarily. Therefore A is true.

## Key Points

- Stereotypes extend UML vocabulary for a domain while reusing existing UML element types.

## Why the other options are incorrect

A stereotyped class need not be abstract, so B is false. A stereotype does not make an element immutable, so C is false. Profiles package stereotypes for a particular domain or platform; D's backward-compatibility claim is not their defining purpose.
