# Question 54

*UGC NET CS · 2018 Dec Paper 1 And 2 · Counting, Mathematical Induction and Discrete Probability · Three-Set Inclusion-Exclusion*

A commuter survey allowed each respondent to select Bus, Train, or Automobile, with multiple selections permitted. Counts were: Bus 30, Train 35, Automobile 100, Bus and Train 15, Bus and Automobile 15, Train and Automobile 20, and all three 5. How many people completed the survey?

- **1.** 120
- **2.** 165
- **3.** 160
- **4.** 115

> [!TIP]
> **Correct answer: 1. 120**

## Solution

Apply inclusion–exclusion to the three sets. The number in at least one set is 30+35+100−15−15−20+5=120. Pairwise intersections were counted twice in the first sum, so they are subtracted once; the triple intersection was then removed too many times, so it is added back. Therefore option 1 is correct.

## Key Points

- For three sets, |A∪B∪C|=|A|+|B|+|C|−|A∩B|−|A∩C|−|B∩C|+|A∩B∩C|.

## Why the other options are incorrect

Adding the three set sizes alone double-counts overlaps. Subtracting pairwise overlaps without restoring the triple intersection also gives a wrong result because each element common to all three was added three times and subtracted three times.
