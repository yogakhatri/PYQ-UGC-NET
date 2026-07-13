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

This guide contains all **394 question blocks currently recoverable and assigned to Unit 2** from the local UGC NET archive. Questions are arranged chapter-wise and numbered continuously through the unit.

> [!WARNING]
> This is a working extraction inventory, not a solved guide. All answers remain unvalidated. Some unit and chapter placements use fallback routing, and OCR or missing figures can make questions incomplete.

Use this file for question discovery and broad chapter revision. The chapter notes and exam methods are general, not question-specific solutions. Full source paths, PDF pages and classification states remain in the structured data for auditing.

## Unit-wide exam playbook

- **Core idea:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.
- **Method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.
- **Rules/formulas:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.
- **Frequent traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

## Chapter-wise concepts and PYQs

<a id="chapter-1"></a>

### 1. Digital Logic Circuits and Components (11 questions)

**What to master:** Digital Computers; Logic Gates; Boolean Algebra; Map Simplifications; Combinational Circuits; Flip-Flops; Sequential Circuits; Integrated Circuits; Decoders; Multiplexers; Registers and Counters; Memory Unit.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 1

*UGC NET Dec 2009, Paper II, original Q7*

> Identify the logic function performed by the circuit shown (A) exclusive OR (B) exclusive NOR (C) NAND (D) NOR

**Chapter foundations**

This question belongs to the ideas covered by **Digital Logic Circuits and Components**. Revise these foundations: Digital Computers; Logic Gates; Boolean Algebra; Map Simplifications; Combinational Circuits; Flip-Flops; Sequential Circuits; Integrated Circuits; Decoders; Multiplexers; Registers and Counters; Memory Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Digital Logic Circuits and Components questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 2

*UGC NET June 2010, Paper II, original Q10*

> The function represented by the k- map given below is BC A 1 0 0 1 1 0 0 1 (A) A ⋅ B (B) AB + BC + CA (C) B ⊕ C (D) A ⋅ B ⋅ C

**Chapter foundations**

This question belongs to the ideas covered by **Digital Logic Circuits and Components**. Revise these foundations: Digital Computers; Logic Gates; Boolean Algebra; Map Simplifications; Combinational Circuits; Flip-Flops; Sequential Circuits; Integrated Circuits; Decoders; Multiplexers; Registers and Counters; Memory Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Digital Logic Circuits and Components questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 3

*UGC NET Dec 2011, Paper III, original Q9*

> Obtain the logic diagram of a master-slave JK flip flop with AND and NOR Gates, include provision for setting and clearing the flip flop asynchronously. _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________

**Chapter foundations**

This question belongs to the ideas covered by **Digital Logic Circuits and Components**. Revise these foundations: Digital Computers; Logic Gates; Boolean Algebra; Map Simplifications; Combinational Circuits; Flip-Flops; Sequential Circuits; Integrated Circuits; Decoders; Multiplexers; Registers and Counters; Memory Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Digital Logic Circuits and Components questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 4

*UGC NET June 2012, Paper II, original Q36*

> Which of the following logic families is well suited for high-speed operations ? (A) TTL (B) ECL (C) MOS (D) CMOS

**Chapter foundations**

This question belongs to the ideas covered by **Digital Logic Circuits and Components**. Revise these foundations: Digital Computers; Logic Gates; Boolean Algebra; Map Simplifications; Combinational Circuits; Flip-Flops; Sequential Circuits; Integrated Circuits; Decoders; Multiplexers; Registers and Counters; Memory Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Digital Logic Circuits and Components questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 5

*UGC NET Dec 2013, Paper II, original Q49*

> How much space will be required to store the bit map of a 1.3 GB disk with 512 bytes block size ? (A) 332.8 KB (B) 83.6 KB (C) 266.2 KB (D) 256.6 KB

**Chapter foundations**

This question belongs to the ideas covered by **Digital Logic Circuits and Components**. Revise these foundations: Digital Computers; Logic Gates; Boolean Algebra; Map Simplifications; Combinational Circuits; Flip-Flops; Sequential Circuits; Integrated Circuits; Decoders; Multiplexers; Registers and Counters; Memory Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Digital Logic Circuits and Components questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 6

*UGC NET Dec 2013, Paper III, original Q22*

> What are the final values of Q 1 and Q0 after 4 clock cycles, if initial values are 00 in the sequential circuit shown below : (A) 11 (B) 10 (C) 01 (D) 00

**Chapter foundations**

This question belongs to the ideas covered by **Digital Logic Circuits and Components**. Revise these foundations: Digital Computers; Logic Gates; Boolean Algebra; Map Simplifications; Combinational Circuits; Flip-Flops; Sequential Circuits; Integrated Circuits; Decoders; Multiplexers; Registers and Counters; Memory Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Digital Logic Circuits and Components questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 7

*UGC NET June 2013, Paper III, original Q57*

> If f( x, y) is a digital image, then x, y and amplitude values of f are (A) Finite (B) Infinite (C) Neither finite nor infinite (D) None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Digital Logic Circuits and Components**. Revise these foundations: Digital Computers; Logic Gates; Boolean Algebra; Map Simplifications; Combinational Circuits; Flip-Flops; Sequential Circuits; Integrated Circuits; Decoders; Multiplexers; Registers and Counters; Memory Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Digital Logic Circuits and Components questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 8

*UGC NET Dec 2018, original Q104*

> Match each UML diagram in List I to its appropriate description in List II. List I List II (a) State Diagram (i) Describes how the external entities (people, devices) can interact with the system. (b) Use-Case Diagram (ii) Used to describe the static or structural view of a system. (c) Class Diagram (i) Used to show the flow of a business process, the steps of a use-case or the logic of an object behaviour. (d) Activity Diagram (iv) Used to describe the dynamic behaviour of objects and could also be used to describe the entire system behaviour. Code: (a)-(i), (b)-(iv), (c)-(iii, (d)-(ili) 91394342414. (a)-(iv), (b)-(ii), (c)-(i), (d)-(ili) 91394342415. (a)-(i), (b)-(iv), (c)-(ii, (d)-(ii) 91394342416. (a)-(iv), (b)-(i), (c)-(ii), (d)-(ili) ingle Line Question Option: No

**Chapter foundations**

This question belongs to the ideas covered by **Digital Logic Circuits and Components**. Revise these foundations: Digital Computers; Logic Gates; Boolean Algebra; Map Simplifications; Combinational Circuits; Flip-Flops; Sequential Circuits; Integrated Circuits; Decoders; Multiplexers; Registers and Counters; Memory Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Digital Logic Circuits and Components questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 9

*UGC NET Dec 2018, original Q115*

> The Third Generation mobile phones are digital and based on Options: Guide 91394342457. AMPS Personal Exam 91394342458. D-AMPS 91394342459. CDMA 91394342460. Broadband CDMA Single Lie Quet ons: on: No Op: 90303130 Veru Vern aye: MCQ Option Shufting : Yes

**Chapter foundations**

This question belongs to the ideas covered by **Digital Logic Circuits and Components**. Revise these foundations: Digital Computers; Logic Gates; Boolean Algebra; Map Simplifications; Combinational Circuits; Flip-Flops; Sequential Circuits; Integrated Circuits; Decoders; Multiplexers; Registers and Counters; Memory Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Digital Logic Circuits and Components questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 10

*UGC NET Nov 2021, original Q83*

> (15.6) A digital computer has a common bus system for 8 registers 16 bits each. How many multiplexers are required to implement common bus? What size of multiplexers is required? 1. 16, 8x1 2. 8, 16x1 3. 8, 8x1 4. 16, 16x1

**Chapter foundations**

This question belongs to the ideas covered by **Digital Logic Circuits and Components**. Revise these foundations: Digital Computers; Logic Gates; Boolean Algebra; Map Simplifications; Combinational Circuits; Flip-Flops; Sequential Circuits; Integrated Circuits; Decoders; Multiplexers; Registers and Counters; Memory Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Digital Logic Circuits and Components questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 11

*UGC NET Dec 2025 session (Jan 2026), original Q112*

> Question Number: 112 C. In NRZ- L, the level of the signal is dependent upon the state of the bit. D. In NRZ-I, the signal is not inverted of a 1 is an encountered. E. RZ encoding scheme removes both DC components and problem of synchronization. Choose the correct answer from the options given below: 1. A, B, C & E Only 2. A, C, D & E Only 3. B, C, D & E Only 4. A, B, D & E Only 6119878846.2 6119878847.3 6119878848.4 Number: Yes

**Chapter foundations**

This question belongs to the ideas covered by **Digital Logic Circuits and Components**. Revise these foundations: Digital Computers; Logic Gates; Boolean Algebra; Map Simplifications; Combinational Circuits; Flip-Flops; Sequential Circuits; Integrated Circuits; Decoders; Multiplexers; Registers and Counters; Memory Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Digital Logic Circuits and Components questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-2"></a>

### 2. Data Representation (138 questions)

**What to master:** Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 12

*UGC NET Dec 2009, Paper II, original Q10*

> How many 1’s are present in the binary representation of 3 × 512 + 7 × 64 + 5 × 8 + 3 (A) 8 (B) 9 (C) 10 (D) 11

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 13

*UGC NET Dec 2009, Paper II, original Q20*

> Which of the following statement is wrong ? I. 2-phase locking protocol suffer from dead lock. II. Time stamp protocol suffer from more aborts. III. A block hole in a DFD is a data store with only inbound flow s. IV. Multivalued dependency among attribute is checked at 3 NF level. V. An entity-relationship diagram is a tool to represent eve nt model. (A) I, II, II (B) II, III, IV (C) III, IV, V (D) I I, IV, V

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 14

*UGC NET June 2010, Paper II, original Q26*

> The ______ field is the SNMP PDV reports an error in a response message. (A) error index (B) error status (C) set request (D) agent index

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 15

*UGC NET June 2012, Paper II, original Q16*

> In which circuit switching, delivery of data is delayed because data must be stored and retrieved from RAM ? (A) Space division (B) Time division (C) Virtual (D) Packet www.solutionsadda.in

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 16

*UGC NET Dec 2013, Paper II, original Q20*

> The correct way to round off a floating number x to an integer value is (A) y = (int) ( x + 0.5) (B) y = int ( x + 0.5) (C) y = (int) x + 0.5 (D) y = (int) ((int) x + 0.5)

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 17

*UGC NET Dec 2013, Paper II, original Q32*

> Given that (292) 10 = (1204) x in some number system x. The base x of that number system is (A) 2 (B) 8 (C) 10 (D) None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 18

*UGC NET Dec 2013, Paper III, original Q17*

> The compiler converts all operands upto the type of the largest operand is called (A) Type Promotion (B) Type Evaluation (C) Type Conversion (D) Type Declaration

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 19

*UGC NET Dec 2013, Paper III, original Q52*

> Serial access memories are useful in applications where (A) Data consists of numbers (B) Short access time is required (C) Each stored word is processed differently. (D) None of these

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 20

*UGC NET Dec 2013, Paper III, original Q55*

> Consider the following ER diagram : The minimum number of tables required to represent M, N, P, R 1, R2 is (A) 2 (B) 3 (C) 4 (D) 5

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 21

*UGC NET June 2013, Paper III, original Q27*

> Bresenham line drawing algorithm is attractive because it uses (A) Real arithmetic only (B) Integer arithmetic only (C) Floating point arithmetic (D) Real and integer arithmetic

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 22

*UGC NET June 2013, Paper III, original Q31*

> Images tend to be very large collection of data. The size of memory required for a 1024 by 1024 image in which the colour of each pixel is represented by a n-bit number, (in an 8 bit machines) is (A) n × 8 MB (B) n / 8 MB (C) (1024 × 1024) / 8 MB (D) 1024 MB

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 23

*UGC NET June 2013, Paper III, original Q44*

> Interrupt which arises from illegal or erroneous use of an instruction or data is (A) Software interrupt (B) Internal interrupt (C) External interrupt (D) All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 24

*UGC NET Dec 2014, Paper II, original Q9*

> The range of representable normalized numbers in the floating point binary fractional representation in a 32-bit word with 1-bit sign, 8-bit excess 128 bias ed exponent and 23-bit mantissa is (A) 2 –128 to (1 – 2 –23 ) × 2 127 (B) (1 – 2 –23 ) × 2 –127 to 2 128 (C) (1 – 2 –23 ) × 2 –127 to 2 23 (D) 2 –129 to (1 – 2 –23 ) × 2 127

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 25

*UGC NET Dec 2014, Paper III, original Q6*

> Specify the contents of the accumulator and the status of the S, Z and CY flags when 8085 microprocessor performs addition of 87 H and 79 H. (A) 11, 1, 1, 1 (B) 10, 0, 1, 0 (C) 01, 1, 0, 0 (D) 00, 0, 1, 1

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 26

*UGC NET Dec 2014, Paper III, original Q16*

> Consider a triangle represented by A(0, 0), B(1, 1), C(5, 2). The t riangle is rotated by 45 degrees about a point P(–1, –1). The co-ordinates of the new triangle obt ained after rotation shall be _______ (A) A' ( )–1, 2 – 1 , B' ( )–1, 2 2 – 1 , C'  3 2 2 – 1 , 9 2 2 – 1 (B) A' ( )2 – 1, –1 , B' ( )2 2 – 1, –1 , C'  3 2 2 – 1 , 9 2 2 – 1 (C) A' ( )–1, 2 – 1 , B' ( )2 2 – 1, –1 , C'  3 2 2 – 1 , 9 2 2 – 1 (D) A' ( )–1, 2 – 1 , B' ( )2 2 – 1, –1 , C'  9 2 2 – 1 , 3 2 2 – 1

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 27

*UGC NET June 2015, Paper II, original Q1*

> Write your roll number in the space provided on the top of this page.

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 28

*UGC NET June 2015, Paper III, original Q1*

> Write your roll number in the space provided on the top of

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 29

*UGC NET June 2015, Paper III, original Q66*

> In a binary Hamming Code the number of check digits is r then number of message digits is equal to : (1) 2*-1 2) 2'-r-1 (3) 25-r+ 1 (4) 2"+r-1

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 30

*UGC NET June 2015, Paper III, original Q67*

> In the Hungarian method for solving assignment problem, an optimal assignment requires that the maximum number of lines that can be drawn through squares with zero opportunity cost be equal to the number of : (1) rows or columns (2) rows + columns (3) rows + columns - 1 (4) rows + columns +1

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 31

*UGC NET July 2016, Paper II, original Q7*

> The IEEE-754 double-precision format to repr esent floating point numbers, has a length of _____ bits. (1) 16 (2) 32 (3) 48 (4) 64

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 32

*UGC NET July 2016, Paper II, original Q18*

> In a relational database model, NULL values can be used for all but which one of the following ? (1) To allow duplicate tuples in the table by filling the primary key column(s) with NULL. (2) To avoid confusion with actual legitimate data values like 0 (zero) for integer columns and ’’ (the empty string) for string columns. (3) To leave columns in a tuple marked as ’’unknown’’ when the actual value is unknown. (4) To fill a column in a tuple when that column does not really ”exist” for that particular tuple.

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 33

*UGC NET July 2016, Paper II, original Q48*

> Pipelining improves performance by : (1) decreasing instruction latency (2) eliminating data hazards (3) exploiting instruction level parallelism (4) decreasing the cache miss rate

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 34

*UGC NET July 2016, Paper III, original Q17*

> Let us consider that the original point is ( x, y) and new transformed point is ( x′, y ′). Further, Sh x and Sh y are shearing factors in x and y directions. If we perform the y-direction shear relative to x = xref then the transformed point is given by _______. (1) x′ = x + Shx ⋅ (y – yref) (2) x′ = x y ′ = y y ′ = y ⋅ Shx (3) x′ = x (4) x′ = Shy ⋅ y y′ = Shy (x – xref) + y y ′ = y ⋅ (x – xref)

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 35

*UGC NET Jan 2017, Paper II, original Q10*

> The hexadecimal equivalent of the octal number 2357 is : (1) 2EE (2) 2FF (3) 4EF (4) 4FE

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 36

*UGC NET Jan 2017, Paper II, original Q15*

> If X is a binary number which is power of 2, then the value of X & (X – 1) is : (1) 11….11 (2) 00…..00 (3) 100…..0 (4) 000……1

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 37

*UGC NET Jan 2017, Paper II, original Q18*

> Let M and N be two entities in an E-R diagram with simple sing le value attributes. R 1 and R2 are two relationship between M and N, where as R 1 is one-to-many and R 2 is many-to-many. The minimum number of tables required to represent M, N, R 1 and R 2 in the relational model are _______. (1) 4 (2) 6 (3) 7 (4) 3

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 38

*UGC NET Jan 2017, Paper III, original Q34*

> The minimum number of scalar multiplicati on required, for parenthe sization of a matrix- chain product whose sequence of dimensions for four matrices is <5, 10, 3, 12, 5> is (1) 630 (2) 580 (3) 480 (4) 405

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 39

*UGC NET Jan 2017, Paper III, original Q64*

> Let C be a binary linear code with minimu m distance 2t + 1 then it can correct upto _____ bits of error. (1) t + 1 (2) t (3) t – 2 (4) t 2

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 40

*UGC NET Nov 2017, Paper II, original Q7*

> The Octal equivalent of the binary number 1011101011 is : (1) 7353 (2) 1353 (3) 5651 (4) 5657

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 41

*UGC NET Dec 2018, original Q60*

> In computers, subtraction is generally carried out by 's complement 91394342238. 1's complement ional Exam Guide. 91394342239. 10's complement 91394342240. 2's complement

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 42

*UGC NET Dec 2018, original Q63*

> ingle Line Question Option: No

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 43

*UGC NET Dec 2018, original Q64*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 44

*UGC NET Dec 2018, original Q66*

> The decimal floating point number -40.1 represented using IEEE-754 32-bit representation and written in hexadecimal form is xC2206666 91394342262. 0xC2206000 91394342263. 0xC2006666 91394342264. 0xC2006000 Single Line Question pion: No Option Orient on: Vertype: MCQ

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 45

*UGC NET Dec 2018, original Q73*

> Consider two sequences X and Y: X = <0, 1, 2, 1, 3, 0, 1> Y = <1, 3, 2, 0, 1, 0> The length of longest common subsequence between X and Y is 91394342290. 3 91394342291. 4 91394342292. 5 ingle Line Question Option: No

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 46

*UGC NET Dec 2018, original Q89*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 47

*UGC NET Dec 2018, original Q92*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 48

*UGC NET Dec 2018, original Q96*

> Consider the following pseudo-code fragment, where m is a non-negative integer that has been initialized: p = 0; k= 0; while (k < m) p=p + 25; k=k + 1; end while Which of the following is a loop invariant for the while statement? (Note : a loop invariant for a while statement is an assertion that is true each time the guard is evaluated during the execution of the while statement). Options: p= 2k- 1 and 0≤k< m 91394342381.

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 49

*UGC NET Dec 2018, original Q98*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 50

*UGC NET Dec 2018, original Q99*

> What does the following Java function perform ? (Assume int occupies four bytes of storage) publie static int f(int a) { //Pre-conditions : a > 0 and no overflow/underflow occurs int b = 0; for (int i = 0; i < 32; i++) b= b << 1; b=b | (a & 1); a = a >>> 1;// This is a logical shift } return b; } . Returns the int that has the binary representation of integer a. 91394342394 Return the int that has the reversed binary representation of integer a. 91394342395. Return the int that represents the number of 1's in the binary representation of integer a. 91394342396. Return the int that represents the number of O's in the binary representation of integer a.

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 51

*UGC NET Dec 2018, original Q100*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 52

*UGC NET Dec 2018, original Q106*

> Consider the following method : int f (int m, int n, boolean x, boolean y) int res = 0; if (m < 0) fres = n- m:) else if (x || y) { res = - 1; if (n == m) fres = 1;) } else fres = n;} return res; ) /* end off*/ If P is the minimum number of tests to achieve full statement coverage for fO, and Q is the minimum number of tests to achieve full branch coverage for fi), then (P, Q) = 'our Personal Exam . (3,4) 91394342422. (4,3) (2,3) 91394342423. 91394342424 (3,2)

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 53

