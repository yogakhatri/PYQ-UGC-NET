# Question 39

*UGC NET CS · 2017 Jan Paper 3 · Java Programming · Recursive Calls and Return Unwinding*

Consider the following JAVA program : public class First { public static int CBSE (int x) { if (x < 100) x = CBSE (x + 10); return (x – 1); } public static void main (String[] args){ System.out.print(First.CBSE(60)); } } What does this program print ?

- **1.** 59
- **2.** 95
- **3.** 69
- **4.** 99

> [!TIP]
> **Correct answer: 2. 95**

## Solution

Calls descend as CBSE(60)→70→80→90→100. At x=100 the condition is false, so that call returns 99. Each waiting call assigns the returned value to its local x and then subtracts one: the x=90 frame returns 98, x=80 returns 97, x=70 returns 96, and x=60 returns 95. The program therefore prints 95, option 2.

## Key Points

- Trace recursive code in two phases: calls change 60 to 100; returns subtract one once per suspended frame.

## Why the other options are incorrect

99 is only the base-frame result before four earlier calls unwind. 59 would result from subtracting once from the original argument, and 69 does not match either the descent or the returned chain.
