# Question 13

*UGC NET CS · 2014 Dec Paper 2 · Programming in C++ · Friend Functions versus Class Members*

Which of the following is not a member of class ?

- **A.** Static function
- **B.** Friend function
- **C.** Const function
- **D.** Virtual function

> [!TIP]
> **Correct answer: B. Friend function**

## Solution

A friend function may be declared inside a class and receives access to its private and protected members, but it is not a member function: it has no this pointer and is called like an ordinary function. Static, const-qualified and virtual functions can all be class member functions.

## Key Points

- friend grants access, not class membership.

## Why the other options are incorrect

A static member function is a member despite lacking a this pointer. C describes a member function that promises not to modify the object's nonmutable state. D is a member function participating in dynamic dispatch. Friend status grants access without membership.
