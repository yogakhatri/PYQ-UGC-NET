# Question 10

*UGC NET CS · 2012 June Paper 2 · Database Languages and Interfaces · xBase Copy Commands*

Which command is the fastest among the following ?

- **A.** COPY TO <NEW FILE>
- **B.** COPY STRUCTURE TO <NEW FILE>
- **C.** COPY FILE <FILE 1> <FILE 2>
- **D.** COPY TO MFILE-DAT DELIMITED

> [!TIP]
> **Correct answer: B. COPY STRUCTURE TO <NEW FILE>**

## Solution

COPY STRUCTURE TO creates only a new empty DBF definition containing field names, types and widths. It does not read, convert or write the table's data records, so among the listed operations it has the least work and is the expected fastest command.

## Key Points

- Copying metadata/structure only is faster than copying or converting all stored records.

## Why the other options are incorrect

COPY TO copies records into another table. COPY FILE duplicates the entire file byte-for-byte, including all data. COPY TO ... DELIMITED must read records, convert fields to delimited text and write that output, usually making it the most processing-intensive choice.
