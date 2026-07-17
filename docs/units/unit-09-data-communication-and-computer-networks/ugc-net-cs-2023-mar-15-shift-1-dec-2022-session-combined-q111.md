# Question 111

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · OSI and TCP/IP Layer Functions · Error Detection and Correction*

Consider a computer network using the distance vector routing algorithm in its network layer. The Objective is to find the shortest cost path from router R to routers Pand Q. Assume that R does not initially know the shortest routes toP and Q. Assume that R has three neighboring routers, namely: X, Y and Z. During one iteration R measures its distance as 3, 2, and 5 from its neighbors X, Y and Z, respectively. Router R getting routing vectors from its neighbors that indicates a distance of 7,6 and 5 from router X, Y and Z to router P, respectively. The routing vector also indicates that the distance to router Q from Routers X, Y and Zare 4, 6, 8 respectively. Which of the following statements is/are Ture with respect to the new routing table at router R after updation during this iteration. A. The distance from R to P will be stored as 10 B. The distance from R to Q will be stored as 7 C. The next hop router for a packet from R to P is Y D. The next hop router for a packet from R to Q is Z Choose the correct answer from the options given below:

- **1.** B and C only
- **2.** A and Conly
- **3.** C and D only
- **4.** B and D only

> [!TIP]
> **Correct answer: 1. B and C only**

## Solution

For P, routes through X,Y,Z cost 3+7=10, 2+6=8, 5+5=10, so R stores 8 via Y: C true, A false. For Q the costs are 3+4=7, 2+6=8, 5+8=13, so R stores 7 via X: B true, D false. Thus B and C.

## Key Points

- Distance-vector update takes min_neighbor[cost to neighbor + neighbor's advertised cost].

## Why the other options are incorrect

The alternatives use nonminimum costs or the wrong next hop.
