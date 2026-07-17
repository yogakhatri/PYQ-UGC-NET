# Question 32

*UGC NET CS · 2015 June Paper 2 · System Software · Macro Processors and Expansion*

The translator which performs macro calls expansion is called :

- **1.** Macro processor
- **2.** Micro pre - processor
- **3.** Macro pre - processor
- **4.** Dynamic Linker

> [!TIP]
> **Correct answer: 1. Macro processor**

## Solution

A macro processor recognizes a macro call, binds its actual arguments to formal parameters, and substitutes the stored macro body to produce the expanded source text. That translator is therefore called a macro processor. It may run as a preprocessing stage, but `macro processor` is the standard general name asked for.

## Key Points

- Macro definition + call + argument substitution are handled by the macro processor.

## Why the other options are incorrect

`Micro pre-processor` is not the relevant standard term. `Macro pre-processor` describes one possible placement of a macro facility but is less general than the named translator in option 1. A dynamic linker resolves and loads object-code dependencies at run time; it does not expand source macros.
