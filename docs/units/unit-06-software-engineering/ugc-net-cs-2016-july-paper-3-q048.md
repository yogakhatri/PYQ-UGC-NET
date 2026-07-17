# Question 48

*UGC NET CS · 2016 July Paper 3 · Estimation and Scheduling · LOC and FP Estimation*

The number of function points of a proposed system is calculated as 500. Suppose that the system is planned to be developed in Java and the LOC/FP ratio of Java is 50. Estimate the effort (E) required to complete the project using the effort formula of basic COCOMO given below : E = a(KLOC)b Assume that the values of a and b are 2.5 and 1.0 respectively.

- **1.** 25 person months
- **2.** 75 person months
- **3.** 62.5 person months
- **4.** 72.5 person months

> [!TIP]
> **Correct answer: 3. 62.5 person months**

## Solution

First convert function points to source lines: 500 FP × 50 LOC/FP = 25,000 LOC = 25 KLOC. Substitute this into the stated basic COCOMO equation: E = a(KLOC)^b = 2.5(25)^1.0 = 62.5 person-months. Hence option 3 is correct.

## Key Points

- For a function-point-to-COCOMO question: FP × LOC/FP → LOC; divide by 1,000 → KLOC; then apply the effort equation.

## Why the other options are incorrect

The common mistake is to insert 25,000 directly even though the formula requires KLOC, or to omit the coefficient 2.5. The remaining values do not follow from the supplied FP-to-LOC conversion and COCOMO parameters.
