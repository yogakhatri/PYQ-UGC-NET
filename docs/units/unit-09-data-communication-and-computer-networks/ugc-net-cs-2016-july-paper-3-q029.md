# Question 29

*UGC NET CS · 2016 July Paper 3 · Data Communication · Text-Transfer Bit-Rate Calculation*

Assume that we need to download text documents at the rate of 100 pages per minute. A page is an average of 24 lines with 80 characters in each line and each character requires 8 bits. Then the required bit rate of the channel is _____.

- **1.** 1.636 Kbps
- **2.** 1.636 Mbps
- **3.** 3.272 Mbps
- **4.** 3.272 Kbps

> [!TIP]
> **Correct answer: No listed option — the stated rate requires 25.6 Kbps**

## Solution

One page contains 24×80×8=15,360 bits. At 100 pages per minute, the data rate is 1,536,000 bits/min. Bit rate must be expressed per second, so divide by 60: 1,536,000/60=25,600 bit/s=25.6 Kbps. None of the four options matches.

## Key Points

- Preserve units through the calculation: bits/page × pages/min ÷ 60 = bits/s.

## Why the other options are incorrect

1.636 Kbps and 3.272 Kbps are far too small; the Mbps choices incorrectly treat a per-minute total as a per-second rate. If the source had said 100 pages per second, the result would be 1.536 Mbps—not the printed 1.636 Mbps—showing that both the time unit and a digit in the choices are defective.

## Additional Information

Some keys select option 2 by silently changing 'per minute' to 'per second' and approximating or mistyping 1.536 as 1.636. That is not valid for the question as printed.
