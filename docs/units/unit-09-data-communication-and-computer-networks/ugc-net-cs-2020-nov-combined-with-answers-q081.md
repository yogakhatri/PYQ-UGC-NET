# Question 81

*UGC NET CS · 2020 Nov With Answers · Data Communication and Computer Networks · Minimum-Distance Decoding*

Consider a code with only four valid codewords: 0000000000, 0000011111, 1111100000, and 1111111111. This code has minimum distance 5. If the received word is 0000000111, then the original codeword must be

- **1.** 0000011111
- **2.** 0000000000
- **3.** 1111100000
- **4.** 1111111111

> [!TIP]
> **Correct answer: 1. 0000011111**

## Solution

Minimum-distance decoding chooses the valid codeword with the fewest bit disagreements with the received word r=0000000111. Compare r with the four candidates: d(r,0000000000)=3, d(r,0000011111)=2, d(r,1111100000)=8, and d(r,1111111111)=7. The unique nearest codeword is therefore 0000011111, option 1. The stated minimum distance 5 also means the code can correct up to floor((5−1)/2)=2 errors, exactly the distance found here.

## Key Points

- For a block code, compute the Hamming distance to every valid codeword and select the unique minimum.

## Why the other options are incorrect

0000000000 is three bits away, so it is not the nearest valid word. The two codewords beginning with five 1s are seven or eight bits away. Decoding is based on distance from the received word, not merely on sharing a long prefix.