*UGC NET Dec 2018, original Q108*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 54

*UGC NET Dec 2018, original Q126*

> Question Number: 126

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 55

*UGC NET Dec 2018, original Q127*

> An attribute A of datatype varchar(20) has the value 'xyz', and the attribute B of datatype char(20) has the value "Imnop", then the attribute A has _ spaces and attribute B has_ _ spaces. Options : Your Personal Exam Gl 91394342505. 3,5 20,20 91394342506. 91394342507. 3, 20 20,5 91394342508.

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 56

*UGC NET Dec 2018, original Q130*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 57

*UGC NET Dec 2018, original Q134*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 58

*UGC NET July 2018, Paper II, original Q95*

> The hexadecimal equivalent of the binary integer number 110101101 is : (1) D24 (2) 1 B D (3) 1 A E (4) 1 A D

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 59

*UGC NET Dec 2019, original Q51*

> Question Number: 51

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 60

*UGC NET Dec 2019, original Q62*

> rsonal Exal Given following equation: (142) + (112) o-2= (75)g. find base b. (1) 3 (2) 6 (3) 7 (4) 5 61547540946. 2 61547540947.3 61547540948.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 61

*UGC NET Dec 2019, original Q64*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 62

*UGC NET Dec 2019, original Q85*

> Let a"modn = (a) modn and a?+ modn=a (a) modn. For a = 7. b=17 and n=561. what is the value of a (modn)? (1) 160 (2) 166 (3) 157 (4) 67 xam 'sonal 61547541038.2 61547541039. 3 61547541040. 4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 63

*UGC NET Dec 2019, original Q90*

> Consider a weighted directed graph. The current shortest distance from source S to node x is represented by d[x]. Let d[v]= 29, d[u]=15, w[u. v]=12. What is the updated value of d[ul based on current information? (1) 29 (2) 27 (3) 25 (4) 17 61547541058. 2 61547541059.3 61547541060. 4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 64

*UGC NET Dec 2019, original Q110*

> Persona our

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 65

*UGC NET Dec 2019, original Q119*

> Which of the following binary codes for decimal digits are self complementing? (a) 8421 code (b) 2421 code (c) excess-3 code (d) excess-3 gray code O Choose the correct option: (1) (a) and (b) (2) (b) and (c) (3) (c) and (d) (4) (d) and (a) 61547541174.2 61547541175.3 61547541176. 4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 66

*UGC NET Dec 2019, original Q125*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 67

*UGC NET Dec 2019, original Q137*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 68

*UGC NET Dec 2019, original Q141*

> How many nodes are there in flowgraph F? (1) 9 (2) 10 (3) 11 (4) 12 61547541262. 2 61547541263.3 61547541264.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 69

*UGC NET Dec 2019, original Q143*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 70

*UGC NET June 2019, original Q59*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 71

*UGC NET June 2019, original Q60*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 72

*UGC NET June 2019, original Q65*

> What will be the number of states when a MOD-2 counter is followed by a MOD-S counter? 1. 5 2. 10 sona our Persi 3. 15 er: 4. 20 64635085596. 2 64635085597.3 64635085598. 4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 73

*UGC NET June 2019, original Q68*

> Consider the equation (146), + (313)6-2 = (240),. Which of the following is the value of b? 8 xam 2. 7 3. 10 4. 16 our 64635085608. 2 64635085609. 3 64635085610.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 74

*UGC NET June 2019, original Q69*

> How many address lines and data lines are required to provide a memory capacity of 16K × 16? 1. 10,4 2. 16,16 3. 14,16 4. 4,16 64635085612.2 64635085613.3 64635085614.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 75

*UGC NET June 2019, original Q70*

> Suppose that a computer program takes 100 seconds of execution time on a computer with multiplication operation responsible for 80 seconds of this time. How much do you have to improve the speed of multiplication operation if you are asked to execute this program four times faster? 1. 14 times faster 15 times faster 16 times faster 17 times faster 64635085616.2 64635085617.3 64635085618. 4 Single Line Ouestion Option: No

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 76

*UGC NET June 2019, original Q71*

> Your

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 77

*UGC NET June 2019, original Q72*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 78

*UGC NET June 2019, original Q73*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 79

*UGC NET June 2019, original Q74*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 80

*UGC NET June 2019, original Q79*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 81

*UGC NET June 2019, original Q83*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 82

*UGC NET June 2019, original Q87*

> Which of the following statements are DML statements? (a) Update [tablename] Set [columnname] = VALUE (b) Delete [tablename] (c) Select * from [tablename] 1. (a) and (b) 2. (a) and (d) repp 3. (a), (b) and (c) irsonal Exam Guidel 4. (b) and (c) 64635085684. 2 64635085685. 3 64635085686. 4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 83

*UGC NET June 2019, original Q89*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 84

*UGC NET June 2019, original Q90*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 85

*UGC NET June 2019, original Q92*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 86

*UGC NET June 2019, original Q101*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 87

*UGC NET June 2019, original Q107*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 88

*UGC NET June 2019, original Q109*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 89

*UGC NET June 2019, original Q111*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 90

*UGC NET June 2019, original Q113*

> Consider the Euler's phi function given by where p runs over all the primes dividing n. What is the value of (45) ? 3 2. 12 6 24 Options :

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 91

*UGC NET June 2019, original Q116*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 92

*UGC NET June 2019, original Q117*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 93

*UGC NET June 2019, original Q123*

> Replacing the expression 4* 2-14 by 8•56 is known as constant folding 2. induction variable 3. strength reduction code reduction 64635085828.2 64635085829.3 64635085830. 4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 94

*UGC NET June 2019, original Q124*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 95

*UGC NET June 2019, original Q127*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 96

*UGC NET June 2019, original Q128*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 97

*UGC NET June 2019, original Q129*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 98

*UGC NET June 2019, original Q140*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 99

*UGC NET June 2019, original Q141*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 100

*UGC NET June 2019, original Q142*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 101

*UGC NET June 2019, original Q149*

> The value of the derivative of Sigmoid function given by 1 f(x) = 1+e-2x at x = 0 is 0 1 repp rsonal Exam Guide. 4. 00 64635085932. 2 64635085933.3 64635085934.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 102

*UGC NET Nov 2020, original Q59*

> Consider the following pseudo-code fragment, where a and b are integer variables that have been initialized: /• Pre-conditions : (a > 1 a < b) •/ /* Assume that overflow never occurs */ int x = 0; int p = 1; while (p <b){ P = p*a; x= x+1; } When the while loop terminates. what will be the value of x in terms of a and b? (1) a" (2) ba (3) [log.] /- 1 ] means floor +/ (4) logal/• 1 means ceil -/ , 1 53622816734.2 53622816735.3 53622816736.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 103

*UGC NET Nov 2020, original Q62*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 104

*UGC NET Nov 2020, original Q69*

> Which of the following UML diagrams has a static view? (1) Collaboration diagram (2) Use-Case diagram (3) State chart diagram (4) Activity diagram . I 53622816774. 2 53622816775.3 53622816776.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 105

*UGC NET Nov 2020, original Q73*

> A complete n-ary tree is a tree in which each node has n children or no children. Let I be the number of internal nodes and L be the number of leaves in a complete n-ary tree. If L=41. and I=10. What is the value of n? (1) 3 (2) 4 (3) 5 (4) 6 53622816790.2 53622816791.3 53622816792.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 106

*UGC NET Nov 2020, original Q81*

> 1111111111. This code has distance 5. If the code word arrived is 0000000111 then the Consider a code with only four valid code words: 0000000000, 0000011111. 1111100000, and original code word must be (1) 0000011111 (2) 0000000000 (3) 1111100000 (4) 1lll111111 53622816822. 2 53622816823.3 53622816824.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 107

*UGC NET Nov 2020, original Q82*

> Using RSA' public key cryptosystem, if P = 3, q = 11 and d = 7, find the value of e and encrypt the number 19. (1) 20. 19 (2) 33.11 (3) 3,28 (4) 77,28 53622816826.2 53622816827.3 53622816828.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 108

*UGC NET Nov 2020, original Q85*

> The process of removing details from a given state representation is called (1) Extraction (2) Mining (3) Selection (4) Abstraction 53622816838.2 53622816839.3 53622816840.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 109

*UGC NET Nov 2020, original Q100*

> To create an object-behavioral model, the analyst performs the following steps: (A) Evaluates all use-cases (B) Builds state transition diagram for the system. (C) Reviews the object behaviour model to verify accuracy and consistency (D) Identifies events that do not derive the interaction sequence. Choose the correct answer from the options given below: (1) (A). (B) and (C) only (2) (A). (B) and (D) only (3) (B). (C) and (D) only (4) (A), (C) and (D) only 53622816898.2 53622816899.3 53622816900.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 110

*UGC NET Nov 2020, original Q101*

> Which of the following is/are behavioral testing technique(s)? (A) Equivalence Partitioning (B) Graph-Based Teating Method (C) Boundery Value Analysis (D) Data flow Testing (E) Loop Testing Choose the correct answer from the options given below: (1) (B) and (D) only (2) (A), (B) and (C) only (3) (D) and (E) only (4) (A). (C) and (E) only 53622816902.2 53622816903.3 53622816904.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 111

*UGC NET Nov 2020, original Q116*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 112

*UGC NET Nov 2020, original Q117*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 113

*UGC NET Nov 2020, original Q124*

> Find the lexicographic ordering of the bit strings given below based on the ordering 0 < 1. (A) 001 (B) 010 (C) 011 (D) 0001 (E) 0101 Choose the correct answer from the options given below: (1) 001 < 010 < 011 < 0001 < 0101 (2) 0001 < 001 < 010 < 0101 < 011 (S) 0001 < 0101 < 001 < 010 < 011 (4) 001 < 010 < 0001 < 0101 < 011 . I 53622816994.2 53622816995.3 53622816996.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 114

*UGC NET Nov 2020, original Q127*

> Question Number: 127

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 115

*UGC NET Nov 2020, original Q134*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 116

*UGC NET Nov 2020, original Q141*

> If T is the capacity of a track in bytes. and S is the capacity of each surface in bytes, then (T,S) =_ (1) (50 K. 50000 K) (2) (25 K. 25000 K) (3) (25 K, 50000 K) (4) (40 K, 36000 K) L1 53622817062.2 53622817063.3 53622817064. 4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 117

*UGC NET Nov 2020, original Q142*

> What is the capacity of the disk, in bytes? (1) 25.000 K (2) 500,000 K (3) 250.000 K (4) 50,000 K 53622817066. 2 53622817067.3 53622817068. 4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 118

*UGC NET Nov 2020, original Q143*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 119

*UGC NET Nov 2020, original Q146*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 120

*UGC NET Nov 2020, original Q149*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 121

*UGC NET Nov 2020, original Q150*

> 

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 122

*UGC NET Nov 2021, original Q2*

> A only What does the following function f() in 'C' return? int f(unsigned int N) { unsigned int counter = 0; while(N > 0) { counter += N & 1; N = N >> 1;} return counter == 1;} 1. 1 if N is odd, otherwise 0 2. 1 if N is a power of 2, otherwise 0 3. 1 if the binary representation of N is all 1's, otherwise 0 4. 1 if the binary representation of N has any 1's, otherwise 0

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 123

*UGC NET Oct 2022, original Q5*

> The representation of 4 bit code 1101 into 7 bit. even parity Hamming code is 1. (1010101) 2. (1111001) 3. (1011101) 4. (1110000)

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 124

*UGC NET Oct 2022, original Q86*

> Of the following, which is NOT a logical error? 1. Using the '=. instead of* == to determine if two values are equal 2. Divide by zero 3. Failing to initialize counter and total variables before the body of loop

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 125

*UGC NET Aug 2024, original Q56*

> 38/101

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 126

*UGC NET Aug 2024, original Q68*

> 45/101

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 127

*UGC NET Aug 2024, original Q69*

> 46/101

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 128

*UGC NET Aug 2024, original Q72*

> 48/101

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 129

*UGC NET Aug 2024, original Q73*

> 50/101

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 130

*UGC NET Aug 2024, original Q98*

> Arrange the following steps in the correct order to solve the Knapsack problem using Dynamic Programming. (A) Define the base case when the capacity is zero (0) or no items are left to consider (B) Compute the maximum value that can be obtained using items up to the i-th item and a knapsack capacity of 0 (C) Identify subproblems and their dependencies based on items weights and values (D) Initialize a table to store results of subproblems (E) Iterate through each item and each possible Capacity to fill the table Choose the correct answer from the options given below : (1) (C), (D), (A), (E), (B) (2) (D), (C), (A), (E), (B) (3) (A), (C), (D), (E), (B) (4) (D), (A), (C), (E), (B) 63/101

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 131

*UGC NET Aug 2024, original Q108*

> Consider the given number (45)y where y is the base of the number. Some of the possible values of y are given below. (A) 5 (B) 6 (C) 7 (D) 8 Choose the correct answer from the options given below : (1) (A), (B) and (C) Only (2) (B), (C) and (D) Only (A), (C) and (D) Only (4) (A), (B), (C) and (D) 70/101

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 132

*UGC NET June 2024, original Q2*

> A-I, B-II, C-L, D-IV (3) A-III, B-I, C-IV, D-II (4) A-IV, B-II, C-III, D-I B. Ex-OR IL. Instruction decoding C. Accumulator Negative number representation D. Control Unit IV Arithmetic and Logic operations Choose the correct answer from the options given below: (1) A-L, B-II, C-III, D-IV 2 A-III, B-II, C-I, D-IV (3) A-III, B-I, C-IV, D-II (4) A-IV, B-II, C-II, Đ-1

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 133

*UGC NET June 2024, original Q127*

> Match List - 1 with List - I. List - I List - 11 A- Complement Adder B. Ex-OR IL. Tratructin decoding C. Accumulator TIL. Negative number representation D. Control Unit IV. Arithmetic and Logic operations Choose the correct answer from the options given below : (1) A-I, B-II, C-III, D-IV

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 134

*UGC NET June 2025, original Q52*

> In a pack of 42 cards, 3 cards are chosen one after the other. Find the number of ways this can be done without replacement: (1) 1722 (2) 1752 (3) 68880 (4) 6880 12558919260. 42558919261.2 42558919262. 3 42558919263.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 135

*UGC NET June 2025, original Q56*

> Binary equivalent to (AOF)16 is : 1. 111000111 2. 101001111 3. 101000001111 4. 111100001010 42558919277.2 42558919278.3 42558919279.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 136

*UGC NET June 2025, original Q59*

> Gray code equivalent to decimal number 8 is: 1. 1000 2. 1100 3. 1010 4. 1110 , 1 42558919289.2 42558919290. 3 42558919291.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 137

*UGC NET June 2025, original Q78*

> The longest common subsequence of (1,2,3,2,4,1,2) and (2,4,3,1,2,1} is (1) 2,1,2,3 (2) 1,3,2,1 (3) 2,3,2,1 (4) 2,3,1,2,1 2558919364. ptions 42558919365.2 42558919366.3 42558919367.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 138

*UGC NET June 2025, original Q79*

> Maintaining a graph in memory by means of its adjacency matrix is known as (1) Complete Representation (2) Linked Representation (3) Circular Representation (4) Sequential Representation 42558919368.1 42558919370.3 42558919371.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 139

*UGC NET June 2025, original Q84*

> CB84000D001C001C is the content of a UP header in hexadecimal format. The source port number is (1) 52100 (2) 13 (3) 28 (4) 52000 42558919388.1 42558919390.3 42558919391.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 140

*UGC NET June 2025, original Q100*

> When developing a dynamic programming algorithm, the sequence of steps followed is: A. Construct an optimal solution from computed information. B. Recursively define the value of an optimal solution. C. Characterize the structure of an optimal solution. D. Compute the value of an optimal solution, typically in a bottom-up fashion. Choose the correct answer from the options given below: 1. B, C, A, D 2. B, A, C, D 3. C, B, A, D 4. C, B, D, A 42558919453.2 42558919454. 3 42558919455.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 141

*UGC NET June 2025, original Q119*

> Which of the following are examples of data encoding schemes? A. Non-Return to Zero (NRZ) B. Manchester Encoding C. Amplitude Modulation D. Hamming code E. Bipolar AMI Choose the correct answer from the options given below: 1. A, C and D Only 2. A, B and D Only 3. C, D and E Only 4. A, B and E Only 42558919529.2 42558919530.3 42558919531.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 142

*UGC NET June 2025, original Q140*

> Match List I with List II List I (GA termination criteria) List I (description) A. Worst Individual I. At least half of the individual will be better than or equal to convergence value B. Best Individual Il. Guarantees that virtually all individuals in the population will be within a particular fitness range C. Sum of Fitness III. Guarantees that the entire population to be of a minimum standard D. Median Fitness IV. Faster search Convergence, guaranteeing at least one best solution Choose the correct answer from the options given below: 1. A→III, B→IV, C→II, D→I 2. A→IV, B→III, C→I, D→II 3. A→II, B→I, C→III, D→IV 4. A→II, B→III, C→IV, D→I 42558919613.2 42558919614. 3 42558919615.4 Sub-Section Number : 2 Sub-Section Id: 425589203 Question Shuffling Allowed : No

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 143

*UGC NET Dec 2025 session (Jan 2026), original Q68*

> Question Number: 68

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 144

*UGC NET Dec 2025 session (Jan 2026), original Q78*

> Question Number : 78

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 145

*UGC NET Dec 2025 session (Jan 2026), original Q79*

> Question Number: 79

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 146

*UGC NET Dec 2025 session (Jan 2026), original Q117*

> Question Number : 117 B. DIFS(DCF interframe Spacing) C. SIFS(Short interframe Spacing) D. EIFS (Extended interframe Spacing) Choose the correct answer from the options given below: 1. A, B, C, D 2. B. C, A, D 3. D, A, B, C 4. C, A, B, D 6119878866.2 6119878867.3 6119878868.4 Number : Yes

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 147

*UGC NET Dec 2025 session (Jan 2026), original Q143*

> Question Number : 143

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 148

*UGC NET Dec 2025 session (Jan 2026), original Q146*

> Question Number : 146

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 149

*UGC NET Dec 2025 session (Jan 2026), original Q148*

> Question Number : 148

**Chapter foundations**

This question belongs to the ideas covered by **Data Representation**. Revise these foundations: Data Types; Number Systems and Conversion; Complements; Fixed-Point Representation; Floating-Point Representation; Error-Detection Codes; Computer Arithmetic - Addition, Subtraction, Multiplication and Division Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Representation questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-3"></a>

### 3. Register Transfer and Microoperations (23 questions)

**What to master:** Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 150

*UGC NET Dec 2013, Paper III, original Q49*

> Match the following : List – I List – II a. Indexed Addressing i. is not used when an operand is moved from memory into a register or from a register to memory. b. Direct Addressing ii. Memory address is computed by adding up two registers plus an (optional) offset. c. Register Addressing iii. Addressing memory by giving a register plus a content offset. d. Base- Indexed Addressing iv. can only be used to access global variables whose address is known at compile time. Codes : a b c d (A) ii i iv iii (B) ii iv i iii (C) iii iv i ii (D) iii i iv ii

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 151

*UGC NET June 2013, Paper III, original Q41*

> Which one of the following is not an addressing mode ? (A) Register indirect (B) Autoincrement (C) Relative indexed (D) Immediate operand

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 152

*UGC NET Dec 2014, Paper II, original Q34*

> Debugger is a program that (A) allows to examine and modify the contents of registers (B) does not allow execution of a segment of program (C) allows to set breakpoints, execute a segment of program and di splay contents of register (D) All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 153

*UGC NET Dec 2014, Paper III, original Q66*

> A Butterworth lowpass filter of order n, with a cutoff frequen cy at distance D 0 from the origin, has the transfer function H(u, v) given by (A) 1 1 +  D(u, v) D0 2n (B) 1 1 +  D(u, v) D0 n (C) 1 1 +  D0 D(u, v) 2n (D) 1 1 +  D0 D(u, v) n

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 154

*UGC NET Dec 2015, Paper II, original Q42*

> What will be the hexadecimal value in the register ax (32-bit) after executing the following instructions? mov al, 15 mov ah, 15 xor al, al mov cl, 3 shr ax, cl Codes: (1) OF00 h (2) OFOF h (3) 01E0 h (4) FFFF h

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 155

*UGC NET Dec 2015, Paper III, original Q5*

> A DMA controller transfers 32-bit words to memory using cycle Stealing. The words are assembled from a device that transmits characters at a rate of 4800 characters per second. The CPU is fetching and executing instructions at an average rate of one million instructions per second. By how much will the CPU be slowed down because of the DMA transfer ? (1) 0.06% (2) 0.12% (3) 1.2% (4) 2.5%

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 156

*UGC NET Dec 2015, Paper III, original Q6*

> A CPU handles interrupt by executing interrupt service subroutine. (1) by checking interrupt register after execution of each instruction (2) by checking interrupt register at the end of the fetch cycle (3) whenever an interrupt is registered by checking interrupt register at regular time interval D-8715 2 Paper-IlI

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 157

*UGC NET June 2015, Paper III, original Q5*

> The CPU of a system having 1 MIPS execution rate needs 4 machine cycles on an average for executing an instruction. The fifty percent of the cycles use memory bus. A memory read/ write employs one machine cycle. For execution of the programs, the system utilizes 90 percent of the CPU time. For block data transfer, an IO device is attached to the system while CPU executes the background programs continuously. What is the maximum IO data transfer rate if programmed IO data transfer technique is used ? (L) 500 Kbytes/sec (2) 2.2 Mbytes/sec (3) 125 Kbytes/sec (4) 250 Kbytes/sec

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 158

*UGC NET July 2016, Paper III, original Q5*

> The _____ addressing mode is similar to regist er indirect addressing mode, except that an offset is added to the contents of the register . The offset and register are specified in the instruction. (1) Base indexed (2) Base indexed plus displacement (3) Indexed (4) Displacement

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 159

*UGC NET Jan 2017, Paper II, original Q32*

> Consider the following assembly language instructions : mov al, 15 mov ah, 15 xor al, al mov cl, 3 shr ax, cl add al, 90H adc ah, 0 What is the value in a x register after execution of above instructions ? (1) 0270H (2) 0170H (3) 01E0H (4) 0370H

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 160

*UGC NET Jan 2017, Paper II, original Q34*

> The contents of Register (BL) and Register (AL) of 8085 microproc essor are 49H and 3AH respectively. The contents of AL, the status of carry flag (CF) and sign flag (SF) after executing ‘SUB AL, BL’ assembly language instruction, are (1) AL = 0FH; CF = 1; SF = 1 (2) AL = F0H; CF = 0; SF = 0 (3) AL = F1H; CF = 1; SF = 1 (4) AL = 1FH; CF = 1; SF = 1

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 161

*UGC NET Jan 2017, Paper III, original Q4*

> Match the following : Addressing Mode Location of operand a. Implied i. Registers which are in CPU b. Immediate ii. Register specif ies the address of the operand. c. Register iii. Specified in the register d. Register Indirect iv. Specified implic itly in the definition of instruction Codes : a b c d (1) iv iii i ii (2) iv i iii ii (3) iv ii i iii (4) iv iii ii i

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 162

*UGC NET Jan 2017, Paper III, original Q6*

> In 8085, which of the following performs : load register pair immediate operation ? (1) LDAX rp (2) LHLD addr (3) LXI rp, data (4) INX rp

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 163

*UGC NET Nov 2017, Paper II, original Q32*

> Consider the following assembly program fragment : stc mov al, 11010110b mov cl, 2 rcl al, 3 rol al, 4 shr al, cl mul cl The contents of the destination register ax (in hexadecimal) and the status of Carry Flag (CF) after the execution of above instructions, are : (1) ax= 003CH; CF = 0 (2) ax= 001EH; CF = 0 (3) ax= 007BH; CF = 1 (4) ax= 00B7H; CF = 1

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 164

*UGC NET Dec 2018, original Q65*

> Consider the following x86 - assembly language instructions: MOV AL, 153 NEG AL The contents of the destination register AL (in 8-bit binary notation), the status of Carry Flag (CF) and Sign Flag (SF) after the execution of above instructions, are Options :

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 165

*UGC NET Dec 2019, original Q61*

> A micro instruction format has microoperation field which is divided into 2 subfields F1 and F2. each having 15 distinct microoperations, condition field CD for four status bits, branch field BR having four options used in conjunction with address field AD. The address space is of 128 memory words. The size of micro instruction is : (1) 19 (2) 18 (3) 17 (4) 20 61547540942. 61547540943.3 61547540944. 4

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 166

*UGC NET Dec 2019, original Q136*

> An instruction is stored at location 500 with its address field at location 501. The address field has the value 400. A processor register Ri contains the number 200. Match the addressing mode (List-I) given below with effective address (List-Il) for the given instruction: List I List II (a) Direct (i) 200 (b) Register indirect (ii) 902 (c) Index with Ri as the index register (iii) 400 (d) Relative (iv) 600 Your Personal Exam Guidel Choose the correct option from those given below : (1) (a)-(iii), (b)-(i). (c) -(iv). (d)-(ii) (2) (a)-(i). (b) -(ii), (c)-(ili), (d) (iv) (3) (a)-(iv). (b)-(ii), (c)-(iii), (d)-(i) (4) (a)-(iv), (b)-(iii), (c)-(ii), (d)-(i) 61547541242.2 61547541243.3 61547541244.4

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 167

*UGC NET June 2019, original Q61*

> Which type of addressing mode, less number of memory references are required? Immediate Implied Register 4. Indexed 64635085580. 2 64635085581.3

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 168

*UGC NET Aug 2024, original Q93*

> Arrange the given steps required for a Direct Memory Access (DMA) transfer in the correct order. (A) Initiate DMA transfer request (B) Transfer data directly between peripheral and memory (C) Processor grants DMA control over the system bus (D) DMA controller completes data transfer and signals completion Choose the correct answer from the options given below : (1) (C), (A), (B), (D) (2) (A), (C), (B), (D) 3) (A), (B), (C), (D) (4) (C), (B), (A), (D)

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 169

