# Question 1

*UGC NET CS · 2011 Dec Paper 3 · OSI and TCP/IP Layer Functions · Distance-Vector Routing*

(a) Compare and contrast the TCP/IP Stack with the OSI model. W hat factor do you think will affect setting an appropriate TCP time out period be fore the sending host performs a retransmission ? (b) Briefly explain the major difference between Ethernet V2.0 and IEE E 802.3. OR (a) What are the necessary and sufficient conditions for Deadloc k ? Explain in brief each of them. (b) What is a semaphore and how it is used to prevent entry in the critical secti on ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: Both alternatives are explained below**

## Solution

**Alternative A — Networks**

**TCP/IP and OSI:** OSI is a seven-layer reference model: Physical, Data Link, Network, Transport, Session, Presentation and Application. TCP/IP is the deployed Internet architecture, commonly shown with four layers: Link/Network Access, Internet, Transport and Application. TCP/IP's Link layer covers OSI Physical and Data Link; Internet corresponds to Network; Transport corresponds closely to Transport; and TCP/IP Application absorbs OSI Session, Presentation and Application. OSI clearly separates services, interfaces and protocols; TCP/IP grew around working protocols such as IP, TCP, UDP, HTTP and DNS and has looser boundaries.

**TCP retransmission timeout:** The timeout must exceed the expected round-trip time but remain short enough to recover promptly from loss. TCP estimates a smoothed RTT and its variation and forms an RTO approximately as SRTT + 4xRTTVAR, subject to implementation limits. Important influences are propagation distance, transmission rate, queueing and congestion, route changes, receiver delayed acknowledgements, RTT jitter and clock granularity. Samples from retransmitted segments are ambiguous and are normally excluded (Karn's rule); repeated timeout causes exponential backoff.

**Ethernet II versus IEEE 802.3:** Both use destination and source MAC addresses and essentially the same physical Ethernet frame sizes. The two-byte field after the source address is the distinction. Ethernet II interprets it as an EtherType identifying the upper-layer protocol. IEEE 802.3 interprets it as payload Length and identifies the upper-layer protocol through an IEEE 802.2 LLC header, optionally SNAP. Values at most 1500 indicate length; values at least 1536 are used as EtherTypes.

**Alternative B — Deadlock and semaphores**

Deadlock can occur only when all four Coffman conditions hold simultaneously: (1) mutual exclusion—a resource has one user at a time; (2) hold and wait—a process holds resources while requesting more; (3) no preemption—resources cannot be forcibly taken; and (4) circular wait—a cycle of processes exists, each waiting for a resource held by the next. Breaking any one prevents deadlock.

A semaphore is an atomic synchronization variable changed only through wait/P and signal/V. For a critical section, initialize a binary semaphore mutex=1. Each process executes wait(mutex); critical section; signal(mutex). wait atomically changes 1 to 0 or blocks the caller; signal restores availability and wakes a waiter. The signal must execute on every exit path, ideally with structured cleanup.

## Key Points

- TCP/IP maps practical Internet protocols onto fewer layers; TCP RTO adapts to RTT and variance; Ethernet II uses EtherType while 802.3 uses Length plus LLC; deadlock needs all four Coffman conditions; a binary semaphore enforces mutual exclusion.

## Common mistakes to avoid

Do not map TCP/IP Application only to OSI Application; it also absorbs Session and Presentation. Do not set TCP's timeout to a fixed RTT without variance and backoff. For deadlock, listing three conditions is insufficient, and a semaphore is safe only when wait/signal are atomic and signal cannot be skipped.
