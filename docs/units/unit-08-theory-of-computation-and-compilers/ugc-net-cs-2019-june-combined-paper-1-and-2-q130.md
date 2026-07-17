# Question 130

*UGC NET CS · 2019 June Paper 1 And 2 · Turing Machines · Recursive and Recursively Enumerable Languages*

A language L contained in Sigma* is recursive if there exists a Turing machine M satisfying which condition for every string omega?

- **1.** If omega is in L, M accepts omega and does not halt
- **2.** If omega is not in L, M accepts omega and halts in a final state
- **3.** If omega is in L, M halts without reaching an accepting state
- **4.** If omega is not in L, M halts without reaching an accepting state

> [!TIP]
> **Correct answer: 4. If omega is not in L, M halts without reaching an accepting state**

## Solution

A recursive language has a decider: a Turing machine that halts on every input, accepting members and rejecting non-members. Therefore, when omega is not in L, M must halt without reaching an accepting state, exactly as option 4 states. The guaranteed halt on both yes and no instances is what distinguishes a decider from a mere recognizer.

## Key Points

- Recursive means decidable: halt and accept on members; halt and reject on non-members.

## Why the other options are incorrect

Option 1 does not halt, contradicting the definition of a decider. Option 2 accepts a non-member. Option 3 rejects a member. Only option 4 gives the required behaviour for a non-member.
