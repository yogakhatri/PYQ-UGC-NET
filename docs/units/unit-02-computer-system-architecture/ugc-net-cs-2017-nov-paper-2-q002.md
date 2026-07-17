# Question 2

*UGC NET CS · 2017 Nov Paper 2 · Data Representation · Base-4 Arithmetic*

Let m=(313)4 and n=(322)4. Find the base 4 expansion of m+n.

- **1.** (635) 4
- **2.** (32312) 4
- **3.** (21323) 4
- **4.** (1301)₄

> [!TIP]
> **Correct answer: 4. (1301)₄**

## Solution

Add directly in base 4. In the units column, 3+2=5=11₄, so write 1 and carry 1. Next, 1+2+1=4=10₄, so write 0 and carry 1. Then 3+3+1=7=13₄, so write 3 and carry 1. The final carry becomes the leading digit, giving (1301)₄. Thus option 4 is correct.

## Key Points

- Base-4 addition uses the usual column method, but every total of 4 contributes a carry to the next column.

## Why the other options are incorrect

Option 1 writes digits larger than the allowed base-4 digits 0–3. Options 2 and 3 do not follow column-wise carrying. A decimal check agrees: (313)₄=55 and (322)₄=58; 55+58=113=(1301)₄.
