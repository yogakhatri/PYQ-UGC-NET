# Question 29

*UGC NET CS · 2017 Nov Paper 2 · OSI and TCP/IP Layer Functions · Transport as the End-to-End Layer*

Which of the following layer of OSI Reference model is also called end-to-end layer ?

- **1.** Network layer
- **2.** Datalink layer
- **3.** Session layer
- **4.** Transport layer

> [!TIP]
> **Correct answer: 4. Transport layer**

## Solution

The transport layer provides logical end-to-end communication between processes on the source and destination hosts. It performs functions such as segmentation/reassembly and, depending on the protocol, reliability, flow control, and multiplexing by port numbers. Therefore option 4 is correct.

## Key Points

- Data link is node-to-node, network is host-to-host, and transport is process-to-process end-to-end delivery.

## Why the other options are incorrect

The data-link layer is hop-to-hop over one link. The network layer delivers packets host-to-host across routers. The session layer manages dialogs above transport. The phrase 'end-to-end layer' conventionally refers to transport because its protocol endpoints are the communicating hosts/processes.
