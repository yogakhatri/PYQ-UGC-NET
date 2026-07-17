# Question 58

*UGC NET CS · 2016 July Paper 3 · Data Communication · Channel Capacity and Mutual Information*

Consider a discrete memoryless channel and assume that H(x) is the amount of information per symbol at the input of the channel; H(y) is the amount of information per symbol at the output of the channel; H(x|y) is the amount of uncertainty remaining on x knowing y; and I (x; y) is the information transmission. Which of the following does not define the channel capacity of a discrete memoryless channel ?

- **1.** max over p(x) of I(x; y)
- **2.** max over p(x) of [H(y) − H(y|x)]
- **3.** max over p(x) of [H(x) − H(x|y)]
- **4.** max over p(x) of H(x|y)

> [!TIP]
> **Correct answer: 4. max over p(x) of H(x|y)**

## Solution

The capacity of a discrete memoryless channel is C = max over input distributions p(x) of I(X;Y). Mutual information has the equivalent identities I(X;Y) = H(Y) − H(Y|X) and I(X;Y) = H(X) − H(X|Y). Therefore options 1, 2, and 3 all express channel capacity after maximization over p(x). Option 4 maximizes only H(X|Y), the uncertainty about the input that remains after observing the output, so it does not define capacity.

## Key Points

- Memorize the identity I(X;Y) = H(X) − H(X|Y) = H(Y) − H(Y|X); channel capacity maximizes this mutual information over p(x).

## Why the other options are incorrect

Options 2 and 3 may look different, but they are the two standard entropy forms of mutual information. Capacity rewards transmitted information; maximizing residual uncertainty H(X|Y) would instead favor ambiguity at the receiver.
