# Question 46

*UGC NET CS · 2016 July Paper 3 · Software Quality and Process Improvement · Software Safety and Hazard Analysis*

Software safety is quality assurance activity that focuses on hazards that

- **1.** affect the reliability of a software component.
- **2.** may cause an entire system to fail.
- **3.** may result from user input errors.
- **4.** prevent profitable marketing of the final product.

> [!TIP]
> **Correct answer: 2. may cause an entire system to fail.**

## Solution

Software safety asks whether software-controlled behavior can create or fail to control a hazardous condition. Its concern is therefore system-level harm: a software fault, bad state, or unsafe control action may contribute to failure of the entire system. That is exactly the situation described by option 2.

## Key Points

- Reliability asks whether software continues to operate correctly; safety asks whether its behavior can lead to unacceptable system-level harm.

## Why the other options are incorrect

A component-reliability defect is relevant only when it creates a hazard; reliability and safety are related but not identical. User-input errors are merely one possible initiating cause, not the focus that defines software safety. Marketing profitability is a business concern, not a safety hazard.
