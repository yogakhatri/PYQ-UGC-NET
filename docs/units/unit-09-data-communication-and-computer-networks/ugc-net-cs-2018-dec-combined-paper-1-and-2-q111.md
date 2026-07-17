# Question 111

*UGC NET CS · 2018 Dec Paper 1 And 2 · Network Security · Symmetric-Cipher Key Lengths*

Match the secret-key algorithms in List I with the key lengths in List II. List I: (a) Blowfish, (b) DES, (c) IDEA, (d) RC5. List II: (i) 128–256 bits, (ii) 128 bits, (iii) 1–448 bits, (iv) 56 bits.

- **1.** (a)-(iv), (b)-(iii), (c)-(ii), (d)-(i)
- **2.** (a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)
- **3.** (a)-(iii), (b)-(iv), (c)-(ii), (d)-(i)
- **4.** (a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)

> [!TIP]
> **Correct answer: 3. (a)-(iii), (b)-(iv), (c)-(ii), (d)-(i)**

## Solution

The intended matches are Blowfish→(iii), DES→(iv), IDEA→(ii), and RC5→(i). DES has a 56-bit effective key, and IDEA uses a 128-bit key. Blowfish is the variable-length cipher in the list extending up to 448 bits, while the question associates RC5 with the remaining 128–256-bit range. This gives (a)-(iii), (b)-(iv), (c)-(ii), (d)-(i), option 3. Technical caveat: the printed ranges are simplified and not exact specifications—Blowfish is normally specified as 32–448 bits, not 1–448, and RC5 itself permits a much wider variable key length, with common choices/recommendations such as 128 bits.

## Key Points

- Use the fixed anchors first: DES=56 bits and IDEA=128 bits; then flag any printed variable-key ranges that simplify the actual algorithm specifications.

## Why the other options are incorrect

Options 1 and 4 assign DES something other than its distinctive 56-bit effective key. Option 2 gives IDEA the 128–256-bit range instead of its fixed 128-bit key. Those two unambiguous anchors leave only option 3, despite the table's loose ranges for Blowfish and RC5.

## References

- [Bruce Schneier — The Blowfish Encryption Algorithm](https://www.schneier.com/academic/blowfish/)
- [IETF RFC 2040 — RC5 Algorithms and Key-Length Parameter](https://datatracker.ietf.org/doc/html/rfc2040)
