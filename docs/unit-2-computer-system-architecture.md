# Unit 2: Computer System Architecture

[Project home](../README.md) · [All units](README.md) · [Official syllabus](syllabus.md)

## Contents

- [How to use this guide](#status-and-use)
- [Unit-wide exam playbook](#unit-wide-exam-playbook)
- [1. Digital Logic Circuits and Components](#chapter-1)
- [2. Data Representation](#chapter-2)
- [3. Register Transfer and Microoperations](#chapter-3)
- [4. Basic Computer Organization and Design](#chapter-4)
- [5. Programming the Basic Computer](#chapter-5)
- [6. Microprogrammed Control](#chapter-6)
- [7. Central Processing Unit](#chapter-7)
- [8. Pipeline and Vector Processing](#chapter-8)
- [9. Input-Output Organization](#chapter-9)
- [10. Memory Hierarchy](#chapter-10)
- [11. Multiprocessors](#chapter-11)
- [Coverage and quality notes](#coverage-and-quality-notes)

## Status and use

This guide contains all **14 question blocks currently recoverable and assigned to Unit 2** from the local UGC NET archive. Questions are arranged chapter-wise and numbered continuously through the unit.

> [!WARNING]
> This is a working extraction inventory, not a complete solved guide. **0 answers are validated and 14 remain pending** in this unit. Some unit and chapter placements use fallback routing, and OCR or missing figures can make questions incomplete.

Use this file for question discovery and broad chapter revision. The chapter notes and exam methods are general, not question-specific solutions. Full source paths, PDF pages and classification states remain in the structured data for auditing.

## Unit-wide exam playbook

- **Core idea:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.
- **Method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.
- **Rules/formulas:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.
- **Frequent traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

## Chapter-wise concepts and PYQs

<a id="chapter-1"></a>

### 1. Digital Logic Circuits and Components (1 questions)

**What to master:** Digital Computers; Logic Gates; Boolean Algebra; Map Simplifications; Combinational Circuits; Flip-Flops; Sequential Circuits; Integrated Circuits; Decoders; Multiplexers; Registers and Counters; Memory Unit.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 1

*UGC NET Nov 2021, original Q83*

> A digital computer has a common bus system for 8 registers 16 bits each. How many multiplexers are required to implement common bus? What size of multiplexers is required?

**Options**

1. 16, 8x1
2. 8, 16x1
3. 8, 8x1
4. 16, 16x1

**Chapter foundations**

This question belongs to the ideas covered by **Digital Logic Circuits and Components**. Revise these foundations: Digital Computers; Logic Gates; Boolean Algebra; Map Simplifications; Combinational Circuits; Flip-Flops; Sequential Circuits; Integrated Circuits; Decoders; Multiplexers; Registers and Counters; Memory Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Digital Logic Circuits and Components questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-2"></a>

### 2. Data Representation (0 questions)

**What to master:** Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._

<a id="chapter-3"></a>

### 3. Register Transfer and Microoperations (0 questions)

**What to master:** Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._

<a id="chapter-4"></a>

### 4. Basic Computer Organization and Design (0 questions)

**What to master:** Stored-Program Organization and Instruction Codes; Computer Registers; Computer Instructions; Timing and Control; Instruction Cycle; Memory-Reference Instructions; Input-Output; Interrupt.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._

<a id="chapter-5"></a>

### 5. Programming the Basic Computer (0 questions)

**What to master:** Machine Language; Assembly Language; Assembler; Program Loops; Subroutines; Input-Output Programming.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._

<a id="chapter-6"></a>

### 6. Microprogrammed Control (1 questions)

**What to master:** Control Memory; Address Sequencing; Design of Control Unit.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 2

*UGC NET Nov 2021, original Q90*

> Which of the following statement is true?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Control memory is part of the hardwired control unit.
> - **B.** Program control instructions are used to alter the sequential flow of the program.
> - **C.** The register indirect addressing mode for accessing memory operand is similar to displacement addressing mode.
> - **D.** CPU utilization is not affected by the introduction of Interrupts.

**Options**

1. A
2. B
3. C
4. D

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-7"></a>

### 7. Central Processing Unit (0 questions)

**What to master:** General Register Organization; Stack Organization; Instruction Formats; Addressing Modes; RISC; CISC.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._

<a id="chapter-8"></a>

### 8. Pipeline and Vector Processing (0 questions)

**What to master:** Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._

<a id="chapter-9"></a>

### 9. Input-Output Organization (1 questions)

**What to master:** Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 3

*UGC NET Nov 2021, original Q86*

> Arrange the following in the increasing order of complexity.
>
> **Additional extracted choices — check the source page:**
>
> - **A.** I/O Module
> - **B.** I/O processor
> - **C.** I/O Channel
> - **D.** DMA Choose the correct answer from the options given below

**Options**

1. D, C, B, A
2. C, D, A, B
3. A, B, C, D
4. A, D, C, B

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-10"></a>

### 10. Memory Hierarchy (8 questions)

**What to master:** Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 4

*UGC NET Nov 2021, original Q73*

> Given below are three statements related to interrupt handling mechanism A. Interrupt handler routine is not stored at a fixed address in the memory. B. CPU hardware has a dedicated wire called the interrupt request line used for handling interrupts C. Interrupt vector contains the memory addresses for speciaized interrupt handlers. In the context of above statements, choose the correct answer from the options given below:

**Options**

1. A is TRUE only
2. Both B and C are TRUE only
3. Both A and B are TRUE only
4. Both A, C are TRUE only

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 5

*UGC NET Nov 2021, original Q76*

> Read the following and answer the questions: Consider a machine with 16 GB main memory and 32‐bits virtual address space, with page size as 4KB. Frame size and page size is same for the given machine. The number of bits reserved for the frame offset is ______

**Options**

1. 12
2. 14
3. 32
4. 8

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 6

*UGC NET Nov 2021, original Q77*

> Read the following and answer the questions: Consider a machine with 16 GB main memory and 32‐bits virtual address space, with page size as 4KB. Frame size and page size is same for the given machine. Find number of pages required for the given virtual address space

**Options**

1. 2
2. 2
3. 2
4. 2

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 7

*UGC NET Nov 2021, original Q78*

> Read the following and answer the questions: Consider a machine with 16 GB main memory and 32‐bits virtual address space, with page size as 4KB. Frame size and page size is same for the given machine. What is the minimum number of bits needed for the physical address?

**Options**

1. 28
2. 34
3. 24
4. 12

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 8

*UGC NET Nov 2021, original Q79*

> Read the following and answer the questions: Consider a machine with 16 GB main memory and 32‐bits virtual address space, with page size as 4KB. Frame size and page size is same for the given machine. What is the size of page table for handling the given virtual address space, given that each page table entry is of size 2 bytes?

**Options**

1. 2MB
2. 2KB
3. 32MB
4. 12KB

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 9

*UGC NET Nov 2021, original Q80*

> Read the following and answer the questions: Consider a machine with 16 GB main memory and 32‐bits virtual address space, with page size as 4KB. Frame size and page size is same for the given machine. If a process of size 34KB is to be executed on this machine, then what will be the size of internal fragmentation for this process?

**Options**

1. 4KB
2. Zero
3. 1KB
4. 2KB

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 10

*UGC NET Nov 2021, original Q88*

> The cache coherence problem can be solved
>
> **Additional extracted choices — check the source page:**
>
> - **A.** by having multiport memory
> - **B.** allow only nonshared data to be stored in cache
> - **C.** using a snoopy cache controller
> - **D.** uisng memory interleaving Choose the correct answer from the options given below:

**Options**

1. A and C only
2. B and C only
3. D and C only
4. B and D only

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 11

*UGC NET Nov 2021, original Q89*

> Given below are two statements 10 20 30 12 10 16 8 8 8 8 8 Statement I: CISC computers have a large of number of addressing modes. Statement II: In RISC machines memory access is limited to load and store instructions. In light of the above statements, choose the correct answer from the options given below

**Options**

1. Both Statement I and Statement II are true
2. Both Statement I and Statement II are false
3. Statement I is true but Statement II is false
4. Statement I is false but Statement II is true

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-11"></a>

### 11. Multiprocessors (3 questions)

**What to master:** Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 12

*UGC NET Nov 2021, original Q26*

> For which value of n is Wheel graph W regular?

**Options**

1. 2
2. 3
3. 4
4. 5

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 13

*UGC NET Nov 2021, original Q31*

> Which of the following languages are not regular? A. L={ (01) 0 | n > k, k>=0 } B. L={ c b a | n >= 0, k>=0 } C. L={ 0 1 | n≠k } Choose the correct answer from the options given below:

**Options**

1. A and B only
2. A and C only
3. B and C only
4. A, B and C

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 14

*UGC NET Nov 2021, original Q82*

> The Octal equivalent of hexadecimal (D.C) is:

**Options**

1. (15.6)
2. (61.6)
3. (15.3)
4. (61.3)

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

## Coverage and quality notes

- Recovered question blocks in this unit: **14**
- Chapter placements with direct keyword support: **11**
- Chapter placements needing manual review: **3**
- Questions with validated answers in this guide: **0**
- OCR may flatten mathematical notation, tables, code indentation, and figures. Full audit references are retained in the structured data.
- Some combined Paper 1/Paper 2 scans and older papers lack a trustworthy embedded key. Such questions remain pending rather than receiving guessed answers.

---

[Back to contents](#contents) · [All units](README.md) · [Project home](../README.md)

