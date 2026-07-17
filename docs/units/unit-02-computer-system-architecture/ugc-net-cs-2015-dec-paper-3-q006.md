# Question 6

*UGC NET CS · 2015 Dec Paper 3 · Input-Output Organization · Interrupt Recognition and Service*

A CPU handles interrupt by executing interrupt service subroutine __________.

- **1.** by checking interrupt register after execution of each instruction
- **2.** by checking interrupt register at the end of the fetch cycle
- **3.** whenever an interrupt is registered
- **4.** by checking the interrupt register at regular time intervals

> [!TIP]
> **Correct answer: 1. by checking interrupt register after execution of each instruction**

## Solution

A CPU normally recognizes maskable interrupts at an instruction boundary. After completing the current instruction, it samples the interrupt request/status, saves the necessary state, and branches to the interrupt service routine. Thus checking after each instruction is the best description.

## Key Points

- Interrupts are normally accepted between instructions so architectural state remains precise.

## Why the other options are incorrect

Checking at the end of the fetch cycle could interrupt a partly executed instruction. The CPU does not branch at an arbitrary instant merely because a request arrives, and periodic-time polling is a different mechanism.
