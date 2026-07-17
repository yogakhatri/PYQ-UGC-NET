# Question 55

*UGC NET CS · 2015 Dec Paper 3 · Windows Operating Systems · UTF-16 Unicode*

The character set used in Windows 2000 operating system is __________.

- **1.** 8 bit ASCII
- **2.** Extended ASCII
- **3.** 16 bit UNICODE
- **4.** 12 bit UNICODE

> [!TIP]
> **Correct answer: 3. 16 bit UNICODE**

## Solution

Windows 2000's native wide-character APIs use Unicode represented as UTF-16 code units. In the terminology used when Windows 2000 was released, this was described as a 16-bit Unicode character set, so option 3 is correct.

## Key Points

- Windows NT-family native text model: Unicode through 16-bit wide-character/UTF-16 code units.

## Why the other options are incorrect

ASCII and extended single-byte code pages cannot directly represent the broad multilingual repertoire targeted by Unicode. Twelve-bit Unicode is not the Windows 2000 representation. Strictly, modern UTF-16 may use a pair of 16-bit code units for supplementary characters, but that does not change the expected historical answer.
