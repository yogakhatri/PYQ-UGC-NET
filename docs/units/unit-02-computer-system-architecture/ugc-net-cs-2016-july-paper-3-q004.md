# Question 4

*UGC NET CS · 2016 July Paper 3 · Input-Output Organization · Interrupt Request Register*

The register that stores all interrupt requests is :

- **1.** Interrupt mask register
- **2.** Interrupt service register
- **3.** Interrupt request register
- **4.** Status register

> [!TIP]
> **Correct answer: 3. Interrupt request register**

## Solution

In an interrupt controller, the Interrupt Request Register (IRR) records pending requests received on the interrupt input lines. It therefore stores the set of interrupt requests waiting to be considered, making option 3 correct.

## Key Points

- IRR=pending requests, IMR=masked requests, ISR=requests currently in service.

## Why the other options are incorrect

The Interrupt Mask Register enables or blocks selected interrupt lines. The In-Service Register records requests currently being serviced. A status register holds general state flags rather than the complete set of pending interrupt requests.
