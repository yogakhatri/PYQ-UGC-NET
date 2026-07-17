# Question 14

*UGC NET CS · 2017 Nov Paper 2 · Programming in C++ · Virtual Functions*

Which of the following is not correct for virtual function in C++ ?

- **1.** Must be declared in public section of class.
- **2.** Virtual function can be static.
- **3.** Virtual function should be accessed using pointers.
- **4.** Virtual function is defined in base class.

> [!TIP]
> **Correct answer: No unique answer as written: option 2 is false, but options 1 and 3 are also false statements about C++ virtual functions.**

## Solution

A virtual function must be a non-static member function because dynamic dispatch selects an overrider using a particular object's dynamic type; a static member has no `this` object. Thus option 2 is certainly incorrect and is almost surely the intended answer. However, option 1 is also incorrect because a virtual function may be public, protected, or private. Option 3 is also too restrictive: virtual dispatch works through references as well as pointers, and a virtual function can be called using an object expression. Consequently the question does not have exactly one standards-correct choice.

## Key Points

- Virtual dispatch needs an object and a non-static member; access level and use of a pointer are separate issues.

## Why the other options are incorrect

Option 4 describes the usual base-class declaration/definition model, although a pure virtual function need not have an ordinary base implementation. For exam recall, remember the intended contrast: virtual implies non-static. For accurate C++, do not memorize the claims that virtuals must be public or must be called only through pointers.

## References

- [C++ working draft — Virtual functions](https://eel.is/c++draft/class.virtual)
- [C++ working draft — Static member functions](https://eel.is/c++draft/class.static.mfct)
- [C++ working draft — Access to virtual functions](https://eel.is/c++draft/class.access.virt)
