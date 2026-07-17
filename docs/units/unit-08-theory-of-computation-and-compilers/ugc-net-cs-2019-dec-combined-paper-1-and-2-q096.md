# Question 96

*UGC NET CS · 2019 Dec Paper 1 And 2 · Regular Language Models · Homomorphisms of Regular Languages*

If L is the regular language denoted by r = (w + x*)(ww)*, which regular expression denotes h(L)?

- **1.** (zxyy + xzy)(zxyy)
- **2.** (zxyy + (xzy)*)(zxyy zxyy)*
- **3.** (zxyy + xzy)(zxyy)*
- **4.** (zxyy + (xzy)*)(zxyy zxyy)

> [!TIP]
> **Correct answer: 2. (zxyy + (xzy)*)(zxyy zxyy)***

## Solution

A homomorphism is applied symbol by symbol and preserves regular-expression operations. Thus h(w+x*)=h(w)+h(x)*=zxyy+(xzy)*. Also h((ww)*)=(h(w)h(w))*=(zxyy zxyy)*. Concatenating the two transformed factors gives (zxyy+(xzy)*)(zxyy zxyy)*, exactly option 2.

## Key Points

- For a homomorphism h, substitute each alphabet symbol by its image while retaining union, concatenation, and Kleene-star structure.

## Why the other options are incorrect

Option 1 loses both Kleene stars. Option 3 replaces x* by a single x image and incorrectly changes (ww)* into w*. Option 4 has the correct first factor but omits the star on the repeated ww image, so it permits exactly one pair rather than any number of pairs.
