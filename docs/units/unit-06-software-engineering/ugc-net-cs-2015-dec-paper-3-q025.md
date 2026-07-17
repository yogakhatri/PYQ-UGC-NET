# Question 25

*UGC NET CS · 2015 Dec Paper 3 · Software Quality · Architecture-Sensitive Quality Attributes*

Which one of the following non-functional quality attributes is not highly affected by the architecture of the software ?

- **1.** Performance
- **2.** Reliability
- **3.** Usability
- **4.** Portability

> [!TIP]
> **Correct answer: 3. Usability**

## Solution

Performance, reliability, and portability are strongly shaped by architectural choices such as component decomposition, redundancy, communication paths, deployment, and platform isolation. Usability depends much more directly on user-interface design and interaction details, which are often below the architectural level. It is therefore the least highly affected attribute among the choices.

## Key Points

- Architecture most strongly controls system-wide runtime and structural qualities; interface-level usability is less directly determined.

## Why the other options are incorrect

Architecture determines performance bottlenecks, fault-containment/recovery structures, and platform dependencies, so options 1, 2, and 4 are architecturally significant quality attributes.
