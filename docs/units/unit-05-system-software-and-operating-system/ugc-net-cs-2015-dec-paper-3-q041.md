# Question 41

*UGC NET CS · 2015 Dec Paper 3 · File and Input/Output Systems · Unix File-System Layout*

Match the following in Unix file system : List - I List - II (a) Boot block (i) Information about file system (b) Super block (ii) Information about file (c) Inode table (iii) Storage space (d) Data block (iv) Code for making OS ready Codes : (a) (b) (c) (d)

- **1.** (iv) (i) (ii) (iii)
- **2.** (i) (iii) (ii) (iv)
- **3.** (iii) (i) (ii) (iv)
- **4.** (iv) (ii) (i) (iii)

> [!TIP]
> **Correct answer: 1. (iv) (i) (ii) (iii)**

## Solution

The boot block contains bootstrap code that helps make the OS ready: (a)–(iv). The superblock stores filesystem-wide metadata: (b)–(i). The inode table stores per-file metadata: (c)–(ii). Data blocks provide storage for file/directory contents: (d)–(iii). The sequence is (iv),(i),(ii),(iii).

## Key Points

- Boot block boots; superblock describes the filesystem; inodes describe files; data blocks hold contents.

## Why the other options are incorrect

The other codes place filesystem metadata, per-file metadata, boot code, or content storage in the wrong on-disk regions.
