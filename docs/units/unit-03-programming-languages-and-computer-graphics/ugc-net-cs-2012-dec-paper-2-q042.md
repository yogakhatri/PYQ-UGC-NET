# Question 42

*UGC NET CS · 2012 Dec Paper 2 · Programming in C++ · File Open Modes*

Which mode declaration is used in C++ to open a file for input?

- **1.** ios::app
- **2.** in::ios
- **3.** ios::file
- **4.** ios::in

> [!TIP]
> **Correct answer: 4. ios::in**

## Solution

The C++ stream open mode ios::in requests input access, meaning the file is opened for reading. It can be supplied to a stream constructor or open() call, and ifstream uses input mode by default.

## Key Points

- C++ file modes: ios::in for reading, ios::out for writing, and ios::app for appending.

## Why the other options are incorrect

ios::app opens for append-style output, with writes placed at the end. in::ios reverses the scope qualification and is not a valid mode name. ios::file is not a standard C++ open mode.
