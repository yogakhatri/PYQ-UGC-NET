# Question 39

*UGC NET CS · 2014 Dec Paper 3 · Object-Oriented Programming · Autoboxing and Wrapper Classes*

In Java, converting primitive-type data into an instance of the corresponding wrapper class is called:

- **A.** Boxing
- **B.** Wrapping
- **C.** Instantiation
- **D.** Autoboxing

> [!TIP]
> **Correct answer: D. Autoboxing**

## Solution

The expected Java term is autoboxing: the compiler automatically converts a primitive value to the corresponding wrapper object when an object is required, for example `Integer x = 5;`. The reverse automatic conversion is unboxing. This Java feature removes the need to write an explicit wrapper construction or conversion call.

## Key Points

- Autoboxing is compiler-supplied primitive→wrapper conversion; unboxing is wrapper→primitive conversion.

## Why the other options are incorrect

Wrapping is only a general descriptive word, and instantiation is the broader creation of any object. `Boxing` can generically mean primitive-to-wrapper conversion, so the printed wording is broader than ideal; the exam's intended distinction is that Java's automatic conversion is specifically autoboxing, option D.
