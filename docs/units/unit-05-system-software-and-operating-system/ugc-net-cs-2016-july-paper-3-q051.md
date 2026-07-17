# Question 51

*UGC NET CS · 2016 July Paper 3 · File and Input/Output Systems · Unix File-System Layout and Inodes*

Which of the following information about the UNIX file system is not correct ?

- **1.** Super block contains the number of i-nodes, the number of disk blocks, and the start of the list of free disk blocks.
- **2.** An i-node contains accounting information as well as enough information to locate all the disk blocks that holds the file’s data.
- **3.** Each i-node is 256-bytes long.
- **4.** All the files and directories are stored in data blocks.

> [!TIP]
> **Correct answer: 3. Each i-node is 256-bytes long.**

## Solution

An inode's size is a property of a particular UNIX or Unix-like file-system format; it is not universally 256 bytes. Historical and modern file systems use different inode sizes. Therefore the absolute claim in option 3 is the incorrect statement.

## Key Points

- An inode describes a file and points to its data; it normally does not store the filename, and its on-disk size is file-system dependent.

## Why the other options are incorrect

The superblock stores file-system-wide metadata, including counts and free-space information in the traditional layout. An inode stores ownership, permissions, timestamps, size, and addresses needed to locate file data. Directory contents and ordinary-file contents reside in data blocks; a directory is a special file containing name-to-inode mappings.
