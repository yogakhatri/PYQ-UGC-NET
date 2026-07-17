# Question 74

*UGC NET CS · 2017 Jan Paper 3 · Linux and Unix · Pipelines with head and tr*

Unix command to change the case of first three lines of file “shortlist” from lower to upper

- **1.** tr '[a-z]' '[A-Z]' shortlist | head -3
- **2.** head -3 shortlist | tr '[a-z]' '[A-Z]'
- **3.** tr head -3 shortlist '[A-Z]' '[a-z]'
- **4.** tr shortlist head -3 '[a-z]' '[A-Z]'

> [!TIP]
> **Correct answer: 2. head -3 shortlist | tr '[a-z]' '[A-Z]'**

## Solution

A Unix pipeline sends the standard output of the command on the left to the standard input of the command on the right. `head -3 shortlist` first emits only the first three lines. `tr '[a-z]' '[A-Z]'` then translates lowercase characters in that stream to uppercase. Therefore option 2 has the correct order and syntax.

## Key Points

- Filter pipeline order follows data flow: select lines with `head`, then transform characters with `tr`.

## Why the other options are incorrect

Option 1 incorrectly supplies the filename as an operand to `tr` and places `head` after it. Options 3 and 4 do not follow the command syntax or pipeline data flow. Also, the shown command prints transformed lines; redirect its output to a file if persistent replacement is desired.
