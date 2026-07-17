# Question 14

*UGC NET CS · 2014 Dec Paper 2 · Programming in C · Arrays as Function Parameters*

When an array is passed as parameter to a function, which of the following statements is correct ?

- **A.** The function can change values in the original array.
- **B.** In C, parameters are passed by value, the function cannot chan ge the original value in the array.
- **C.** It results in compilation error when the function tries to a ccess the elements in the array.
- **D.** Results in a run time error when the function tries to acc ess the elements in the array.

> [!TIP]
> **Correct answer: A. The function can change values in the original array.**

## Solution

In a C parameter list, an array parameter is adjusted to a pointer to the array's first element. The pointer value itself is passed by value, but it still points into the caller's original array. Assigning through it, such as a[i]=new_value, therefore changes the original element unless the pointed-to type is const-qualified.

## Key Points

- C is pass-by-value, but the passed value is a pointer to the original array storage.

## Why the other options are incorrect

B confuses copying the pointer with copying the entire array. Accessing a valid passed array is legal and normally safe, so C and D do not follow merely from array parameter passing.
