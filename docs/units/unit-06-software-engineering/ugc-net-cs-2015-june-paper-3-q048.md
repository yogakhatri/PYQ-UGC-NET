# Question 48

*UGC NET CS · 2015 June Paper 3 · Software Design · Cohesion and Coupling*

A software design is highly modular if :

- **1.** cohesion is functional and coupling is data type.
- **2.** cohesion is coincidental and coupling is data type.
- **3.** cohesion is sequential and coupling is content type.
- **4.** cohesion is functional and coupling is stamp type.

> [!TIP]
> **Correct answer: 1. cohesion is functional and coupling is data type.**

## Solution

A highly modular design aims for high cohesion inside each module and low coupling between modules. Functional cohesion is the strongest classical cohesion: every element contributes to one well-defined task. Data coupling is the weakest and most desirable listed coupling: modules communicate through only the necessary simple data values. Option 1 combines these best cases.

## Key Points

- Best classical modularity = functional cohesion + data coupling.

## Why the other options are incorrect

Coincidental cohesion is weakest, content coupling is strongest and worst, and stamp coupling passes an entire record when only part may be needed. Option 4 has good cohesion but worse coupling than option 1; options 2 and 3 include seriously poor cohesion or coupling.
