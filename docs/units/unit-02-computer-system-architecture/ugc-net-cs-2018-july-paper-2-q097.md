# Question 97

*UGC NET CS · 2018 July Paper 2 · Input-Output Organization · Maskable, Exception and Synchronous Interrupts*

Match: (a) interrupts that can be delayed when a higher-priority interrupt occurs, (b) unplanned interrupts occurring while a program executes, (c) an interrupt source in phase with the system clock; with (i) normal, (ii) synchronous, (iii) maskable, and (iv) exception.

- **1.** (ii) (i) (iv)
- **2.** (ii) (iv) (iii)
- **3.** (iii) (i) (ii)
- **4.** (iii) (iv) (ii)

> [!TIP]
> **Correct answer: 4. (iii) (iv) (ii)**

## Solution

An interrupt that may be postponed or disabled is maskable, so a→iii. An unplanned event arising during program execution—such as a fault or trap—is an exception, so b→iv. An interrupt/event synchronized in phase with the system clock is synchronous, so c→ii. The sequence (iii),(iv),(ii) is option 4.

## Key Points

- Maskable=can be deferred; exception=execution-generated abnormal event; synchronous=aligned with clock/instruction timing.

## Why the other options are incorrect

The other matchings label a delayable interrupt as synchronous or normal, or fail to recognize an execution-time abnormal event as an exception. `Synchronous` classifies timing relative to instruction/clock activity; `maskable` classifies whether handling can be deferred.
