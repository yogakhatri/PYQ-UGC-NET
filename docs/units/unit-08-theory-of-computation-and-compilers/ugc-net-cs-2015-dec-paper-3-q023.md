# Question 23

*UGC NET CS · 2015 Dec Paper 3 · Language Hierarchy · Regular, CFL, CSL, Recursive and RE Languages*

Match: (a) {a^n b^n | n>0} is deterministic context-free; (b) the complement of {a^n b^n a^n | n>0} is context-free; (c) {a^n b^n a^n} is context-sensitive; (d) L is a recursive language. Endings: (i) but not recursive, (ii) but not context-free, (iii) but cannot be accepted by a deterministic PDA, (iv) but not regular.

- **1.** (i) (ii) (iii) (iv)
- **2.** (i) (ii) (iv) (iii)
- **3.** (iv) (iii) (ii) (i)
- **4.** (iv) (iii) (i) (ii)

> [!TIP]
> **Correct answer: No option is fully valid as printed; option 3 is clearly intended if (d) says ‘recursively enumerable’**

## Solution

The sound matches are (a)–(iv), because {a^n b^n} is deterministic context-free but not regular; (b)–(iii), because the stated complement is context-free but cannot be deterministic context-free (DCFLs are closed under complement, while {a^n b^n a^n} is not CFL); and (c)–(ii), because {a^n b^n a^n} is context-sensitive but not context-free. These force option 3's first three positions. Its last pair (d)–(i) would correctly read ‘recursively enumerable but not recursive’, but the source instead prints ‘recursive ... but not recursive’, a contradiction.

## Key Points

- Use the Chomsky hierarchy and remember: DCFL is closed under complement, CFL is not.

## Why the other options are incorrect

Options 1, 2, and 4 already mismatch one of (a)–(c). Option 3 captures all three mathematical matches but cannot make the printed statement (d) self-consistent without restoring the evidently omitted word ‘enumerable’.
