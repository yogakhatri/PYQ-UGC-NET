# Question 12

*UGC NET CS · 2010 June Paper 2 · 3-D Object Representation, Geometric Transformations and Viewing · Bezier and B-Spline Curves and Surfaces*

What will be the output of the following c-code ? void main ( ) { char *P = "ayqm" ; char c; c = ++ *p ; printf ("%c", c); }

- **A.** a
- **B.** c
- **C.** b
- **D.** q

> [!TIP]
> **Correct answer: C. b**

## Solution

Under the question's intended older-C execution model, p points at the first character 'a'; ++*p increments that character code to 'b', assigns it to c, and printf prints b. However, modifying a string literal is undefined behavior in C and may fault on a real conforming implementation; robust code should use char p[] = "ayqm".

## Key Points

- ++*p means increment the character pointed to by p, but string literals must not be modified.

## Why the other options are incorrect

The prefix increment changes the first character before assignment, so neither a nor q is intended. There is no arithmetic route to c.
