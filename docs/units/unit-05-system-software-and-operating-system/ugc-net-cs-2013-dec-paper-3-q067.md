# Question 67

*UGC NET CS · 2013 Dec Paper 3 · Unix and Shell Programming · String Comparison with test*

In Unix, how do you check that two given strings a and b are equal ?

- **A.** test "$a" -eq "$b"
- **B.** test $a –equal $b
- **C.** test "$a" = "$b"
- **D.** sh -c 'test "$a" == "$b"'

> [!TIP]
> **Correct answer: C. test "$a" = "$b"**

## Solution

The POSIX test utility uses the binary operator = for string equality, so the safe form is test "$a" = "$b". Quoting preserves each expanded value as one argument and handles empty strings. The command exits with status 0 when the strings are identical and 1 when they differ.

## Key Points

- Shell test: = compares strings, -eq compares integers; quote variable expansions.

## Why the other options are incorrect

-eq performs integer comparison, not string comparison. -equal is not a test operator. The final command uses a nonportable/incorrect construction and also starts a new shell without guaranteeing that a and b are exported into it.

## References

- [The Open Group - POSIX test utility](https://pubs.opengroup.org/onlinepubs/9699919799.2016edition/utilities/test.html)
