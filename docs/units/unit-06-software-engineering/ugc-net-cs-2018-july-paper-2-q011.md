# Question 11

*UGC NET CS · 2018 July Paper 2 · Estimation and Scheduling · LOC Productivity, Effort, Duration and Cost*

For software system P: estimated size=33,480 LOC; productivity=620 LOC per person-month; developers=6; salary=₹50,000 per developer-month. If E is effort (person-months), D is development time (months), and C is cost (₹ lakh), find (E,D,C).

- **1.** (48, 8, 24)
- **2.** (54, 9, 27)
- **3.** (60, 10, 30)
- **4.** (42, 7, 21)

> [!TIP]
> **Correct answer: 2. (54, 9, 27)**

## Solution

Effort is size divided by productivity: E=33,480/620=54 person-months. With 6 developers, development time is D=54/6=9 months. Cost is 54 developer-months×₹50,000=₹2,700,000=₹27 lakh. Thus (E,D,C)=(54,9,27), which is option 2.

## Key Points

- Effort=size/productivity; duration=effort/team size; labor cost=effort×cost per person-month.

## Why the other options are incorrect

The other triples do not satisfy all three given relationships. Salary must multiply person-month effort, not merely calendar duration; the six developers are already accounted for when converting effort to elapsed months.
