# Question 29

*UGC NET CS · 2012 Dec Paper 2 · Programming in C++ · Exception-Handling Functions*

Which two special functions handle exceptions that occur during exception handling itself?

- **1.** void terminate() and void unexpected()
- **2.** non-void terminate() and void unexpected()
- **3.** void terminate() and non-void unexpected()
- **4.** non-void terminate() and non-void unexpected()

> [!TIP]
> **Correct answer: 1. void terminate() and void unexpected()**

## Solution

In the C++ exception model used when this question was written, terminate() is invoked when exception handling cannot continue, while unexpected() handles violation of an old dynamic exception specification. Both functions have void return type, so the intended declarations are void terminate() and void unexpected().

## Key Points

- Historical C++ exception hooks terminate() and unexpected() both return void; in modern C++, focus on std::terminate and noexcept.

## Why the other options are incorrect

Options 2, 3 and 4 assign a non-void return type to at least one function, which contradicts the historical library interface. Modern C++ has removed unexpected() and dynamic exception specifications, so this is an exam-era language-history question rather than current coding advice.
