# Question 26

*UGC NET CS · 2015 June Paper 2 · Application-Layer Protocols · Session Initiation Protocol*

Which of the following protocols is an application layer protocol that establishes, manages and terminates multimedia sessions ?

- **1.** Session Maintenance Protocol
- **2.** Real - time Streaming Protocol
- **3.** Real - time Transport Control Protocol
- **4.** Session Initiation Protocol

> [!TIP]
> **Correct answer: 4. Session Initiation Protocol**

## Solution

SIP, the Session Initiation Protocol, is an application-layer signaling protocol for creating, modifying, and terminating multimedia sessions such as voice and video calls. It locates participants and negotiates session parameters, while the actual media is normally carried by other protocols. Therefore option 4 matches the wording exactly.

## Key Points

- SIP handles multimedia-session signaling; RTP/RTCP carry and monitor media, while RTSP controls streaming playback.

## Why the other options are incorrect

`Session Maintenance Protocol` is not the standard protocol intended here. RTSP controls playback operations such as play and pause for streaming media, and RTCP reports quality and participant information alongside RTP; neither is the general call/session setup protocol described.
