# Question 54

*UGC NET CS · 2015 June Paper 3 · File and Input/Output Systems · Unix File Types*

A unix file may be of the type :

- **1.** Regular file
- **2.** Directory file
- **3.** Device file
- **4.** Any one of the above

> [!TIP]
> **Correct answer: 4. Any one of the above**

## Solution

Unix represents many resources through the file abstraction. It has regular files for data, directory files that map names to file identifiers, and special device files that provide interfaces to character or block devices. Therefore a Unix file may be any of the listed types.

## Key Points

- Unix's uniform file model includes regular, directory, and device-special files, among other types.

## Why the other options are incorrect

Options 1–3 each name a valid Unix file type but omit the other valid categories. The inclusive option is required.
