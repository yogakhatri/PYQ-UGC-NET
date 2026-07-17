# Question 25

*UGC NET CS · 2012 June Paper 2 · Software Metrics · Function Points and Language Independence*

Which software-size metric does not depend on the programming language used?

- **A.** Lines of code
- **B.** Function count/function points
- **C.** Number of tokens
- **D.** All of the above

> [!TIP]
> **Correct answer: B. Function count/function points**

## Solution

Function-oriented size measures count externally visible inputs, outputs, inquiries, logical files and interfaces, then adjust by prescribed weights. They describe delivered functionality before a language is chosen. The same requirements can therefore be estimated across different implementation languages.

## Key Points

- Function points measure user-visible functionality; LOC and token counts measure language-specific implementation.

## Why the other options are incorrect

Lines of code vary greatly by language expressiveness and style. Token counts depend directly on a language's lexical and syntactic forms. Since A and C are language-dependent, 'all of the above' is false.
