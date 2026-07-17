# Question 5

*UGC NET CS · 2015 Dec Paper 3 · Input-Output Organization · DMA Cycle Stealing*

A DMA controller transfers 32-bit words to memory using cycle Stealing. The words are assembled from a device that transmits characters at a rate of 4800 characters per second. The CPU is fetching and executing instructions at an average rate of one million instructions per second. By how much will the CPU be slowed down because of the DMA transfer ?

- **1.** 0.06%
- **2.** 0.12%
- **3.** 1.2%
- **4.** 2.5%

> [!TIP]
> **Correct answer: 2. 0.12%**

## Solution

Assume an 8-bit character, so four characters form each 32-bit DMA word. At 4,800 characters/s, the DMA controller transfers 4,800/4=1,200 words/s. Cycle stealing takes one memory cycle per word. Relative to 1,000,000 CPU instruction cycles per second, the stolen fraction is 1,200/1,000,000=0.0012=0.12%.

## Key Points

- DMA slowdown under cycle stealing = stolen memory cycles per second ÷ CPU cycles per second.

## Why the other options are incorrect

0.06% halves the required steals; 1.2% misses a factor of ten; 2.5% is far too large. The essential conversion is from characters to 32-bit words before comparing rates.
