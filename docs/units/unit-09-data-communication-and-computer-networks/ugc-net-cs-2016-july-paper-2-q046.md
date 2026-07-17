# Question 46

*UGC NET CS · 2016 July Paper 2 · Network Security · Replay versus Man-in-the-Middle Attacks*

An attacker sits between customer and Banker, and captures the information from the customer and retransmits to the banker by altering the information. This attack is called as ______.

- **1.** Masquerade Attack
- **2.** Replay Attack
- **3.** Passive Attack
- **4.** Denial of Service Attack

> [!TIP]
> **Correct answer: 2. Replay Attack**

## Solution

The intended clue is that the attacker captures a transmitted message and later retransmits it to obtain an unauthorized effect. That is the defining pattern of a replay attack, so the exam answer is option 2.

## Key Points

- Replay = capture and subsequent retransmission; interception plus live alteration = man-in-the-middle/message modification.

## Why the other options are incorrect

A masquerade attack centers on using a false identity, a passive attack only observes and does not alter or retransmit traffic, and denial of service attacks availability. However, the phrase 'sits between' and 'altering the information' technically describes active message modification or a man-in-the-middle attack, which the choices omit.

## Additional Information

Treat option 2 as the intended PYQ answer, but remember the terminology distinction for concept questions: replay normally reuses a captured message, whereas a man-in-the-middle attacker intercepts and selectively changes messages in transit.

## References

- [NIST replay attack definition](https://csrc.nist.gov/glossary/term/replay_attack)
- [NIST man-in-the-middle definition](https://csrc.nist.gov/glossary/term/man_in_the_middle_attack)