*UGC NET June 2025, original Q57*

> The write operation in l/0 operation does the following- 1. Transfer data from l/O device to memory 2. Transfer data from memory to I/O device 3. Transfer data from CPU register to memory 4. Transfer data from CPU register to 1/O device 42558919281.2 42558919282. 3 42558919283.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 170

*UGC NET June 2025, original Q93*

> The right sequence of CPU program to input data will be : A. Read status register B. Check flag bit C. Read Data Register D. Transfer data to memory Choose the correct answer from the options given below: 1. A, B, C, D 2. B, A, C, D 3. C, B, A, D 4. A, C, B, D 42558919425.2 42558919426.3 42558919427.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 171

*UGC NET Dec 2025 session (Jan 2026), original Q132*

> Question Number : 132 and status register. B. Fetch interrupt vector from memory. C. Execute the interrupted instruction completely. D. Transfer control to interrupt service routine (ISR) E. Restore PC and register after ISR Choose the correct answer from the options given below: 1. A, B, C, D, E 2. E, D, C, B, A 3. C, A, B, D. E 4. A, B, E, C, D 6119878926.2 6119878927.3 6119878928.4

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 172

*UGC NET Dec 2025 session (Jan 2026), original Q150*

> Question Number : 150

**Chapter foundations**

This question belongs to the ideas covered by **Register Transfer and Microoperations**. Revise these foundations: Register Transfer Language; Bus and Memory Transfers; Arithmetic, Logic and Shift Microoperations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Register Transfer and Microoperations questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-4"></a>

### 4. Basic Computer Organization and Design (13 questions)

**What to master:** Stored-Program Organization and Instruction Codes; Computer Registers; Computer Instructions; Timing and Control; Instruction Cycle; Memory-Reference Instructions; Input-Output; Interrupt.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 173

*UGC NET Dec 2009, Paper II, original Q4*

> P : “Program is a step by step execution of the instructions”. Given P, which of the following is true ? (A) Program is a subset of an instruction set. (B) Program is a sequence of a subset of an instruction s et. (C) Program is a partially ordered set of an instructi on set. (D) All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Basic Computer Organization and Design**. Revise these foundations: Stored-Program Organization and Instruction Codes; Computer Registers; Computer Instructions; Timing and Control; Instruction Cycle; Memory-Reference Instructions; Input-Output; Interrupt.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Basic Computer Organization and Design questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 174

*UGC NET Dec 2013, Paper III, original Q50*

> Which of the following is a design criteria for instruction formats ? (A) The size of instructions (B) The number of bits in the address fields (C) The sufficient space in the instruction format to express all the operations desired. (D) All of these

**Chapter foundations**

This question belongs to the ideas covered by **Basic Computer Organization and Design**. Revise these foundations: Stored-Program Organization and Instruction Codes; Computer Registers; Computer Instructions; Timing and Control; Instruction Cycle; Memory-Reference Instructions; Input-Output; Interrupt.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Basic Computer Organization and Design questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 175

*UGC NET June 2013, Paper III, original Q33*

> Refer the points as listed below : (a) What are the operator precedence rules ? (b) What are the operator associativity rules ? (c) What is the order of operand evaluation ? (d) Are there restrictions on operand evaluation side effects ? Which of the above must be considered as primary design issues for arithmetic expressions ? (A) (a), (b) and (c) (B) (a), (c) and (d) (C) (a), (b) and (d) (D) (a), (b), (c) and (d)

**Chapter foundations**

This question belongs to the ideas covered by **Basic Computer Organization and Design**. Revise these foundations: Stored-Program Organization and Instruction Codes; Computer Registers; Computer Instructions; Timing and Control; Instruction Cycle; Memory-Reference Instructions; Input-Output; Interrupt.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Basic Computer Organization and Design questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 176

*UGC NET Dec 2014, Paper III, original Q4*

> Match the following 8085 instructions with the flags : List – I List – II a. XCHG i. only carry flag is affected. b. SUB ii. no flags are affected. c. STC iii. all flags other than carry flag are affected. d. DCR iv. all flags are affected. Codes : a b c d (A) iv i iii ii (B) iii ii i iv (C) ii iii i iv (D) ii iv i iii

**Chapter foundations**

This question belongs to the ideas covered by **Basic Computer Organization and Design**. Revise these foundations: Stored-Program Organization and Instruction Codes; Computer Registers; Computer Instructions; Timing and Control; Instruction Cycle; Memory-Reference Instructions; Input-Output; Interrupt.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Basic Computer Organization and Design questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 177

*UGC NET Dec 2014, Paper III, original Q19*

> Consider the following statements S1, S2 and S3 : S1 : In call-by-value, anything that is passed into a functi on call is unchanged in the caller’s scope when the function returns. S2 : In call-by-reference, a function receives implicit refer ence to a variable used as argument. S3 : In call-by-reference, caller is unable to see the modified varia ble used as argument. (A) S3 and S2 are true. (B) S3 and S1 are true. (C) S2 and S1 are true. (D) S1, S2, S3 are true.

