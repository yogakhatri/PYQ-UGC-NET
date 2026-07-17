# Question 37

*UGC NET CS · 2013 Dec Paper 2 · Functions · Function Composition*

Let f and g be the functions from the set of integers to the set integers defined by f( x) = 2x + 3 and g(x) = 3x + 2 Then the composition of f and g and g and f is given as

- **A.** 6 x + 7, 6x + 11
- **B.** 6 x + 11, 6x + 7
- **C.** 5 x + 5, 5x + 5
- **D.** None of the above

> [!TIP]
> **Correct answer: A. 6 x + 7, 6x + 11**

## Solution

Composition order matters. (f∘g)(x)=f(3x+2)=2(3x+2)+3=6x+7. Conversely, (g∘f)(x)=g(2x+3)=3(2x+3)+2=6x+11. Thus the requested pair is 6x+7, 6x+11.

## Key Points

- Read f∘g as f after g: substitute the complete formula for g(x) into f.

## Why the other options are incorrect

B reverses the two compositions. C incorrectly adds the functions instead of substituting one into the other. Since A matches both substitutions, 'none' is false.
