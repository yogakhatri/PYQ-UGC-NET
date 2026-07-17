# Question 5

*UGC NET CS · 2014 Dec Paper 2 · Functions and Relations · Associativity of Function Composition*

Let f,g,h map R into R with f(x)=x⁴, g(x)=√(x²+1), and h(x)=x²+72. The values of h∘(g∘f) and (h∘g)∘f are

- **A.** x⁸−71 and x⁸−71
- **B.** x⁸−73 and x⁸−73
- **C.** x⁸+71 and x⁸+71
- **D.** x⁸+73 and x⁸+73

> [!TIP]
> **Correct answer: D. x⁸+73 and x⁸+73**

## Solution

First, f(x)=x⁴. Then g(f(x))=√((x⁴)²+1)=√(x⁸+1). Applying h squares this result and adds 72: h(g(f(x)))=x⁸+1+72=x⁸+73. Function composition is associative, so h∘(g∘f) and (h∘g)∘f give the same result, x⁸+73.

## Key Points

- Composition is associative; substitute from the innermost function outward and preserve the square root before h squares it.

## Why the other options are incorrect

The −71 and −73 choices use subtraction even though h adds 72. The +71 choice mishandles the +1 inside g. Correctly squaring the square root contributes +1, producing +73.
