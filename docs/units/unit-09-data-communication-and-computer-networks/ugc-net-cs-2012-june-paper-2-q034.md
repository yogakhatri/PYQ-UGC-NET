# Question 34

*UGC NET CS · 2012 June Paper 2 · OSI and TCP/IP Layer Functions · Internet Checksum*

Check sum used along with each packet computes the sum of the data, where data is treated as a sequence of

- **A.** Integer
- **B.** Character
- **C.** Real numbers
- **D.** Bits www.solutionsadda.in

> [!TIP]
> **Correct answer: A. Integer**

## Solution

A packet checksum groups the data bits into fixed-width words and treats each word as an integer. For the Internet checksum, these are 16-bit integers added with one's-complement arithmetic; the complemented sum is transmitted. The receiver repeats the operation to detect corruption.

## Key Points

- Checksums add fixed-width integer words; CRCs instead treat bits as coefficients of a polynomial.

## Why the other options are incorrect

Characters and real numbers are not the general checksum interpretation. Although the words consist of bits, the algorithm does not simply add individual bit values; it adds multi-bit integer words with carry handling.
