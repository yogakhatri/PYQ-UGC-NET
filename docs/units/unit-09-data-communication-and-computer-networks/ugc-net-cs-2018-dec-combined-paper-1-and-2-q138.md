# Question 138

*UGC NET CS · 2018 Dec Paper 1 And 2 · Transport Layer · TCP and UDP Flow and Congestion Control*

Consider S1: TCP handles both congestion and flow control. S2: UDP handles congestion but not flow control. Which is correct?

- **1.** Neither S1 nor S2
- **2.** S1 is false but S2 is true
- **3.** S1 is true but S2 is false
- **4.** Both S1 and S2 are true

> [!TIP]
> **Correct answer: 3. S1 is true but S2 is false**

## Solution

S1 is true. TCP performs receiver flow control with the advertised receive window and network congestion control with mechanisms such as the congestion window, slow start, and congestion avoidance. S2 is false: UDP supplies connectionless datagrams without built-in flow control or congestion control; an application using UDP must add any such behavior itself. Thus S1 is true and S2 is false, option 3.

## Key Points

- TCP has two separate windows/limits: receiver capacity for flow control and network capacity for congestion control; bare UDP has neither.

## Why the other options are incorrect

Options 1 and 2 wrongly reject TCP's two controls. Option 4 wrongly grants UDP native congestion control. Checksums provide corruption detection, not congestion or receiver-flow regulation.
