# Question 43

*UGC NET CS · 2014 Dec Paper 3 · Software Metrics · Source-Code versus Functional-Size Metrics*

Which one of the following is not a source code metric ?

- **A.** Halstead metric
- **B.** Function point metric
- **C.** Complexity metric
- **D.** Length metric

> [!TIP]
> **Correct answer: B. Function point metric**

## Solution

Halstead measures derive from operators and operands in source code. Length metrics count source-level size, and complexity metrics such as cyclomatic complexity derive from the program's control structure. Function points instead measure externally visible functionality from inputs, outputs, inquiries, files, and interfaces; they can be estimated before source code exists. Therefore function point is not a source-code metric.

## Key Points

- Source metrics inspect code artifacts; function points measure user-visible functional size independently of implementation language.

## Why the other options are incorrect

A, C, and D all require or directly describe properties of code. B is deliberately language-independent and measures delivered functionality rather than lexical or structural source properties.
