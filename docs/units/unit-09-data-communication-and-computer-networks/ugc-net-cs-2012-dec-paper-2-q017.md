# Question 17

*UGC NET CS · 2012 Dec Paper 2 · OSI and TCP/IP Layer Functions · Data-Link Framing*

A design issue of the data-link layer in the OSI reference model is:

- **1.** Framing
- **2.** Representation of bits
- **3.** Synchronization of bits
- **4.** Connection control

> [!TIP]
> **Correct answer: 1. Framing**

## Solution

The data-link layer groups the physical layer's raw bit stream into identifiable frames. It also commonly handles link-level addressing, error control, flow control and medium access. Therefore framing is a central data-link design issue.

## Key Points

- Layer cue: physical layer handles bits; data-link layer packages those bits into frames.

## Why the other options are incorrect

Representation and synchronization of individual bits are physical-layer concerns: they deal with signals, encoding and clocking. Connection control is normally associated with establishing and managing end-to-end transport connections in this layer-oriented comparison, not with the defining data-link task asked here.