**Chapter foundations**

This question belongs to the ideas covered by **Basic Computer Organization and Design**. Revise these foundations: Stored-Program Organization and Instruction Codes; Computer Registers; Computer Instructions; Timing and Control; Instruction Cycle; Memory-Reference Instructions; Input-Output; Interrupt.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Basic Computer Organization and Design questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 178

*UGC NET Dec 2014, Paper III, original Q72*

> Match the following learning modes w.r.t. characteristics of available information for learning : a. Supervised i. Instructive information on desired responses, explicitly specified by a teacher. b. Recording ii. A priori design information for memory storing c. Reinforcement iii. Partial information about desired responses, or only “right” or “wrong” evaluative information d. Unsupervised iv. No information about desired responses Codes : a b c d (A) i ii iii iv (B) i iii ii iv (C) ii iv iii i (D) ii iii iv i

**Chapter foundations**

This question belongs to the ideas covered by **Basic Computer Organization and Design**. Revise these foundations: Stored-Program Organization and Instruction Codes; Computer Registers; Computer Instructions; Timing and Control; Instruction Cycle; Memory-Reference Instructions; Input-Output; Interrupt.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Basic Computer Organization and Design questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 179

*UGC NET Dec 2015, Paper II, original Q44*

> System calls are usually invoked by using: (1) A privileged instruction (2) An indirect jump (3) A software interrupt (4) Polling

**Chapter foundations**

This question belongs to the ideas covered by **Basic Computer Organization and Design**. Revise these foundations: Stored-Program Organization and Instruction Codes; Computer Registers; Computer Instructions; Timing and Control; Instruction Cycle; Memory-Reference Instructions; Input-Output; Interrupt.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Basic Computer Organization and Design questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 180

*UGC NET June 2015, Paper III, original Q6*

> The number of flip-flops required to design a modulo - 272 counter is : (1) 8 (2) 9 (3) 27 (4) 11 Let Ey and Ez be two entities in E-R diagram with simple single valued attributes. Ry and R2 Ry and R, donot have any attribute of their own. How many minimum number of tables are are two relationships between E, and Ez where R, is one - many and R is many - many. required to represent this situation in the Relational Model ? (1) 4 (2) 3 (3) 2 (4) 1 J-8715 2 Paper-III

**Chapter foundations**

This question belongs to the ideas covered by **Basic Computer Organization and Design**. Revise these foundations: Stored-Program Organization and Instruction Codes; Computer Registers; Computer Instructions; Timing and Control; Instruction Cycle; Memory-Reference Instructions; Input-Output; Interrupt.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Basic Computer Organization and Design questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 181

*UGC NET Dec 2018, original Q137*

> An Internet Service Provider (ISP) has following chunk of CIDR-based IP addresses available with it : 245.248.128.0/20. The ISP wants to give half of this chunk of addresses to organization A and a quarter to organization B while retaining the remaining with itself. Which of the following is a valid allocation of addresses to A and B? .248.136.0/21 and 245.248.128.0/22 91394342546. 245.248.128.0/21 and 245.248.128.0/22

**Chapter foundations**

This question belongs to the ideas covered by **Basic Computer Organization and Design**. Revise these foundations: Stored-Program Organization and Instruction Codes; Computer Registers; Computer Instructions; Timing and Control; Instruction Cycle; Memory-Reference Instructions; Input-Output; Interrupt.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Basic Computer Organization and Design questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 182

*UGC NET Dec 2019, original Q63*

> The following program is stored in the memory unit of the basic computer. Give the content of accumulator register in hexadecimal after the execution of the program. Location Instruction 010 CLA 011 ADD 016 012 BUN 014 013 HLT 014 AND 017 015 BUN 013 Guide 016 C1A5 017 93C6 (1) A1B4 (2) 81B4 (3) A184 (4) 8184 61547540950. 2 61547540951. 3 61547540952. 4 Single Line Ouestion Option: No

**Chapter foundations**

This question belongs to the ideas covered by **Basic Computer Organization and Design**. Revise these foundations: Stored-Program Organization and Instruction Codes; Computer Registers; Computer Instructions; Timing and Control; Instruction Cycle; Memory-Reference Instructions; Input-Output; Interrupt.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Basic Computer Organization and Design questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 183

*UGC NET Nov 2020, original Q56*

> The following program is stored in memory unit of the basic computer. What is the content of the accumulator after the execution of program? (All location numbers listed below are in hexadecimal). Location Instruction 210 CLA 211 ADD 217 212 INC 213 STA 217 214 LDA 218 215 CMA 216 AND 217 217 1234H 218 9CE2H (1) 1002H (2) 2011H (3) 2022H (4) 021H 53622816722.2 53622816723.3 53622816724.4

**Chapter foundations**

This question belongs to the ideas covered by **Basic Computer Organization and Design**. Revise these foundations: Stored-Program Organization and Instruction Codes; Computer Registers; Computer Instructions; Timing and Control; Instruction Cycle; Memory-Reference Instructions; Input-Output; Interrupt.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Basic Computer Organization and Design questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 184

*UGC NET Oct 2022, original Q3*

> Consider a memory system having address spaced at a distance of m. T = Bank cycle time and n number of banks. then the average data access time per word access in synchronous organization is m. - form <<n T 1. Iform>> 2. 1= T form >>7 3. t= Im T form & n I form>> n 4. m.I form <<n form >1

**Chapter foundations**

This question belongs to the ideas covered by **Basic Computer Organization and Design**. Revise these foundations: Stored-Program Organization and Instruction Codes; Computer Registers; Computer Instructions; Timing and Control; Instruction Cycle; Memory-Reference Instructions; Input-Output; Interrupt.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Basic Computer Organization and Design questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 185

*UGC NET Oct 2022, original Q88*

> Which statement is false? 1. All function calls in C pass arguments using call by value. 2. Call by reference enables a called function to modify a variable in calling function. 3. Call by value is always more efficient than call by reference. 4. Programmers use pointers and indirection operation to simulate call by reference.

**Chapter foundations**

This question belongs to the ideas covered by **Basic Computer Organization and Design**. Revise these foundations: Stored-Program Organization and Instruction Codes; Computer Registers; Computer Instructions; Timing and Control; Instruction Cycle; Memory-Reference Instructions; Input-Output; Interrupt.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Basic Computer Organization and Design questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-5"></a>

### 5. Programming the Basic Computer (6 questions)

**What to master:** Machine Language; Assembly Language; Assembler; Program Loops; Subroutines; Input-Output Programming.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 186

*UGC NET Dec 2012, Paper II, original Q32*

> The User Work Area (UWA) is a set associated with Electronic payment of Program variables declared in the system. host program to communicate the (A) Fraudulent use of Credit Cards. contents of individual records between (A) DBMS & the Host record (B) Sending Credit Card details over internet. (B) Host program and Host record (C) Host program and DBMS (C) Remote storage of Credit Card details. (D) Host program and Host language (D) All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Programming the Basic Computer**. Revise these foundations: Machine Language; Assembly Language; Assembler; Program Loops; Subroutines; Input-Output Programming.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming the Basic Computer questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 187

*UGC NET Dec 2014, Paper II, original Q4*

> A computer program selects an integer in the set {k : 1 ≤ k ≤ 10,00,000} at random and prints out the result. This process is repeated 1 million times. What is the probability that the value k = 1 appears in the printout atleast once ? (A) 0.5 (B) 0.704 (C) 0.632121 (D) 0.68

**Chapter foundations**

This question belongs to the ideas covered by **Programming the Basic Computer**. Revise these foundations: Machine Language; Assembly Language; Assembler; Program Loops; Subroutines; Input-Output Programming.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming the Basic Computer questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 188

*UGC NET June 2015, Paper III, original Q23*

> Which of the following is false for the programming language PROLOG? (1) A PROLOG variable can only be assigned to a value once (2) PROLOG is a strongly typed language (3) The scope of a variable in PROLOG is a single clause or rule (4) The scope of a variable in PROLOG is a single query

**Chapter foundations**

This question belongs to the ideas covered by **Programming the Basic Computer**. Revise these foundations: Machine Language; Assembly Language; Assembler; Program Loops; Subroutines; Input-Output Programming.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming the Basic Computer questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 189

*UGC NET July 2016, Paper II, original Q32*

> The content of the accumulator after th e execution of the following 8085 assembly language program, is : MVI A, 42H MVI B, 05H UGC: ADD B DCR B JNZ UGC ADI 25H HLT (1) 82 H (2) 78 H (3) 76 H (4) 47 H

**Chapter foundations**

This question belongs to the ideas covered by **Programming the Basic Computer**. Revise these foundations: Machine Language; Assembly Language; Assembler; Program Loops; Subroutines; Input-Output Programming.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming the Basic Computer questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 190

*UGC NET Nov 2017, Paper II, original Q31*

> Consider the following program fragment in assembly language : mov ax, 0h mov cx, 0A h doloop : dec a x loop doloop What is the value of a x and cx registers after the completion of the doloop ? (1) ax= FFF5 h and c x= 0 h (2) ax= FFF6 h and c x= 0 h (3) ax= FFF7 h and c x= 0A h (4) ax= FFF5 h and c x= 0A h

**Chapter foundations**

This question belongs to the ideas covered by **Programming the Basic Computer**. Revise these foundations: Machine Language; Assembly Language; Assembler; Program Loops; Subroutines; Input-Output Programming.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming the Basic Computer questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 191

*UGC NET Nov 2017, Paper II, original Q50*

> Which speed up could be achieved according to Amdahl’s Law for infinite number of processes if 5% of a program is sequential and the remaining part is ideally par allel ? (1) Infinite (2) 5 (3) 20 (4) 50 - o 0 o -

**Chapter foundations**

This question belongs to the ideas covered by **Programming the Basic Computer**. Revise these foundations: Machine Language; Assembly Language; Assembler; Program Loops; Subroutines; Input-Output Programming.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming the Basic Computer questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-6"></a>

### 6. Microprogrammed Control (17 questions)

**What to master:** Control Memory; Address Sequencing; Design of Control Unit.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 192

*UGC NET Dec 2012, Paper II, original Q17*

> The design issue of Datalink Layer in generated by adding a constant value to OSI Reference Model is the contents of register? (A) Framing (A) Absolute (B) Representation of bits (B) Indirect (C) Synchronization of bits (C) Immediate (D) Connection control (D) Index

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 193

*UGC NET June 2012, Paper II, original Q3*

> The branch logic that provides making capabilities in the control unit is known as (A) Controlled transfer (B) Conditional transfer (C) Unconditional transfer (D) None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 194

*UGC NET Dec 2013, Paper III, original Q20*

> Match the following control strategies of prolog : List – I List – II a. Forward movement i. Variable can be done with a constant, another variable or a function. b. Unifica- tion ii. The entire conjunctive goal is executed. c. Deep back- tracking iii. Previous sub goal to find alternative solutions. d. Shallow back- tracking iv. Chooses sub goal with possible unifier. Codes : a b c d (A) iv i ii iii (B) ii iv i iii (C) iii i iv ii (D) ii iii iv i

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 195

*UGC NET June 2013, Paper III, original Q43*

> Which is not a typical program control instruction ? (A) BR (B) JMP (C) SHL (D) TST

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 196

*UGC NET Dec 2014, Paper II, original Q50*

> Match the following : List – I List – II a. Call control protocol i. Interface between Base Transceiver Stat ion (BTS) and Base Station Controller (BSC) b. A-bis ii. Spread spectrum c. BSMAP iii. Connection management d. CDMA iv. Works between Mobile Switching Centre (MSC) and Base Station Subsystem (BSS) Codes : a b c d (A) iii iv i ii (B) iii i iv ii (C) i ii iii iv (D) iv iii ii i _______________

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 197

*UGC NET Dec 2014, Paper III, original Q46*

> Maximum possible value of reliability is (A) 100 (B) 10 (C) 1 (D) 0 47. ‘FAN IN’ of a component A is defined as (A) Count of the number of components that can call, or pass control, to a component A (B) Number of components related to component A (C) Number of components dependent on component A (D) None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 198

*UGC NET June 2015, Paper III, original Q12*

> In the indexed scheme of blocks to a file, the maximum possible size of the file depends on : (1) The number of blocks used for index and the size of index (2) Size of Blocks and size of Address (3) Size of index (4) Size of Block J-8715 3 Paper-IlI

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 199

*UGC NET Jan 2017, Paper III, original Q3*

> The general configuration of the micr oprogrammed control unit is given below : What are blocks B and C in the diagram respectively ? (1) Block address register and cache memory (2) Control address regi ster and control memory (3) Branch register and cache memory (4) Control address register and random access memory

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 200

*UGC NET Nov 2017, Paper II, original Q39*

> Which module gives control of the CPU to the process selected by the short - term schedular ? (1) Dispatcher (2) Interrupt (3) Schedular (4) Threading

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 201

*UGC NET Dec 2019, original Q138*

> Match List-I with List-II : List I List II (a) Micro operation (i) Specify micro operations (b) Micro programmed control unit (ii) Improve CPU utilization (c) Interrupts (iti) Control Memory (d) Micro instruction (iv) Elementary operation performed on data stored in registers Choose the correct option from those given below : (1) (a)-(iv). (b)-(ili). (c)-(ii), (d)-(i) (2) (a)-(iv), (b)-(ili). (c)-(i), (d) -(ii) (3) (a)-(iii). (b)-(iv). (c) -(i). (d)-(i) (4) (a)-(iii). (b)-(iv). (c) -(ii), (d)-(i)

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 202

*UGC NET June 2019, original Q64*

> The fault can be easily diagnosed in the micro-program control unit using diagnostic tools by maintaining the contents of 1. flags and counters 2. registers and counters 3. flags and registers 4. flags, registers and counters 64635085592. 2 64635085593. 3 64635085594.4

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 203

*UGC NET Nov 2020, original Q115*

> Match List I with List II List I List II (A) Handshaking IO interface informs the CPU that device is ready for transfer (B) Programmed I/O (IL) requires two control signals working in opposite directions (C) Interrupt-initiated I/O III) has local memory & control large set of I/O devices. (D) I/O processor (IV) require CPU to check the I/O flag & perform transfer Choose the correct answer from the options given below: (1) A-I, B-II, C-III. D-IV (2) A-II, B-IV, C-III, D-I (3) A-II, B-IV. C-I, D-III (4) A-IV. B-III. C-II. D-I . I 53622816958.2 53622816959, 3 53622816960.4

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 204

*UGC NET Nov 2020, original Q131*

> Given below are two statements: Statement I: Hardwired control unit can be optimized to produce fast mode of operation. Statement II: Indirect addressing mode needs two memory reference to fetch the operand. In the light of the above statements, choose the correct answer from the options given below (1) Both Statement I and Statement Il are true (2) Both Statement I and Statement II are false (3) Statement I is correct but Statement Il is false (4) Statement I is incorrect but Statement II is true. 53622817022.2 53622817023.3 53622817024.4

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 205

*UGC NET Nov 2021, original Q90*

> Both Statement I and Statement II are true Which of the following statement is true? A. Control memory is part of the hardwired control unit. B. Program control instructions are used to alter the sequential flow of the program. C. The register indirect addressing mode for accessing memory operand is similar to displacement addressing mode. D. CPU utilization is not affected by the introduction of Interrupts. 1. A 2. B 3. C 4. D

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 206

*UGC NET Oct 2022, original Q38*

> A classless address is given as 167.199.170.82/27. The number of addresses in the network is 1. 64 addresses 2. 32 addresses 3. 28 addresses 4. 30 addresses

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 207

*UGC NET June 2024, original Q94*

> A. frame format establishment of the lint C. flow control D. sequence numbring Choose the correct answer from the options faren below : authentication (1) A. B and E Only (2) A. C and D Only (3) D, E and B Only (4) B.C and D Only

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 208

*UGC NET June 2024, original Q115*

> The I/O methods in which memory addresses and I/O addresses are distinct, is called : A. Isolated 1/0 C. Strobe Control B. Memory-Mapped I/O E. Interrupt D. Handshaking Choose the most appropriate answer from the options given below : (1) A, B Only (2) C, D Only (3) C, E Only (4) BE Only (4) 16 non-real-time priorities

**Chapter foundations**

This question belongs to the ideas covered by **Microprogrammed Control**. Revise these foundations: Control Memory; Address Sequencing; Design of Control Unit.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Microprogrammed Control questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-7"></a>

### 7. Central Processing Unit (10 questions)

**What to master:** General Register Organization; Stack Organization; Instruction Formats; Addressing Modes; RISC; CISC.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 209

*UGC NET Dec 2012, Paper II, original Q12*

> In which addressing mode, the effective address of the operand is

**Chapter foundations**

This question belongs to the ideas covered by **Central Processing Unit**. Revise these foundations: General Register Organization; Stack Organization; Instruction Formats; Addressing Modes; RISC; CISC.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Central Processing Unit questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 210

