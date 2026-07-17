# Question 47

*UGC NET CS · 2018 July Paper 2 · Network Security · Challenge-Response Authentication*

In Challenge-Response authentication the claimant ________.

- **1.** Proves that she knows the secret without revealing it
- **2.** Proves that she doesn’t know the secret
- **3.** Reveals the secret
- **4.** Gives a challenge

> [!TIP]
> **Correct answer: 1. Proves that she knows the secret without revealing it**

## Solution

In challenge-response authentication, the verifier sends a fresh challenge. The claimant combines that challenge with a secret—typically through a keyed hash, MAC, encryption operation, or signature—and returns the response. A verifier who can check the response gains evidence that the claimant possesses the secret, but the secret itself is not sent. Therefore option 1 is correct.

## Key Points

- Challenge-response proves possession of a secret by answering a fresh unpredictable value without transmitting the secret.

## Why the other options are incorrect

The claimant does not prove ignorance or reveal the secret. The verifier, not the claimant, ordinarily supplies the challenge; the claimant supplies the response. Freshness is important because it prevents an old captured response from being replayed successfully.
