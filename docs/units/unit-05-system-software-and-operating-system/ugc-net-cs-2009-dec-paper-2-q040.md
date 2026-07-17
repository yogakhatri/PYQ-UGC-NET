# Question 40

*UGC NET CS · 2009 Dec Paper 2 · File and Input/Output Systems · Transforming Requests to Hardware Operations*

The Unix command used to find out the number of characters in a file is

- **A.** nc
- **B.** wc
- **C.** chcnt
- **D.** lc

> [!TIP]
> **Correct answer: B. wc**

## Solution

The Unix wc utility reports counts of lines, words, and bytes/characters; wc -c gives bytes and wc -m gives characters in implementations supporting it. Thus wc is the listed command used for the required count.

## Key Points

- Use wc with the appropriate count option, especially -m for characters.

## Why the other options are incorrect

nc is commonly netcat, while chcnt and lc are not the standard Unix character-count utility.
