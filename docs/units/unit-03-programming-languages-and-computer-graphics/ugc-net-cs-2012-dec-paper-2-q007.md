# Question 7

*UGC NET CS · 2012 Dec Paper 2 · Language Design and Translation Issues · Context-Free Syntax of C*

The C language is:

- **A.** Context-free language
- **B.** Context-sensitive language
- **C.** Regular language
- **D.** None of the above

> [!TIP]
> **Correct answer: A. Context-free language**

## Solution

In compiler theory, the lexical tokens of C are recognized by regular techniques, while the grammatical structure of declarations, expressions, statements and functions is described with a context-free grammar and parsed with context-free parsing methods. Under the standard exam convention, this makes C a context-free language at the syntax level.

## Key Points

- Separate syntax from semantics: C syntax is modeled by a context-free grammar; name, type and declaration checks are handled during semantic analysis.

## Why the other options are incorrect

Regular languages are not expressive enough for arbitrary recursive nesting such as balanced parentheses and blocks. 'Context-sensitive' is not the intended syntactic classification, although a complete C implementation must enforce context-dependent semantic constraints such as declarations and types. Therefore 'none' is unnecessary.
