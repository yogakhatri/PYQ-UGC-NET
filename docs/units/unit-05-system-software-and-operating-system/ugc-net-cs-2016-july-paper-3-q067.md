# Question 67

*UGC NET CS · 2016 July Paper 3 · Unix and Shell Programming · Redirection and Background Jobs*

What is the function of the following UNIX command? wc -l < a > b &

- **1.** It runs the word count program to count the number of lines in its input, a, writing the result to b, as a foreground process.
- **2.** It runs the word count program to count the number of lines in its input, a, writing the result to b, but does it in the background.
- **3.** It counts the errors during the execution of a process, a, and puts the result in process b.
- **4.** It copies the ‘l’ numbers of lines of program from file, a, and stores in file b.

> [!TIP]
> **Correct answer: 2. It runs the word count program to count the number of lines in its input, a, writing the result to b, but does it in the background.**

## Solution

The command wc -l counts input lines. The redirection < a makes file a its standard input, and > b sends its standard output to file b, replacing b if it already exists. The trailing & asks the shell to run the command asynchronously as a background job. Therefore option 2 describes all four parts correctly.

## Key Points

- Read a shell command left to right: program and option, input redirection, output redirection, then job-control operator.

## Why the other options are incorrect

Option 1 ignores the trailing background operator. wc does not count execution errors, so option 3 is unrelated. The -l option counts lines; it does not copy a specified number of lines, so option 4 is false.

## Additional Information

The source prints 'WC' and a typographic dash, but UNIX command names and options are normally written exactly as wc -l; the answer choices make that intended command unambiguous.
