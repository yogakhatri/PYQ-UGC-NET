# Question 6

*UGC NET CS · 2018 July Paper 2 · Java Programming · Final Classes, Interfaces and Method Overriding*

In Java, which statements are true? S1: Applying `final` to a class prevents it from being extended. S2: A class can inherit from only one class but can implement multiple interfaces. S3: Replacing an inherited method implementation is called method overloading.

- **1.** S1 and S2 only
- **2.** S1 and S3 only
- **3.** S2 and S3 only
- **4.** All of S1, S2 and S3

> [!TIP]
> **Correct answer: 1. S1 and S2 only**

## Solution

S1 is true: a `final` class cannot be subclassed. S2 is true: a Java class has at most one direct superclass but may implement multiple interfaces. S3's behavior is possible, but its name is wrong—providing a new implementation with the same method signature in a subclass is method overriding, not overloading. Thus only S1 and S2 are true, option 1.

## Key Points

- Overriding = same signature across inheritance; overloading = same name with different parameter lists.

## Why the other options are incorrect

Options 2–4 treat S3 as true. Overloading means declaring multiple methods with the same name but different parameter lists, commonly within one class; overriding replaces an inherited instance-method implementation with a compatible same-signature method.
