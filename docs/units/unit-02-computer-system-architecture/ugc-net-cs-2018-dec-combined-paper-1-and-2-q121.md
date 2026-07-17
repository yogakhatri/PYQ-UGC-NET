# Question 121

*UGC NET CS · 2018 Dec Paper 1 And 2 · Memory Hierarchy · Dirty Bit and Write-Back*

A dirty bit is used to show:

- **1.** a wrong page
- **2.** a page with corrupted data
- **3.** a page with low frequency of occurrence
- **4.** a page that is modified after being loaded into cache memory

> [!TIP]
> **Correct answer: 4. a page that is modified after being loaded into cache memory**

## Solution

A dirty or modified bit is set when a cache block/page has been written since it was loaded. In a write-back system, a clean block can be discarded because the lower-level copy is current, but a dirty block must be written back before replacement. Therefore the bit identifies a page modified after being loaded into cache memory, option 4.

## Key Points

- Dirty means modified relative to the backing copy; eviction requires a write-back.

## Why the other options are incorrect

The bit does not signal an invalid address, corrupted contents, or low access frequency. Validity, error detection, and replacement-frequency information require different metadata or mechanisms.
