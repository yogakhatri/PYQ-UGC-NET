# Question 60

*UGC NET CS · 2018 Dec Paper 1 And 2 · Data Representation · Two's-Complement Subtraction*

In computers, subtraction is generally carried out by:

- **1.** 9's complement
- **2.** 1's complement
- **3.** 10's complement
- **4.** 2's complement

> [!TIP]
> **Correct answer: 4. 2's complement**

## Solution

Digital computers normally perform subtraction A−B by adding A to the two's complement of B. The complementing circuit inverts every bit of B and injects the required +1 through the adder's carry input, allowing the same binary adder to perform both addition and subtraction. Therefore option 4, two's complement, is correct.

## Key Points

- Binary subtraction is implemented as A−B=A+(two's complement of B).

## Why the other options are incorrect

One's complement inversion alone omits the +1 and would require end-around-carry handling. Nine's and ten's complements are decimal arithmetic methods, not the standard binary adder method described here.
