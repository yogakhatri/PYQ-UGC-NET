# Question 6

*UGC NET CS · 2013 Dec Paper 2 · Software Design · Fan-In and Fan-Out*

FAN IN of a component A is defined as

- **A.** Number of components that can call or pass control to component A.
- **B.** Number of components that are called by component A.
- **C.** Number of components related to component A.
- **D.** Number of components dependent on component A.

> [!TIP]
> **Correct answer: A. Number of components that can call or pass control to component A.**

## Solution

Fan-in of module A is the number of other modules that directly call A or transfer control/data into it. It measures how many incoming dependencies A has. A high fan-in often indicates a reused service, although its interface must remain stable.

## Key Points

- Fan-in counts incoming callers; fan-out counts modules called by the component.

## Why the other options are incorrect

The number of modules called by A is fan-out, not fan-in. 'Related to' is too vague, while 'dependent on A' may describe transitive or conceptual dependence rather than the direct incoming call/control definition.
