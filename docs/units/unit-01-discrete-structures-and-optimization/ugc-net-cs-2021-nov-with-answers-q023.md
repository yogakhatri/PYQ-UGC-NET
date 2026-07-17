# Question 23

*UGC NET CS · 2021 Nov With Answers · Counting · Surjections and Assigning Distinct Jobs*

How many ways are there to assign 5 different jobs to 4 different employees if every employee is assigned at least 1 job?

- **1.** 1024
- **2.** 625
- **3.** 240
- **4.** 20

> [!TIP]
> **Correct answer: 3. 240**

## Solution

Because five distinct jobs must reach four distinct employees with none empty, exactly one employee receives two jobs and the other three receive one each. Choose the employee receiving two jobs in 4 ways, choose that pair of jobs in C(5,2)=10 ways, and biject the remaining three jobs to the remaining employees in 3!=6 ways. Total=4×10×6=240, option 3.

## Key Points

- An onto assignment of 5 objects to 4 recipients must have occupancy pattern 2,1,1,1.

## Why the other options are incorrect

1024=4^5 counts every unrestricted assignment, including employees with no job. The values 625 and 20 do not account for the onto constraint and all permutations of distinct jobs and employees.
