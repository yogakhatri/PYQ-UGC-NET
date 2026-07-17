# Question 35

*UGC NET CS · 2015 Dec Paper 2 · Data Structures · Hashing*

The hash function used in double hashing is of the form :

- **1.** h(k,i) = (h1(k) + h2(k) + i) mod m
- **2.** h(k,i) = (h1(k) + h2(k) − i) mod m
- **3.** h(k,i) = (h1(k) + i·h2(k)) mod m
- **4.** h(k,i) = (h1(k) − i·h2(k)) mod m

> [!TIP]
> **Correct answer: 3. h(k,i) = (h1(k) + i·h2(k)) mod m**

## Solution

Double hashing uses one hash value as the initial position and a second as the step size. Probe i is h(k,i)=(h1(k)+i·h2(k)) mod m, with i=0,1,2,… . If h2(k) is chosen relatively prime to m, the probe sequence can visit every table position before repeating.

## Key Points

- Double hashing probe = initial hash + probe number × second-hash step, modulo table size.

## Why the other options are incorrect

Options 1 and 2 add h2 only once, so they do not use it as a per-probe step. Option 4 uses subtraction rather than the conventional positive-step formula printed in the definition.
