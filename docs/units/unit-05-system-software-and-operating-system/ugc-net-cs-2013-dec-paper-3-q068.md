# Question 68

*UGC NET CS · 2013 Dec Paper 3 · Windows Operating Systems · Hardware Abstraction Layer*

In the Windows 2000 operating system, all processor-dependent code is isolated in a dynamic-link library called the

- **A.** NTFS file system
- **B.** Hardware abstraction layer
- **C.** Microkernel
- **D.** Process Manager

> [!TIP]
> **Correct answer: B. Hardware abstraction layer**

## Solution

Windows isolates low-level, platform- and processor-dependent operations behind the Hardware Abstraction Layer (HAL). In the Windows 2000 architecture this layer is supplied as HAL.DLL, allowing the kernel and device drivers to use a stable interface across different hardware configurations.

## Key Points

- HAL hides hardware-specific details from the rest of Windows; historically its binary is HAL.DLL.

## Why the other options are incorrect

NTFS is a file system, not the processor-abstraction library. The microkernel contains core scheduling and interrupt mechanisms but is not the named DLL boundary in the question. Process Manager is an executive component concerned with processes, not processor-dependent hardware access.

## References

- [Microsoft Learn - Windows kernel-mode HAL library](https://learn.microsoft.com/en-au/windows-hardware/drivers/kernel/windows-kernel-mode-hal-library)
