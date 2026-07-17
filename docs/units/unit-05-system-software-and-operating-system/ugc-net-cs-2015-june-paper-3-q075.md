# Question 75

*UGC NET CS · 2015 June Paper 3 · Unix and Shell Commands · Editing Multiple Files with vi*

The unix command : $ vi file1 file2

- **1.** Edits file1 and stores the contents of file1 in file2
- **2.** Both file1 and file2 can be edited using ex commands to move between the files
- **3.** Both files can be edited using mv to move between the files
- **4.** Edits file1 first, saves it, and then edits file2

> [!TIP]
> **Correct answer: 2. Both file1 and file2 can be edited using ex commands to move between the files**

## Solution

`vi file1 file2` places both names in vi's argument list and opens the first. Because vi includes ex command mode, the user can move through the argument list with commands such as `:next` (`:n`), `:previous`, and `:args`, editing both files in the same session. This is the behavior described by option 2.

## Key Points

- Multiple filenames become vi's argument list; use ex navigation commands to switch among them.

## Why the other options are incorrect

The command does not copy file1 into file2. `mv` is a shell rename/move utility, not a vi navigation command. Vi does not automatically save file1 and advance; the user controls saving and movement, and unsaved changes may block `:next` unless saved or overridden.
