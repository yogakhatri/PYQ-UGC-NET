# Question 13

*UGC NET CS · 2016 July Paper 2 · Programming in C++ · Friend Classes*

Which one of the following is correct, when a class grants friend status to another class ?

- **1.** The member functions of the class generating friendship can access the members of the friend class.
- **2.** All member functions of the class granted friendship have unrestricted access to the members of the class granting the friendship.
- **3.** Class friendship is reciprocal to each other.
- **4.** There is no such concept.

> [!TIP]
> **Correct answer: 2. All member functions of the class granted friendship have unrestricted access to the members of the class granting the friendship.**

## Solution

If class A declares class B as a friend, every member function of B may access A's private and protected members, subject to having an A object or other valid access path. B is the class granted friendship and A is the class granting it, exactly as option 2 states.

## Key Points

- Friendship is granted, directional, and non-reciprocal: A names B as friend → B may access A.

## Why the other options are incorrect

Friendship grants access in the opposite direction from option 1. It is neither reciprocal nor automatically transitive or inherited, so option 3 is false. C++ explicitly supports friend functions and friend classes, so option 4 is false.
