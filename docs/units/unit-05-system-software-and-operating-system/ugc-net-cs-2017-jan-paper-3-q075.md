# Question 75

*UGC NET CS · 2017 Jan Paper 3 · Linux and Unix · vi Save, Quit, and Shell Commands*

Match the following vi commands in Unix : List – I List – II a. : w i. saves the file and quits editing mode b. : x ii. escapes unix shell c. : q iii. saves file and remains in editing mode d. : sh iv. quits editing mode and no changes are saved to the file Codes : a b c d

- **1.** ii iii i iv
- **2.** iv iii ii i
- **3.** iii iv i ii
- **4.** iii i iv ii

> [!TIP]
> **Correct answer: 4. iii i iv ii**

## Solution

In vi command mode, `:w` writes the file and remains in the editor, so a→iii. `:x` writes if needed and exits, so b→i. `:q` quits when there are no unsaved changes, matching c→iv in the paper's wording. `:sh` starts a shell and temporarily escapes the editing session, so d→ii. The sequence iii,i,iv,ii is option 4.

## Key Points

- vi: `:w` write, `:x` save-and-exit, `:q` quit if safe, `:sh` open a shell.

## Why the other options are incorrect

The other codes interchange writing, exiting, and shell escape. Remember that `:q` refuses to discard unsaved changes unless forced as `:q!`; the option's 'no changes are saved' description assumes an ordinary permissible quit.
