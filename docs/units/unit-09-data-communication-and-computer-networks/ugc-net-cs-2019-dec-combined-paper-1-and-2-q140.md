# Question 140

*UGC NET CS · 2019 Dec Paper 1 And 2 · Network Security · DES Structure and Rounds*

The Data Encryption Standard (DES) round function has four steps. Which is their correct order?

- **1.** expansion permutation, S-boxes, XOR operation, straight permutation
- **2.** expansion permutation, XOR operation, S-boxes, straight permutation
- **3.** straight permutation, S-boxes, XOR operation, expansion permutation
- **4.** straight permutation, XOR operation, S-boxes, expansion permutation

> [!TIP]
> **Correct answer: 2. expansion permutation, XOR operation, S-boxes, straight permutation**

## Solution

DES applies its round function f to the 32-bit right half and a 48-bit round key. First, the expansion permutation E expands the 32-bit half-block to 48 bits. Second, that result is XORed with the 48-bit round key. Third, eight S-boxes substitute the eight 6-bit groups with eight 4-bit outputs, returning the data to 32 bits. Fourth, the straight P permutation rearranges those 32 bits to spread each S-box's influence before the Feistel XOR. Hence the order is expansion → XOR → S-boxes → straight permutation, option 2.

## Key Points

- DES round-function mnemonic: E, key XOR, S, P—expand, mix, substitute, permute.

## Why the other options are incorrect

Option 1 places substitution before key mixing, but S-box input must be the expanded data XORed with the round key. Options 3 and 4 begin with a 32-bit straight permutation and put the 32-to-48-bit expansion last, contradicting the required input sizes and DES structure.
