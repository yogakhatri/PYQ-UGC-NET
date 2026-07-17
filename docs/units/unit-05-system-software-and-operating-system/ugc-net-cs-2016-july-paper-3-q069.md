# Question 69

*UGC NET CS · 2016 July Paper 3 · Unix and Shell Commands · Octal File-Permission Bits*

In Unix, files can be protected by assigning each one a 9-bit mode called rights bits. Now, consider the following two statements: I. A mode of 641 (octal) means that the owner can read and write the file, other members of the owner’s group can read it, and users can execute only. II. A mode of 100 (octal) allows the owner to execute the file, but prohibits all other access. Which of the following options is correct with reference to above statements ?

- **1.** Only I is correct.
- **2.** Only II is correct.
- **3.** Both I and II are correct.
- **4.** Both I and II are incorrect.

> [!TIP]
> **Correct answer: 3. Both I and II are correct.**

## Solution

Each octal permission digit encodes read=4, write=2, and execute=1 for owner, group, and others. Mode 641 therefore expands to owner 6=rw−, group 4=r−−, others 1=−−x, exactly as statement I says. Mode 100 expands to owner −−x, group −−−, others −−−, so only the owner may execute and every other permission is absent. Statement II is also correct. Hence option 3 is correct.

## Key Points

- UNIX permission digits are sums of r=4, w=2, x=1, ordered as owner-group-others.

## Why the other options are incorrect

Options 1 and 2 wrongly reject one true decoding; option 4 rejects both. The quickest check is to translate each octal digit independently using 4-2-1.
