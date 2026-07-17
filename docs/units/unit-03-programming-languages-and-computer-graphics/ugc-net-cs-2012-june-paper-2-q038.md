# Question 38

*UGC NET CS · 2012 June Paper 2 · Programming in C · printf Character Conversion*

What does printf("%c", 100); do?

- **1.** Prints 100
- **2.** Prints the ASCII character corresponding to 100
- **3.** Prints garbage
- **4.** None of the above

> [!TIP]
> **Correct answer: 2. Prints the ASCII character corresponding to 100**

## Solution

The %c conversion tells printf to interpret the integer argument as an unsigned-character code and output the corresponding character. In ASCII, decimal 100 is the lowercase letter d, so the statement prints d rather than the digits '100'.

## Key Points

- printf format controls interpretation: %d prints an integer's digits; %c prints the character with that code.

## Why the other options are incorrect

Printing 100 numerically would require %d. The integer argument is valid for %c after the normal variadic promotion, so the result is not garbage or 'none'.
