# Question 97

*UGC NET CS · 2018 Dec Paper 1 And 2 · Programming in C++ · Pointers, References and Reference Returns*

Consider the following two C++ programs. P1: void f(int a, int *b, int &c) { a = 1; *b = 2; c = 3; } int main() { int i = 0; f(i, &i, i); cout << i; } P2: double a = 1, b = 2; double &f(double &d) { d = 4; return b; } int main() { f(a) = 5; cout << a << ':' << b; } S1: P1 prints 3. S2: P2 prints 4:2. Which statement is correct?

- **1.** Only S1 is true
- **2.** Only S2 is true
- **3.** Both S1 and S2 are true
- **4.** Neither S1 nor S2 is true

> [!TIP]
> **Correct answer: 1. Only S1 is true**

## Solution

In P1, parameter a is passed by value, so a=1 changes only the local copy. Parameter b points to i, so *b=2 makes i equal to 2. Parameter c is a reference to the same i, so c=3 subsequently makes i equal to 3. P1 therefore prints 3 and S1 is true. In P2, f(a) first assigns d=4, so global a becomes 4. The function returns b by reference, which means the expression f(a) is an assignable alias for b; f(a)=5 therefore sets b to 5. P2 prints 4:5, not 4:2, so S2 is false. Only S1 is true, option 1.

## Key Points

- Pass-by-value changes a copy; pointer dereference and reference parameters can alias the caller's object; a function returning T& produces an assignable lvalue.

## Why the other options are incorrect

Options 2 and 3 treat S2 as true and overlook that assigning to a reference-returning function call modifies b. Option 4 overlooks that both the pointer and reference parameters of P1 alias i, with the later c=3 assignment determining the printed value.
