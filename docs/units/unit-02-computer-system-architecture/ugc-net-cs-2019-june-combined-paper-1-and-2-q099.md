# Question 99

*UGC NET CS · 2019 June Paper 1 And 2 · Memory Hierarchy · Address-bus width*

A processor can support a maximum memory of 4 GB where memory is word addressable and a word is 2 bytes. What will be the size of the address bus of the processor?

- **1.** At least 28 bits
- **2.** At least 2 bytes
- **3.** At least 31 bits
- **4.** Minimum 4 bytes Single Line Ouestion Option: No Option Orientation: Vertic

> [!TIP]
> **Correct answer: 3. At least 31 bits**

## Solution

The maximum memory is 4 GB=2^32 bytes. Because memory is word-addressable with two bytes per word, the number of distinct word addresses is 2^32/2=2^31. Selecting one of 2^31 addresses requires at least 31 address bits.

## Key Points

- For word-addressable memory, divide byte capacity by bytes per word before taking log2 to find address bits.

## Why the other options are incorrect

- **Option 1:** 28 bits address only 2^28 words.
- **Option 2:** two bytes provide only 16 address bits.
- **Option 4:** four bytes means 32 bits, which would work but is not the minimum required by the question.
