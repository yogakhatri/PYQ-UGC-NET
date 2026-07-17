# Question 66

*UGC NET CS · 2015 June Paper 3 · Data Representation and Error Control · Hamming-Code Message and Check Bits*

In a binary Hamming Code the number of check digits is r then number of message digits is equal to :

- **1.** 2^r − 1
- **2.** 2^r − r − 1
- **3.** 2^r − r + 1
- **4.** 2^r + r − 1

> [!TIP]
> **Correct answer: 2. 2^r − r − 1**

## Solution

A full binary Hamming code with r check bits has block length `n = 2^r − 1`, because the r-bit syndrome must identify every one of n bit positions plus the no-error case. Of these n positions, r hold check bits. The number of message bits is therefore `k = n − r = 2^r − r − 1`.

## Key Points

- Perfect Hamming code parameters: `[n,k]=[2^r−1, 2^r−r−1]`.

## Why the other options are incorrect

Option 1 is the total codeword length, not the message length. Options 3 and 4 add check-bit terms instead of subtracting the r parity positions from the block length.
