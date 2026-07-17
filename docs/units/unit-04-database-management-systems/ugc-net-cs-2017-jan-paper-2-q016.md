# Question 16

*UGC NET CS · 2017 Jan Paper 2 · SQL Data Types · CHAR versus VARCHAR Storage*

An attribute A of datatype varchar (20) has value ‘Ram’ and the attribute B of datatype char (20) has value ‘Sita’ in oracle. The attribute A has _______ memory spaces and B has _______ memory spaces.

- **1.** 20, 20
- **2.** 3, 20
- **3.** 3, 4
- **4.** 20, 4

> [!TIP]
> **Correct answer: 2. 3, 20**

## Solution

Under the question's single-byte-character convention, VARCHAR(20) stores only the characters actually present, up to a maximum of 20. 'Ram' therefore occupies 3 character spaces. CHAR(20) is fixed-width and blank-pads 'Sita' from length 4 to length 20, so it occupies 20 character spaces. The pair is 3,20, which is option 2.

## Key Points

- CHAR(n) is fixed and padded; VARCHAR(n) is variable and stores the actual value length up to n.

## Why the other options are incorrect

Options assigning 20 to A treat variable-width VARCHAR as fixed-width. Options assigning 4 to B ignore CHAR padding. The declared size is a maximum for VARCHAR but the fixed stored width for CHAR in the simplified model.

## Additional Information

Real Oracle storage includes length metadata and may use multiple bytes per character depending on the character set. The MCQ uses the usual one-character/one-byte teaching model and asks only for the value-space comparison.
