# Question 40

*UGC NET CS · 2015 Dec Paper 3 · Linux Operating Systems · Unix special files*

In Unix operating system, special files are used to :

- **1.** buffer data received in its input from where a process reads
- **2.** provide a mechanism to map physical device to file names
- **3.** store list of file names plus pointers associated with i-nodes
- **4.** store information entered by a user application program or utility program

> [!TIP]
> **Correct answer: 2. provide a mechanism to map physical device to file names**

## Solution

Unix represents devices through special files, conventionally under `/dev`. A character or block special file has a pathname and inode-like metadata that identify the device driver and device number, letting processes use ordinary file operations on physical devices. Thus special files map devices into the file-name namespace.

## Key Points

- Unix ‘everything is a file’: device special files give hardware devices pathnames and file-like access.

## Why the other options are incorrect

Option 1 describes a pipe or stream buffer, option 3 describes a directory, and option 4 describes a regular file containing application data.
