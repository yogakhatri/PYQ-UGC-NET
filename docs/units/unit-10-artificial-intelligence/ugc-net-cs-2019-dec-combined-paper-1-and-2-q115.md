# Question 115

*UGC NET CS · 2019 Dec Paper 1 And 2 · Genetic Algorithms · Fitness-Proportionate Selection*

A genetic-algorithm population is P={01101,11000,01000,10011}. For decimal chromosome value x, let f(x)=x² and normalized fitness strength be Sf(x)=f(x)/Σf(x), reported as a percentage. What is the fitness strength of chromosome 11000?

- **1.** 24
- **2.** 576
- **3.** 14.4
- **4.** 49.2

> [!TIP]
> **Correct answer: 4. 49.2**

## Solution

Convert the chromosomes to decimal: 01101=13, 11000=24, 01000=8, and 10011=19. Their squared fitnesses are 169, 576, 64, and 361, whose sum is 1170. Thus the normalized strength of 11000 is 576/1170≈0.4923, or 49.2%. Therefore option 4 is correct.

## Key Points

- For roulette-wheel fitness strength, evaluate every chromosome, sum all fitness values, then divide the selected fitness by that total.

## Why the other options are incorrect

Twenty-four is only the chromosome's decimal value, and 576 is its unnormalized f(x)=x² value. Fourteen point four does not result from dividing 576 by the total population fitness. Fitness-proportionate strength must use the whole population in the denominator.
