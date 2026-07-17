# Question 91

*UGC NET CS · 2020 Nov With Answers · Compiler Design · Compiler Uses of Symbol Tables*

Which are applications of a symbol table? A. Storage allocation. B. Checking type compatibility. C. Suppressing duplicate error messages.

- **1.** A and B only
- **2.** A and C only
- **3.** B and C only
- **4.** A, B and C

> [!TIP]
> **Correct answer: 4. A, B and C**

## Solution

A symbol table stores attributes associated with names, such as declared type, scope, memory location or offset, and diagnostic state. These entries support storage allocation (A), permit semantic analysis to check type compatibility (B), and allow the compiler to remember that an error for a name has already been reported so repeated diagnostics can be suppressed (C). All three are applications, option 4.

## Key Points

- Think of a symbol-table entry as the compiler’s central record for a name’s semantic, storage, and diagnostic attributes.

## Why the other options are incorrect

Each of options 1–3 omits one valid use. A symbol table is shared infrastructure used by semantic analysis, code generation/storage layout, and error reporting—not merely a dictionary of identifier spellings.
