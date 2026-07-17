# Question 12

*UGC NET CS · 2021 Nov With Answers · Software Architecture · Model–View–Controller Responsibilities*

The V components in MVC are responsible for:

- **1.** User interface.
- **2.** Security of the system.
- **3.** Business logic and domain objects.
- **4.** Translating between user interface actions/events and operations on the domain objects.

> [!TIP]
> **Correct answer: 1. User interface.**

## Solution

In MVC, V means View. The View presents application data and forms the user-facing interface, so option 1 is correct. The Model holds domain state and business logic, while the Controller interprets user actions and coordinates operations on the model and selection of a view.

## Key Points

- MVC mnemonic: Model=data/logic, View=presentation, Controller=input coordination.

## Why the other options are incorrect

Security is a cross-cutting concern rather than the View's defining role. Option 3 describes the Model, and option 4 describes the Controller.
