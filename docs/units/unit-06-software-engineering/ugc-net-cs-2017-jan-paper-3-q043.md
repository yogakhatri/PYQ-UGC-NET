# Question 43

*UGC NET CS · 2017 Jan Paper 3 · Software Testing · Regression Testing and Equivalence Partitioning*

Which of the following statement(s) is/are TRUE with regard to software testing ? I. Regression testing technique ensures that the software product runs correctly after the changes during maintenance. II. Equivalence partitioning is a white-box testing technique that divides the input domain of a program into classes of data from which test cases can be derived.

- **1.** only I
- **2.** only II
- **3.** both I and II
- **4.** neither I nor II

> [!TIP]
> **Correct answer: 1. only I**

## Solution

Regression testing reruns relevant tests after modification to detect whether previously working behavior has been broken, so statement I is true. Equivalence partitioning divides the input domain into classes expected to behave similarly and chooses representatives from each; it is a black-box specification-based technique, not white-box testing. Thus II is false and only I is correct, giving option 1.

## Key Points

- Regression testing protects existing behavior after change; equivalence partitioning is black-box input-domain testing.

## Why the other options are incorrect

Options 2 and 3 accept the incorrect white-box classification. Option 4 rejects regression testing's central maintenance purpose. White-box techniques instead derive tests from internal control flow, paths, conditions, or data flow.
