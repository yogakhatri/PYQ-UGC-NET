# Question 51

*UGC NET CS · 2020 Nov With Answers · Set Theory · Inclusion–Exclusion Counting*

The number of positive integers not exceeding 100 that are either odd or the square of an integer is

- **1.** 63
- **2.** 59
- **3.** 55
- **4.** 50

> [!TIP]
> **Correct answer: 3. 55**

## Solution

There are 50 odd positive integers from 1 through 100. The positive squares not exceeding 100 are 1² through 10², so there are 10 squares. Five of those squares are already odd—1, 9, 25, 49, and 81—because they come from odd bases. By inclusion–exclusion, the union contains 50+10−5=55 integers. Therefore option 3.

## Key Points

- For ‘odd or square,’ use |O∪S|=|O|+|S|−|O∩S|; an odd square has an odd base.

## Why the other options are incorrect

Fifty counts only the odd integers. Adding all ten squares without subtracting the five odd squares gives 60, which is not even listed. Values 59 and 63 arise from an incorrect overlap count; an integer cannot be counted twice in the union.
