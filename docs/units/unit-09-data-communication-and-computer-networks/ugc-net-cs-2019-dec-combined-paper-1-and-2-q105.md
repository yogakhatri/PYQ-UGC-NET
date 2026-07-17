# Question 105

*UGC NET CS · 2019 Dec Paper 1 And 2 · Mobile Technology · Bluetooth Piconets*

A piconet, the basic unit of a Bluetooth system, consists of how many master nodes and up to how many active slave nodes?

- **1.** one, five
- **2.** one, seven
- **3.** Two, eight
- **4.** One, eight

> [!TIP]
> **Correct answer: 2. one, seven**

## Solution

A classic Bluetooth piconet has exactly one device acting as master and can have up to seven active slave devices. Thus at most eight devices are active in one piconet at a time: one master plus seven slaves. The required pair is one, seven—option 2.

## Key Points

- Bluetooth piconet capacity counts one master separately from a maximum of seven active slaves.

## Why the other options are incorrect

Five understates the allowed active-slave count. Two masters contradict the piconet's single-master coordination. Eight active slaves would make nine active devices including the master; additional devices may be parked or inactive, but not simultaneously active slaves in the classic piconet definition.
