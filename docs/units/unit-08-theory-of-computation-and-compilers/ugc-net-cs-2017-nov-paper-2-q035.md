# Question 35

*UGC NET CS · 2017 Nov Paper 2 · Compiler Phases · Scanner, Parser, Semantic Analysis and Optimizer*

Match the description of several parts of a classic optimizing compiler in List - I, with the names of those parts in List - II : List - I List - II (a) A part of a compiler that is responsible for recognizing (i) Optimizer syntax. (b) A part of a compiler that takes as input a stream of (ii) Semantic Analysis characters and produces as output a stream of words along with their associated syntactic categories. (c) A part of a compiler that understand the meanings of (iii) Parser variable names and other symbols and checks that they are used in ways consistent with their definitions. (d) An IR-to-IR transformer that tries to improve the IR (iv) Scanner program in some way (Intermediate Representation). Code : (a) (b) (c) (d)

- **1.** (iii) (iv) (ii) (i)
- **2.** (iv) (iii) (ii) (i)
- **3.** (ii) (iv) (i) (iii)
- **4.** (ii) (iv) (iii) (i)

> [!TIP]
> **Correct answer: 1. (iii) (iv) (ii) (i)**

## Solution

Recognizing grammatical syntax is the parser's job, so a→iii. Turning a character stream into tokens/words and token categories is lexical scanning, so b→iv. Checking declarations, types, and consistent symbol use is semantic analysis, so c→ii. Transforming intermediate representation to improve the program is optimization, so d→i. The code (iii),(iv),(ii),(i) is option 1.

## Key Points

- Compiler pipeline: characters → scanner/tokens → parser/syntax → semantic checks → IR optimization → code generation.

## Why the other options are incorrect

The other options interchange phases with clearly different input/output levels. A scanner does not build full syntactic structure; a parser does not normally perform all type/name checks; and only the optimizer is described as IR-to-IR improvement.
