# Question 24

*UGC NET CS · 2015 June Paper 2 · Searching Algorithms · Average Case of Linear Search*

The average case occurs in the Linear Search Algorithm when :

- **1.** The item to be searched is in some where middle of the Array
- **2.** The item to be searched is not in the array
- **3.** The item to be searched is in the last of the array
- **4.** The item to be searched is either in the last or not in the array

> [!TIP]
> **Correct answer: 1. The item to be searched is in some where middle of the Array**

## Solution

For a successful linear search with the target equally likely to occupy any of `n` positions, the comparison counts are 1, 2, ..., n. Their mean is `(1 + 2 + ... + n)/n = (n + 1)/2`, so the typical successful target lies conceptually around the middle of the array. This is what option 1 intends.

## Key Points

- Uniform successful linear search averages `(n + 1)/2` comparisons; failure or a last-position match costs `n`.

## Why the other options are incorrect

An absent item and an item in the final position both require all `n` comparisons and describe worst-case behavior, not the successful average case. Their combination in option 4 is therefore also worst-case. Strictly, average case is a probability-weighted expectation rather than one fixed position, but option 1 is the matching textbook description.
