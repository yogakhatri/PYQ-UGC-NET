# Question 106

*UGC NET CS · 2019 June Paper 1 And 2 · Software Quality · Web-application integrity risk*

A Web application and its support environment has not been fully fortified against attack. Web engineers estimate that the likelihood of repelling an attack is only 30 percent. The application does not contain sensitive or controversial information, so the threat probability is 25 percent. What is the integrity of the web application?

- **1.** 0.625
- **2.** 0.725
- **3.** 0.775
- **4.** 0.825

> [!TIP]
> **Correct answer: 4. 0.825**

## Solution

The probability that an attack both occurs and defeats the defences is threat probability × failure-to-repel probability. The threat probability is 0.25 and the failure-to-repel probability is 1-0.30=0.70. Thus compromise probability is 0.25×0.70=0.175, and integrity is 1-0.175=0.825.

## Key Points

- Integrity here is 1-[threat probability × (1-probability of repelling the attack)].

## Why the other options are incorrect

The other values do not correctly combine the chance of an attack with the conditional chance that the attack succeeds.
