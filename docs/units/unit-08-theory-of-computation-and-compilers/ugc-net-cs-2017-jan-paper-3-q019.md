# Question 19

*UGC NET CS · 2017 Jan Paper 3 · Regular Language Models · Non-Regular Unary and Palindrome Languages*

Which of the following are not regular ? (A) Strings of even number of a’s. (B) Strings of a’s, whose length is a prime number. (C) Set of all palindromes made up of a’s and b’s. (D) Strings of a’s whose length is a perfect square.

- **1.** (A) and (B) only
- **2.** (A), (B) and (C) only
- **3.** (B), (C) and (D) only
- **4.** (B) and (D) only

> [!TIP]
> **Correct answer: 3. (B), (C) and (D) only**

## Solution

A is regular because a two-state DFA can track whether the number of a's is even. B is not regular: a finite automaton cannot recognize exactly the unary prime lengths. C, the set of all palindromes over {a,b}, is not regular because recognizing an unbounded first half requires remembering it for comparison with the second half. D is also not regular because the gaps between successive square lengths grow without bound and violate the eventual periodicity of unary regular languages. Hence B, C, and D only are non-regular, which is option 3.

## Key Points

- Unary regular languages have eventually periodic accepted lengths; parity is periodic, but primes and squares are not.

## Why the other options are incorrect

Options 1 and 2 wrongly include A, while option 4 omits the non-regular palindrome language C. Parity is finite-state; primality, arbitrary mirror equality, and perfect-square length are not.
