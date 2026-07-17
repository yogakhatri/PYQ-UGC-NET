# Question 115

*UGC NET CS · 2020 Nov With Answers · Input-Output Organization · Programmed, Interrupt and Handshaking I/O*

Match: (A) handshaking, (B) programmed I/O, (C) interrupt-initiated I/O, (D) I/O processor with (I) the I/O interface informs the CPU that the device is ready, (II) two control signals work in opposite directions, (III) has local memory and controls many I/O devices, (IV) requires the CPU to check the I/O flag and perform the transfer.

- **1.** A-I, B-II, C-III, D-IV
- **2.** A-II, B-IV, C-III, D-I
- **3.** A-II, B-IV, C-I, D-III
- **4.** A-IV, B-III, C-II, D-I

> [!TIP]
> **Correct answer: 3. A-II, B-IV, C-I, D-III**

## Solution

Asynchronous handshaking coordinates sender and receiver with request/data-valid and acknowledgement signals travelling in opposite directions, so A→II. In programmed I/O, the CPU repeatedly checks the status flag and performs the transfer itself, so B→IV. In interrupt-initiated I/O, the interface signals the CPU when service is needed, so C→I. An I/O processor has its own control and local storage to manage many devices, so D→III. This is option 3.

## Key Points

- Polling keeps the CPU checking; interrupts notify it; an I/O processor offloads control; handshaking uses two-way control signals.

## Why the other options are incorrect

The other mappings confuse polling with interrupts or assign the autonomous I/O-processor description to a basic interface. The CPU’s role distinguishes programmed, interrupt-driven, and processor-controlled I/O.
