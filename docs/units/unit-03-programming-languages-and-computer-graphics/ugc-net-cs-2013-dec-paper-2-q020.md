# Question 20

*UGC NET CS · 2013 Dec Paper 2 · Programming in C · Type Casting and Rounding*

The correct way to round off a floating number x to an integer value is

- **A.** y = (int) ( x + 0.5)
- **B.** y = int ( x + 0.5)
- **C.** y = (int) x + 0.5
- **D.** y = (int) ((int) x + 0.5)

> [!TIP]
> **Correct answer: A. y = (int) ( x + 0.5)**

## Solution

For a nonnegative floating-point value x, adding 0.5 moves values with fractional part at least 0.5 into the next integer interval. Casting the entire sum to int then truncates the fractional part, producing the usual round-to-nearest result: y=(int)(x+0.5).

## Key Points

- Classic positive-number rounding uses cast after addition: (int)(x+0.5).
- The placement of parentheses is essential.

## Why the other options are incorrect

Option B uses function-call syntax for int rather than the C-style cast expected by the question. C casts only x before adding 0.5, so assigning to an integer then truncates and fails to round up. D casts x too early and has the same problem. For negative values, the simple +0.5 formula is not symmetric; use a standard rounding function in real code.
