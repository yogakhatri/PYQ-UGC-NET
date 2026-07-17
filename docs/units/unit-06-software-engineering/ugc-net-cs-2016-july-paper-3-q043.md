# Question 43

*UGC NET CS · 2016 July Paper 3 · Software Quality · Availability from MTBF and MTTR*

A server crashes on the average once in 30 days, that is, the Mean Time Between Failures (MTBF) is 30 days. When this happens, it takes 12 hours to reboot it, that is, the Mean Time to Repair (MTTR) is 12 hours. The availability of server with these reliability data values is approximately :

- **1.** 96.3%
- **2.** 97.3%
- **3.** 98.3%
- **4.** 99.3%

> [!TIP]
> **Correct answer: 3. 98.3%**

## Solution

Use steady-state availability A=MTBF/(MTBF+MTTR) with consistent units. Thirty days is 30×24=720 hours, so A=720/(720+12)=720/732≈0.9836=98.36%. The closest option is 98.3%, option 3.

## Key Points

- Availability = mean uptime/(mean uptime+mean repair time); always convert both values to the same unit.

## Why the other options are incorrect

The other percentages result from failing to convert days to hours, dividing MTTR by MTBF incorrectly, or omitting repair time from the cycle denominator.
