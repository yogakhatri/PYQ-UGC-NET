# Question 106

*UGC NET CS · 2020 Nov With Answers · Regular Languages · Unary and Copy-Language Regularity*

Consider L₁={a^(2^z) | z is an integer and the exponent is a nonnegative integer}, L₂={a^(2z) | z≥0}, and L₃={ww | w∈{a,b}*}. Which languages are regular?

- **1.** L1 and L2 only
- **2.** L1 and L3 only
- **3.** L1 only
- **4.** L2 only

> [!TIP]
> **Correct answer: 4. L2 only**

## Solution

L₂ contains exactly the unary strings of even length: L₂=(aa)*, so it is regular. L₁ has lengths 1,2,4,8,… (powers of two). A unary regular language has an ultimately periodic set of lengths, but the gaps between consecutive powers of two grow without bound, so L₁ is not regular. L₃ is the copy language {ww}; a finite automaton cannot remember an arbitrary first half and compare it with the second, and the language is nonregular. Hence only L₂ is regular, option 4.

## Key Points

- Unary regular languages have eventually periodic lengths; powers of two do not, while even lengths do.

## Why the other options are incorrect

Every other option includes L₁ or L₃. A simple pumping or Myhill–Nerode argument separates both from regular languages, whereas L₂ needs only a two-state parity automaton.
