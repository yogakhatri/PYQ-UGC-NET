# Question 97

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Language Design and Translation Issues · Virtual Computers and Binding Times*

S N87047 Which of the following are correct using the constructor? A. string s1; B. string s2 (s1); C. string s3 (7); D. string s4 (a'); E. string s5{7, a'); Choose the most appropriate answer from the options given below:

- **1.** A, D, E only
- **2.** A, B, C only
- **3.** A, B, D only
- **4.** A and B only

> [!TIP]
> **Correct answer: No listed option — A, B, and E are valid C++ string constructions**

## Solution

`string s1;` default-constructs and `string s2(s1);` copy-constructs. A single integer or character in braces does not match a valid `std::string` constructor, so C and D fail. `string s5{7,'a'};` matches the count-and-character constructor and creates seven a characters. The valid set A,B,E is absent.

## Key Points

- The repeated-character string constructor requires both count and character.

## Why the other options are incorrect

Each listed combination either includes invalid C/D or omits valid E.
