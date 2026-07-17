# Question 5

*UGC NET CS · 2011 Dec Paper 3 · Programming in C · Win32 Window Creation and Shell Commands*

(a) Describe briefly six windows functions usually called while creating a window. (b) What is the difference between UNIX and Windows Navigat ion and directory control commands ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: Use the standard Win32 registration, creation, display and message-loop calls; UNIX and Windows use different navigation command names and path syntax**

## Solution

**Typical Win32 window-creation flow:** (1) RegisterClassEx registers a WNDCLASSEX describing the window procedure, icon, cursor, background and class name. (2) CreateWindowEx creates an instance and returns its window handle. (3) ShowWindow makes it visible in the requested state. (4) UpdateWindow requests immediate painting if its update region is nonempty. (5) GetMessage retrieves messages until WM_QUIT; PeekMessage is an alternative for nonblocking loops. (6) TranslateMessage converts keyboard messages and DispatchMessage sends each message to the registered WndProc. The window procedure handles messages such as WM_PAINT and WM_DESTROY and calls DefWindowProc for defaults. These calls are often grouped as six stages even though the message-loop stage contains several API calls.

**UNIX versus Windows navigation/directory control:** UNIX-like shells use / as the normal separator and a single rooted tree; Windows traditionally uses drive letters such as C: and backslash separators, although modern shells often accept /. Common equivalents are: current directory pwd versus cd with no argument in Command Prompt; list ls versus dir; change cd path in both; create mkdir versus mkdir/md; remove empty directory rmdir versus rmdir/rd; copy cp versus copy; move/rename mv versus move/ren; delete rm versus del; clear clear versus cls. Options and wildcard/quoting rules differ by shell, so commands should be interpreted in their actual shell (bash/zsh, cmd.exe or PowerShell).

## Key Points

- Win32 setup is register -> create -> show/update -> message loop -> window procedure; shell navigation concepts correspond even when command names and path syntax differ.

## Common mistakes to avoid

Do not call CreateWindowEx before registering the class, and do not omit the message loop or window procedure. Do not claim modern UNIX and Windows directory concepts are completely different: both are hierarchical, but roots, separators, commands, permissions and shell syntax differ.
