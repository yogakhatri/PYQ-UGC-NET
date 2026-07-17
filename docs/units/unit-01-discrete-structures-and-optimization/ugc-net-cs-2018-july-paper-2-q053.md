# Question 53

*UGC NET CS · 2018 July Paper 2 · Counting, Mathematical Induction and Discrete Probability · Poisson Arrival Distribution*

In a multi-user operating system, 30 requests are made to use a particul ar resource per hour, on an average. The probability that no requests are made in 40 minutes, when arr ival pattern is a poisson distribution, is _________.

- **1.** e−15
- **2.** 1−e−15
- **3.** 1−e−20
- **4.** e−20

> [!TIP]
> **Correct answer: 4. e−20**

## Solution

The mean arrival rate is 30 requests per hour. Forty minutes is 2/3 hour, so the Poisson mean for that interval is λ=30×(2/3)=20. For a Poisson random variable, P(N=0)=e^(−λ)λ⁰/0!=e^(−λ). Thus the probability is e^(−20), option 4.

## Key Points

- For Poisson arrivals, scale λ to the requested time interval; zero events has probability e^(−λ).

## Why the other options are incorrect

e^(−15) would correspond to a 30-minute interval, not 40 minutes. The expressions 1−e^(−15) and 1−e^(−20) are probabilities of at least one arrival for those respective means, whereas the question asks for no arrivals.
