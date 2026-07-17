# Question 73

*UGC NET CS · 2018 July Paper 2 · Heuristic Search · Combining Admissible Heuristics*

If admissible heuristics h1,…,hm are available for a search problem and none dominates all the others, which combined heuristic should be chosen?

- **1.** h(n)= max{h 1(n),....,h m(n)}
- **2.** h(n)= min{h 1(n),....,h m(n)}
- **3.** h(n)= avg{h 1(n),....,h m(n)}
- **4.** h(n)= sum{h 1(n),....,h m(n)}

> [!TIP]
> **Correct answer: 1. h(n)= max{h 1(n),....,h m(n)}**

## Solution

Let h(n)=max{h1(n),…,hm(n)}. Because every hi is admissible, each is at most the true remaining cost h*(n); their maximum is therefore also at most h*(n), so it remains admissible. At every node it is at least as informative as each component heuristic and hence dominates them. Option 1 is correct.

## Key Points

- The pointwise maximum of admissible heuristics is admissible and dominates every member of the collection.

## Why the other options are incorrect

The minimum and average can remain admissible but give a weaker estimate than the maximum. A sum can exceed the true remaining cost when the heuristics estimate overlapping work, so admissibility is not guaranteed.
