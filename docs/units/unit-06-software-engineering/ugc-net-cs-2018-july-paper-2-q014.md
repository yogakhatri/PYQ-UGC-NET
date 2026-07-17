# Question 14

*UGC NET CS · 2018 July Paper 2 · Software Reliability · Availability from Downtime*

A software system crashed 20 times in 2017, and each crash took 2 minutes to restart. Approximately what was its availability that year?

- **1.** 96.9924%
- **2.** 97.9924%
- **3.** 98.9924%
- **4.** 99.9924%

> [!TIP]
> **Correct answer: 4. 99.9924%**

## Solution

Total downtime is 20 crashes×2 minutes=40 minutes. A 365-day year contains 365×24×60=525,600 minutes. Availability=(total time−downtime)/total time×100=[1−40/525,600]×100≈99.992389%, which rounds to 99.9924%. Therefore option 4 is correct.

## Key Points

- Availability = uptime/(uptime+downtime) = 1−downtime/total scheduled time.

## Why the other options are incorrect

Options 1–3 imply downtime of roughly 1–3% of the year, far larger than 40 minutes. Availability is not 100 minus the number of crashes; it is the proportion of scheduled time during which service is operational.
