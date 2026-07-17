# Question 65

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Storage Management · RAID selection for transaction logs*

S8.ND:87015 Which RAID level is appropriate for storing the log file of a ticket booking system where a huge database update is required?

- **1.** Level 0
- **2.** Level 1
- **3.** Level 2
- **4.** Level 3

> [!TIP]
> **Correct answer: 2. Level 1**

## Solution

A transaction log is critical recovery data and is written frequently. RAID 1 mirrors every log write, providing redundancy with no parity-update penalty and allowing recovery if one disk fails.

## Key Points

- For critical write-heavy logs, simple mirroring prioritizes reliability and write behavior.

## Why the other options are incorrect

RAID 0 has no redundancy; RAID 2/3 use specialized striping/parity and are unsuitable for small frequent log writes compared with mirroring.
