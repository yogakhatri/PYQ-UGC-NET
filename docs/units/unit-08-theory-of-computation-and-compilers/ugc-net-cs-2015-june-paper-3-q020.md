# Question 20

*UGC NET CS · 2015 June Paper 3 · Regular Language Models · Constructing Regular Expressions from Constraints*

Which regular expression denotes L = {x ∈ {0,1}* | x ends with 1 and does not contain the substring 00}? Here `+` denotes union.

- **1.** (1+01)*(10+01)
- **2.** (1+01)*01
- **3.** (1+01)*(1+01)
- **4.** (10+01)*01

> [!TIP]
> **Correct answer: 3. (1+01)*(1+01)**

## Solution

Any string that contains no `00` and ends in `1` can be split into blocks `1` or `01`: every zero must be immediately followed by one, and isolated ones form the other block. At least one block is required. `(1+01)*(1+01)` expresses zero or more such blocks followed by one final block, exactly the positive closure of `{1,01}`.

## Key Points

- No `00` plus final `1` means a nonempty sequence of the blocks `1` and `01`.

## Why the other options are incorrect

Option 1 permits a final `10`, which ends in 0. Option 2 forces the whole string to end with block `01`, excluding valid strings such as `1` and `11`. Option 4 allows only repeated `10`/`01` blocks before a forced `01` and misses many valid strings.
