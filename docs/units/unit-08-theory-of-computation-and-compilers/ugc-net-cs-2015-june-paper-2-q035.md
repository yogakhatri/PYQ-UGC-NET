# Question 35

*UGC NET CS · 2015 June Paper 2 · Compiler Design · Lexical Analysis and Tokens*

Which phase of compiler generates stream of atoms ?

- **1.** Syntax Analysis
- **2.** Lexical Analysis
- **3.** Code Generation
- **4.** Code Optimization

> [!TIP]
> **Correct answer: 2. Lexical Analysis**

## Solution

Lexical analysis reads the source character stream, groups characters into lexemes, and emits a stream of lexical atoms or tokens such as identifiers, keywords, literals, and operators. That token stream becomes the input to syntax analysis. Hence lexical analysis is the phase requested.

## Key Points

- Characters → lexemes/tokens in the lexer; tokens → syntax tree in the parser.

## Why the other options are incorrect

Syntax analysis consumes tokens to build a parse structure; it does not create the token stream. Code generation translates an intermediate representation to target code, while optimization improves an intermediate or target representation. Neither operates at the character-to-token stage.
