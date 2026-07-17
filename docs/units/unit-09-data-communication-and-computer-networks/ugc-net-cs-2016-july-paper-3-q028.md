# Question 28

*UGC NET CS · 2016 July Paper 3 · Data Communication · Line Coding, Block Coding, Scrambling and PCM*

Match the following : (a) Line coding (i) A technique to change analog signal to digital data. (b) Block coding (ii) Provides synchronization without increasing number of bits. (c) Scrambling (iii) Process of converting digital data to digital signal. (d) Pulse code modulation (iv) Provides redundancy to ensure synchronization and inherits error detection. Codes : (a) (b) (c) (d)

- **1.** (iv) (iii) (ii) (i)
- **2.** (iii) (iv) (ii) (i)
- **3.** (i) (iii) (ii) (iv)
- **4.** (ii) (i) (iv) (iii)

> [!TIP]
> **Correct answer: 2. (iii) (iv) (ii) (i)**

## Solution

Line coding converts digital data to a digital signal, so (a)→(iii). Block coding adds redundant bits for synchronization and some error detection, so (b)→(iv). Scrambling replaces troublesome long runs without increasing the bit count, so (c)→(ii). PCM samples, quantizes, and encodes an analog signal as digital data, so (d)→(i). This gives (iii),(iv),(ii),(i), option 2.

## Key Points

- PCM: analog→digital data; line coding: digital data→digital signal; block coding adds redundancy; scrambling preserves bit count.

## Why the other options are incorrect

The other codes confuse source conversion with signal encoding or assign redundancy to scrambling. Remember that block coding changes m data bits into n>m coded bits, while scrambling changes bit patterns at the same nominal bit count.
