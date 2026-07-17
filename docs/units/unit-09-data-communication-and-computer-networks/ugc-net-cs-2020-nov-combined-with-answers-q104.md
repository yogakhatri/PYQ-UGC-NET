# Question 104

*UGC NET CS · 2020 Nov With Answers · Network Security · Cryptographic Hash Functions*

Which statements about a hash function are true? (A) It takes a message of arbitrary length and generates a fixed-length code. (B) It takes a fixed-length message and generates a variable-length code. (C) It may give the same hash value for distinct messages.

- **1.** (A) only
- **2.** (B) and (C) only
- **3.** (A) and (C) only
- **4.** (B) only

> [!TIP]
> **Correct answer: 3. (A) and (C) only**

## Solution

A conventional cryptographic hash maps messages of arbitrary finite length to a digest of a fixed length determined by the algorithm, so A is true and B is false. Because infinitely many possible messages are mapped into only finitely many fixed-length digests, the pigeonhole principle guarantees that distinct messages can share a hash value; this is a collision, so C is true. Therefore A and C only, option 3.

## Key Points

- Hashing compresses an unbounded input space into a fixed-size output space, so collisions must exist.

## Why the other options are incorrect

Variable-length output is not the defining hash interface. Collision resistance means finding a collision should be computationally difficult for a secure hash; it cannot mean collisions are mathematically impossible.
