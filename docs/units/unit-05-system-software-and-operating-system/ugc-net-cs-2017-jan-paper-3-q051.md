# Question 51

*UGC NET CS · 2017 Jan Paper 3 · File and Input/Output Systems · Unix Boot, Superblock, Inode, and Data Blocks*

Match the following for Unix file system : List – I List – II a. Boot block i. Information about file system, free block list, free inode list etc. b. Super block ii. Contains operating system files as well as program and data files created by users. c. Inode block iii. Contains boot program and partition table. d. Data block iv. Contains a table for every file in the file system. Attributes of files are stored here. Codes : a b c d

- **1.** iii i ii iv
- **2.** iii i iv ii
- **3.** iv iii ii i
- **4.** iv iii i ii

> [!TIP]
> **Correct answer: 2. iii i iv ii**

## Solution

The boot block contains bootstrap code and partition information, so a→iii. The superblock stores file-system-wide metadata such as size and free-block/free-inode information, so b→i. The inode area contains one metadata record per file, including attributes and block addresses, so c→iv. Data blocks store file contents, including operating-system and user files, so d→ii. The code iii,i,iv,ii is option 2.

## Key Points

- Unix filesystem layout: boot block → superblock → inode table → data blocks.

## Why the other options are incorrect

The other codes confuse global file-system metadata, per-file metadata, file contents, and boot information. These four regions have distinct scopes: boot, whole filesystem, individual file, and content.
