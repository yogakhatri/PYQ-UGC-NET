# Question 11

*UGC NET CS · 2017 Nov Paper 2 · Programming in C++ · Operator Precedence and Pointer Increment*

‘ptrdata’ is a pointer to a data type. The expression *ptrdata++ is evaluated as (in C++) :

- **1.** *(ptrdata++)
- **2.** (*ptrdata)++
- **3.** *(ptrdata)++
- **4.** Depends on compiler

> [!TIP]
> **Correct answer: 1. *(ptrdata++)**

## Solution

Postfix increment has higher precedence than unary dereference. Therefore `*ptrdata++` is parsed as `*(ptrdata++)`: use the pointer's old value for the dereference, then advance the pointer to the next element. It does not increment the pointed-to data. Thus option 1 is correct.

## Key Points

- Postfix `++` binds before unary `*`; parentheses are the safest way to state which object is incremented.

## Why the other options are incorrect

Options 2 and 3 effectively describe `(*ptrdata)++`, which increments the value being pointed at while leaving the pointer unchanged. The parse is fixed by the C++ precedence rules, so it does not depend on the compiler.
