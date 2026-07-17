# Question 71

*UGC NET CS · 2020 Nov With Answers · Software Project Management · Development and Maintenance Cost Trade-offs*

A project may use language L1 or L2. L2 requires three times as many LOC as L1. For either language, development effort in man-years equals LOC/1000. Development cost per man-year is ₹70,000 for L1 and ₹90,000 for L2; annual maintenance is ₹1,00,000 for L1 and ₹40,000 for L2 over 10 years. For what L1 LOC are the total costs equal?

- **1.** 2000
- **2.** 6000
- **3.** 3000
- **4.** 5000

> [!TIP]
> **Correct answer: 3. 3000**

## Solution

Let t be L1's size in thousands of LOC. L2 then has 3t thousand LOC. L1 development costs ₹70,000t and ten-year maintenance costs ₹10,00,000, so C1=70,000t+10,00,000. L2 costs ₹90,000×3t for development and ₹4,00,000 for maintenance, so C2=2,70,000t+4,00,000. Equating gives 6,00,000=2,00,000t, hence t=3. Thus L1 has 3,000 LOC, option 3.

## Key Points

- Build total lifecycle cost for each language: development effort×rate plus ten years of maintenance.

## Why the other options are incorrect

The other LOC values do not balance the larger L2 development cost against its smaller maintenance cost. The factor of three applies to L2's LOC before its per-man-year development rate is used.
