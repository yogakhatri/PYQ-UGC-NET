# Question 25

*UGC NET CS · 2015 June Paper 3 · Switching Techniques · Packet Ordering in Circuit Switching*

Which transmission technique guarantees that data packets will be received by the receiver in the same order in which they were sent by the sender ?

- **1.** Broadcasting
- **2.** Unicasting
- **3.** Packet switching
- **4.** Circuit switching

> [!TIP]
> **Correct answer: 4. Circuit switching**

## Solution

Circuit switching first establishes one dedicated end-to-end path. All bits then traverse that same serial path for the duration of the connection, so later data cannot take a faster alternative route and overtake earlier data. The receiver therefore obtains the stream in sending order.

## Key Points

- A fixed circuit preserves stream order; independent packet routes may reorder arrivals.

## Why the other options are incorrect

Broadcast and unicast describe how many destinations receive data, not ordering. Packet switching may route different packets independently and can deliver them out of order unless a higher-layer protocol such as TCP restores order. Thus packet switching alone supplies no such guarantee.
