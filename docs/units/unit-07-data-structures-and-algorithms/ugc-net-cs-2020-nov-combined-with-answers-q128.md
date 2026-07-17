# Question 128

*UGC NET CS · 2020 Nov With Answers · Graph Algorithms · Minimum Spanning Trees*

Consider the undirected weighted graph with edges a-b(4), a-h(8), b-h(11), b-c(8), h-i(7), h-g(1), i-c(2), i-g(6), g-f(2), c-f(4), c-d(7), d-f(14), d-e(9), and f-e(10). Using Prim's algorithm to construct a minimum spanning tree starting at vertex a, which sequence is a possible order in which the edges are added?

- **1.** (a,b), (a,h), (g,h), (f,g), (c,f), (c,i), (c,d), (d,e)
- **2.** (a,b), (b,h), (g,h), (g,i), (c,i), (c,f), (c,d), (d,e)
- **3.** (a,b), (b,c), (c,i), (c,f), (f,g), (g,h), (c,d), (d,e)
- **4.** (a,b), (g,h), (g,f), (c,f), (c,i), (f,e), (b,c), (d,e)

> [!TIP]
> **Correct answer: 3. (a,b), (b,c), (c,i), (c,f), (f,g), (g,h), (c,d), (d,e)**

## Solution

Prim's algorithm repeatedly adds the lightest edge crossing from the current tree to an outside vertex. From a, add (a,b) of weight 4. The two weight-8 choices (a,h) and (b,c) tie, so choosing (b,c) is valid. The successive lightest crossing edges are then (c,i)=2, (c,f)=4, (f,g)=2, (g,h)=1, (c,d)=7, and (d,e)=9. This produces exactly the sequence in option 3 and connects all nine vertices without a cycle.

## Key Points

- At every Prim step, inspect only edges crossing the current cut; ties may give several valid orders, but a disconnected edge can never be chosen.

## Why the other options are incorrect

Option 1 chooses (a,h)=8 legitimately at the tie but later lists (g,h) before either endpoint g has joined the tree, so it is not a valid Prim step. Option 2 chooses the heavier (b,h)=11 while weight-8 (b,c) is available. Option 4 begins adding edges disconnected from the tree rooted at a.
