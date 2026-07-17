# Question 118

*UGC NET CS · 2018 Dec Paper 1 And 2 · Linux Operating Systems · Printing Commands*

In a Linux operating-system environment, which command is used to print a file?

- **1.** print
- **2.** ptr
- **3.** pr
- **4.** lpr

> [!TIP]
> **Correct answer: 4. lpr**

## Solution

The `lpr` command submits a file to the line-printer spooling system, optionally selecting a printer and job settings. Thus it is the command used to print a file in the traditional Linux/Unix printing environment, option 4.

## Key Points

- `pr` prepares/formats text; `lpr` sends the file to the print spooler.

## Why the other options are incorrect

`print` and `ptr` are not the standard commands shown for submitting the job. `pr` reformats or paginates text and writes the result to standard output; it can prepare content for printing but does not itself submit the print job. `lpr` performs the submission.
