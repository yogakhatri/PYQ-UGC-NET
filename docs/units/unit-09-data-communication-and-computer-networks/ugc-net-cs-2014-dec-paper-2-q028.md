# Question 28

*UGC NET CS · 2014 Dec Paper 2 · Routing Algorithms · Broadcast Routing*

Which of the following algorithms is not a broadcast routing algorithm ?

- **A.** Flooding
- **B.** Multidestination routing
- **C.** Reverse path forwarding
- **D.** All of the above

> [!TIP]
> **Correct answer: No listed option is correct: flooding, multidestination routing and reverse-path forwarding are all broadcast-routing techniques.**

## Solution

Flooding sends copies over outgoing links with controls such as hop limits. Multidestination routing carries a destination set and lets routers split it among outgoing links. Reverse-path forwarding accepts a broadcast packet only when it arrives on the link that lies on the router's shortest path back to the source, reducing duplicates. All three are standard ways to implement broadcasting, so A–C are not answers and 'all of the above' is also false for a 'not' question.

## Key Points

- Broadcast methods include flooding, multidestination forwarding and reverse-path forwarding.

## Why the other options are incorrect

A, B and C each name a genuine broadcast method. D would assert that all three are not broadcast methods, the opposite of the facts. The item needs a 'none of the above' option to have a correct label.
