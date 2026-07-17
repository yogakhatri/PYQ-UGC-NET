# Question 102

*UGC NET CS · 2019 June Paper 1 And 2 · Software Design · Model-View-Controller architecture*

The M components in MVC are responsible for:

- **1.** user interface
- **2.** security of the system
- **3.** business logic and domain objects
- **4.** translating between user-interface actions/events and operations on domain objects

> [!TIP]
> **Correct answer: 3. business logic and domain objects**

## Solution

In Model-View-Controller, the Model represents application state, domain objects and business rules. The View presents the user interface, while the Controller translates user actions into operations on the model. Therefore business logic and domain objects belong to the Model.

## Key Points

- MVC: Model = data and business logic; View = presentation; Controller = input coordination.

## Why the other options are incorrect

- **Option 1:** is the View's responsibility.
- **Option 2:** security is cross-cutting and is not the defining Model responsibility.
- **Option 4:** describes the Controller.
