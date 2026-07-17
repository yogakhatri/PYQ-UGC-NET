# Question 31

*UGC NET CS · 2009 Dec Paper 2 · System Software · Linking and Relocation*

In an absolute loading scheme which loader function is accomplishe d by assembler ?

- **A.** re-allocation
- **B.** allocation
- **C.** linking
- **D.** loading

> [!TIP]
> **Correct answer: A. re-allocation**

## Solution

An absolute loader places object code at the addresses already prescribed in the object program. Address adjustment/relocation decisions must therefore be resolved before loading; in the standard scheme the assembler produces the absolute addresses. Option A's 're-allocation' is evidently the paper's wording for relocation.

## Key Points

- An absolute loader does no run-time relocation; it obeys addresses prepared earlier.

## Why the other options are incorrect

The loader itself performs the physical loading. In the classic absolute scheme, allocation and intermodule linking are typically assigned by the programmer, whereas the assembler translates/relocates address-dependent references into absolute form.
