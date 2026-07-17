# Question 141

*UGC NET CS · 2020 Nov With Answers · Memory Hierarchy · Magnetic-Disk Track and Surface Capacity*

If T is the capacity of one track in bytes and S is the capacity of one surface in bytes, what is (T,S)?

- **1.** (50 K, 50,000 K)
- **2.** (25 K, 25,000 K)
- **3.** (25 K, 50,000 K)
- **4.** (40 K, 36,000 K)

> [!TIP]
> **Correct answer: 3. (25 K, 50,000 K)**

## Solution

One track contains 50 sectors, each of 512 bytes. Therefore T=50×512=25,600 bytes=25 KBytes when K=1,024 bytes. One surface contains 2,000 such tracks, so S=2,000×25 KBytes=50,000 KBytes. Hence (T,S)=(25 K, 50,000 K), which is option 3.

## Key Points

- Track capacity = sectors per track × bytes per sector; surface capacity = tracks per surface × track capacity.

## Why the other options are incorrect

Option 1 doubles the track capacity. Option 2 uses only 1,000 tracks when finding surface capacity. Option 4 matches neither the 50-sector track nor the 2,000-track surface specified in the question.
