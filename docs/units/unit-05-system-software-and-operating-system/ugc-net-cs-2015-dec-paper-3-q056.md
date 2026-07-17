# Question 56

*UGC NET CS · 2015 Dec Paper 3 · Unix and Shell Commands · chmod Symbolic Permissions*

In Unix, the command to enable execution permission for file "mylife" by all is ____________.

- **1.** chmod ugo+X myfile
- **2.** chmod a+X myfile
- **3.** chmod +X myfile
- **4.** All of the above

> [!TIP]
> **Correct answer: 4. All of the above**

## Solution

In symbolic chmod syntax, ugo names user, group, and others, while a is shorthand for all three. Thus ugo+X and a+X express the same affected classes. Omitting the class also defaults broadly to all classes, which is why the paper intends all three commands and therefore option 4.

## Key Points

- Exam shorthand: ugo and a mean all users.
- Real command for unconditional all-user execution: chmod a+x file.

## Why the other options are incorrect

No single listed command is the uniquely intended one. Two technical qualifications matter in real shell use: uppercase X grants execute/search only to directories or to files that already have some execute bit, whereas lowercase x unconditionally adds execute permission; and when 'who' is omitted, the process umask can suppress some added bits. To guarantee execution for every class on an ordinary file, use chmod a+x myfile, which the options unfortunately do not show.
