# Question 112

*UGC NET CS · 2019 Dec Paper 1 And 2 · Fuzzy Sets · Fuzzy Conjunction and Disjunction*

A fuzzy conjunction t(x,y) and fuzzy disjunction s(x,y) form a dual pair when t(x,y)=1−s(1−x,1−y). If t(x,y)=xy/(x+y−xy), what is s(x,y)?

- **1.** (x + y)/(1 − xy)
- **2.** (x + y − 2xy)/(1 − xy)
- **3.** (x + y − xy)/(1 − xy)
- **4.** (x + y − xy)/(1 + xy)

> [!TIP]
> **Correct answer: 2. (x + y − 2xy)/(1 − xy)**

## Solution

Duality gives s(x,y)=1−t(1−x,1−y). Substitute the stated t-norm: t(1−x,1−y)=[(1−x)(1−y)]/[(1−x)+(1−y)−(1−x)(1−y)]. The denominator simplifies to 1−xy and the numerator to 1−x−y+xy. Therefore s=1−(1−x−y+xy)/(1−xy)=(x+y−2xy)/(1−xy), which is option 2.

## Key Points

- To find a t-norm's dual s-norm under standard negation, use s(x,y)=1−t(1−x,1−y) and simplify carefully.

## Why the other options are incorrect

Option 1 omits the −2xy term created when the numerator is subtracted from the denominator. Option 3 subtracts only one xy, and option 4 changes the denominator's sign. Direct substitution into the duality identity rules out each alternative.
