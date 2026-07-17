# Question 14

*UGC NET CS · 2015 June Paper 2 · Programming in C++ · Overloads, Templates and Macros*

Which of the following is incorrect in C++ ?

- **1.** When we write overloaded function we must code the function for each usage.
- **2.** When we write function template we code the function only once.
- **3.** It is difficult to debug macros
- **4.** Templates are more efficient than macros

> [!TIP]
> **Correct answer: No unique incorrect statement is supplied. Statements 1–3 are standard textbook claims; statement 4 depends on what 'efficient' means and is not an objective language rule.**

## Solution

Separate overloads normally require separate function definitions, while a function template expresses the generic source once and the compiler instantiates needed specializations. Preprocessor macros are harder to type-check and debug because they operate by token substitution. Templates are generally safer and more maintainable than function-like macros, and often compile to equally efficient machine code, but they are not unconditionally more efficient in compile time, code size, or runtime. Thus the word 'efficient' makes statement 4 ambiguous rather than cleanly false or true.

## Key Points

- Templates are typed language constructs; macros are token substitution.
- Compare safety, reuse, code size, compile time, and runtime separately instead of saying only 'efficient.'

## Why the other options are incorrect

Calling 1, 2, or 3 incorrect contradicts their standard pedagogical meanings. Calling 4 categorically incorrect assumes efficiency means runtime only; calling every statement correct assumes a broader engineering meaning. The source provides no metric and no 'none' option, so forcing one choice compromises precision.