*UGC NET June 2013, Paper III, original Q42*

> Computers can have instruction formats with (A) only two address and three address instructions (B) only one address and two address instructions (C) only one address, two address and three address instructions (D) zero address, one address, two address and three address instructions

**Chapter foundations**

This question belongs to the ideas covered by **Central Processing Unit**. Revise these foundations: General Register Organization; Stack Organization; Instruction Formats; Addressing Modes; RISC; CISC.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Central Processing Unit questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 211

*UGC NET Dec 2014, Paper II, original Q27*

> In a classful addressing, first four bits in Class A IP address is (A) 1010 (B) 1100 (C) 1011 (D) 1110

**Chapter foundations**

This question belongs to the ideas covered by **Central Processing Unit**. Revise these foundations: General Register Organization; Stack Organization; Instruction Formats; Addressing Modes; RISC; CISC.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Central Processing Unit questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 212

*UGC NET June 2015, Paper II, original Q30*

> Which of the following is/ are restriction(s) in classless addressing ? (1) The number of addresses needs to be a power of 2. (2) The mask needs to be included in the address to define the block. (3) The starting address must be divisible by the number of addresses in the block. (4) All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Central Processing Unit**. Revise these foundations: General Register Organization; Stack Organization; Instruction Formats; Addressing Modes; RISC; CISC.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Central Processing Unit questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 213

*UGC NET June 2015, Paper III, original Q17*

> Which of the following statements) is/are incorrect? (a) Mapping the co-ordinates of the points and lines that form the picture into the appropriate co-ordinates on the device or workstation is known as viewing transformation. (b) The right-handed cartesian co-ordinates system in whose co-ordinates we describe the picture is known as world co-ordinate system. The co-ordinate system that corresponds to the device or workstation where the image is to be displayed is known as physical device co-ordinate system. Left - handed co-ordinate system in which the display area of the virtual display device corresponds to the unit (x) square whose lower left-hand corner is at the origin of the co-ordinate system, is known as normalized device co-ordinate system. Codes : (1) (a) only (2) (a) and (b) (3) (c) only (4) (d) only J-8715 4 Paper-III

**Chapter foundations**

This question belongs to the ideas covered by **Central Processing Unit**. Revise these foundations: General Register Organization; Stack Organization; Instruction Formats; Addressing Modes; RISC; CISC.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Central Processing Unit questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 214

*UGC NET July 2016, Paper II, original Q24*

> Which of the following is not an inherent application of stack ? (1) Implementation of recursion (2) Evaluation of a postfix expression (3) Job scheduling (4) Reverse a string

**Chapter foundations**

This question belongs to the ideas covered by **Central Processing Unit**. Revise these foundations: General Register Organization; Stack Organization; Instruction Formats; Addressing Modes; RISC; CISC.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Central Processing Unit questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 215

*UGC NET Dec 2018, original Q74*

> Consider the following postfix expression with single digit operands: 623*/42*+68*- The top two elements of the stack after the second * is evaluated, are : ,2 91394342293. 91394342294. 8, 1 6, 2 91394342295. 6, 3 91394342296. ingle Line Question Option: No

**Chapter foundations**

This question belongs to the ideas covered by **Central Processing Unit**. Revise these foundations: General Register Organization; Stack Organization; Instruction Formats; Addressing Modes; RISC; CISC.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Central Processing Unit questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 216

*UGC NET Dec 2019, original Q60*

> A computer uses a memory unit of 512 K words of 32 bits each. A binary instruction code is stored in one word of the memory. The instruction has four parts: an addressing mode field to specify one of the two-addresssing mode (direct and indirect), an operation code. a register code part to specify one of the 256 registers and an address part. How many bits are there in addressing mode part. opcode part. register code part and the address part? (1) 1. 3. 9. 19 (2) 1. 4. 9. 18 (3) 1. 4, 8. 19 (4) 1. 3. 8. 20 61547540938. 2 61547540939.3 61547540940.4

**Chapter foundations**

This question belongs to the ideas covered by **Central Processing Unit**. Revise these foundations: General Register Organization; Stack Organization; Instruction Formats; Addressing Modes; RISC; CISC.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Central Processing Unit questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 217

*UGC NET June 2024, original Q81*

> The instructions ADD R,. A, B ADD R. C, D evaluates the X- (A + B)(C+D) in which of the following 21 MUL X R, R. (1) 3 - Address instructions (2) 2 - Address instructions (3) 1 - Address instructions (4) RISC instructions

**Chapter foundations**

This question belongs to the ideas covered by **Central Processing Unit**. Revise these foundations: General Register Organization; Stack Organization; Instruction Formats; Addressing Modes; RISC; CISC.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Central Processing Unit questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 218

*UGC NET Dec 2025 session (Jan 2026), original Q133*

> Question Number: 133

**Chapter foundations**

This question belongs to the ideas covered by **Central Processing Unit**. Revise these foundations: General Register Organization; Stack Organization; Instruction Formats; Addressing Modes; RISC; CISC.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Central Processing Unit questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-8"></a>

### 8. Pipeline and Vector Processing (23 questions)

**What to master:** Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 219

*UGC NET Dec 2009, Paper II, original Q46*

> The single stage network is also called (A) one sided network (B) two sided network (C) recirculating network (D) pipeline network

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 220

*UGC NET June 2010, Paper II, original Q5*

> Four your ATM debit card, you have a 4-decimal-digit personal secret code. In the absence of any clue, a brute-force attack takes time-‘t’ to crack the code on an ATM terminal. Therefore ‘t’ is the secure-time for a customer to report in case the card is misplaced. Your Bank has decided to facilitate an increased secure-time. Out of the following, which option should provide the largest rise in the value of ‘t’ ? (A) Instead of 4-decimal-digits, maintain the personal secret code in 4-hexadecimal-digits. (B) Instead of 4-decimal digits, maintain a 5-decimal-digit personal secret code. (C) Reduce the processing speed of the ATM terminals to the half of their current speed. (D) None of the above provides any improvement.

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 221

*UGC NET June 2010, Paper II, original Q40*

> Remote Computing Service involves the use of time sharing and _______. (A) multi-processing (B) interactive processing (C) batch processing (D) real-time processing

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 222

*UGC NET June 2012, Paper II, original Q48*

> Pipelining strategy is called implement (A) instruction execution (B) instruction prefetch (C) instruction decoding (D) instruction manipulation

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 223

*UGC NET June 2013, Paper III, original Q29*

> In homogenous coordinate system (x, y, z) the points with z = 0 are called (A) Cartesian points (B) Parallel points (C) Origin point (D) Point at infinity

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 224

*UGC NET June 2013, Paper III, original Q48*

> When an array is passed as a parameter to a function which of the following statements is correct ? (A) The function can change values in the original array. (B) The function cannot change values in the original array. (C) Results in compilation error. (D) Results in runtime error.

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 225

*UGC NET June 2013, Paper III, original Q52*

> Match the following : a. calloc( ) i. Frees previously allocated space b. free( ) ii. Modifies previously allocated space c. malloc( ) iii. Allocates space for array d. realloc( ) iv. Allocates requested size of space Codes : a b c d (A) iii i iv ii (B) iii ii i iv (C) iii iv i ii (D) iv ii iii i

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 226

*UGC NET Dec 2014, Paper II, original Q14*

> When an array is passed as parameter to a function, which of the following statements is correct ? (A) The function can change values in the original array. (B) In C, parameters are passed by value, the function cannot chan ge the original value in the array. (C) It results in compilation error when the function tries to a ccess the elements in the array. (D) Results in a run time error when the function tries to acc ess the elements in the array.

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 227

*UGC NET Dec 2015, Paper II, original Q16*

