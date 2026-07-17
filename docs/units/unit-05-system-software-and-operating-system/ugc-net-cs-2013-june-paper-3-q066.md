# Question 66

*UGC NET CS · 2013 June Paper 3 · Windows File Systems · FAT and NTFS Support*

The versions of windows operating system like windows XP and window Vista uses following file system :

- **A.** FAT-16
- **B.** FAT-32
- **C.** NTFS (NT File System)
- **D.** All of the above

> [!TIP]
> **Correct answer: D. All of the above**

## Solution

Windows XP and Vista-era Windows can recognize and use FAT16, FAT32 and NTFS volumes, so all three listed file systems are within their support. NTFS is the native and normally preferred system-disk format because it adds permissions, journaling, compression, quotas and other features, but support is broader than the default recommendation.

## Key Points

- Distinguish a Windows version's supported file systems from its preferred/default system-volume format.

## Why the other options are incorrect

A, B and C each name a supported file system but exclude the other supported choices. If the question had asked for the usual installation/default system volume, NTFS would be the better wording; as printed, 'uses' is broad enough that all of the above is intended.
