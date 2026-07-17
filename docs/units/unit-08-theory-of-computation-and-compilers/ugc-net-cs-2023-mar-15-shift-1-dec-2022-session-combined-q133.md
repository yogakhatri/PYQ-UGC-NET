# Question 133

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Regular Language Models · Regular Languages*

The precedence of regular expression operators from lowest to highest precedence is:

- **1.** Star, Concatenation, Union
- **2.** Union, Star, Concatenation
- **3.** Union, Concatenation, Star
- **4.** Star, Union, Concatenation

> [!TIP]
> **Correct answer: 3. Union, Concatenation, Star**

## Solution

In conventional regular-expression notation, union (| or +) has the lowest precedence, concatenation has the next higher precedence, and Kleene star (*) has the highest precedence. The required low-to-high order is therefore Union, Concatenation, Star.

## Key Points

- Regular-expression precedence is union < concatenation < closure/star.

## Why the other options are incorrect

Every other option places star too low or places union above concatenation.
