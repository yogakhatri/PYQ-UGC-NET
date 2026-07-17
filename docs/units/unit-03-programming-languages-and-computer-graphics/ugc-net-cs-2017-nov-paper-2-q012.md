# Question 12

*UGC NET CS · 2017 Nov Paper 2 · Programming in C++ · Operator Associativity*

The associativity of which of the following operators is Left to Right, in C++ ?

- **1.** Unary Operator
- **2.** Logical not
- **3.** Array element access
- **4.** addressof

> [!TIP]
> **Correct answer: 3. Array element access**

## Solution

Array subscripting is a postfix expression operation, and postfix operations associate from left to right. This is why a chain such as `a[i][j]` is grouped as `(a[i])[j]`. Unary operators, logical NOT `!`, and address-of `&` belong to the unary level and associate from right to left. Therefore option 3 is correct.

## Key Points

- Postfix operators associate left-to-right; prefix unary operators associate right-to-left.

## Why the other options are incorrect

Options 1, 2, and 4 all name unary operators or a unary-operator category, whose repeated application groups right to left. Precedence tells which operator binds first; associativity resolves operators at the same precedence level.
