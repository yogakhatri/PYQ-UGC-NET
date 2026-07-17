# Question 61

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Language Design and Translation Issues · Virtual Computers and Binding Times*

OBID:187011 If a constructor Date' is declared explicitly and has to be defined outside the class, which of the following is correct?

- **1.** Date:: Date(int dd) //*...*/; ...*/)
- **2.** explicit Date:: Date(int dd) (/*
- **3.** Such a constructor cannot be defined
- **4.** Constructor always has to be defined inside the class

> [!TIP]
> **Correct answer: 1. Date:: Date(int dd) //*...*/; ...*/)**

## Solution

A constructor defined outside its class uses the class scope-resolution qualifier: Date::Date(int dd) { ... }. The explicit specifier belongs on the constructor declaration inside the class; it is not repeated on the out-of-class definition. Therefore the form shown in option 1 is the correct definition syntax.

## Key Points

- Declare `explicit Date(int)` in the class; define it later as `Date::Date(int) { ...
- }`.

## Why the other options are incorrect

Option 2 incorrectly places explicit on the out-of-class definition. Options 3 and 4 are false because constructors may be declared in the class and defined outside it just like other member functions.
