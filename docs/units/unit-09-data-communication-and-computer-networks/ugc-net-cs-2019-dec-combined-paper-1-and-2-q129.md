# Question 129

*UGC NET CS · 2019 Dec Paper 1 And 2 · Network Security · Confidentiality, Integrity and Authentication*

Consider the following statements with respect to network security: (a) Message confidentiality means that the sender and the receiver expect privacy. (b) Message integrity means that the data must arrive at the receiver exactly as they were sent. (c) Message authentication means the receiver is ensured that the message is coming from the intended sender. Which of the statements is (are) correct?

- **1.** Only (a) and (b)
- **2.** Only (a) and (c)
- **3.** Only (b) and (c)
- **4.** (a), (b) and (c)

> [!TIP]
> **Correct answer: 4. (a), (b) and (c)**

## Solution

All three statements express core security services. Confidentiality prevents unauthorized disclosure, so the communicating parties can expect the message contents to remain private. Integrity assures that data has not been altered, inserted, deleted, or reordered without detection; in the question's wording, it arrives as sent. Authentication gives the receiver confidence about the claimed origin of the message—often called data-origin authentication. These properties answer different questions: who may read it, whether it changed, and who sent it. Since (a), (b), and (c) are all correct, the answer is option 4.

## Key Points

- Confidentiality protects secrecy, integrity protects correctness, and authentication verifies origin or identity.

## Why the other options are incorrect

Options 1–3 each omit one valid security property. Confidentiality alone does not detect modification, integrity alone does not establish identity, and authentication alone does not keep content secret; all three definitions remain correct.
