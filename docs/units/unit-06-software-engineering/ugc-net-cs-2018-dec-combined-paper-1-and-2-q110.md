# Question 110

*UGC NET CS · 2018 Dec Paper 1 And 2 · Software Design · Common, Stamp, Control and Content Coupling*

Software coupling involves dependencies among pieces of software called modules. Which of the following are correct statements with respect to module coupling? P: Common coupling occurs when two modules share the same global data. Q: Control coupling occurs when modules share a composite data structure and use only parts of it. R: Content coupling occurs when one module modifies or relies on the internal working of another module. Choose the correct answer from the code given below :

- **1.** P and Q only
- **2.** P and R only
- **3.** Q and R only
- **4.** All of P, Q and R

> [!TIP]
> **Correct answer: 2. P and R only**

## Solution

P is true: common coupling exists when modules depend on the same global data. Q is false: passing a composite record or structure when a module uses only part of it is stamp (data-structured) coupling. Control coupling instead passes information such as a flag or command that determines another module's control flow. R is true: content coupling is the very strong dependency in which one module uses, changes, or relies on another module's internal implementation. Therefore P and R only are correct, option 2.

## Key Points

- Common shares globals; stamp passes an oversized structure; control passes control-driving information; content reaches into another module's internals.

## Why the other options are incorrect

Options 1, 3, and 4 all accept Q, which confuses stamp coupling with control coupling. Option 1 also omits the correct definition of content coupling in R.
