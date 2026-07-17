# Question 23

*UGC NET CS · 2014 Dec Paper 2 · File Systems · Directory as a Symbol Table*

The directory can be viewed as ________ that translates filenames into their directory entries.

- **A.** Symbol table
- **B.** Partition
- **C.** Swap space
- **D.** Cache

> [!TIP]
> **Correct answer: A. Symbol table**

## Solution

A file-system directory maps human-readable file names to directory entries containing an inode number, file control block reference or equivalent metadata locator. That name-to-record mapping is the same abstract role performed by a symbol table.

## Key Points

- Directory lookup is a symbol-table operation: name→metadata/location entry.

## Why the other options are incorrect

A partition is a storage-region division, not a name map. Swap space backs virtual memory. A cache stores copies for faster access but does not define the directory's filename-translation role.
