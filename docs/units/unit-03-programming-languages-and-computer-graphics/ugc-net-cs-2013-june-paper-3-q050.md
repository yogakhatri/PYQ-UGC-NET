# Question 50

*UGC NET CS · 2013 June Paper 3 · Programming in C · printf Dynamic Precision for Strings*

What will be the output of the following C program segment? main() { char *s = "hello world"; int i = 7; printf("%.*s", i, s); }

- **A.** Syntax error
- **B.** hello w
- **C.** hello
- **D.** o world

> [!TIP]
> **Correct answer: B. hello w**

## Solution

In printf, the precision on a %s conversion limits the maximum number of characters printed. In %.*s, the asterisk says to read that precision from the next int argument. Here i is 7, so printf outputs the first seven characters of 'hello world': h e l l o, a space, and w—namely 'hello w'. The following s argument supplies the string.

## Key Points

- %.*s means print at most the next integer's number of characters from the supplied string.

## Why the other options are incorrect

There is no error in the %.*s format itself. 'hello' would require a precision of 5. 'o world' would require starting at s+4 rather than limiting the length from the beginning. The source uses an old-style main declaration; modern C should write int main(void), but the MCQ is testing dynamic string precision.
