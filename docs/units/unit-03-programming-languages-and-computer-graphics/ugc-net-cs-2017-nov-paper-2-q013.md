# Question 13

*UGC NET CS · 2017 Nov Paper 2 · Object-Oriented Programming · Class Member Access*

A member function can always access the data in __________ , (in C++).

- **1.** the class of which it is member
- **2.** the object of which it is a member
- **3.** the public part of its class
- **4.** the private part of its class

> [!TIP]
> **Correct answer: 1. the class of which it is member**

## Solution

A non-static member function is defined in the scope of its class and has access to the class's members, including private and protected data. Therefore the most complete statement is that it can access data in the class of which it is a member—option 1. Accessing a particular non-static member still requires an object, normally the implicit `this` object or another object supplied to the function.

## Key Points

- Class membership grants a member function access to all access sections of that class; object identity determines which non-static instance is read or changed.

## Why the other options are incorrect

Option 2 is conceptually wrong because a member function is a member of a class, not of one particular object. Options 3 and 4 mention only one access section; the function's class-member access is not restricted to public-only or private-only data.
