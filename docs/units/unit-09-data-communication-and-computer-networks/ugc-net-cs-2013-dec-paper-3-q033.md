# Question 33

*UGC NET CS · 2013 Dec Paper 3 · Data Communication · CRC Polynomial Division*

The message 11001001 is to be transmitted using the CRC polynomial x^3+1. What message should be transmitted?

- **A.** 110010011001
- **B.** 11001001
- **C.** 110010011001001
- **D.** 11001001011

> [!TIP]
> **Correct answer: D. 11001001011**

## Solution

The generator polynomial x^3+1 corresponds to the bit pattern 1001 and has degree 3. Append three zeros to the data: 11001001 000. Modulo-2 long division of 11001001000 by 1001 gives remainder 011. Replace the appended zeros with this remainder, producing the transmitted codeword 11001001 011 = 11001001011. At the receiver, dividing that codeword by 1001 gives zero remainder when no error occurred.

## Key Points

- CRC steps: convert the polynomial to bits, append r zeros for degree r, divide with XOR, and append the r-bit remainder.

## Why the other options are incorrect

B sends the original message without a CRC. A and C append bit strings of the wrong construction or length; a degree-3 generator requires exactly three CRC bits, so the transmitted word must contain 8+3=11 bits.
