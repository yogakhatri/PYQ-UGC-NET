# Question 47

*UGC NET CS · 2014 Dec Paper 3 · Software Design · Component Fan-In*

The fan-in of a component A is defined as:

- **A.** The number of components that can call, or pass control, to component A
- **B.** The number of components related to component A
- **C.** The number of components dependent on component A
- **D.** None of the above

> [!TIP]
> **Correct answer: A. The number of components that can call, or pass control, to component A**

## Solution

Fan-in measures incoming dependency or control flow. For component A, count the distinct components that call A or can pass control to it. A high fan-in often suggests that A provides a widely reused service, although it can also make A a critical dependency.

## Key Points

- Fan-in counts incoming callers; fan-out counts components called by the component.

## Why the other options are incorrect

B says only 'related,' which does not specify direction. C's 'dependent on A' is vague and may describe semantic dependency rather than incoming calls; A gives the precise control-transfer definition. Because A is valid, none of the above is false.
