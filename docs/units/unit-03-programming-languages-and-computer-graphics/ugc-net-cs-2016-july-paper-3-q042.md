# Question 42

*UGC NET CS · 2016 July Paper 3 · Object-Oriented Programming · Reference Assignment and Object Aliasing*

When one object reference variable is assigned to another object reference variable then

- **1.** a copy of the object is created.
- **2.** a copy of the reference is created.
- **3.** a copy of the reference is not created.
- **4.** it is illegal to assign one object reference variable to another object reference variable.

> [!TIP]
> **Correct answer: 2. a copy of the reference is created.**

## Solution

Assigning one object-reference variable to another copies the reference value. Both variables then refer to the same object; the object itself is not cloned. Hence option 2 is correct.

## Key Points

- Reference assignment creates an alias to the same object, not a second object.

## Why the other options are incorrect

Option 1 incorrectly implies a deep or shallow object copy. Option 3 denies the reference-value assignment that actually occurs. Option 4 is false for compatible reference types. Mutating the shared object through either alias is visible through the other.
