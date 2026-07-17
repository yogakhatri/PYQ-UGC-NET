# Question 19

*UGC NET CS · 2014 Dec Paper 3 · Language Design and Translation Issues · Call-by-Value and Call-by-Reference*

Consider these statements. S1: In call-by-value, an argument variable is unchanged in the caller's scope when the function returns. S2: In call-by-reference, a function receives an implicit reference to the variable used as argument. S3: In call-by-reference, the caller is unable to see the modified argument variable. Which statements are true?

- **A.** S3 and S2 are true.
- **B.** S3 and S1 are true.
- **C.** S2 and S1 are true.
- **D.** S1, S2, S3 are true.

> [!TIP]
> **Correct answer: C. S2 and S1 are true.**

## Solution

Under call-by-value, the formal parameter receives a copy, so assigning to it does not change the caller's argument variable; S1 is true in the standard model. Under call-by-reference, the formal parameter denotes the caller's variable itself, so the function receives an implicit reference; S2 is true. Consequently, changes through that formal parameter are visible to the caller, making S3 false. Therefore S1 and S2 are the true pair.

## Key Points

- Value passes a copy of the variable's value; reference aliases the caller's variable, so direct modifications are visible after return.

## Why the other options are incorrect

A and B both include the false statement S3. D declares all three true and therefore contains the same contradiction. Option C contains exactly the two standard parameter-passing facts.
