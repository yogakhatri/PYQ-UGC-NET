# Question 46

*UGC NET CS · 2013 Dec Paper 3 · Data Communication · Satellite Propagation Delay*

A client-server system uses a satellite network, with the satellite at a height of 40,000 kms. What is the best-case delay in response to a request ? (Note that the speed of light in air is 3,00,000 km/second).

- **A.** 133.33 m sec
- **B.** 266.67 m sec
- **C.** 400.00 m sec
- **D.** 533.33 m sec

> [!TIP]
> **Correct answer: D. 533.33 m sec**

## Solution

A request travels from the ground client up 40,000 km to the satellite and down 40,000 km to the ground server: 80,000 km. The response follows the same two-hop route back, so the best-case propagation distance is 4×40,000=160,000 km. Ignoring transmission, processing and queuing delays as best-case assumptions, delay=distance/speed=160,000/300,000 second=0.53333 second=533.33 ms.

## Key Points

- Satellite request-response propagation uses four altitude legs: up, down, up, down.

## Why the other options are incorrect

133.33 ms counts only one ground-to-satellite leg. 266.67 ms counts a one-way client-to-server route through the satellite. 400 ms omits one of the four 40,000 km legs. A response time must include both the request and its reply.
