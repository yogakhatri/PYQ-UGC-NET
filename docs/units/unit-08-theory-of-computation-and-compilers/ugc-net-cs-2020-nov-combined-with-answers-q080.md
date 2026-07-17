# Question 80

*UGC NET CS · 2020 Nov With Answers · Intermediate Code Generation · Intermediate Forms and Representations*

Which of the following is not an intermediate code form?

- **1.** Syntax trees
- **2.** Three-address code
- **3.** Quadruples
- **4.** Postfix notation

> [!TIP]
> **Correct answer: 3. Quadruples**

## Solution

Standard broad forms of intermediate representation include syntax trees, postfix notation, and three-address code. A quadruple is not a separate code form in that classification; it is one concrete record layout for storing three-address instructions, with fields such as (operator, argument1, argument2, result). Therefore the item that is not itself an intermediate-code form is quadruples, option 3.

## Key Points

- Distinguish an IR form from its storage layout: quadruples encode three-address code rather than defining a fourth form.

## Why the other options are incorrect

Syntax trees represent hierarchical expression structure, postfix notation gives a linear stack-oriented form, and three-address code gives an explicit low-level statement sequence. Quadruples, triples, and indirect triples are implementation representations of the third form.
