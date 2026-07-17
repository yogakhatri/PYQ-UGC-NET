# Question 119

*UGC NET CS · 2019 June Paper 1 And 2 · Graph Algorithms · Maximum Flow*

Consider the following properties for a flow network G=(V,E), where a flow is a real-valued function f:VxV->R. P1: For all u,v in V, f(u,v)=-f(v,u). P2: The sum over all v in V of f(u,v) equals 0, for all u in V. Which is/are correct?

- **1.** Only P1
- **2.** Only P2
- **3.** Both P1 and P2
- **4.** Neither P1 nor P2

> [!TIP]
> **Correct answer: 1. Only P1**

## Solution

P1 is the skew-symmetry convention for flows: recording net flow on ordered pairs gives f(u,v)=-f(v,u). P2 is not valid for every vertex. Flow conservation makes the net sum zero only at intermediate vertices; the source has positive net outflow and the sink has equal net inflow. Because P2 quantifies over all u in V, including source and sink, it is false. Hence only P1 is correct.

## Key Points

- Flow conservation excludes source and sink; skew symmetry applies to every ordered vertex pair in the net-flow representation.

## Why the other options are incorrect

Options 2 and 3 accept the overbroad conservation claim. Option 4 also rejects the valid skew-symmetry property.
