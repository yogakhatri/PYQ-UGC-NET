# Question 15

*UGC NET CS · 2021 Nov With Answers · Software Reliability · Availability, MTBF and Repair Time*

A system has a 99.99% availability goal and a mean time between failures of one day. Approximately how quickly must it repair itself to reach this availability?

- **1.** ~9 Seconds
- **2.** ~10 Seconds
- **3.** ~11 Seconds
- **4.** ~12 Seconds

> [!TIP]
> **Correct answer: 1. ~9 Seconds**

## Solution

Use availability A=MTBF/(MTBF+MTTR). Solving gives MTTR=MTBF(1−A)/A. With MTBF=1 day=86,400 seconds and A=0.9999, MTTR=86,400×0.0001/0.9999≈8.64 seconds. The nearest choice is approximately 9 seconds, option 1.

## Key Points

- Rearrange A=uptime/(uptime+downtime); four nines leaves about 8.6 seconds of downtime per day.

## Why the other options are incorrect

The other choices are farther from 8.64 seconds. A useful mental check is that 99.99% availability permits only 0.01% downtime, roughly 8.64 seconds per day.