> A three dimensional array in 'C' is declared as int A[x]ly][z]. Here, the address of an item at the location Alp]lq|[r] can be computed as follows (where w is the word length of an integer) : (1) &A[O][0][0] +W(y*z*q+z*p+r) (2) &A[[[[[0]w(y**p+z*9+)

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 228

*UGC NET Dec 2015, Paper III, original Q50*

> Why hot the following is ta losy compressio) technique 4) Arithmetic coding

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 229

*UGC NET June 2015, Paper II, original Q46*

> In the case of parallelization, Amdahl's law states that if P is the proportion of a program hat can be made parallel and (1 -P) is the proportion that cannot be parallelized, then the naximum speed-up that can be achieved by using N processors is 1 P + (1 - P) 1 (1 - P) + N•P (N - 1)P + P (1 - P) +

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 230

*UGC NET July 2016, Paper III, original Q71*

> Which of the following is characteristic of an MIS ? (1) Provides guidance in identifying probl ems, finding and evaluating alternative solutions, and selecting or comparing alternatives. (2) Draws on diverse yet predictable data resources to aggregate and summarize data. (3) High volume, data capture focus. (4) Has as its goal the efficiency of da ta movement and processing and interfacing different TPS.

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 231

*UGC NET Dec 2019, original Q59*

> A non-pipelined system takes 30ns to process a task. The same task can be processed in a four-segment pipeline with a clock cycle of 10ns. Determine the speed up of the pipeline for 100 tasks. (1) 3 (2) 4 (3) 3.91 (4) 2.91 61547540934.2 61547540935. 3 61547540936. 4

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 232

*UGC NET Dec 2019, original Q118*

> The Reduced Instruction Set Computer (RISC) characteristics are : (a) Single cycle instruction execution (b) Variable length instruction formats (c) Instructions that manipulates operands in memory (d) Efficient instruction pipeline Choose the correct characteristics from the options given below : (1) (a) and (b) (2) (b) and (c) (3) (a) and (d) (4) (c) and (d) 61547541170.2 61547541171.3 61547541172. 4

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 233

*UGC NET Nov 2020, original Q57*

> A non-pipeline system takes 50ns to process a task. The same task can be processed in six-segment pipeline with a clockeycle of 10ns. Determine approximately the speedup ratio of the pipeline for 500 tasks. (1) 6 (2) 4.95 (3) 5.7 (4) 5.5 53622816726.2 53622816727.3 53622816728.4

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 234

*UGC NET Nov 2020, original Q93*

> Which of the following statements with respect to K-segment pipelining are true? (A) Maximum speedup that a pipeline can provide is k theoretically. (B) It is impossible to achieve maximum speedup k in k-segment pipeline: (C) All segments in pipeline take same time in computation. Choose the correct answer from the options given below: (1) (A) and (B) only (2) (B) and (C) only (3) (A) and (C) only (4) (A), (B) and (C) 53622816870. 2 53622816871. 3 53622816872. 4

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 235

*UGC NET Nov 2021, original Q84*

> 16, 8x1 Which of the following is not an example of pseudo‐instruction? 1. ORG 2. DEC 3. END 4. HLT

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 236

*UGC NET Oct 2022, original Q40*

> A 4-stage pipeline has the stage delay as 150,120.160 and 140 ns respectively. Registers total time required to process 1000 data items on this pipeline is that are used between the stages have delay of 5 ns. Assuming constant locking rate. the 1. 160.5 ms 2. 165.5 ms 3. 120.5 mg 4. 590.5 ms

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 237

*UGC NET Oct 2022, original Q90*

> Given below are two statements: Statement 1: Consider 20 bit Branch' microinstruction code format given below: 2 2 F2 F3 CD BR AD] F1. F2. F3 : Micro-operation fields CD: Condition for branching BR: Branch field AD : Address field Statement I: Instruction represented in above format can perform branch in 4 conditions. In the light of the above statements, choose the most appropriate answer from the options given below : 1. Both Statement I and Statement II are correct 2. Both Statement I and Statement II are incorrect 3. Statement I is correct but Statement II is incorrect 4. Statement I is incorrect but Statement II is correct

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 238

*UGC NET Aug 2024, original Q88*

> A multi processor system with 16 processors is used to execute a parallelizable task. If the serial portion of the task takes 200 clock cycles and the parallel portion take 800 clock cycles. When all 16 processor are used how many total clock cycles are required to complete the task ? (1) 250 (2) 300 (3) 400 (4) 450

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 239

*UGC NET Aug 2024, original Q90*

> A vector processor with 16 lanes can perform an operation on 1024 elements with each operation taking 5 clock cycles. How many cycles are needed to complete the operation ? (1) 64 (2) 80 (3) 100 (4) 128

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 240

*UGC NET June 2025, original Q92*

> The right sequence of suboperations that are performed in arithmetic pipeline is- A. Align the mantissas B. Add or subtract the mantissas C. Normalize the result D. Compare the exponents Choose the correct answer from the options given below: 1. D, A, B, C 2. D, B, A, C 3. B, C, A, D 4. B, C, D, A 42558919421.2 42558919422. 3 42558919423.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 241

*UGC NET Dec 2025 session (Jan 2026), original Q84*

> Question Number : 84

**Chapter foundations**

This question belongs to the ideas covered by **Pipeline and Vector Processing**. Revise these foundations: Parallel Processing; Pipelining; Arithmetic Pipeline; Instruction Pipeline; Vector Processing; Array Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Pipeline and Vector Processing questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-9"></a>

### 9. Input-Output Organization (25 questions)

**What to master:** Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 242

*UGC NET Dec 2012, Paper II, original Q11*

> In compiler design "reducing the (C) 32-Bits strength' refers to (D) 64-Bits (A) reducing the range of values of input variables.

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 243

*UGC NET Dec 2013, Paper II, original Q40*

> Which of the following statements are true ? I. A circuit that adds two bits, producing a sum bit and a carry bit is called half adder. II. A circuit that adds two bits, producing a sum bit and a carry bit is called full adder. III. A circuit that adds two bits and a carry bit producing a sum bit and a carry bit is called full adder. IV. A device that accepts the value of a Boolean variable as input and produces its complement is called an inverter. (A) I & II (B) II & III (C) I, II, III (D) I, III & IV

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 244

*UGC NET Dec 2013, Paper III, original Q54*

> The essential difference between traps and interrupts is (A) traps are asynchronous and interrupts are synchronous with the program. (B) traps are synchronous and interrupts are asynchronous with the program. (C) traps are synchronous and interrupts are asynchronous with the I/O devices. (D) None of these.

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 245

*UGC NET Dec 2014, Paper II, original Q10*

> The size of the ROM required to build an 8-bit adder/subtractor with mode control, carry input, carry output and two’s complement overflow output is given as (A) 2 16 × 8 (B) 2 18 × 10 (C) 2 16 × 10 (D) 2 18 × 8

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 246

*UGC NET Dec 2014, Paper III, original Q2*

> For switching from a CPU user mode to the supervisor mode following type of interrupt is most appropriate (A) Internal interrupts (B) External interrupts (C) Software interrupts (D) None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 247

*UGC NET Dec 2015, Paper III, original Q3*

> Which of the following 8085 microprocessor hardware interrupt has the lowest priority? (1) RST 6.5 (2) RST 7.5 TRAP INTR

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 248

*UGC NET June 2015, Paper II, original Q7*

> Consider a full-adder with the following input values: (a) x=1, y =0 and C¡(carry input) =0 (b) x=0, y = 1 and C;=1 Compute the values of S(sum) and C. (carry output) for the above input values. (1) S=1, C.=0 and S=0, C.=1 (2) S=0, C. =0 and S=1, C.=1 (3) S=1, C.=1 and S=0, C.=0 (4) S=0, C.=1 and S=1, C.=0

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 249

*UGC NET July 2016, Paper III, original Q66*

> A perceptron has input weights W 1 = – 3.9 and W 2 = 1.1 with threshold value T = 0.3. What output does it give for the input x1 = 1.3 and x2 = 2.2 ? (1) – 2.65 (2) – 2.30 (3) 0 (4) 1

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 250

*UGC NET Jan 2017, Paper II, original Q38*

> Match the following w.r.t. Input/Output management : List – I List – II a. Device controller i. Extracts information from the controller register and store it in data buffer b. Device driver ii. I/O scheduling c. Interrupt handler iii. Performs data transfer d. Kernel I/O subsystem iv. Processing of I/O request Codes : a b c d (1) iii iv i ii (2) ii i iv iii (3) iv i ii iii (4) i iii iv ii

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 251

*UGC NET Jan 2017, Paper III, original Q1*

> Which of the following is an interrupt according to temporal relationship with system clock ? (1) Maskable interrupt (2) Periodic interrupt (3) Division by zero (4) Synchronous interrupt

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 252

*UGC NET Jan 2017, Paper III, original Q72*

> A neuron with 3 inputs has the weight vector [0.2 –0.1 0.1] T and a bias θ = 0. If the input vector is X = [0.2 0.4 0.2]T then the total input to the neuron is : (1) 0.20 (2) 1.0 (3) 0.02 (4) –1.0

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 253

*UGC NET Nov 2017, Paper II, original Q10*

> The output of the following combinational circuit is F. The value of F is : (1) 1 3 2P P P /c4977+ (2) 1 2 3P P P /c4977 /c4977+ (3) 1 2 3P P P /c4977+ (4) 1 2 3P P P/c4977+

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 254

*UGC NET July 2018, Paper II, original Q92*

> In RS flip-flop, the output of the flip-flop at time (t +1) is same as the output at time t, after the occurance of a clock pulse if : (1) S= R= 1 (2) S= 0, R = 1 (3) S= 1, R = 0 (4) S= R= 0

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 255

*UGC NET July 2018, Paper II, original Q97*

> Match the items in List - I and List - II : List - I List - II (a) Interrupts which can be delayed when a much highest (i) Normal priority interrupt has occurred (b) Unplanned interrupts which occur while executing (ii) Synchronous a program (c) Source of interrupt is in phase with the system clock (iii) Maskable (iv) Exception Code : (a) (b) (c) (1) (ii) (i) (iv) (2) (ii) (iv) (iii) (3) (iii) (i) (ii) (4) (iii) (iv) (ii)

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 256

*UGC NET July 2018, Paper II, original Q100*

> In 8085 microprocessor, what is the output of following program ? LDA 8000H MVI B, 30H ADD B STA 8001H (1) Read a number from input port and store it in memory (2) Read a number from input device with address 8000H and store it in memory at location 8001H (3) Read a number from memory at location 8000H and store it in memory lo cation 8001H (4) Load A with data from input device with address 8000H and display it on the output device with address 8001H - o 0 o -

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 257

*UGC NET Nov 2021, original Q86*

> ABCDE+*+*FGH+*/ Arrange the following in the increasing order of complexity. A. I/O Module B. I/O processor C. I/O Channel D. DMA Choose the correct answer from the options given below 1. D, C, B, A 2. C, D, A, B 3. A, B, C, D 4. A, D, C, B

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 258

*UGC NET Oct 2022, original Q7*

> Consider a logic gate circuit, with 8 input lines (Do. Di.....Di) and 3 output lines (Ao. Ai. At) specified by following operations Ay = D, + D, + D6+ D, A = Do+Da+ D6+ DT Where + indicates logical OR operation. This circuit is 1. 3x8 multiplexer 2. Decimal to BCD converter 3. Octal to Binary encoder 4. Priority encoder

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 259

*UGC NET Oct 2022, original Q50*

> Consider the following two lists: List I List II (A) Stack overflow (1) Software interrupt B) Timer (1I) Internal interrupt (C) Invalid opcode (IID External interrupt (D). Superior call (IV) Machine check interrupt Which of the following is correct match ? 1. (A)-D. (B)-(ID. (C)-III). (D)-(IV) 2. (A)-(II. (B)-(III. (C)-(D), (D)-(IV) 3. (A)-(I. (B)-(II. (C)-(IV). (D)-I) 4. (A)-(II, (B)-II, (C)-(IV), (D)-(I)

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 260

*UGC NET Aug 2024, original Q109*

> Consider the following statement regarding special purpose registers. (A) Program Counter (PC) keeps the track of next instruction executed (B) Instruction register holds the address of first instruction to be executed (C) Accumulator holds the output of ALU (D) Program Counter (PC) keeps the track of only first instruction of the program Choose the correct answer from the options given below : (1) (A) and (C) Only (2) (A) and (D) Only (3) (B) and (D) Only (4) (A), (B) and (C) Only

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 261

*UGC NET Aug 2024, original Q131*

> Match List - I with List - II. List - I List - II (computing systems) (working/output) (A) Half Adder (1) Has n input and 2" output (B) Decoder (II) CPU Storage Unit (C) Register (III) Used to store program at runtime (D) Main memory (IV) 2-bit addition circuit Choose the correct answer from the options given below : (1) (A)-(LI), (B)-(III), (C)-(IV), (D)-(I) (2) (A)-(IV), (B)-(I, (C)-(Ш), (D)-(I) (3) (A)-(IV), (B)-(I), (C)-(I), (D)-(III) (4) (A) -(IL), (B)-(IV), (C)-(LI), (D)-(1)

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 262

*UGC NET June 2024, original Q104*

> Match List-I with List-ll : List - T List - I T A. Union B. Function I. Virtual Reality C. Interactive Environment II. Shadow mask D. Output device Subroutine Choose the correct answer from the options given below : IV. User defined data type (1) A-IV, B-III, C-I, D-TI (3) A-II, B-IV, C-L, D.M (2) A-IV, B-II, C-II, D-T (4) A-I, B-III, C-IV, D-TI

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 263

*UGC NET June 2025, original Q95*

> Consider the following interrupt protection levels in Linux, and arrange them in the increasing order of their priorities. A. User-Mode Programs (Preemptible) B. Bottom Half Interrupt Handlers C. Top Half Interrupt Handlers D. Kernel System Service Routines (Preemptible) Choose the correct answer from the options given below: 1. B→ A → C → D 2. C→ B → A → D 3. C→ A → B → D 4. A→D →B → C 42558919432.1 42558919434. 3 42558919435.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 264

*UGC NET Dec 2025 session (Jan 2026), original Q85*

> Question Number: 85

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 265

*UGC NET Dec 2025 session (Jan 2026), original Q147*

> Question Number : 147

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 266

*UGC NET Dec 2025 session (Jan 2026), original Q149*

> Question Number : 149

**Chapter foundations**

This question belongs to the ideas covered by **Input-Output Organization**. Revise these foundations: Peripheral Devices; Input-Output Interface; Asynchronous Data Transfer; Modes of Transfer; Priority Interrupt; DMA; Serial Communication.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Input-Output Organization questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-10"></a>

### 10. Memory Hierarchy (57 questions)

**What to master:** Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 267

*UGC NET Dec 2009, Paper II, original Q39*

> A program is located in the smallest available hole in t he memory is _________ (A) best – fit (B) first – bit (C) worst – fit (D) buddy

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 268

*UGC NET Dec 2011, Paper III, original Q15*

> An eight way set associative cache consists of a total of 256 B locks. The main memory contains 8192 blocks, each consisting of 128 words. (a) How many bits are there in the main memory address ? (b) How many bits are there in TAG, SET and WORD fields ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ ______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 269

*UGC NET Dec 2012, Paper II, original Q14*

> Given memory partitions of 100K, is "l' and a fragmentation offset value 500 K, 200 K, 300 K and 600 K (in "O', then it is fragment. order) and processes of 212 K, 417 K, (A) First 112 K, and 426 K (in order), using the (B) Middle first-fit algorithm, in which partition (C) Last would the process requiring 426 K be placed? (D) All of the above (A) 500 K (B) 200 K

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 270

*UGC NET June 2012, Paper II, original Q32*

> Cached and interleaved memories are ways of speeding up memory access between CPU’s and slower RAM. Which memory models are best suited (i.e. improves the performance most) for which programs ? (i) Cached memory is best suited for small loops. (ii) Interleaved memory is best suited for small loops (iii) Interleaved memory is best suited for large sequential code. (iv) Cached memory is best suited for large sequential code. (A) (i) and (ii) are true. (B) (i) and (iii) are true. (C) (iv) and (ii) are true. (D) (iv) and (iii) are true.

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 271

*UGC NET June 2012, Paper II, original Q37*

> Interrupts which are initiated by an instruction are (A) Internal (B) External (C) Hardware (D) Software 38. printf(“%c”, 100); (A) prints 100 (B) prints ASCII equivalent of 100 (C) prints garbage (D) none of the above

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 272

*UGC NET June 2012, Paper II, original Q46*

> A complete microcomputer system consists of (A) Microprocessor (B) Memory (C) Peripheral equipment (D) All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 273

*UGC NET June 2012, Paper II, original Q47*

> Where does a computer add and compare data ? (A) Hard disk (B) Floppy disk (C) CPU chip (D) Memory chip

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 274

*UGC NET Dec 2013, Paper II, original Q47*

> The virtual address generated by a CPU is 32 bits. The Translation Look-aside Buffer (TLB) can hold total 64 page table entries and a 4-way set associative (i.e. with 4- cache lines in the set). The page size is 4 KB. The mini mum size of TLB tag is (A) 12 bits (B) 15 bits (C) 16 bits (D) 20 bits

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 275

*UGC NET Dec 2013, Paper III, original Q70*

> Translation Look-aside Buffer (TLB) is (A) a cache-memory in which item to be searched is compared one-by-one with the keys. (B) a cache-memory in which item to be searched is compared with all the keys simultaneously. (C) an associative memory in which item to be searched is compared one-by-one with the keys. (D) an associative memory in which item to be searched is compared with all the keys simultaneously.

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 276

*UGC NET June 2013, Paper III, original Q59*

> A job has four pages A, B, C, D and the main memory has two page frames only. The job needs to process its pages in following order : ABACABDBACD Assuming that a page interrupt occurs when a new page is brought in the main memory, irrespective of whether the page is swapped out or not. The number of page interrupts in FIFO and LRU page replacement algorithms are (A) 9 and 7 (B) 7 and 6 (C) 9 and 8 (D) 8 and 6

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 277

*UGC NET Dec 2014, Paper II, original Q24*

> Consider an array A[20, 10], assume 4 words per memory cell and t he base address of array A is 100. What is the address of A[11, 5] ? Assume row major storage. (A) 560 (B) 565 (C) 570 (D) 575

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 278

*UGC NET Dec 2014, Paper II, original Q37*

> A specific editor has 200 K of program text, 15 K of initial sta ck, 50 K of initialized data, and 70 K of bootstrap code. If five editors are started simultaneousl y, how much physical memory is needed if shared text is used ? (A) 1135 K (B) 335 K (C) 1065 K (D) 320 K

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 279

*UGC NET Dec 2014, Paper III, original Q1*

> A hierarchical memory system that uses cache memory has ca che access time of 50 nano seconds, main memory access time of 300 nano seconds, 75% of memory reques ts are for read, hit ratio of 0.8 for read access and the write-through scheme is used. What will be the average access time of the system both for read and write requests ? (A) 157.5 n.sec. (B) 110 n.sec. (C) 75 n.sec. (D) 82.5 n.sec.

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 280

*UGC NET Dec 2014, Paper III, original Q49*

> Various storage devices used by an operating system can be arra nged as follows in increasing order of accessing speed : (A) Magnetic tapes → magnetic disks → optical disks → electronic disks → main memory → cache → registers (B) Magnetic tapes → magnetic disks → electronic disks → optical disks → main memory → cache → registers (C) Magnetic tapes → electronic disks → magnetic disks → optical disks → main memory → cache → registers (D) Magnetic tapes → optical disks → magnetic disks → electronic disks → main memory → cache → registers

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 281

*UGC NET Dec 2015, Paper III, original Q4*

> A dynamic RAM has refresh cycle of 32 times per msec. Each refresh operation requires 100 nsec and a memory cycle requires 250 nsec. What percentage of memory's total operating time is required for refreshes ? (1) 0.64 (2) 0.96 (3) 2.00 (4) 0.32

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 282

*UGC NET Dec 2015, Paper III, original Q38*

> Function of memory management unit is : (1) Address translation (2) Memory allocation (3) Cache management (4) All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 283

*UGC NET June 2015, Paper III, original Q51*

> What is the most appropriate function of Memory Management Unit (MMU) ? (1) It is an associative memory to store TLB (2) It is a technique of supporting multiprogramming by creating dynamic partitions (3) It is a chip to map virtual address to physical address (4) It is an algorithm to allocate and deallocate main memory to a process J-8715 9 Paper-III

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 284

*UGC NET July 2016, Paper II, original Q34*

> Which of the following is not typically a benefit of dynamic linking ? I. Reduction in overall program execution time. II. Reduction in overall space consumption in memory. III. Reduction in overall space consumption on disk. IV. Reduction in the cost of software updates. (1) I and IV (2) I only (3) II and III (4) IV only

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 285

*UGC NET July 2016, Paper III, original Q1*

> Which of the following is a sequential circuit ? (1) Multiplexer (2) Decoder (3) Counter (4) Full adder 2. 8085 microprocessor has _____ hardware interrupts. (1) 2 (2) 3 (3) 4 (4) 5

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 286

*UGC NET July 2016, Paper III, original Q6*

> In _____ method, the word is written to the bl ock in both the cache and main memory, in parallel. (1) Write through (2) Write back (3) Write protected (4) Direct mapping

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 287

*UGC NET Jan 2017, Paper II, original Q16*

> An attribute A of datatype varchar (20) has value ‘Ram’ and the attribute B of datatype char (20) has value ‘Sita’ in oracle. The attribute A has _______ mem ory spaces and B has _______ memory spaces. (1) 20, 20 (2) 3, 20 (3) 3, 4 (4) 20, 4

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 288

*UGC NET Jan 2017, Paper II, original Q37*

> In a paging system, it takes 30 ns to search translation Look-a-si de Buffer (TLB) and 90 ns to access the main memory. If the TLB hit ratio is 70%, the effective memory access time is : (1) 48ns (2) 147ns (3) 120ns (4) 84ns

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 289

*UGC NET Jan 2017, Paper III, original Q2*

> Which of the following is incorrect for virtual memory ? (1) Large programs can be written (2) More I/O is required (3) More addressable memory available (4) Faster and easy swapping of process

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 290

*UGC NET Jan 2017, Paper III, original Q49*

> A memory management system has 64 pages with 512 bytes page size. Physical memory consists of 32 page frames. Nu mber of bits required in logi cal and physical address are respectively : (1) 14 and 15 (2) 14 and 29 (3) 15 and 14 (4) 16 and 32

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 291

*UGC NET Dec 2018, original Q69*

> Consider a system with 2 level cache. Access times of Level 1 cache, Level 2 cache and main memory are 0•5 ns, 5 ns and 100 ns respectively. The hit rates of Level 1 and Level 2 caches are 0-7 and 0-8, respectively. What is the average access time of the system ignoring the search time within the cache? -20 ns 91394342274. 7•55 ns 91394342275. 20-75 ns Guide 91394342276. 24-35 ns Let or e Oneto pies in 03 Orient Ou: vien Type: MCQ Option Shufling : Xes

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 292

*UGC NET Dec 2018, original Q122*

> Suppose for a process P, reference to pages in order are 1, 2, 4, 5, 2, 1, 2, 4. Assume that main memory can accomodate 3 pages and the main memory has already pages 1 and 2 in the order 1 - first, 2 - second. At this moment, assume FIFO Page Replacement Algorithm is used then the number of page faults that occur to complete the execution of process Pis 91394342486. 3 91394342487. 5 91394342488 6

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 293

*UGC NET July 2018, Paper II, original Q56*

> Which of the following statements are true ? (a) External Fragmentation exists when there is enough total memory space t o satisfy a request but the available space is contiguous. (b) Memory Fragmentation can be internal as well as external. (c) One solution to external Fragmentation is compaction. Code : (1) (a) and (b) only (2) (a) and (c) only (3) (b) and (c) only (4) (a), (b) and (c)

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 294

*UGC NET July 2018, Paper II, original Q98*

> Which of the following mapping is not used for mapping process in cache memory ? (1) Associative mapping (2) Direct mapping (3) Set-Associative mapping (4) Segmented - page mapping

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 295

*UGC NET Dec 2019, original Q77*

> Consider a paging system where translation look aside buffer (TLB) a special type of associative memory is used with hit ratio of 80%. Assume that memory reference takes 80 nanoseconds and reference time to TLB is 20 nanoseconds. What will be the effective memory access time given 80% hit ratio? (1) 110 nanoseconds (2) 116 nanoseconds (3) 200 nanoseconds (4) 100 nanoseconds 61547541006.2 61547541007.3 61547541008. 4

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 296

*UGC NET Dec 2019, original Q81*

> Which of the following methods are used to pass any number of parameters to the operating system through system calls? (1) Registers (2) Block or table in main memory (3) Stack (4) Block in main memory and stack 61547541022. 2 61547541023. 3 61547541024.4

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 297

*UGC NET Dec 2019, original Q83*

> In a system for a restaurant. the main scenario for placing order is given below : (a) Customer reads menu (b) Customer places order (c) Order is sent to kitchen for preparation (d) Ordered items are served (e) Customer requests for a bill for the order (f) Bill is prepared for this order (g) Customer is given the bill (h) Customer pays the bill A sequence diagram for the scenario will have atleast how many objects among whom the messages will be exchanged. (1) (2) 4 (3) 5 (4) 6 61547541030. 2 61547541031.3 61547541032. 4

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 298

*UGC NET June 2019, original Q99*

> A processor can support a maximum memory of 4 GB where memory is word addressable and a word is 2 bytes. What will be the size of the address bus of the processor? 1. At least 28 bits 2. At least 2 bytes 3. At least 31 bits 4. Minimum 4 bytes 64635085732. 2 64635085733.3 64635085734. 4 Single Line Ouestion Option: No

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 299

*UGC NET Nov 2020, original Q55*

> Consider a machine with a byte addressable main memory of 216 bytes and block size of 8 bytes. Assume that a direct mapped cache consisting of 32 lines used with this machine. How many bits will be there in Tag, line and word field of format of main memory addresses? (1) 8, 5, 3 (2) 8. 6. 2 (3) 7, 5, 4 (4) 7, 6, 3 53622816718.2 53622816719.3 53622816720.4

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 300

*UGC NET Nov 2020, original Q68*

> Consider a single level page table system, with the page table stored in the memory, If the hit rate to TIB is 80%, and it takes 15 nanoseconds to search the TB, and 150 nanoseconds to access the main memory, then what is the effective memory access time, in nanoseconds? (1) 185 (2) 195 (3) 205 (4) 175 53622816770.2 53622816771.3 53622816772.4

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 301

*UGC NET Nov 2021, original Q73*

> A only Given below are three statements related to interrupt handling mechanism A. Interrupt handler routine is not stored at a fixed address in the memory. B. CPU hardware has a dedicated wire called the interrupt request line used for handling interrupts C. Interrupt vector contains the memory addresses for speciaized interrupt handlers. In the context of above statements, choose the correct answer from the options given below: 1. A is TRUE only 2. Both B and C are TRUE only 3. Both A and B are TRUE only 4. Both A, C are TRUE only

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 302

*UGC NET Nov 2021, original Q76*

> 5 Read the following and answer the questions: Consider a machine with 16 GB main memory and 32‐bits virtual address space, with page size as 4KB. Frame size and page size is same for the given machine. The number of bits reserved for the frame offset is ______ 1. 12 2. 14 3. 32 4. 8

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 303

*UGC NET Nov 2021, original Q77*

> 12 Read the following and answer the questions: Consider a machine with 16 GB main memory and 32‐bits virtual address space, with page size as 4KB. Frame size and page size is same for the given machine. Find number of pages required for the given virtual address space 1. 2 2. 2 3. 2 4. 2

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 304

*UGC NET Nov 2021, original Q78*

> 2 Read the following and answer the questions: Consider a machine with 16 GB main memory and 32‐bits virtual address space, with page size as 4KB. Frame size and page size is same for the given machine. What is the minimum number of bits needed for the physical address? 1. 28 2. 34 3. 24 4. 12

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 305

*UGC NET Nov 2021, original Q79*

> 28 Read the following and answer the questions: Consider a machine with 16 GB main memory and 32‐bits virtual address space, with page size as 4KB. Frame size and page size is same for the given machine. What is the size of page table for handling the given virtual address space, given that each page table entry is of size 2 bytes? 1. 2MB 2. 2KB 3. 32MB 4. 12KB

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 306

*UGC NET Nov 2021, original Q80*

> 2MB Read the following and answer the questions: Consider a machine with 16 GB main memory and 32‐bits virtual address space, with page size as 4KB. Frame size and page size is same for the given machine. If a process of size 34KB is to be executed on this machine, then what will be the size of internal fragmentation for this process? 1. 4KB 2. Zero 3. 1KB 4. 2KB

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 307

*UGC NET Nov 2021, original Q88*

> A and B only The cache coherence problem can be solved A. by having multiport memory B. allow only nonshared data to be stored in cache C. using a snoopy cache controller D. uisng memory interleaving Choose the correct answer from the options given below: 1. A and C only 2. B and C only 3. D and C only 4. B and D only

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 308

*UGC NET Nov 2021, original Q89*

> A and C only Given below are two statements 10 20 30 12 10 16 8 8 8 8 8 10) 11) 12) 13) 14) 15) 16) Statement I: CISC computers have a large of number of addressing modes. Statement II: In RISC machines memory access is limited to load and store instructions. In light of the above statements, choose the correct answer from the options given below 1. Both Statement I and Statement II are true 2. Both Statement I and Statement II are false 3. Statement I is true but Statement II is false 4. Statement I is false but Statement II is true

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 309

