# Question 49

*UGC NET CS · 2015 Dec Paper 3 · Discrete Probability · Conditional Entropy of a Binary Symmetric Channel*

Consider a binary symmetric channel with input alphabet X={0,1}, uniform input probabilities P(X=0)=P(X=1)=1/2, and transition matrix [[1−p,p],[p,1−p]], where p is the crossover probability. What is the conditional entropy H(Y|X)?

- **1.** 1
- **2.** −p log₂(p) − (1−p) log₂(1−p)
- **3.** 1 + p log₂(p) + (1−p) log₂(1−p)
- **4.** 0

> [!TIP]
> **Correct answer: 2. −p log₂(p) − (1−p) log₂(1−p)**

## Solution

For either input bit x, a binary symmetric channel outputs x with probability 1−p and flips it with probability p. Hence H(Y|X=x)=−(1−p)log₂(1−p)−p log₂p. Both input rows have the same entropy, so averaging over the uniform input leaves H(Y|X)=h₂(p)=−p log₂p−(1−p)log₂(1−p), which is option 2.

## Key Points

- A BSC's conditional entropy is the binary-entropy function h₂(p); its mutual information for uniform input is 1−h₂(p).

## Why the other options are incorrect

Option 1 is obtained only at p=1/2, when the channel output is maximally uncertain given the input. Option 4 occurs only at p=0 or p=1, when the output is determined by the input. With a uniform input, option 3 equals 1−h₂(p), which is the mutual information I(X;Y), not the conditional entropy.
