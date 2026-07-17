# Question 144

*UGC NET CS · 2020 Nov With Answers · Memory Hierarchy · Disk Rotational Delay*

If the disk platters rotate at 5,400 rpm, approximately what is the maximum rotational delay?

- **1.** 0.011 seconds
- **2.** 0.11 seconds
- **3.** 0.0011 seconds
- **4.** 1.1 seconds

> [!TIP]
> **Correct answer: 1. 0.011 seconds**

## Solution

At 5,400 revolutions per minute, one revolution takes 60/5,400 seconds = 1/90 second ≈0.0111 second. The maximum rotational delay occurs when the desired sector has just passed the head, requiring almost one full revolution. It is therefore approximately 0.011 second, option 1.

## Key Points

- Maximum rotational delay = time for one revolution = 60/rpm seconds.

## Why the other options are incorrect

The other values are displaced by factors of 10 or 100. Also note that average rotational delay would be half a revolution, about 0.0056 second, but the question asks for the maximum.
