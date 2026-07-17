# Question 57

*UGC NET CS · 2015 Dec Paper 3 · Linux Operating Systems · Shell Quoting and Glob Patterns*

What will be the output of the following Unix command ? $rm chap0\[1 - 3\]

- **1.** Remove file chap0[1 - 3]
- **2.** Remove file chap01, chap02, chap03
- **3.** Remove file chap\[1 - 3\]
- **4.** None of the above

> [!TIP]
> **Correct answer: 1. Remove file chap0[1 - 3]**

## Solution

The backslashes quote the opening and closing square brackets, so the shell does not interpret them as the glob pattern [1-3]. Under the paper's intended typography, rm therefore receives the literal bracketed filename chap0[1 - 3], making option 1 the intended answer.

## Key Points

- Escaping [ and ] suppresses pathname expansion; an unescaped [1-3] is a one-character range glob.

## Why the other options are incorrect

Option 2 would follow from an unescaped glob such as rm chap0[1-3], which expands to chap01, chap02, and chap03 when those files exist. Option 3 omits the 0 and incorrectly treats the backslashes as part of the filename. Literal shell syntax has an additional defect: the displayed unescaped spaces split the argument into multiple words, so no offered description is guaranteed exactly as printed. The answer assumes those spaces are typesetting around the range hyphen.
