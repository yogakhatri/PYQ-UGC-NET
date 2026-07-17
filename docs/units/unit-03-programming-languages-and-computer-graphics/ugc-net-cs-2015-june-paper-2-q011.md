# Question 11

*UGC NET CS · 2015 June Paper 2 · Programming in C · Array Indexing, Pointer Arithmetic and Output*

Under the question's intended C assumptions, what is printed by `char S[]="ABCDEFGH"; printf("%c", *(&S[3])); printf("%s", S+4); printf("%u", S);` if the base address of S is 1000?

- **1.** ABCDEFGH1000
- **2.** CDEFGH1000
- **3.** DDEFGHH1000
- **4.** DEFGH1000

> [!TIP]
> **Correct answer: 4. DEFGH1000**

## Solution

Under the exam's intended assumptions, S[3] is the fourth character, `D`. The pointer S+4 addresses S[4], so `%s` prints `EFGH`. Finally the question asks us to display S's base address as 1000. Concatenating the three outputs gives `DEFGH1000`, option 4.

## Key Points

- Array indexing is zero-based: `*(&S[3])` is D, and `S+4` points to the suffix EFGH.

## Why the other options are incorrect

Option 1 starts from the whole array, option 2 starts the first character at C, and option 3 duplicates characters. Formally, standard C requires `%p` with a `(void*)` argument to print a pointer; passing `char*` to `%u` is a variadic type mismatch and has undefined behavior. The numerical address output is therefore only the paper's stated convention.
