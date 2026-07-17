# Question 15

*UGC NET CS · 2009 Dec Paper 2 · Language Design and Translation Issues · Virtual Computers and Binding Times*

Which of the statements are true ? I. Function overloading is done at compile time. II. Protected members are accessible to the member of derived class. III. A derived class inherits constructors and destructors. IV. A friend function can be called like a normal function. V. Nested class is a derived class.

- **A.** I, II, III
- **B.** II, III, V
- **C.** III, IV, V
- **D.** I , II, IV

> [!TIP]
> **Correct answer: D. I , II, IV**

## Solution

I is true: overload resolution is normally compile-time polymorphism. II is true: derived-class members can access inherited protected members subject to language rules. III is false: constructors and destructors are not inherited in the ordinary C++ sense. IV is true: a nonmember friend function is called with ordinary function syntax. V is false: nesting does not imply inheritance. Thus I, II, and IV are true.

## Key Points

- Overloading is static; protected supports derivation; friendship and nesting are not inheritance.

## Why the other options are incorrect

Options A–C include statement III or V, both of which confuse object lifetime/nesting with inheritance.
