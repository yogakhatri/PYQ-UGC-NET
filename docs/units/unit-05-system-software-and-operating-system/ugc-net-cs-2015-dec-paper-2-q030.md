# Question 30

*UGC NET CS · 2015 Dec Paper 2 · Unix and Linux · getty and Login Configuration*

In Unix, the login prompt can be changed by changing the contents of the file __________.

- **1.** contrab
- **2.** init
- **3.** gettydefs
- **4.** inittab

> [!TIP]
> **Correct answer: 3. gettydefs**

## Solution

In traditional System V-style Unix, `/etc/gettydefs` supplies terminal settings to `getty` and includes a login-prompt field. Editing that field changes the prompt printed while `getty` waits for a login name. Thus the intended file is `gettydefs`.

## Key Points

- Historical Unix login path: init starts getty; getty reads gettydefs and prints the login prompt.

## Why the other options are incorrect

`inittab` controls which processes `init` starts and at which run levels; it may invoke getty but does not hold this prompt field. `init` is a program, not the prompt-definition file. The printed `contrab` option is not the relevant Unix configuration file.
