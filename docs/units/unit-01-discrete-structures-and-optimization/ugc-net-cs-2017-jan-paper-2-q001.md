# Question 1

*UGC NET CS · 2017 Jan Paper 2 · Counting, Mathematical Induction and Discrete Probability · Recurrence Relations and Sequences*

Consider the sequence F₀₀ defined by F₀₀(0)=1, F₀₀(1)=1, and F₀₀(n)=[10F₀₀(n−1)+100]/F₀₀(n−2) for n≥2. What is the set of values taken by the sequence?

- **1.** (1, 110, 1200)
- **2.** (1, 110, 600, 1200)
- **3.** (1, 2, 55, 110, 600, 1200)
- **4.** (1, 55, 110, 600, 1200)

> [!TIP]
> **Correct answer: 1. (1, 110, 1200)**

## Solution

Generate terms directly from the recurrence. F₀₀(2)=(10·1+100)/1=110 and F₀₀(3)=(10·110+100)/1=1200. Next, F₀₀(4)=(10·1200+100)/110=110, F₀₀(5)=(10·110+100)/1200=1, and F₀₀(6)=(10·1+100)/110=1. The ordered pair of consecutive values has now returned to (1,1), so the pattern repeats. The only distinct values ever produced are {1,110,1200}, which is option 1.

## Key Points

- For a deterministic second-order recurrence, repetition of the same consecutive pair forces the entire future sequence to repeat.

## Why the other options are incorrect

The other options include 2, 55, or 600, none of which is produced by substituting into the recurrence. Because this is a second-order recurrence, recognizing the repeated consecutive pair (1,1) proves the later sequence repeats rather than merely suggesting a pattern.
