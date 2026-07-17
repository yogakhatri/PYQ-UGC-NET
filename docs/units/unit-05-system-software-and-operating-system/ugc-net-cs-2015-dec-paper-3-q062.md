# Question 62

*UGC NET CS · 2015 Dec Paper 3 · Distributed Systems · Loosely Coupled Hardware and Message Passing*

A distributed system is a collection of (P), and communication in the system is achieved by (Q). Which option correctly identifies P and Q?

- **1.** Loosely coupled hardware on tightly coupled software and disk sharing, respectively.
- **2.** Tightly coupled hardware on loosely coupled software and shared memory, respectively.
- **3.** Tightly coupled software on loosely coupled hardware and message passing, respectively.
- **4.** Loosely coupled software on tightly coupled hardware and file sharing, respectively.

> [!TIP]
> **Correct answer: 3. Tightly coupled software on loosely coupled hardware and message passing, respectively.**

## Solution

A distributed system runs on autonomous computers connected by a network: the hardware is loosely coupled because processors have separate memories and clocks. System software and distributed services coordinate these machines to present a coherent environment, so the software is described as tightly coupled. With no shared physical memory, processes communicate principally by exchanging messages. This gives tightly coupled software on loosely coupled hardware, with message passing.

## Key Points

- Distributed system: loosely coupled machines coordinated by software, communicating through messages.

## Why the other options are incorrect

Options 1, 2, and 4 reverse the characteristic hardware/software coupling or replace the general communication mechanism with disk/file sharing. Shared memory is characteristic of tightly coupled multiprocessors, not the general distributed-system model.
