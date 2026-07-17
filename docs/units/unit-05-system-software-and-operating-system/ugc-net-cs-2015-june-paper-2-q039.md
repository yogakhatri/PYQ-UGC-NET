# Question 39

*UGC NET CS · 2015 June Paper 2 · Unix and Shell Commands · grep Invert-Match and Line-Number Options*

What does the following command do? `grep -vn "abc" x`

- **1.** It will print all lines in file x that match the search string "abc".
- **2.** It will print all lines in file x that do not match the search string "abc".
- **3.** It will print the total number of lines in file x that match the string "abc".
- **4.** It will print the specific line numbers in file x at which the string "abc" matches.

> [!TIP]
> **Correct answer: 2. It will print all lines in file x that do not match the search string "abc".**

## Solution

In `grep -vn "abc" x`, `-v` inverts selection, so grep selects lines in file `x` that do not match `abc`. The `-n` flag prefixes every selected line with its 1-based line number. Option 2 states the decisive selection behavior; more precisely, the command prints every nonmatching line together with its line number.

## Key Points

- `grep -v` selects nonmatches; `grep -n` prefixes selected lines with their line numbers.

## Why the other options are incorrect

Option 1 ignores `-v`. Option 3 would require a count such as `-c` and also describes matching rather than inverted selection. Option 4 describes only line numbers of matching lines, whereas this command prints the full nonmatching lines, numbered.
