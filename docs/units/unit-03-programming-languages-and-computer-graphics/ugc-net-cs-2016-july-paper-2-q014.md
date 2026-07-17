# Question 14

*UGC NET CS · 2016 July Paper 2 · Object-Oriented Programming · Method Overriding*

When a method in a subclass has the same name and type signatures as a method in the superclass, then the method in the subclass _____ the method in the superclass.

- **1.** Overloads
- **2.** Friendships
- **3.** Inherits
- **4.** Overrides

> [!TIP]
> **Correct answer: 4. Overrides**

## Solution

When a subclass defines an instance method with the same signature as an inherited superclass method, the subclass implementation overrides the superclass implementation. Calls dispatched through an object of the subclass then use the overriding method under the language's dynamic-dispatch rules.

## Key Points

- Same signature across superclass/subclass → overriding; same name with different parameters → overloading.

## Why the other options are incorrect

Overloading uses the same name with a different parameter list, usually within the same class hierarchy scope. Friendship is an unrelated C++ access mechanism. Inheritance makes the superclass method available only when the subclass does not replace it with the matching implementation described here.