*UGC NET Oct 2022, original Q9*

> In a cache memory. if address has 9 bits in Tag field and 12 bits in index field, the size of main memory and cache memory would be respectively 1. 2K.4K 2. 1024 K. 2K 3. 4 K, 2048 K 4. 2048K. 4K

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 310

*UGC NET Oct 2022, original Q20*

> Pointers cannot be used to 1. find the address of a variable in memory 2. reference value directly 3. simulate call by reference 4. manipulate dynamic data structure

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 311

*UGC NET June 2023, Paper II, original Q94*

> Consider the following program fragment that deals with a table T with 17 rows (+2) and 1024 columns, computing an average for each column and printing it to screen (i is row index and j is column index): for j = [O.... 1023]{ temp = 0; for i = [O... 16]: temp = temp + T[il [i]; print (temp/17.0); } T [il lil and temp are 32 bit floating point values and memory is word addressable. The temporary variable temp is kept in a processor register so access to temp does not involve a memory reference. The main memory is page and holds 16 pages of size 1024 words, the page replacement policy is "least recently used", If T is stored in the virtual address space in row major format. How many page faults will be encountered? a. 16,402 al Exams Guid b. 17,408 C. 18,208 d. 18,608

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 312

*UGC NET Aug 2024, original Q89*

> A CPU has a 5-stage pipeline with the following stages Fetch (F), Decode (D), Execute (E), Memory (M) and Write-back (W). Each stage takes one clock cycle to complete. Assume there are no pipeline stalls and the pipeline is initially empty. How many clock cycles are required to complete the execution of 10 instructions? (2) 14 (3) 15 (4) 19

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 313

*UGC NET Aug 2024, original Q95*

> Find the correct sequence of the storage device in ascending order based on their access time. (A) Registers (B) Magnetic Disk (C) Magnetic Tapes (D) Main memory (E) Optical Disk Choose the correct answer from the options given below : (1) (B), (A), (D), (C), (E) (2) (B), (A), (E), (D), (C) (3) (C), (B), (A), (E), (D) (4) (C), (E), (B), (D), (A)

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 314

*UGC NET Aug 2024, original Q130*

> Match List - I with List - II. List - I List - Il (Counter) (uses/working) (A) N-bit Ring Counter (I) Uses universal clock (B) Synchronous Counter (LI) Counts exactly N states (C) Asynchronous Counter (1) Counts 0 to 9 (D) Decimal Counter (IV) Main clock is applied to first flip-flop only Choose the correct answer from the options given below : (1) (A)-(II, (B)-(IV), (C)-(I), (D) -(I) (2) (A)-(IV), (B)-(I, (C)-(Ш), (D)-(l) (3) (A)-(II), (B)-(I), (C)-(IV), (D) -(III) (4) (A)-(IV), (B)-(1), (C)-(II, (D) -(Ш) 86/101

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 315

*UGC NET June 2024, original Q31*

> The Boolean expression for the following repubt be HA. B. C) - 1(0, 2, 6) MA. B. C) - 5(1. 3. 5) (1) AC +BC (2) B+ AC PA+ BC (a) A + BC 8S. Arrange the folleving in corree order, so that dry can follow a pruper run time environment : A. Programming statement Compilation C. Memory allocation p. type of vaciable E. Memory deallocation Choose the correct answer from We options given below : (1) A. B, C, D, E

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 316

*UGC NET June 2024, original Q56*

> A computer system with cache access time of 100 ns, a main memory access time of 1100 ns, and a hit ratio of 0.9, then average access time would be : (1) 200 ns (2) 190 ns (5) 210 ns (4) 120 n5 hops can this packet travel before bring dropped? The data belong to what upper-layer protocol? An IPe packet has arrived with the list few hexadecimal digits as shown below. How many 87. 5400001800100110040601 ...to UDP

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 317

*UGC NET June 2024, original Q67*

> Match List-I with List-ll : List - L allows more efficient use of main memory Tist - II A. Batch Multiprogramming user no longer has direct access to the processor B. Time sharing IL. C. Monitor OC Maximize processor use D. Reentrant Procedures IV. minimize response time Choose the correct answer from the options given below : (1) A-MI, B-II, C-IV, D-I (2) A-III, B-IV, C-II, D-I (3) A-I, B-III, C-IV, D-I (4) A-II, B-I, C-IV, D-III Which of the following is the function of the semantic analysis phase of compilation process ?

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 318

*UGC NET June 2025, original Q58*

> The transformation of data from main memory to cache memory is referred as: 1. Data exchange 2. Data transformation 3. Mapping 4. Matching 42558919284. 1 42558919286. 3 42558919287.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 319

*UGC NET June 2025, original Q91*

> The computer needs to process each instruction with the following sequence of steps: A. Calculate the effective address B. Fetch the Instruction from memory C. Decode the instruction D. Fetch the operands from the memory E. Execute the Instruction Choose the correct answer from the options given below: 1. A, B, C, D, E 2. B, A, D, A, E 3. B, C, A, D, E 4. C, B, A, D, E 42558919416. 1 42558919418.3 42558919419.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 320

*UGC NET June 2025, original Q108*

> Which of the following statements are true? A. In the write-through policy, only the cache is updated B. In the write-back policy, both cache and main memory are updated C. Cache coherence problems exist in multiprocessors with private caches because of the need to share writable data D. Cache coherence problem can be solved by means of hardware-only scheme Choose the correct answer from the options given below: 1. A, B Only 2. B, C Only 3. C, D Only 4. A, B, C Only 42558919485.2 42558919486. 3 42558919487.4

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 321

*UGC NET June 2025, original Q128*

> Match List I with List I! List I List Il A. Address Space I. Associative Mapping B. Memory Space Il. Logical address C. Cache Memory Ill. physical address D. Segmented Program IV. Virtual address Choose the correct answer from the options given below: 1. A-IV, B-III, C-I, D-II 2. A-I, B-II, C-IV, D-IlI 3. A-III, B-IV, C-I, D-II 4. A-II, B-IV, C-I, D-III 42558919565.2 42558919566.3 42558919567.4 Mastor Ner: 128

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 322

*UGC NET Dec 2025 session (Jan 2026), original Q58*

> Question Number : 58 = (x+y)(x+ z) C. Distributive law III. x + xy =x D. Absorption law IV. x+(y +z) = (x+ y)+ z Choose the correct answer from the options given below: 1. A-I, B-II, C-IV, D-III 2. A-I, B-IV, C-II, D-III 3. A-III, B-IV, C-II, D-I 4. A-III, B-II, C-IV, D-I 6119878634.2 6119878635.3 6119878636.4

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 323

*UGC NET Dec 2025 session (Jan 2026), original Q59*

> Question Number : 59 = (x+y)(x+ z) C. Distributive law II. x+ xy =x D. Absorption law IV. x+(y+z) = (x+y)+ z Choose the correct answer from the options given below: 1. A-I, B-II, C-IV, D-III 2. A-I, B-IV, C-II, D-III 3. A-III, B-IV, C-II, D-I 4. A-II, B-II, C-IV, D-I 6119878634.2 6119878635.3 6119878636.4

**Chapter foundations**

This question belongs to the ideas covered by **Memory Hierarchy**. Revise these foundations: Main Memory; Auxiliary Memory; Associative Memory; Cache Memory; Virtual Memory; Memory-Management Hardware.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Memory Hierarchy questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-11"></a>

### 11. Multiprocessors (71 questions)

**What to master:** Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam lens:** Translate the machine description into bits, register transfers, memory blocks, or pipeline stages before calculating.

**Reusable method:** Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation.

**High-yield rules:** Two's complement range for n bits is -2^(n-1) to 2^(n-1)-1. AMAT = hit time + miss rate x miss penalty. Pipeline time is approximately (k+n-1) stage times when stages are balanced.

**Common traps:** Do not mix bytes with words, logical with physical addresses, hit ratio with miss ratio, or latency with throughput.

---

#### Question 324

*UGC NET June 2010, Paper II, original Q9*

> What is decimal equivalent of BCD 11011.1100 ? (A) 22.0 (B) 22.2 (C) 20.2 (D) 21.2

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 325

*UGC NET June 2010, Paper II, original Q48*

> CDMA Cell uses ________ carriers of 1.25 MHz. (A) 9 (B) 18 (C) 22 (D) 64

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 326

*UGC NET Dec 2011, Paper III, original Q3*

> (a) What are the kinds of degradation that can be easily restore d ? Explain inverse filteration and wiener filteration method. (b) A source emits 6 symbols with probabilities 1/2, 1/4, 1/8, 1/16, 1/32, 1/32. Determine its Huffman code.

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 327

*UGC NET Dec 2011, Paper III, original Q16*

> Why does LAN tend to use Broadcast Network ? Why not use Netw orks consisting of multiplexer and switches ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ ______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 328

*UGC NET June 2012, Paper II, original Q4*

> Each item has four alternative responses marked (A), (B), (C) and (D). You have to darken the circle as indicated below on the correct response against each item. Example : where (C) is the correct response.

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 329

*UGC NET June 2012, Paper II, original Q35*

> If an integer needs two bytes of storage, then the maximum value of a signed integer is (A) 2 16 – 1 (B) 2 15 – 1 (C) 2 16 (D) 2 15

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 330

*UGC NET Dec 2013, Paper II, original Q4*

> Each item has four alternative responses marked (A), (B), (C) and (D). You have to darken the circle as indicated below on the correct response against each item. Example : where (C) is the correct response.

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 331

*UGC NET Dec 2013, Paper II, original Q5*

> Using the RSA public key crypto system, if p = 13, q = 31 and d = 7, then the value of e is (A) 101 (B) 103 (C) 105 (D) 107

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 332

*UGC NET Dec 2013, Paper II, original Q21*

> What is the value of the postfix expression ? a b c d + – ∗ (where a = 8, b = 4, c = 2 and d = 5) (A) – 3 8 (B) – 8 3 (C) 24 (D) –24

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 333

*UGC NET Dec 2013, Paper II, original Q41*

> Active X controls are Pentium binary programs that can be embedded in ________ (A) Word pages (B) URL pages (C) Script pages (D) Web pages

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 334

*UGC NET Dec 2013, Paper III, original Q4*

> Each item has four alternative responses marked (A), (B), (C) and (D). You have to darken the circle as indicated below on the correct response against each item. Example : where (C) is the correct response.

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 335

*UGC NET Dec 2013, Paper III, original Q51*

> Synchronization is achieved by a timing device called a ________ which generates a periodic train of ________. (A) clock generator, clock pulse (B) master generator, clock pulse (C) generator, clock (D) master clock generator, clock pulse

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 336

*UGC NET June 2013, Paper III, original Q35*

> Which of the following is/are the fundamental semantic model(s) of parameter passing ? (A) in mode (B) out mode (C) in-out mode (D) all of the above

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 337

*UGC NET June 2013, Paper III, original Q55*

> Given code word 1110001010 is to be transmitted with even parity check bit. The encoded word to be transmitted for this code is (A) 11100010101 (B) 11100010100 (C) 1110001010 (D) 111000101

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 338

*UGC NET Dec 2014, Paper II, original Q6*

> The BCD adder to add two decimal digits needs minimum of (A) 6 full adders and 2 half adders (B) 5 full adders and 3 half adders (C) 4 full adders and 3 half adders (D) 5 full adders and 2 half adders

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 339

*UGC NET Dec 2014, Paper II, original Q7*

> The Excess-3 decimal code is a self-complementing code because (A) The binary sum of a code and its 9’s complement is equal to 9. (B) It is a weighted code. (C) Complement can be generated by inverting each bit pattern. (D) The binary sum of a code and its 10’s complement is equal to 9.

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 340

*UGC NET Dec 2014, Paper II, original Q30*

> How many distinct stages are there in DES algorithm, which i s parameterized by a 56-bit key ? (A) 16 (B) 17 (C) 18 (D) 19

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 341

*UGC NET Dec 2014, Paper III, original Q5*

> How many times will the following loop be executed ? LXI B, 0007 H LOP : DCX B MOV A, B ORA C JNZ LOP (A) 05 (B) 07 (C) 09 (D) 00

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 342

*UGC NET Dec 2014, Paper III, original Q44*

> To compute function points (FP), the following relationship is used FP = Count – total × (0.65 + 0.01 × Σ(F i)) where F i (i = 1 to n) are value adjustment factors (VAF) based on n questions. The value of n is (A) 12 (B) 14 (C) 16 (D) 18

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 343

*UGC NET Dec 2014, Paper III, original Q65*

> Given a simple image of size 10 × 10 whose histogram models the symbol probabilities and is given by p1 p 2 p 3 p 4 a b c d The first order estimate of image entropy is maximum when (A) a = 0, b = 0, c = 0, d = 1 (B) a = 1 2 , b = 1 2 , c = 0, d = 0 (C) a = 1 3 , b = 1 3 , c = 1 3 , d = 0 (D) a = 1 4 , b = 1 4 , c = 1 4 , d = 1 4

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 344

*UGC NET Dec 2014, Paper III, original Q69*

> Five men are available to do five different jobs. From past recor ds, the time (in hours) that each man takes to do each job is known and is given in the following table : Jobs I II III IV V P 2 9 2 7 1 Q 6 8 7 6 1 R 4 6 5 3 1 S 4 2 7 3 1 Men T 5 3 9 5 1 Find out the minimum time required to complete all the jobs. (A) 5 (B) 11 (C) 13 (D) 15

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 345

*UGC NET Dec 2015, Paper II, original Q24*

> In a typical mobile phone system with hexagonal cells, it is forbidden to reuse a frequency Cand in adjacent cells. If 840 frequencies are available, how many can be used in a givey (1) 280 2) 210 (3) 140 (4) 120

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 346

*UGC NET Dec 2015, Paper II, original Q25*

> Using p =3, q=13, d = 7 and e = 3 in the RSA algorithm, what is the value of ciphertext for a plain text 5? (1) 13 (2) 21 (3) 26 (4) 33

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 347

*UGC NET Dec 2015, Paper II, original Q29*

> A system has four processes and five allocatable resources. The current allocation and maximum needs are as follows: Allocated Maximum Available Process A 10211 11213 00×11 Process B 20110 22210 Process C 11010 21310 Process D 11110 11221 The smallest value of x for which the above system in safe state is (1) 1 (2) 3 (3) 2 (4) 0

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 348

*UGC NET Dec 2015, Paper III, original Q32*

> The end points of a given line are (0, 0) and (6, 18). Compute each value of y as x steps from 0 to 3, by using equation of straight line : (1) For x=0, y=0; x=1, y= 3; x=2, y= 6; x= 3, y= 9 (2) For x=0, y=1; x=1, y= 3; x= 2, y=4; x= 3, y= 9 (3) For x=0, y=2; x=1, y=3; x=2, y=6; x=3, y=9 (4) For x=0, y=0; x=1, y=3; x=2, y=4; x=3, y = 6

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 349

*UGC NET Dec 2015, Paper III, original Q43*

> A horn clause is (1) A clause in which no variables occur in the expression (2) A clause that has at least one negative literal

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 350

*UGC NET Dec 2015, Paper III, original Q47*

> In constraint satisfaction problem, constraints can be stated as (1) Arithmatic equations and inequalities that bind the values of variables (2) Arithmatic equations and inequalities that doesn't bind any restriction over variables (3) Arithmatic equations that impose restrictions over variables (4) Arithmatic equations that discard constraints over the given variables

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 351

*UGC NET June 2015, Paper II, original Q13*

> Given that x=7.5, j= - 1.0, n=1.0, m=2.0 the value of - -x+j= =x>n>=m is : (1) 0 (2) 1 (3) 2 (4)

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 352

*UGC NET June 2015, Paper III, original Q4*

> Each item has four alternative responses marked (1), (2), (3) and (4). You have to darken the circle as indicated below on the correct response against each item. Example: 1 2 * where (3) is the correct response. 30 :

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 353

*UGC NET July 2016, Paper II, original Q15*

> What is the value returned by the function f given below when n = 100 ? int f (int n) { if (n = = 0) then return n; else return n + f(n-2); } (1) 2550 (2) 2556 (3) 5220 (4) 5520

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 354

*UGC NET July 2016, Paper II, original Q26*

> A multiplexer combines four 100-Kbps channels us ing a time slot of 2 bits. What is the bit rate ? (1) 100 Kbps (2) 200 Kbps (3) 400 Kbps (4) 1000 Kbps

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 355

*UGC NET July 2016, Paper III, original Q3*

> Which of the following in 8085 microprocessor performs HL = HL + DE ? (1) DAD D (2) DAD H (3) DAD B (4) DAD SP

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 356

*UGC NET July 2016, Paper III, original Q4*

> Each item has four alternative responses marked (1), (2), (3) and (4). You have to darken the circle as indicated below on the correct response against each item. Example : where (3) is the correct response.

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 357

*UGC NET July 2016, Paper III, original Q72*

> How does randomized hill-climbing choose the next move each time ? (1) It generates a random move from the moveset, and accepts this move. (2) It generates a random move from the whole state space, and accepts this move. (3) It generates a random move from the m oveset, and accepts this move only if this move improves the evaluation function. (4) It generates a random move from the whole state space, and accepts this move only if this move improves the evaluation function.

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 358

*UGC NET Jan 2017, Paper II, original Q1*

> Consider a sequence F 00 defined as : F 00 (0) = 1, F 00 (1) = 1 F 00 (n) = 10 ∗ F00 (n – 1) + 100 F00 (n – 2) for n ≥ 2 Then what shall be the set of values of the sequence F 00 ? (1) (1, 110, 1200) (2) (1, 110, 600, 1200) (3) (1, 2, 55, 110, 600, 1200) (4) (1, 55, 110, 600, 1200)

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 359

*UGC NET Jan 2017, Paper II, original Q4*

> Each item has four alternative responses marked (1), (2), (3) and (4). You have to darken the circle as indicated below on the correct response against each item. Example : where (3) is the correct response.

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 360

*UGC NET Jan 2017, Paper II, original Q49*

> In 3G network, W-CDMA is also known as UMTS. The minimum spectrum a llocation required for W-CDMA is _______. (1) 2 MHz (2) 20 KHz (3) 5 KHz (4) 5 MHz

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 361

*UGC NET Jan 2017, Paper III, original Q16*

> Below are the few steps given for scan-conve rting a circle using Bresenham’s Algorithm. Which of the given steps is not correct ? (1) Compute d = 3 – 2r (where r is radius) (2) Stop if x > y (3) If d < 0, then d = 4 x + 6 and x = x + 1 (4) If d ≥ 0, then d = 4 ∗ (x – y) + 10, x = x + 1 and y = y + 1

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 362

*UGC NET Jan 2017, Paper III, original Q24*

> A recursive function h, is defined as follows : h(m) = k, if m = 0 = 1, if m = 1 = 2 h(m – 1) + 4h(m – 2), if m ≥ 2 If the value of h(4) is 88 then the value of k is : (1) 0 (2) 1 (3) 2 (4) –1

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 363

*UGC NET Nov 2017, Paper II, original Q1*

> If the time is now 4 O’clock, what will be the time after 101 hours from n ow ? (1) 9 O’clock (2) 8 O’clock (3) 5 O’clock (4) 4 O’clock

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 364

*UGC NET Nov 2017, Paper II, original Q4*

> Each item has four alternative responses marked (1), (2), (3) and (4). You have to darken the circle as indicated below on the correct response against each item. Example : where (3) is the correct response.

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 365

*UGC NET Nov 2017, Paper II, original Q33*

> Which of the following regular expressions, each describing a langu age of binary numbers (MSB to LSB) that represents non-negative decimal values, does not include even values ? (1) 0*1+0*1* (2) 0*1*0+1* (3) 0*1*0*1+ (4) 0+1*0*1* Where {+, *} are quantification characters.

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 366

*UGC NET July 2018, Paper II, original Q44*

> Which of the following statements are true ? (a) Advanced Mobile Phone System (AMPS) is a second generation cellular phone system. (b) IS - 95 is a second generation cellular phone system based on CDMA and DSS S. (c) The Third generation cellular phone system will provide universal per sonnel communication. Code : (1) (a) and (b) only (2) (b) and (c) only (3) (a), (b) and (c) (4) (a) and (c) only

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 367

*UGC NET July 2018, Paper II, original Q86*

> If Ai= {−i, ... −2,−1, 0, 1, 2, . . . . . i} then i i 1 A ∞ = ∪ is : (1) Z (2) Q (3) R (4) C

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 368

*UGC NET July 2018, Paper II, original Q87*

> Match the following in List - I and List - II, for a function f : List - I List - II (a) x y (f (x)= f (y) → x= y) (i) Constant (b) y ∃ x (f (x)= y) (ii) Injective (c) x f (x)= k (iii) Surjective Code : (a) (b) (c) (1) (i) (ii) (iii) (2) (iii) (ii) (i) (3) (ii) (i) (iii) (4) (ii) (iii) (i)

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 369

*UGC NET July 2018, Paper II, original Q91*

> CMOS is a Computer Chip on the motherboard, which is : (1) RAM (2) ROM (3) EPROM (4) Auxillary storage

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 370

*UGC NET July 2018, Paper II, original Q93*

> Match the terms in List - I with the options given in List - II : List - I List - II (a) Decoder (i) 1 line to 2 n lines (b) Multiplexer (ii) n lines to 2n lines (c) De multiplexer (iii) 2n lines to 1 line (iv) 2n lines to 2 n−1 lines Code : (a) (b) (c) (1) (ii) (i) (iii) (2) (ii) (iii) (i) (3) (ii) (i) (iv) (4) (iv) (ii) (i)

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 371

*UGC NET June 2019, original Q67*

> The parallel bus arbitration technique uses an external priority encoder and a decoder. Suppose, a parallel arbiter has 5 bus arbiters. What will be the size of priority encoder and decoder respectively? 1. 4x2, 2x4 2x4,4x2 3. 3x8, 8×3 4. 8x3, 3x8 64635085604. 2 64635085605.3 64635085606.4 Single One Question pros: No Option eng on Vent Type: MCQ Option Shufling : No

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 372

*UGC NET Nov 2021, original Q3*

> 1 if N is odd, otherwise 0 Consider the following recursive function F() in Java that takes an integer value and returns a string value: public static String F( int N) { if ( N <= 0) return "‐"; return F(N ‐ 3) + N + F(N ‐ 2) + N; } The value of F(5) is: 1. ‐2‐25‐3‐135 2. ‐2‐25‐1‐3‐135 3. ‐1‐145‐2‐245 4. ‐2‐25‐3‐1‐135

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 373

*UGC NET Nov 2021, original Q8*

> A and B only 1. M = 2. M = 3. M = 4. M =

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 374

*UGC NET Nov 2021, original Q15*

> correct A system has 99.99% uptime and has a mean‐time‐between‐failure of 1 day. How fast does the system has to repair itself in order to reach this availability goal? 1. ~9 Seconds 2. ~10 Seconds 3. ~11 Seconds 4. ~12 Seconds

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 375

*UGC NET Nov 2021, original Q26*

> 21 For which value of n is Wheel graph W regular? 1. 2 2. 3 3. 4 4. 5

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 376

*UGC NET Nov 2021, original Q28*

> A and B only Match List I with List II n 29) 30) 31) 32) 33) 34) 35) 36) List I List II Identity Name A. x + x =x I. Identity Law B. x + 0 = x II. Absorption Law C. x +1 = 1 III. Idempotent law D. x + xy = x IV. Domination Law Choose the correct answer from the options given below: 1. A ‐ III, B ‐I , C ‐ II, D ‐ IV 2. A ‐ I, B ‐III , C ‐ IV, D ‐ II 3. A ‐ III, B ‐I , C ‐ IV, D ‐ II 4. A ‐ III, B ‐IV , C ‐ I, D ‐ II

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 377

