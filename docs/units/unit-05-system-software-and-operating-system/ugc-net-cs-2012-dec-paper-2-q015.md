# Question 15

*UGC NET CS · 2012 Dec Paper 2 · Windows Operating Systems · UTF-16 Unicode*

What is the size of a Unicode character in the Windows operating system?

- **1.** 8 bits
- **2.** 16 bits
- **3.** 32 bits
- **4.** 64 bits

> [!TIP]
> **Correct answer: 2. 16 bits**

## Solution

Windows historically defines its wide-character APIs and wchar_t representation around 16-bit UTF-16 code units. Therefore the intended answer to this exam-era question is 16 bits per Windows Unicode character/code unit.

## Key Points

- For Windows API questions, remember UTF-16: one wchar_t/code unit is 16 bits, while some Unicode code points require two such units.

## Why the other options are incorrect

8 bits is the width of a byte and is insufficient for a UTF-16 code unit. 32 bits corresponds to UTF-32 or to a full supplementary Unicode code point represented as two UTF-16 code units, not one Windows wide code unit. 64 bits is not a standard Unicode encoding unit. Strictly, a supplementary character uses a surrogate pair totaling 32 bits, so 'character' here should be read as code unit.
