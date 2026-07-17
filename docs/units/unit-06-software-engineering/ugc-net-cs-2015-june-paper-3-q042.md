# Question 42

*UGC NET CS · 2015 June Paper 3 · Software Design · Encapsulation, Cohesion, and Coupling*

Module design is used to maximize cohesion and minimize coupling. Which of the following is the key to implement this rule ?

- **1.** Inheritance
- **2.** Polymorphism
- **3.** Encapsulation
- **4.** Abstraction

> [!TIP]
> **Correct answer: 3. Encapsulation**

## Solution

Encapsulation keeps a module's related state and operations together behind a controlled interface. Internal details can change without forcing clients to change, which lowers coupling, while the module's contents remain centered on one responsibility, which supports cohesion. It is therefore the key implementation mechanism among the choices.

## Key Points

- Encapsulation creates a cohesive module boundary and prevents clients from coupling to its internals.

## Why the other options are incorrect

Inheritance and polymorphism are reuse and substitutability mechanisms; either can even increase coupling if misused. Abstraction helps specify what a module does, but encapsulation is the concrete boundary that hides implementation details and controls dependencies.
