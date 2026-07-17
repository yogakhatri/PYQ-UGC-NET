# Question 46

*UGC NET CS · 2015 Dec Paper 2 · Software Testing · Error, Fault and Failure*

In software testing, how the error, fault and failure are related to each other ?

- **1.** Error leads to failure but fault is not related to error and failure.
- **2.** Fault leads to failure but error is not related to fault and failure.
- **3.** Error leads to fault and fault leads to failure.
- **4.** Fault leads to error and error leads to failure.

> [!TIP]
> **Correct answer: 3. Error leads to fault and fault leads to failure.**

## Solution

An error is a human action or misunderstanding that produces an incorrect result—for example, a developer misunderstands a requirement. That error can introduce a fault (defect) into the software artifact. When the faulty code executes under conditions that expose it, the system may show an externally observable failure. The causal chain is therefore error → fault → failure.

## Key Points

- Human error creates a software fault; an activated fault can produce a failure.

## Why the other options are incorrect

Options 1 and 2 incorrectly detach faults from the chain. Option 4 reverses error and fault: the developer's error generally creates the fault, not the other way around. A fault need not cause a failure on every execution, but it can lead to one when activated.
