# Question 12

*UGC NET CS · 2009 Dec Paper 2 · Programming in C · Command-Line Arguments*

What would be the output of the following program, if run from the command line as “myprog 1 2 3” ? main (int argc, char ∗ argv[ ]) { int i ; i = argv[1] + argv[2] + argv[3] ; printf (“% d”, i) ; }

- **A.** 123
- **B.** 6
- **C.** Error
- **D.** “123”

> [!TIP]
> **Correct answer: C. Error**

## Solution

Each argv[i] has type char*, pointing to a command-line string. C does not define addition of two pointers, so argv[1]+argv[2]+argv[3] is a constraint violation and the program fails to compile as written. Converting the strings to integers would require a function such as strtol.

## Key Points

- Command-line arguments are strings/pointers, not integers.

## Why the other options are incorrect

The program neither concatenates the strings into 123 nor parses and adds them to obtain 6. Quoted '123' is also not produced.
