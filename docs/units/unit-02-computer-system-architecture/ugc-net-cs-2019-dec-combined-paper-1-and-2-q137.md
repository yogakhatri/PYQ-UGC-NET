# Question 137

*UGC NET CS · 2019 Dec Paper 1 And 2 · Input-Output Organization · Isolated, Memory-Mapped and Asynchronous I/O*

Match List I with List II. List I: A. Isolated I/O; B. Memory-mapped I/O; C. I/O interface; D. Asynchronous data transfer. List II: I. same set of control signals for I/O and memory communication; II. separate instructions for I/O and memory communication; III. requires control signals to be transmitted between communicating units; IV. resolves differences between the central computer and peripherals.

- **1.** A-II, B-III, C-IV, D-I
- **2.** A-I, B-II, C-III, D-IV
- **3.** A-II, B-I, C-IV, D-III
- **4.** A-I, B-II, C-IV, D-III

> [!TIP]
> **Correct answer: 3. A-II, B-I, C-IV, D-III**

## Solution

Isolated I/O has a separate I/O address space and special input/output instructions, so A-II. Memory-mapped I/O places device registers in the memory address space and uses the ordinary memory addressing and control framework, so B-I. An I/O interface bridges differences in speed, data representation, and control between the central computer and peripherals, so C-IV. With asynchronous transfer, independently timed units coordinate by exchanging control signals such as request and acknowledge, so D-III. Thus A-II, B-I, C-IV, D-III is option 3.

## Key Points

- Isolated I/O uses special instructions; memory-mapped I/O reuses memory operations; interfaces adapt devices; asynchronous units handshake.

## Why the other options are incorrect

Option 1 gives memory-mapped I/O the separate-instruction property of isolated I/O and gives asynchronous transfer the memory-control property. Options 2 and 4 swap isolated and memory-mapped I/O. Their address-space distinction fixes the first two matches immediately.
