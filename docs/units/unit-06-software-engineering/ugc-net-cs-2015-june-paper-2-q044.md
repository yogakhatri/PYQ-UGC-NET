# Question 44

*UGC NET CS · 2015 June Paper 2 · Software Design · Cohesion and Information Hiding*

Cohesion is an extension of :

- **1.** Abstraction concept
- **2.** Refinement concept
- **3.** Information hiding concept
- **4.** Modularity

> [!TIP]
> **Correct answer: 3. Information hiding concept**

## Solution

Information hiding groups a design decision and the data or procedures it affects inside a module while exposing only what other modules need. Cohesion extends this idea by measuring how strongly the elements inside that module belong together around one focused purpose. High cohesion therefore supports an effective information-hiding boundary.

## Key Points

- Information hiding draws the module boundary; cohesion asks whether everything inside that boundary serves one focused responsibility.

## Why the other options are incorrect

Abstraction, refinement, and modularity are related design concepts, but the standard statement tested here is that cohesion is an extension of information hiding. The question asks for that specific conceptual lineage, not merely any concept related to cohesive modules.
