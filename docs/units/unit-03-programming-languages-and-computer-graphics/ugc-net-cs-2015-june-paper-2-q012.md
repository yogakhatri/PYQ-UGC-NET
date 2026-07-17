# Question 12

*UGC NET CS · 2015 June Paper 2 · Programming in C++ · Inherited Data and Virtual Members*

Which of the following, in C++, is inherited in a derived class from base class ?

- **1.** constructor
- **2.** destructor
- **3.** data members
- **4.** virtual methods

> [!TIP]
> **Correct answer: Both option 3 (base-class data members as the base subobject) and option 4 (virtual member functions) are inherited; the MCQ has no unique standards-correct answer.**

## Solution

A derived object contains a base-class subobject, including the base's non-static data members, although access control may prevent direct naming of private members. Ordinary member functions, including public/protected virtual functions, are inherited; a derived class may use the inherited virtual implementation or override it. Constructors and destructors are special members and are not inherited in the ordinary sense assumed by this older question.

## Key Points

- Inheritance combines a base subobject with inherited member-function behavior; accessibility and overriding are separate questions from inheritance.

## Why the other options are incorrect

Options 1 and 2 are not ordinary inherited members. Selecting only data members ignores that a derived class with no override still calls an inherited virtual method. Selecting only virtual methods ignores the base subobject's data. The question should have asked which is not inherited or allowed multiple answers.
