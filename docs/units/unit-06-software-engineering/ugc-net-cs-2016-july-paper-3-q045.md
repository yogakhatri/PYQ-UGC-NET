# Question 45

*UGC NET CS · 2016 July Paper 3 · Software Design · Cohesion and Coupling*

Match each application/software design concept in List – I to its definition in List – II. List – I List – II I. Coupling (a) Easy to visually inspect the design of the software and understand its purpose. II. Cohesion (b) Easy to add functionality to a software without having to redesign it. III. Scalable (c) Focus of a code upon a single goal. IV. Readable (d) Reliance of a code module upon other code modules. Codes : I II III IV

- **1.** (b) (a) (d) (c)
- **2.** (c) (d) (a) (b)
- **3.** (d) (c) (b) (a)
- **4.** (d) (a) (c) (b)

> [!TIP]
> **Correct answer: 3. (d) (c) (b) (a)**

## Solution

Coupling measures a module's reliance on other modules, so I→(d). Cohesion measures how strongly a module focuses on one goal, so II→(c). Scalable design can accept added functionality or workload without fundamental redesign, so III→(b). Readable design is easy to inspect and understand, so IV→(a). The mapping is option 3.

## Key Points

- Aim for low coupling, high cohesion, scalable structure, and readable design.

## Why the other options are incorrect

The other codes swap internal focus (cohesion), intermodule dependence (coupling), extensibility (scalability), and understandability (readability). These are distinct design qualities.
