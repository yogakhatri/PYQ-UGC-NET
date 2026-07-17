# Question 72

*UGC NET CS · 2015 June Paper 3 · Fuzzy Sets · Image of a Fuzzy Set under a Function*

Let f(x)=(x−3)^2+2 and let the source's fuzzy set 'Around −4' be {(2,0.3),(3,0.6),(4,1),(5,0.6),(6,0.3)}. What is the image fuzzy set under f?

- **1.** {(2, 0.6), (3, 0.3), (6, 1), (11, 0.3)}
- **2.** {(2, 0.6), (3, 1), (6, 1), (11, 0.3)}
- **3.** {(2, 0.6), (3, 1), (6, 0.6), (11, 0.3)}
- **4.** {(2, 0.6), (3, 0.3), (6, 0.6), (11, 0.3)}

> [!TIP]
> **Correct answer: 3. {(2, 0.6), (3, 1), (6, 0.6), (11, 0.3)}**

## Solution

Evaluate f on each support value while carrying its membership: f(2)=3 with 0.3, f(3)=2 with 0.6, f(4)=3 with 1, f(5)=6 with 0.6, and f(6)=11 with 0.3. When several inputs map to the same output, use maximum membership, so μ(3)=max(0.3,1)=1. The image is `{(2,0.6),(3,1),(6,0.6),(11,0.3)}`, option 3.

## Key Points

- For a crisp function applied to a fuzzy set, each output membership is the maximum membership among all preimages.

## Why the other options are incorrect

Options 1 and 4 fail to take the maximum membership for output 3; option 2 incorrectly raises the membership of output 6 to 1. The source label `Around −4` conflicts with a support centered at +4, but the listed support and function determine the answer unambiguously.
