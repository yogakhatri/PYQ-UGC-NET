# Question 44

*UGC NET CS · 2017 Nov Paper 2 · Software Testing · Sequence of Testing Levels*

What is the normal order of activities in which traditional software testing is organized ? (a) Integration Testing (b) System Testing (c) Unit Testing (d) Validation Testing

- **1.** (c), (a), (b), (d)
- **2.** (c), (a), (d), (b)
- **3.** (d), (c), (b), (a)
- **4.** (b), (d), (a), (c)

> [!TIP]
> **Correct answer: 2. (c), (a), (d), (b)**

## Solution

Traditional testing proceeds from the smallest scope outward. Unit testing checks individual components first (c), integration testing checks their interfaces next (a), validation testing checks whether the completed software satisfies requirements (d), and system testing evaluates it within the full system/environment (b). The order c,a,d,b is option 2.

## Key Points

- Traditional testing strategy expands outward: unit → integration → validation → system.

## Why the other options are incorrect

Option 1 places system testing before validation in the traditional sequence used by the question. Options 3 and 4 begin with broad validation/system work before component and interface testing, reversing the normal progression.
