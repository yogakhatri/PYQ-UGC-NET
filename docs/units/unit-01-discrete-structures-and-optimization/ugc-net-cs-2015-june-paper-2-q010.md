# Question 10

*UGC NET CS · 2015 June Paper 2 · Mathematical Logic · Converse and Circular Proof Errors*

The proposition is 'x≥6 if x²≥25.' A proposed proof says: if x≥6, then x²=x·x≥6·6=36≥25. Which comments are correct? (a) It proves the converse. (b) It starts by assuming what is to be shown. (c) The proof is correct.

- **1.** (a) only
- **2.** (c) only
- **3.** (a) and (b)
- **4.** (b) only

> [!TIP]
> **Correct answer: 3. (a) and (b)**

## Solution

The phrase 'x≥6 if x²≥25' means x²≥25→x≥6. The proposed argument assumes x≥6 and derives x²≥25, which is the converse implication. It therefore both proves the wrong direction, making (a) true, and begins by assuming the desired conclusion x≥6, making (b) true. Statement (c) is false. Moreover, the original proposition is itself false over the reals: x=−5 satisfies x²≥25 but not x≥6.

## Key Points

- In 'P if Q,' Q is the antecedent: Q→P.
- Proving P→Q proves the converse, not the original claim.

## Why the other options are incorrect

Option 1 notices only the reversed direction but not the circular starting assumption. Option 4 notices only the assumption. Option 2 calls the proof correct. Option 3 identifies both defects.
