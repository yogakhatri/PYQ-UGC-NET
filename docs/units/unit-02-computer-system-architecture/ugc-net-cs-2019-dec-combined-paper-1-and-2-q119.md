# Question 119

*UGC NET CS · 2019 Dec Paper 1 And 2 · Digital Codes · Self-Complementing Decimal Codes*

Which binary codes for decimal digits are self-complementing? (a) 8421 code, (b) 2421 code, (c) excess-3 code, (d) excess-3 Gray code.

- **1.** (a) and (b)
- **2.** (b) and (c)
- **3.** (c) and (d)
- **4.** (d) and (a)

> [!TIP]
> **Correct answer: 2. (b) and (c)**

## Solution

A decimal code is self-complementing when bitwise complementing the code word for digit d produces the code word for 9−d. The conventional 2421 code has this property because its weights sum to 9 and its assigned code words are complementary in digit pairs. Excess-3 also has it algebraically: complementing the 4-bit representation of d+3 gives 15−(d+3)=12−d=(9−d)+3, the excess-3 code of 9−d. Therefore (b) and (c) are correct, option 2.

## Key Points

- Self-complementing means ones' complement of code(d) equals code(9−d).

## Why the other options are incorrect

8421 is not self-complementing: complementing 0000 for digit 0 gives 1111, not the 8421 code 1001 for digit 9. Excess-3 Gray does not preserve the required digit-pair complement mapping. Options 1, 3, and 4 each include one of those non-self-complementing choices.
