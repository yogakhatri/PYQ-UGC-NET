# Question 45

*UGC NET CS · 2017 Jan Paper 2 · Software Design Patterns · Decorator Pattern*

A software design pattern used to enhance the functionality of an object at run-time is :

- **1.** Adapter
- **2.** Decorator
- **3.** Delegation
- **4.** Proxy

> [!TIP]
> **Correct answer: 2. Decorator**

## Solution

The Decorator pattern wraps an object in another object implementing the same interface and adds behavior before or after delegating to the wrapped component. Decorators can be composed at run time, so responsibilities can be added without changing the original class. Thus option 2 is correct.

## Key Points

- Decorator preserves the interface and layers optional behavior around an object dynamically.

## Why the other options are incorrect

Adapter changes one interface into another. Proxy controls access to another object, for example for lazy loading or remote access. Delegation is a general object-composition mechanism rather than the named pattern whose intent is dynamic responsibility enhancement.
