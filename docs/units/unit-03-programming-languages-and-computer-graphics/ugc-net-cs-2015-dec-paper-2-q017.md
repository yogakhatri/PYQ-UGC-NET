# Question 17

*UGC NET CS · 2015 Dec Paper 2 · Programming in C++ · Unhandled Exceptions and std::terminate*

In C++, which system-provided function is called when no handler is available for an exception?

- **1.** terminate()
- **2.** unexpected()
- **3.** abort()
- **4.** kill()

> [!TIP]
> **Correct answer: 1. terminate()**

## Solution

If exception propagation reaches a point where no matching handler exists, the C++ runtime calls `std::terminate()`. The installed terminate handler normally ends the program; the exact termination mechanism can be customized with `std::set_terminate`.

## Key Points

- Unhandled C++ exception → `std::terminate()`.

## Why the other options are incorrect

Historically, `unexpected()` handled violations of a dynamic exception specification, not an ordinary uncaught exception. `abort()` may be used by a terminate handler but is not the language-level function specified here, and `kill()` is an operating-system interface rather than the C++ exception mechanism.
