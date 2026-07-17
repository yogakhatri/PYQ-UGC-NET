# Question 33

*UGC NET CS · 2017 Jan Paper 2 · Compiler Phases · Lexical versus Syntax Analysis*

Consider the following statements related to compiler construction : I. Lexical Analysis is specified by context-free grammars and implemented by pushdown automata. II. Syntax Analysis is specified by regular expressions and implemented by finite-state machine. Which of the above statement(s) is/are correct ?

- **1.** Only I
- **2.** Only II
- **3.** Both I and II
- **4.** Neither I nor II

> [!TIP]
> **Correct answer: 4. Neither I nor II**

## Solution

Lexical structure—identifiers, literals, keywords, and similar tokens—is normally described by regular expressions and recognized by finite automata. Syntactic phrase structure is described by a context-free grammar and recognized by a parser whose stack gives pushdown-automaton power. Statement I assigns the syntax mechanisms to lexical analysis, while statement II assigns the lexical mechanisms to syntax analysis. Both are false, so option 4 is correct.

## Key Points

- Scanner: regular language; parser: context-free language.

## Why the other options are incorrect

Options 1, 2, and 3 accept at least one reversed statement. The correct pairing is lexical→regular expressions/finite automata and syntax→context-free grammars/pushdown-style parsing.
