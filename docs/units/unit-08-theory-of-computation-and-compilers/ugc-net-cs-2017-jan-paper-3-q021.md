# Question 21

*UGC NET CS · 2017 Jan Paper 3 · Closure Properties · Union, Intersection, and Complement*

Given the following statements : (A) A class of languages that is closed under union and complementation has to be closed under intersection. (B) A class of languages that is closed under union and intersection has to be closed under complementation. Which of the following options is correct ?

- **1.** Both (A) and (B) are false.
- **2.** Both (A) and (B) are true.
- **3.** (A) is true, (B) is false.
- **4.** (A) is false, (B) is true.

> [!TIP]
> **Correct answer: 3. (A) is true, (B) is false.**

## Solution

Statement A is true by De Morgan's law: L∩M = complement(complement(L) ∪ complement(M)). Thus closure under union and complement supplies intersection. Statement B is false: closure under union and intersection alone does not create complements. For example, the class of finite languages over an infinite universe is closed under finite union and intersection, but the complement of a finite language is generally infinite and outside the class. Therefore option 3 is correct.

## Key Points

- Union + complement implies intersection by De Morgan; union + intersection does not by itself imply complement.

## Why the other options are incorrect

Option 1 overlooks the De Morgan construction for A. Options 2 and 4 incorrectly treat complementation as a consequence of union and intersection without also assuming a universal language and an operation that can form relative differences.
