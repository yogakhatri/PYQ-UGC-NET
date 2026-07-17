# Question 62

*UGC NET CS · 2020 Nov With Answers · Programming in Java · Recursive Functions and Geometric Series*

Consider the recursive Java function f that takes two long arguments and returns a float: public static float f(long m, long n) { float result=(float)m/(float)n; if (m<0 || n<0) return 0.0f; else result -= f(m*2,n*3); return result; } Which real value best approximates f(1,3)?

- **1.** 0.2
- **2.** 0.4
- **3.** 0.6
- **4.** 0.8

> [!TIP]
> **Correct answer: 1. 0.2**

## Solution

Ignoring the distant integer-overflow stopping point, each recursive level contributes an alternating geometric term. At depth k the ratio is (2^k)/(3·3^k)=(1/3)(2/3)^k, and subtraction alternates signs. Thus f(1,3)≈(1/3)[1−2/3+(2/3)^2−…]. For |−2/3|<1, the sum is (1/3)/(1+2/3)=1/5=0.2. Java long overflow eventually makes an argument negative and returns 0, truncating the series far out; the requested best approximation remains 0.2, option 1.

## Key Points

- Translate recursive subtraction into an alternating geometric series with first term 1/3 and ratio −2/3.

## Why the other options are incorrect

The other choices are not the sum of the alternating geometric series. Treating every recursive term as positive would give 1 instead, while stopping after only one or two terms gives a poor approximation and ignores the repeated recursion.
