# Question 5

*UGC NET CS · 2010 June Paper 2 · Pipeline and Vector Processing · Parallel Processing*

Four your ATM debit card, you have a 4-decimal-digit personal secret code. In the absence of any clue, a brute-force attack takes time-‘t’ to crack the code on an ATM terminal. Therefore ‘t’ is the secure-time for a customer to report in case the card is misplaced. Your Bank has decided to facilitate an increased secure-time. Out of the following, which option should provide the largest rise in the value of ‘t’ ?

- **A.** Instead of 4-decimal-digits, maintain the personal secret code in 4-hexadecimal-digits.
- **B.** Instead of 4-decimal digits, maintain a 5-decimal-digit personal secret code.
- **C.** Reduce the processing speed of the ATM terminals to the half of their current speed.
- **D.** None of the above provides any improvement.

> [!TIP]
> **Correct answer: B. Instead of 4-decimal digits, maintain a 5-decimal-digit personal secret code.**

## Solution

A four-decimal PIN has 10^4=10,000 possibilities. Four hexadecimal digits give 16^4=65,536 possibilities, a 6.5536× rise. Five decimal digits give 10^5=100,000 possibilities, a 10× rise. Halving terminal speed only doubles attack time. Therefore the five-decimal-digit PIN gives the largest increase.

## Key Points

- Brute-force time is proportional to keyspace size divided by trial rate.

## Why the other options are incorrect

Option A improves security less than B, option C only doubles time, and D is false because all three proposed changes affect brute-force time.
