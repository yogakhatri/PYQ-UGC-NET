# Question 100

*UGC NET CS · 2019 June Paper 1 And 2 · Linux Operating Systems · Shell pipelines and glob patterns*

Which of the following UNIX/Linux pipes will count the number of lines in all the files having c and h as their extension in the current working directory?

- **1.** cat *.ch | wc -l
- **2.** cat *.[c-h] | wc -l
- **3.** cat *.[ch] | wc -l
- **4.** cat * [ch] | wc -l

> [!TIP]
> **Correct answer: 3. cat *.[ch] | wc -l**

## Solution

The shell pattern *.[ch] matches any filename whose final extension character is either c or h, so it selects both .c and .h files. cat concatenates their contents and wc -l counts the resulting lines. The complete pipeline is cat *.[ch] | wc -l.

## Key Points

- In a shell glob, [ch] means one character chosen from c or h; | passes output to the next command.

## Why the other options are incorrect

- ***.ch:** matches the literal extension .ch.
- ***.[c-h]:** is a character range and can match letters between c and h, not only c and h.
- *** [ch]:** does not express the required extension pattern or pipeline correctly.
