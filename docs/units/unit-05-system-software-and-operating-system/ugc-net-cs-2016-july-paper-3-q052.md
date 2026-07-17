# Question 52

*UGC NET CS · 2016 July Paper 3 · Unix Process Management · Unix Signals*

Which of the following option with reference to UNIX operating system is not correct ?

- **1.** INT signal is sent by the terminal driver when one types <Control-C> and it is a request to terminate the current operation.
- **2.** TERM is a request to terminate execution completely. The receiving process will clean up its state and exit.
- **3.** QUIT is similar to TERM, except that it defaults to producing a core dump if not caught.
- **4.** KILL is a blockable signal.

> [!TIP]
> **Correct answer: 4. KILL is a blockable signal.**

## Solution

SIGKILL is specifically designed to terminate a process unconditionally. A process cannot catch it, ignore it, or block it. Thus the statement 'KILL is a blockable signal' is false, making option 4 the required answer.

## Key Points

- SIGTERM asks a process to terminate; SIGKILL forces termination and cannot be caught, ignored, or blocked.

## Why the other options are incorrect

A terminal normally sends SIGINT for Ctrl-C. SIGTERM is the conventional polite termination request and may be handled so a program can clean up before exiting. SIGQUIT resembles an interactive termination request and its default action includes a core dump. The word 'will' in the SIGTERM description is simplified—SIGTERM can be caught or ignored—but option 4 is the unambiguously prohibited operation.
