# Question 27

*UGC NET CS · 2014 Dec Paper 2 · Network Layer · Classful IPv4 Address Prefixes*

In a classful addressing, first four bits in Class A IP address is

- **A.** 1010
- **B.** 1100
- **C.** 1011
- **D.** 1110

> [!TIP]
> **Correct answer: No listed option is correct. A class-A IPv4 address has only its first bit fixed to 0; its first four bits can be any pattern from 0000 through 0111.**

## Solution

In historical classful addressing, Class A is recognized by leading bit 0, Class B by 10, Class C by 110, Class D by 1110 and Class E by 1111. The question asks for four Class-A bits even though only one is fixed. All four offered patterns start with 1, so none can denote a Class-A address. Option D, 1110, would be the fixed four-bit prefix for Class D, suggesting a likely source typo.

## Key Points

- Classful prefixes are variable length: A=0, B=10, C=110, D=1110, E=1111.

## Why the other options are incorrect

1010 and 1011 begin with 10 and therefore fall under Class B prefixes. 1100 begins with 110 and is Class C. 1110 is Class D. No option starts with 0.
