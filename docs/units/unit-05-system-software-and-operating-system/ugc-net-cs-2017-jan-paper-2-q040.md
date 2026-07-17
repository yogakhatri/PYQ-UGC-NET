# Question 40

*UGC NET CS · 2017 Jan Paper 2 · Distributed Systems · Hardware and Software Coupling*

Distributed operating systems consist of :

- **1.** Loosely coupled O.S. software on a loosely coupled hardware.
- **2.** Loosely coupled O.S. software on a tightly coupled hardware.
- **3.** Tightly coupled O.S. software on a loosely coupled hardware.
- **4.** Tightly coupled O.S. software on a tightly coupled hardware.

> [!TIP]
> **Correct answer: 3. Tightly coupled O.S. software on a loosely coupled hardware.**

## Solution

A distributed operating system runs over loosely coupled hardware: autonomous computers have their own processors and memories and communicate through a network. Its OS software is tightly coordinated to present users and applications with a coherent single-system image. Therefore it is tightly coupled OS software on loosely coupled hardware, option 3.

## Key Points

- Distributed OS: physically separate machines, logically integrated system service.

## Why the other options are incorrect

Loosely coupled software on loosely coupled hardware describes a network operating-system style in which machines remain visibly separate. Tightly coupled hardware characterizes shared-memory multiprocessors rather than the standard distributed-system model.
