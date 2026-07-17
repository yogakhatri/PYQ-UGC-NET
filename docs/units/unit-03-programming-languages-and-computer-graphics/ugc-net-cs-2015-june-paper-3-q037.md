# Question 37

*UGC NET CS · 2015 June Paper 3 · Object-Oriented Programming in Java · Visibility of Interface Method Implementations*

In Java, when we implement an interface method, it must be declared as :

- **1.** Private
- **2.** Protected
- **3.** Public
- **4.** Friend

> [!TIP]
> **Correct answer: 3. Public**

## Solution

An ordinary abstract method declared by a Java interface is public. A class method that implements it cannot reduce that accessibility, so the implementation must be declared `public`; leaving off an access modifier would make it package-private and cause a compile-time error.

## Key Points

- Implementing a public interface contract requires a public class method.

## Why the other options are incorrect

Private and protected are less accessible than the interface contract and cannot implement the public method. Java has no `friend` access modifier. Modern interfaces may also contain private helper methods, but those are not methods implemented by a class.
