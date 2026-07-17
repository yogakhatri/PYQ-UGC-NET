# Question 49

*UGC NET CS · 2014 Dec Paper 3 · Memory Hierarchy · Storage Access-Speed Hierarchy*

Which sequence arranges storage devices in increasing order of access speed?

- **A.** Magnetic tapes → magnetic disks → optical disks → electronic disks → main memory → cache → registers
- **B.** Magnetic tapes → magnetic disks → electronic disks → optical disks → main memory → cache → registers
- **C.** Magnetic tapes → electronic disks → magnetic disks → optical disks → main memory → cache → registers
- **D.** Magnetic tapes → optical disks → magnetic disks → electronic disks → main memory → cache → registers

> [!TIP]
> **Correct answer: D. Magnetic tapes → optical disks → magnetic disks → electronic disks → main memory → cache → registers**

## Solution

From slowest to fastest, sequential magnetic tape comes first. Optical disks normally have higher access latency than magnetic disks; solid-state/electronic disks are faster than rotating disks but slower than semiconductor main memory. Cache is faster than main memory, and CPU registers are fastest. The resulting order is tape → optical disk → magnetic disk → electronic disk → main memory → cache → registers.

## Key Points

- Increasing speed usually follows sequential external storage, rotating/optical storage, solid-state disk, RAM, cache, then registers.

## Why the other options are incorrect

A puts magnetic disk below optical disk in speed order. B places electronic disk below optical disk. C places electronic disk even below magnetic and optical storage. D preserves the standard hierarchy used by the question.
