# Question 32

*UGC NET CS · 2015 Dec Paper 2 · Probability · Bayes' Theorem*

Suppose meningitis causes a stiff neck 50% of the time, the proportion of people with meningitis is 1/50,000, and the proportion with a stiff neck is 1/20. Among people who complain of a stiff neck, what percentage have meningitis?

- **1.** 0.01%
- **2.** 0.02%
- **3.** 0.04%
- **4.** 0.05%

> [!TIP]
> **Correct answer: 2. 0.02%**

## Solution

Let M be meningitis and S be stiff neck. Bayes' theorem gives P(M|S)=P(S|M)P(M)/P(S). Substitute 0.5, 1/50,000, and 1/20: P(M|S)=0.5×(1/50,000)÷(1/20)=10/50,000=0.0002. Multiplying by 100 converts this probability to 0.02%.

## Key Points

- Bayes' theorem reverses a condition: P(M|S)=P(S|M)P(M)/P(S).

## Why the other options are incorrect

The alternatives result from mishandling the denominator or percentage conversion. The joint probability P(M∩S)=1/100,000 is not the requested conditional proportion among people with a stiff neck.
