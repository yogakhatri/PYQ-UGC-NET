# Question 13

*UGC NET CS · 2010 June Paper 2 · Object-Oriented Programming · Abstract Class*

Member of a class specified as _______ are accessible only to method of the class.

- **A.** private
- **B.** public
- **C.** protected
- **D.** derive

> [!TIP]
> **Correct answer: A. private**

## Solution

A private class member can be accessed directly only by the class's own member functions (and explicitly granted friends, depending on language). This is the access level described by the stem.

## Key Points

- Private hides implementation members behind the class's own methods.

## Why the other options are incorrect

Public members are accessible to clients; protected members are also accessible in derived classes; 'derive' is not an access specifier.