*UGC NET Nov 2021, original Q32*

> A and B only 1. has at least one 1 2. should end with 0 3. has no consecutive 0’s or 1’s 4. has at least two 0’s

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 378

*UGC NET Nov 2021, original Q81*

> 4KB Match List I with List II List I List II A. Odd Function I. NAND gate B. Universal Gate II. XOR gate C. 2421 code III. Amplification D. Buffer IV. Self‐Complementing Choose the correct answer from the options given below: 1. A ‐ I, B ‐ II, C ‐ III, D ‐ IV 2. A ‐ II, B ‐ I, C ‐ IV, D ‐ III 3. A ‐ I, B ‐ III, C ‐ II, D ‐ IV 4. A ‐ IV, B ‐ II, C ‐ III, D ‐ I

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 379

*UGC NET Nov 2021, original Q82*

> A ‐ I, B ‐ II, C ‐ III, D ‐ IV The Octal equivalent of hexadecimal (D.C) is: 1. (15.6) 2. (61.6) 3. (15.3) 4. (61.3)

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 380

*UGC NET Oct 2022, original Q8*

> The total storage capacity of a floppy disk having 80 tracks and storing 128 bytes/sector is 163,840 bytes. How many sectors does this disk have? 1. 25 2. 2048 3. 4K 4. 16

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 381

*UGC NET Oct 2022, original Q18*

> Using 'RSA' algorithm. if p = 13, q = 5 and e = 7, the value of d and cipher value of 6 with (e. n) key are 1. 7.4 2. 7.1 3. 7,46 4. 55, 1

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 382

*UGC NET Oct 2022, original Q66*

> (A) -III, (B)-(I), (C)-(IV). (D)-(I 2. (A)-ID. (B)-(IV). (C)-Д. (D)-Ш) 3. (A)-(II. (B)-I). (C)-(IV). (D)-(D) 4. (A)-(I). (B)-(D. (C)-(IV), (D)-(ITI)

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 383

*UGC NET Oct 2022, original Q67*

> (A)-(I. (B)-II, (C)-(II). (D)-(IV 2. (A)-II. (B)-(I, (C)-III, (D-(IV) 3. (A)-III. (B)-D, (C-ID. (D)-(IV) 4. (A)-Ш), (B)-(L). (C)-(TV). (D)-(L

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 384

*UGC NET Oct 2022, original Q68*

> (А)-. (B)-(IV). (C)-(I. (D)-(D 2. (A)-(II), (B)-III. (C)-(IV). (D)-(D 3. (A)-III). (B)-(IV), (C)-T, (D)-L 4. (A)-II. (B)-(III, (C)-(I, (D)-(IV)

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 385

*UGC NET Oct 2022, original Q69*

> (A)-(I), (B)-(I). (C)-(IV), (D)-II 2. (A)-I). (B)-II. (C)-II. (D)-(IV) 3. (A)-(IV). (B)-(IL, (C)-D. (D)-ID 4. (A)-(IV). (B)-(D. (C-II. (D)-I)

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 386

*UGC NET Oct 2022, original Q70*

> (A)-Ш). (B)-II. (C)-(IV). (D)-(I) 2. (4)-(D. (B)-ID. (C)-(IL. (D)-(IV) 3. (A)-(1). (B)-I, (C-d. D-(IV) 4. (A)-I). (B)-(D). (C)-(III, (D)-(IV)

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 387

*UGC NET Oct 2022, original Q71*

> (A)-I). (B)-(I. (C)-(IV), (D)-III 2. (A)-(II. (B)-(L), (C)-III. (D)-(IV) 3. (А)-(IV). (В)-ШІ. (С)-(I). (Д)-ШІ) 4. (A)-(IV). (B)-(D. (C)-II, (D)-II

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 388

*UGC NET Oct 2022, original Q72*

> (A)-. (B) -I). (C)-(IV). (D)-(Il) 2. (A)-III). (B)-(I). (C)-(IV). (D)-II) 3. (A)-(I). (B)-(IV), (C)-(II), (D)-(I 4. (A)-(IV). (B)-(II. (C)-(III). (D)-(I)

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 389

*UGC NET Oct 2022, original Q74*

> (A)-(IV). (B)-Ш. (C)-I). (D)-I) 2. (A)-I), (B)-(Ш), (C)-(TV), (D)-(D) 3. (A)-(IV). (B)-III, (C)-I), (D)-II

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 390

*UGC NET June 2024, original Q7*

> Which of the following is not a characteristics of a specialized embedded OS ? (1) real time scheduling policy (2) responds to external interrupts (3) provides special non-sequential Eleg, (4) provides fixed or variable sized partitions.

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 391

*UGC NET June 2024, original Q9*

> The techniques used to handle the phantom problem are A. Time stamping • B. Index locking C. Predicate locking 7D. Execution indexing Choose the correct answer from the options given below: B and COnly (3) A and D Only (4) Cand D Only (1) A and B Only (2)

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 392

*UGC NET June 2024, original Q53*

> A least integer n such that f(x) is O(an) for cach of the following functions, Arrange follow according to the value of n in increasing order : A. f(x) = 3x + (log x)* B. /(x) - (=>+*°+ 1)/(23+1) c. f(x) - (x2+x≥+ 1)/(z? + 1) D. F(x) = (x2 + 5logx)/(x2+1) (1) D, C, A, B Choose the correct answer from the options given below : (2)D, C. B. A (3) B,C, A. D (4) B, A, C, D

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 393

*UGC NET June 2024, original Q90*

> (1) 0.624050 s. 5000 km. (2) 1.691726 s. (3) 2.425080 s. (4) 1.714030s. How much time does an algorithm using 250 bit operations need if each bit operation takes 91. 2-3 second of time? (1) 1 hour (2) 10 minutes (3) 30 minutes (4) 1.5 hour

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 394

*UGC NET June 2024, original Q128*

> Arrange the following prefix expressions based on their values in increasing order : A. +-* 2/8432 * 33*425 C. +-T32T23/6-42 +3+3T 3+113 Choose the correct answer from the options given below : (1) A, B, C, D (2) B, A, C. D (3) D, C, B, A (4) C, D, A, B

**Chapter foundations**

This question belongs to the ideas covered by **Multiprocessors**. Revise these foundations: Characteristics; Interconnection Structures; Interprocessor Arbitration; Interprocessor Communication and Synchronization; Cache Coherence; Multicore Processors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Multiprocessors questions: Write widths and units first; trace one instruction or memory access; then apply the relevant timing, cache, representation, or speedup equation. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

## Coverage and quality notes

- Recovered question blocks in this unit: **394**
- Chapter placements with direct keyword support: **327**
- Chapter placements needing manual review: **67**
- Questions with validated answers in this guide: **0**
- OCR may flatten mathematical notation, tables, code indentation, and figures. Full audit references are retained in the structured data.
- Some combined Paper 1/Paper 2 scans and older papers lack a trustworthy embedded key. Such questions remain pending rather than receiving guessed answers.

---

[Back to contents](#contents) · [All units](README.md) · [Project home](../README.md)

