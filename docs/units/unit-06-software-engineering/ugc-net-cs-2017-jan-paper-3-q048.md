# Question 48

*UGC NET CS · 2017 Jan Paper 3 · Estimation and Scheduling · Basic COCOMO Effort and Duration*

A software company needs to develop a project that is estimated as 1000 function points and is planning to use JAVA as the programming language whose approximate lines of code per function point is accepted as 50. Considering a = 1.4 as multiplicative factor, b = 1.0 as exponention factor for the basic COCOMO effort equation and c = 3.0 as multiplicative factor, d = 0.33 as exponention factor for the basic COCOMO duration equation, approximately how long does the project take to complete ?

- **1.** 11.2 months
- **2.** 12.2 months
- **3.** 13.2 months
- **4.** 10.2 months

> [!TIP]
> **Correct answer: 2. 12.2 months**

## Solution

The size estimate is 1000 FP×50 LOC/FP=50,000 LOC=50 KLOC. Basic COCOMO effort is E=a(KLOC)^b=1.4×50^1=70 person-months. Duration is D=cE^d=3×70^0.33≈3×4.06≈12.18 months, which rounds to 12.2 months. Therefore option 2 is correct.

## Key Points

- Basic COCOMO sequence: FP→LOC→KLOC, then effort a(KLOC)^b, then duration c(effort)^d.

## Why the other options are incorrect

The other durations do not result from applying the supplied duration coefficients to the computed 70 person-month effort. A common mistake is to put KLOC directly into the duration equation instead of first computing effort.
