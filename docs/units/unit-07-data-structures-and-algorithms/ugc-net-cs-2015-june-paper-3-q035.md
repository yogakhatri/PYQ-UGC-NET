# Question 35

*UGC NET CS · 2015 June Paper 3 · Algorithm Analysis · Theta of Sums of Nonnegative Functions*

Let f (n) and g (n) be asymptotically non-negative functions. Which of the following is correct ?

- **1.** Θ(f(n)g(n)) = Θ(min(f(n),g(n)))
- **2.** Θ(f(n)g(n)) = Θ(max(f(n),g(n)))
- **3.** Θ(f(n)+g(n)) = Θ(min(f(n),g(n)))
- **4.** Θ(f(n)+g(n)) = Θ(max(f(n),g(n)))

> [!TIP]
> **Correct answer: 4. Θ(f(n)+g(n)) = Θ(max(f(n),g(n)))**

## Solution

For nonnegative f and g, `max(f,g) ≤ f+g ≤ 2 max(f,g)`. These constant-factor bounds hold pointwise for sufficiently large n, so `f(n)+g(n) = Θ(max(f(n),g(n)))`. This is option 4.

## Key Points

- For asymptotically nonnegative functions, a finite sum has the order of its largest term.

## Why the other options are incorrect

A sum is not generally controlled by the smaller term: if f=n and g=1, the sum is Θ(n), not Θ(1), eliminating option 3. A product is not generally Θ of either the minimum or maximum alone—for example, f=g=n gives product n²—eliminating options 1 and 2.
