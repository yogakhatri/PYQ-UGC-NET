# Question 44

*UGC NET CS · 2017 Jan Paper 3 · Software Testing · Top-Down Integration: Stubs and Drivers*

Which of the following are facts about a top-down software testing approach ? I. Top-down testing typically requires the tester to build method stubs. II. Top-down testing typically requires the tester to build test drivers.

- **1.** only I
- **2.** Only II
- **3.** Both I and II
- **4.** Neither I nor II

> [!TIP]
> **Correct answer: 1. only I**

## Solution

Top-down integration starts with the main control module and progressively substitutes real lower-level modules. Until a called lower module exists, a stub must simulate its interface and return behavior, so statement I is true. A separate driver is normally needed in bottom-up testing to call a lower-level cluster whose real higher-level caller is absent; the top-level control already supplies that role in top-down testing. Hence II is false and option 1 is correct.

## Key Points

- Top-down integration replaces missing callees with stubs; bottom-up integration replaces missing callers with drivers.

## Why the other options are incorrect

Options 2 and 3 incorrectly make drivers a typical top-down requirement. Option 4 incorrectly rejects the need for stubs. Hybrid strategies may use both artifacts in practice, but the textbook contrast is top-down→stubs and bottom-up→drivers.
