# Question 82

*UGC NET CS · 2019 June Paper 1 And 2 · Data Modeling · Relational-model features*

Which of the following features is supported in the relational database model?

- **1.** Complex data-types
- **2.** Multivalued attributes
- **3.** Associations with multiplicities
- **4.** Generalization relationships

> [!TIP]
> **Correct answer: 3. Associations with multiplicities**

## Solution

The relational model represents associations by matching key values and can enforce multiplicities through primary-key, unique and foreign-key constraints. Classical relations require atomic attribute values, so complex types and multivalued attributes are not native first-normal-form features. Generalization is an enhanced ER or object-oriented modelling construct rather than a basic relational construct.

## Key Points

- The relational model represents relationship cardinalities using keys and foreign-key constraints.

## Why the other options are incorrect

- **Option 1:** complex structured types belong to extended/object-relational systems.
- **Option 2:** a multivalued attribute must normally be represented in a separate relation.
- **Option 4:** generalization is converted into relations during mapping but is not itself a relational-model construct.
