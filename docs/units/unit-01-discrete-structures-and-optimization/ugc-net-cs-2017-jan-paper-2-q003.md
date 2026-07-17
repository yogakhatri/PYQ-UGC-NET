# Question 3

*UGC NET CS · 2017 Jan Paper 2 · Sets and Relations · Composition of functions*

Functions from R to R are defined by f(x)=x³−4x, g(x)=1/(x²+1), and h(x)=x⁴. Find (h∘g)(x) and (h∘g∘f)(x).

- **1.** (x²+1)⁴ and [(x³−4x)²+1]⁴
- **2.** (x²+1)⁴ and [(x³−4x)²+1]⁻⁴
- **3.** (x²+1)⁻⁴ and [(x²−4x)²+1]⁴
- **4.** (x²+1)⁻⁴ and [(x³−4x)²+1]⁻⁴

> [!TIP]
> **Correct answer: 4. (x²+1)⁻⁴ and [(x³−4x)²+1]⁻⁴**

## Solution

Composition is evaluated from right to left. Since g(x)=1/(x²+1), (h∘g)(x)=h(g(x))=[1/(x²+1)]⁴=(x²+1)⁻⁴. For the three-function composition, first f(x)=x³−4x; then g(f(x))=1/[(x³−4x)²+1]; finally raising this to the fourth power gives (h∘g∘f)(x)=[(x³−4x)²+1]⁻⁴. Both expressions match option 4.

## Key Points

- In h∘g∘f, apply f first, substitute that result into g, and only then apply h.

## Why the other options are incorrect

Options 1 and 2 give the wrong positive exponent for h∘g. Option 3 changes f(x) from x³−4x to x²−4x and also gives the wrong sign on the final exponent.
