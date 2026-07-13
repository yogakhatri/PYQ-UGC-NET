# Unit 7: Data Structures and Algorithms

[Project home](../README.md) · [All units](README.md) · [Official syllabus](syllabus.md)

## Contents

- [How to use this guide](#status-and-use)
- [Unit-wide exam playbook](#unit-wide-exam-playbook)
- [1. Data Structures](#chapter-1)
- [2. Performance Analysis and Recurrences](#chapter-2)
- [3. Design Techniques](#chapter-3)
- [4. Lower-Bound Theory](#chapter-4)
- [5. Graph Algorithms](#chapter-5)
- [6. Complexity Theory](#chapter-6)
- [7. Selected Topics](#chapter-7)
- [8. Advanced Algorithms](#chapter-8)
- [Coverage and quality notes](#coverage-and-quality-notes)

## Status and use

This guide contains all **250 question blocks currently recoverable and assigned to Unit 7** from the local UGC NET archive. Questions are arranged chapter-wise and numbered continuously through the unit.

> [!WARNING]
> This is a working extraction inventory, not a solved guide. All answers remain unvalidated. Some unit and chapter placements use fallback routing, and OCR or missing figures can make questions incomplete.

Use this file for question discovery and broad chapter revision. The chapter notes and exam methods are general, not question-specific solutions. Full source paths, PDF pages and classification states remain in the structured data for auditing.

## Unit-wide exam playbook

- **Core idea:** Choose the data structure or invariant first, then derive the complexity rather than recalling it in isolation.
- **Method:** Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked.
- **Rules/formulas:** Master theorem applies only to suitable forms. BFS gives unweighted shortest paths; Dijkstra needs nonnegative edges; comparison sorting has an Omega(n log n) lower bound.
- **Frequent traps:** Do not confuse tree height with node count, stable with in-place sorting, amortized with average complexity, or NP-hard with NP-complete.

## Chapter-wise concepts and PYQs

<a id="chapter-1"></a>

### 1. Data Structures (53 questions)

**What to master:** Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam lens:** Choose the data structure or invariant first, then derive the complexity rather than recalling it in isolation.

**Reusable method:** Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked.

**High-yield rules:** Master theorem applies only to suitable forms. BFS gives unweighted shortest paths; Dijkstra needs nonnegative edges; comparison sorting has an Omega(n log n) lower bound.

**Common traps:** Do not confuse tree height with node count, stable with in-place sorting, amortized with average complexity, or NP-hard with NP-complete.

---

#### Question 1

*UGC NET Dec 2009, Paper II, original Q23*

> At a hill station, the parking lot is one long drive way snaking up a hill side. Cars drive in and park right behind the car in front of them, one behind another. A car can’t leave until all the cars in front of it have left. Is the parking lot more like (A) An array (B) A stack (C) A queue (D) A linked list

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 2

*UGC NET Dec 2009, Paper II, original Q24*

> With regard to linked list, which of the following stateme nt is false ? (A) An algorithm to search for an element in a singly linked li st requires 0(n) operations in the worst case. (B) An algorithm for deleting the first element in a singly linked list requires 0(n) operations in the worst case. (C) An algorithm for finding the maximum value in a circular li nked list requires 0(n) operations. (D) An algorithm for deleting the middle node of a circular li nked list requires 0(n) operations.

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 3

*UGC NET June 2010, Paper II, original Q22*

> What is the most appropriate data structure to implement a priority queue ? (A) Heap (B) Circular array (C) Linked list (D) Binary tree

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 4

*UGC NET June 2010, Paper II, original Q23*

> In a complete binary tree of n nodes, how far are the two most distant nodes ? Assume each edge in the path counts as ! (A) About log 2n (B) About 2 log 2n (C) About n log 2n (D) About 2n

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 5

*UGC NET Dec 2011, Paper III, original Q10*

> Two binary trees are similar if they are either empty or both non-empty and have similar left and right sub trees. Write a function in C++ to dec ide whether two binary trees are similar. What is the running time of your function ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 6

*UGC NET Dec 2012, Paper II, original Q16*

> In which tree, for every node the height of its left subtree and right subtree (B) code optimization using cheaper machine instructions. differ almost by one? (A) (C) reducing efficiency of program. Binary search tree (B) AVL tree (D) None of the above (C) Threaded Binary Tree (D) Complete Binary Tree

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 7

*UGC NET Dec 2012, Paper II, original Q40*

> Given an empty stack, after performing command is used to set the task push (1), push (2), Pop, push (3), push priority? (4), Pop, Pop, push(5), Pop, what is the (A) init value of the top of the stack? (B) nice (A) 4 (C) kill (B) 3 (D) PS (C) 2

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 8

*UGC NET June 2012, Paper II, original Q1*

> The postfix expression AB + CD – * can be evaluated using a (A) stack (B) tree (C) queue (D) linked list

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 9

*UGC NET June 2012, Paper II, original Q2*

> The post order traversal of a binary tree is DEBFCA. Find out the pre- order traversal. (A) ABFCDE (B) ADBFEC (C) ABDECF (D) None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 10

*UGC NET June 2012, Paper II, original Q8*

> A binary search tree is a binary tree : (A) All items in the left subtree are less than root (B) All items in the right subtree are greater than or equal to the root (C) Each subtree is itself a binary search tree (D) All of the above COMPUTER SCIENCE AND APPLICATIONS Paper – II Note : This paper contains fifty (50) objective type questions, each question carrying two (2) marks. Attempt all the questions. www.solutionsadda.in

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 11

*UGC NET June 2012, Paper II, original Q11*

> B+ tree are preferred to binary tree in Database because (A) Disk capacity are greater than memory capacities (B) Disk access is much slower than memory access (C) Disk data transfer rates are much less than memory data transfer rate (D) Disks are more reliable than memory

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 12

*UGC NET June 2012, Paper II, original Q13*

> Leaves of which of the following trees are at the same level ? (A) Binary tree (B) B-tree (C) AVL-tree (D) Expression tree

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 13

*UGC NET June 2012, Paper II, original Q27*

> The Inorder traversal of the tree will yield a sorted listing of elements of tree in (A) Binary tree (B) Binary search tree (C) Heaps (D) None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 14

*UGC NET June 2012, Paper II, original Q49*

> Which of the following data structure is linear type ? (A) Strings (B) Lists (C) Queues (D) All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 15

*UGC NET June 2012, Paper II, original Q50*

> To represent hierarchical relationship between elements, which data structure is suitable ? (A) Dequeue (B) Priority (C) Tree (D) All of the above www.solutionsadda.in

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 16

*UGC NET June 2013, Paper III, original Q49*

> Suppose you want to delete the name that occurs before “Vivek” in an alphabetical listing. Which of the following data structures shall be most efficient for this operation ? (A) Circular linked list (B) Doubly linked list (C) Linked list (D) Dequeue

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 17

*UGC NET Dec 2014, Paper II, original Q25*

> A full binary tree with n leaves contains (A) n nodes (B) log 2 n nodes (C) 2n –1 nodes (D) 2 n nodes

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 18

*UGC NET Dec 2014, Paper III, original Q36*

> Suppose that we have numbers between 1 and 1000 in a binary search tree and we want to search for the number 365. Which of the following sequences could not be the sequence of nodes examined ? (A) 4, 254, 403, 400, 332, 346, 399, 365 (B) 926, 222, 913, 246, 900, 260, 364, 365 (C) 927, 204,913, 242, 914, 247, 365 (D) 4, 401, 389, 221, 268, 384, 383, 280, 365

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 19

*UGC NET Dec 2014, Paper III, original Q39*

> Converting a primitive type data into its corresponding wrapper c lass object instance is called (A) Boxing (B) Wrapping (C) Instantiation (D) Autoboxing

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 20

*UGC NET Dec 2014, Paper III, original Q53*

> Monitor is an Interprocess Communication (IPC) technique which can be describe d as (A) It is higher level synchronization primitive and is a collec tion of procedures, variables, and data structures grouped together in a special package. (B) It is a non-negative integer which apart from initializat ion can be acted upon by wait and signal operations. (C) It uses two primitives, send and receive which are system calls rather than language constructs. (D) It consists of the IPC primitives implemented as syste m calls to block the process when they are not allowed to enter critical region to save CPU time.

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 21

*UGC NET Dec 2015, Paper II, original Q35*

> The hash function used in double hashing is of the form : (1) h (k, i) = (h, (k) + h2(k) + i) mod m (2) h (k, i) = (h, (k) + 12(k) - i) mod m (3) h (k, i) = (h,(k) +i h2(k)) mod m (4) h (k, i) = (hy (k) - i h2(k)) mod m D-8715 8 Paper-II

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 22

*UGC NET Dec 2015, Paper III, original Q18*

> If there are n integers to sort, each integer has d digits and each digit is in the set {1, 2, .., k), radix sort can sort the numbers in : (1) O(d n k) (2) O(d nk) (3) 0(d+n)k) (4) Old(n+k))

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 23

*UGC NET June 2015, Paper II, original Q22*

> The inorder and preorder Traversal of binary Tree are dbeafcg and abdecfg respectively. The post-order Traversal is (1) dbefacg (2) debfagc (3) dbefcga (4) debfgca

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 24

*UGC NET June 2015, Paper II, original Q23*

> Level order Traversal of a rooted Tree can be done by starting from root and performing : (1) Breadth First Search

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 25

*UGC NET June 2015, Paper II, original Q24*

> The average case occurs in the Linear Search Algorithm when : (1) The item to be searched is in some where middle of the Array (2) The item to be searched is not in the array (3) The item to be searched is in the last of the array (4) The item to be searched is either in the last or not in the array

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 26

*UGC NET June 2015, Paper II, original Q31*

> Match the following : (a) Forward Reference Table (i) Assembler directive (b) Mnemonic Table (ii) Uses array data structure (c) Segment Register Table (iii) Contains machine OP code (d) EQU (iv) Uses linked list data structure Codes: (a) (b) (c) (d) (1) (ii) (ili) (iv) (i) (2) (iii) (iv) (ii) (i) (3) (iii) (ii) (4) (iv) (ill) (il) (i)

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 27

*UGC NET June 2015, Paper II, original Q40*

> The Unix Kernel maintains two key data structures related to processes, the process table and the user structure. Which of the following information is not the part of user structure ? (1) File descriptor table (2) System call state (3) Scheduling parameters (4) Kernel stack

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 28

*UGC NET July 2016, Paper II, original Q21*

> Consider the following binary search tree : If we remove the root node, which of the node from the left subtree will be the new root ? (1) 11 (2) 12 (3) 13 (4) 16

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 29

*UGC NET July 2016, Paper III, original Q33*

> Which one of the following array represents a binary max-heap ? (1) [26, 13, 17, 14, 11, 9, 15] (2) [26, 15, 14, 17, 11, 9, 13] (3) [26, 15, 17, 14, 11, 9, 13] (4) [26, 15, 13, 14, 11, 9, 17]

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 30

*UGC NET July 2016, Paper III, original Q35*

> Suppose that we have numbers between 1 and 1,000 in a binary search tree and want to search for the number 364. Which of the following sequences could not be the sequence of nodes examined ? (1) 925, 221, 912, 245, 899, 259, 363, 364 (2) 3, 400, 388, 220, 267, 383, 382, 279, 364 (3) 926, 203, 912, 241, 913, 246, 364 (4) 3, 253, 402, 399, 331, 345, 398, 364

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 31

*UGC NET Jan 2017, Paper III, original Q33*

> Red-black trees are one of many search tree schemes that are “balanced” in order to guarantee that basic dynamic-set operations take ________ time in the worst case. (1) O(1) (2) O( lg n) (3) O(n) (4) O(n lg n)

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 32

*UGC NET Nov 2017, Paper II, original Q21*

> Consider an array representation of an n element binary heap where the element s are stored from index 1 to index n of the array. For the element stored at index i of the ar ray (i<= n), the index of the parent is : (1) floor ((i+1)/2) (2) ceiling ((i+1)/2) (3) floor (i/2) (4) ceiling (i/2)

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 33

*UGC NET Nov 2017, Paper II, original Q22*

> The following numbers are inserted into an empty binary search tree in t he given order : 10, 1, 3, 5, 15, 12, 16. What is the height of the binary search tree ? (1) 3 (2) 4 (3) 5 (4) 6

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 34

*UGC NET Nov 2017, Paper II, original Q25*

> Postorder traversal of a given binary search tree T produces followi ng sequence of keys : 3, 5, 7, 9, 4, 17, 16, 20, 18, 15, 14 Which one of the following sequences of keys can be the result of an in-ord er traversal of the tree T ? (1) 3, 4, 5, 7, 9, 14, 20, 18, 17, 16, 15 (2) 20, 18, 17, 16, 15, 14, 3, 4, 5, 7, 9 (3) 20, 18, 17, 16, 15, 14, 9, 7, 5, 4, 3 (4) 3, 4, 5, 7, 9, 14, 15, 16, 17, 18, 20

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 35

*UGC NET Dec 2018, original Q75*

> A binary search tree is constructed by inserting the following numbers in order: 60, 25, 72, 15, 30, 68, 101, 13, 18, 47, 70, 34 Exam The number of nodes is the left subtree is Options : Personal 91394342297. 5 91394342298. 6 91394342299. 7 91394342300. 3

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 36

*UGC NET July 2018, Paper II, original Q26*

> A binary search tree in which every non-leaf node has non-empty left and r ight subtrees is called a strictly binary tree. Such a tree with 19 leaves : (1) cannot have more than 37 nodes (2) has exactly 37 nodes (3) has exactly 35 nodes (4) cannot have more than 35 nodes

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 37

*UGC NET June 2019, original Q121*

> Which data structure is used by the compiler for managing variables and their attributes? 1. Binary tree 2. Link list repp. 3. Symbol table - 4. Parse table 64635085820. 2 64635085821. 3 64635085822.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 38

*UGC NET Nov 2021, original Q39*

> A ‐ III, B ‐I , C ‐ IV, D ‐ II Which of the following concepts can be used to identify loops? A. Depth first ordering B. Dominators C. Reducible graphs Choose the correct answer from the options given below: 1. A and B only 2. A and C only 3. B and C only 4. A, B and C

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 39

*UGC NET Nov 2021, original Q42*

> A B + C D * E – F G / * * A double‐ended queue (dequeue) supports adding and removing items from both the ends of the queue. The operations supported by dequeue are AddFront(adding item to front of the queue), AddRear(adding item to the rear of the queue), RemoveFront(removing item from the front of the queue), and RemoveRear(removing item from the rear of the queue). You are given only stacks to implement this data structure. You can implement only push and pop operations. What’s the time complexity of performing AddFront() and AddRear() assuming m is the size of the stack and n is the number of elements? 1. O(m) and O(n) 2. O(1) and O(n) 3. O(n) and O(1) 4. O(n) and O(m)

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 40

*UGC NET Nov 2021, original Q43*

> O(m) and O(n) Two balanced binary trees are given with m and n elements, respectively. They can be merged into a balanced binary search tree in ____ time. 1. O(m*n) 2. O(m+n) 3. O(m*log n) 4. O(m*log(m+n))

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 41

*UGC NET Nov 2021, original Q44*

> O(m*n) A data structure is required for storing a set of integers such that each of the following operations can be done in O(log n) time, where n is the number of elements in the set. Deletion of the smallest element Insertion of an element if it is not already present in the set Which of the following data structures can be used for this purpose? 1. A heap can be used but not a balanced binary search tree. 2. A balanced binary search tree can be used but not a heap. 3. Both balanced binary search tree and heap can be used. 4. Neither balanced binary search tree nor heap can be used.

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 42

*UGC NET Nov 2021, original Q66*

> A ‐III , B ‐I , C ‐IV , D ‐ II Suppose a B tree is used for indexing a database file. Consider the following information: size of the search key field= 10 bytes, block size = 1024 bytes, size of the record pointer= 9 bytes, size of the block pointer= 8 bytes. Let K be the order of internal node and L be the order of leaf node of B tree, then (K, L)=______. 1. (57, 53) 2. (50, 52) 3. (60, 64) 4. (34, 31)

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 43

*UGC NET Oct 2022, original Q49*

> How many rotations are required during the construction of an AVL tree if the following elements are to be added in the given sequence? 35, 50. 40. 25. 30. 60, 78, 20, 28 1. 2 left rotations, 2 right rotations 2. 2 left rotations. 3 right rotations 3. 8 left rotations, 2 right rotations 4. 3 left rotations. 1 right rotation

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 44

*UGC NET Oct 2022, original Q55*

> Consider two lists A and B of three strings on (0. 1) List A List B X: 1 111 10111 10 10 0 List A List B Y: 10 101 011 11 101 011 Which of the following is true? 1. Only PCP in X has solution. 2. Only PCP in Y has solution. 3. PCP in both X and Y has solution. 4. PCP neither in X nor in Y has solution.

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 45

*UGC NET Dec 2022 session, 11 Mar 2023 Shift 2, original Q3*

> Program and data are stored in the secondary memory (1) 1 (2) 2 (3) 3 (4) 4 1 2 ? A. It is slower than static RAM(SRAM) B. Packing Density is higher than Static RAM (SRAM) C. It is faster than static RAM(SRAM) D. It requires data refreshing Choose the correct answer from the options given below:

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 46

*UGC NET Aug 2024, original Q54*

> is a Self Balancing binary search tree, where the path from the root to the furthest leaf is no more than twice as long as the path from the root to nearest leaf. (1) Expression tree (2) Game tree (3) Red-Black tree (4) Threaded tree

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 47

*UGC NET Aug 2024, original Q150*

> Which data structure does the Banker's Algorithm use to maintain the state of available, maximum and allocated resources? (1) Priority Queue (2) Hash table (3) Wait-for-Graph (4) Matrices and Vectors Question Label: Comprehension 99/101

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 48

*UGC NET June 2024, original Q66*

> The height of a binary search tree for the words banana, peach, apple, pear, coconut, mango anu papaya using alphabetical order in 9 13) 4 (4) (1) 2 (2) 3

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 49

*UGC NET June 2024, original Q113*

> Arrange the steps of Mathematical Modelins NOT Solution fitting with data B. Formulation Mathematically C. Solve Mathematically D. Repeat formulation if it fit worst with data E. Interpretation results Choose the correct answer from the options given below : (4) E. D, C.

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 50

*UGC NET June 2025, original Q117*

> Which of the following trees are height balanced? A. Binary Search Tree B. AVL Tree C. Red-Black Tree D. B Tree Choose the correct answer from the options given below: 1. Aand D Only 2. A, B and D Only 3. C and D Only 4. Band C Only 42558919521.2 42558919522.3 42558919523.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 51

*UGC NET June 2025, original Q136*

> Match List 1 with List I! List I (Hashing Collison Handling Method) List II (Strategy) A. Chaining 1. Check next slot B. Linear Probing Il. Use second hash function C. Quadratic Probing IlI. Linked list at index D. Double Hashing IV. Skip slots using quadratic step Choose the correct answer from the options given below: 1. A-II, B-III, C-I, D-IV 2. A-II, B-III, C-IV, D-I 3. A-III, B-I, C-IV, D-II 4. A-IV, B-II, C-I, D-III 42558919596.1 42558919598.3 42558919599.4

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 52

*UGC NET Dec 2025 session (Jan 2026), original Q77*

> Question Number : 77

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 53

*UGC NET Dec 2025 session (Jan 2026), original Q98*

> Question Number : 98

**Chapter foundations**

This question belongs to the ideas covered by **Data Structures**. Revise these foundations: Arrays and Applications; Sparse Matrices; Stacks; Queues; Priority Queues; Linked Lists; Trees and Forests; Binary, Threaded Binary, Binary Search, AVL, B, B+, and B* Trees; Set Structures; Graphs; Sorting and Searching; Hashing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Data Structures questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-2"></a>

### 2. Performance Analysis and Recurrences (12 questions)

**What to master:** Time and Space Complexity; Asymptotic Notation; Recurrence Relations.

**Exam lens:** Choose the data structure or invariant first, then derive the complexity rather than recalling it in isolation.

**Reusable method:** Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked.

**High-yield rules:** Master theorem applies only to suitable forms. BFS gives unweighted shortest paths; Dijkstra needs nonnegative edges; comparison sorting has an Omega(n log n) lower bound.

**Common traps:** Do not confuse tree height with node count, stable with in-place sorting, amortized with average complexity, or NP-hard with NP-complete.

---

#### Question 54

*UGC NET Dec 2012, Paper II, original Q1*

> Consider the circuit shown below. In a If the disk head is located initially at certain steady state, Y is at logical l'. 32, find the number of disk moves What are possible values of A, B, C? required with FCFS if the disk queue of I/O blocks requests are 98, 37, 14, 124,65, 67. (A) 239 (B) 310 (C) 321 • f (D) 325 (A) A = 0, B = 0, C=1 (B) A = 0, B= C= 1 Component level design is concerned with (C) A= 1,B=C=0 (A) Flow oriented analysis (D) A = B= 1, C=1 (B) Class based analysis (C) Both of the above The worst case time complexity of AVL tree is better in comparison to (D) None of the above binary search tree for (A) Search and Insert Operations

**Chapter foundations**

This question belongs to the ideas covered by **Performance Analysis and Recurrences**. Revise these foundations: Time and Space Complexity; Asymptotic Notation; Recurrence Relations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Performance Analysis and Recurrences questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 55

*UGC NET Dec 2013, Paper III, original Q36*

> The recurrence relation T(n) = m T⎝⎜⎛ ⎠⎟⎞n 2 tan2 is satisfied by (A) O(n 2) (B) O(n 1g m) (C) O(n 2 lg n) (D) O(n 1g n)

**Chapter foundations**

This question belongs to the ideas covered by **Performance Analysis and Recurrences**. Revise these foundations: Time and Space Complexity; Asymptotic Notation; Recurrence Relations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Performance Analysis and Recurrences questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 56

*UGC NET Dec 2013, Paper III, original Q38*

> Assuming there are n keys and each key is in the range [0, m – 1]. The run time of bucket sort is (A) O(n) (B) O(n lgn) (C) O(n lgm) (D) O(n + m)

**Chapter foundations**

This question belongs to the ideas covered by **Performance Analysis and Recurrences**. Revise these foundations: Time and Space Complexity; Asymptotic Notation; Recurrence Relations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Performance Analysis and Recurrences questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 57

*UGC NET June 2013, Paper III, original Q12*

> The solution of recurrence relation, T(n) = 2T(floor ( n)) + logn is (A) O(n log log logn) (B) O(n log logn) (C) O(log logn) (D) O(logn log logn)

**Chapter foundations**

This question belongs to the ideas covered by **Performance Analysis and Recurrences**. Revise these foundations: Time and Space Complexity; Asymptotic Notation; Recurrence Relations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Performance Analysis and Recurrences questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 58

*UGC NET June 2013, Paper III, original Q71*

> The map colouring problem can be solved using which of the following technique ? (A) Means-end analysis (B) Constraint satisfaction (C) AO* search (D) Breadth first search

**Chapter foundations**

This question belongs to the ideas covered by **Performance Analysis and Recurrences**. Revise these foundations: Time and Space Complexity; Asymptotic Notation; Recurrence Relations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Performance Analysis and Recurrences questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 59

*UGC NET Dec 2015, Paper III, original Q16*

> In Activity - Selection problem, each activity i has a start time s; and a finish time f; where s; ≤ fi. Activities i and j are compatible if : (1) s;≥ fj (2) S; ≥ fi (3) S; ≥f; ors; ≥f; (4) s;21; and s; ≥f;

**Chapter foundations**

This question belongs to the ideas covered by **Performance Analysis and Recurrences**. Revise these foundations: Time and Space Complexity; Asymptotic Notation; Recurrence Relations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Performance Analysis and Recurrences questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 60

*UGC NET Dec 2015, Paper III, original Q19*

> The solution of the recurrence relation 0(1) if n ≤ 80 I(n) ≤ *(E) + (70 + 6) + 0(1) if n > 80 is : (1) 0(Ig n) (2) O(n) (3) O(n|gn) (4) None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Performance Analysis and Recurrences**. Revise these foundations: Time and Space Complexity; Asymptotic Notation; Recurrence Relations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Performance Analysis and Recurrences questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 61

*UGC NET Nov 2017, Paper II, original Q24*

> A list of n strings, each of length n, is sorted into lexicographic or der using merge - sort algorithm. The worst case running time of this computation is : (1) O(n log n) (2) O(n2 log n) (3) O(n2 + log n) (4) O(n3)

**Chapter foundations**

This question belongs to the ideas covered by **Performance Analysis and Recurrences**. Revise these foundations: Time and Space Complexity; Asymptotic Notation; Recurrence Relations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Performance Analysis and Recurrences questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 62

*UGC NET July 2018, Paper II, original Q21*

> The solution of the recurrence relation T(m) T( 3m 4) 1= + is : (1) θ (lg m) (2) θ (m) (3) θ (mlg m) (4) θ (lglg m)

**Chapter foundations**

This question belongs to the ideas covered by **Performance Analysis and Recurrences**. Revise these foundations: Time and Space Complexity; Asymptotic Notation; Recurrence Relations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Performance Analysis and Recurrences questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 63

*UGC NET July 2018, Paper II, original Q52*

> In a paged memory, the page hit ratio is 0.40. The time required to access a page in secondary memory is equal to 120 ns. The time required to access a page in primary mem ory is 15 ns. The average time required to access a page is ________. (1) 105 (2) 68 (3) 75 (4) 78

**Chapter foundations**

This question belongs to the ideas covered by **Performance Analysis and Recurrences**. Revise these foundations: Time and Space Complexity; Asymptotic Notation; Recurrence Relations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Performance Analysis and Recurrences questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 64

*UGC NET Dec 2019, original Q126*

> Consider the following statements: (a) The running time of dynamic programming algorithm is alway 0(p) where pis number of subproblems. (b) When a recurrence relation has cyclic dependency, it is impossible to use that recurrence relation (unmodified) in a correct dynamic program. (c) For a dynamic programming algorithm. computing all values in a bottom-up fashion is asymptotically faster than using recursion and memorization. (d) If a problem X can be reduced to a known NP-hard problem, then X must be NP-hard Which of the statement(s) is (are) true? (1) Only (b) and (a) (2) Only (b) (3) Only (b) and (c) (4) Only (b) and (d) 61547541202.2

**Chapter foundations**

This question belongs to the ideas covered by **Performance Analysis and Recurrences**. Revise these foundations: Time and Space Complexity; Asymptotic Notation; Recurrence Relations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Performance Analysis and Recurrences questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 65

*UGC NET Aug 2024, original Q99*

> Arrange the following recurrence relations in increasing order of their time capacity. (A) Tn) = 1(n/2) +1 (B) T(n) = 2T(n/2) + n (C) T(n) = 3T(n/3) + n (D) T(n) = 21(n/ 2) + Vn (E) T(n) = T(n- 1) + 1 Choose the correct answer from the options given below : (1) (E), (A), (B), (D), (C) (2) (A), (E), (D), (B), (C) (3) (E), (A), (D), (B), (C) (4) (А), (B), (D), (E), (C)

**Chapter foundations**

This question belongs to the ideas covered by **Performance Analysis and Recurrences**. Revise these foundations: Time and Space Complexity; Asymptotic Notation; Recurrence Relations.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Performance Analysis and Recurrences questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-3"></a>

### 3. Design Techniques (9 questions)

**What to master:** Divide and Conquer; Dynamic Programming; Greedy Algorithms; Backtracking; Branch and Bound.

**Exam lens:** Choose the data structure or invariant first, then derive the complexity rather than recalling it in isolation.

**Reusable method:** Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked.

**High-yield rules:** Master theorem applies only to suitable forms. BFS gives unweighted shortest paths; Dijkstra needs nonnegative edges; comparison sorting has an Omega(n log n) lower bound.

**Common traps:** Do not confuse tree height with node count, stable with in-place sorting, amortized with average complexity, or NP-hard with NP-complete.

---

#### Question 66

*UGC NET Dec 2012, Paper II, original Q24*

> RAD stands for process are (A) Rapid and Design (A) Initial, Repeatable, Defined, Managed, Optimized. (B) Rapid Aided Development (B) Primary, Secondary, Defined, (C) Rapid Application Development Managed, Optimized. (D) Rapid Application Design (C) Initial, Stating, Defined, Managed, Optimized. (D) None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Design Techniques**. Revise these foundations: Divide and Conquer; Dynamic Programming; Greedy Algorithms; Backtracking; Branch and Bound.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Design Techniques questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 67

*UGC NET Dec 2014, Paper III, original Q34*

> Dijkstra algorithm, which solves the single-source shortest--pa ths problem, is a _________, and the Floyd-Warshall algorithm, which finds shortest paths betw een all pairs of vertices, is a _________ (A) Greedy algorithm, Divide-conquer algorithm (B) Divide-conquer algorithm, Greedy algorithm (C) Greedy algorithm, Dynamic programming algorithm (D) Dynamic programming algorithm, Greedy algorithm

**Chapter foundations**

This question belongs to the ideas covered by **Design Techniques**. Revise these foundations: Divide and Conquer; Dynamic Programming; Greedy Algorithms; Backtracking; Branch and Bound.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Design Techniques questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 68

*UGC NET June 2015, Paper III, original Q50*

> Which of the following statements is not true for Multi Level Feedback Queue processor scheduling algorithm ? (1) Queues have different priorities (2) Each queue may have different scheduling algorithm (3) Processes are permanently assigned to a queue (4) This algorithm can be configured to match a specific system under design

**Chapter foundations**

This question belongs to the ideas covered by **Design Techniques**. Revise these foundations: Divide and Conquer; Dynamic Programming; Greedy Algorithms; Backtracking; Branch and Bound.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Design Techniques questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 69

*UGC NET July 2016, Paper III, original Q20*

> Match the following types of variables w ith the corresponding programming languages : (a) Static variables (i) Local variables in Pascal (b) Stack dynamic (ii) All variables in APL (c) Explicit heap dynamic (iii) Fortran 77 (d) Implicit heap dynamic (iv) All objects in JAVA Codes : (a) (b) (c) (d) (1) (i) (iii) (iv) (ii) (2) (iv) (i) (iii) (ii) (3) (iii) (i) (iv) (ii) (4) (ii) (i) (iii) (iv)

**Chapter foundations**

This question belongs to the ideas covered by **Design Techniques**. Revise these foundations: Divide and Conquer; Dynamic Programming; Greedy Algorithms; Backtracking; Branch and Bound.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Design Techniques questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 70

*UGC NET July 2016, Paper III, original Q36*

> A triangulation of a polygon is a set of T chor ds that divide the polygon into disjoint triangles. Every triangulati on of n-vertex convex polygon has _____ chords and divides the polygon into _____ triangles. (1) n – 2, n – 1 (2) n – 3, n – 2 (3) n – 1, n (4) n – 2, n – 2

**Chapter foundations**

This question belongs to the ideas covered by **Design Techniques**. Revise these foundations: Divide and Conquer; Dynamic Programming; Greedy Algorithms; Backtracking; Branch and Bound.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Design Techniques questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 71

*UGC NET Jan 2017, Paper III, original Q35*

> Dijkstra’s algorithm is based on (1) Divide and conquer paradigm (2) Dynamic programming (3) Greedy Approach (4) Backtracking paradigm

**Chapter foundations**

This question belongs to the ideas covered by **Design Techniques**. Revise these foundations: Divide and Conquer; Dynamic Programming; Greedy Algorithms; Backtracking; Branch and Bound.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Design Techniques questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 72

*UGC NET Jan 2017, Paper III, original Q36*

> Match the following with respect to algorithm paradigms : List – I List – II a. Merge sort i. Dynamic programming b. Huffman coding ii. Greedy approach c. Optimal polygon triangulation iii. Divide and conquer d. Subset sum problem iv. Back tracking Codes : a b c d (1) iii i ii iv (2) ii i iv iii (3) ii i iii iv (4) iii ii i iv

**Chapter foundations**

This question belongs to the ideas covered by **Design Techniques**. Revise these foundations: Divide and Conquer; Dynamic Programming; Greedy Algorithms; Backtracking; Branch and Bound.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Design Techniques questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 73

*UGC NET July 2018, Paper II, original Q27*

> Match the following with respect to algorithm paradigms : List - I List - II (a) The 8-Queen’s problem (i) Dynamic programming (b) Single-Source shortest paths (ii) Divide and conquer (c) STRASSEN’s Matrix multiplication (iii) Greedy approach (d) Optimal binary search trees (iv) Backtracking Code : (a) (b) (c) (d) (1) (iv) (i) (iii) (ii) (2) (iv) (iii) (i) (ii) (3) (iii) (iv) (ii) (i) (4) (iv) (iii) (ii) (i)

**Chapter foundations**

This question belongs to the ideas covered by **Design Techniques**. Revise these foundations: Divide and Conquer; Dynamic Programming; Greedy Algorithms; Backtracking; Branch and Bound.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Design Techniques questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 74

*UGC NET Oct 2022, original Q46*

> Which of the following algorithm design approach is used in Quick sort algorithm? 1. Dynamic programming 2. Back Tracking 3. Divide and conquer 4. Greedy approach

**Chapter foundations**

This question belongs to the ideas covered by **Design Techniques**. Revise these foundations: Divide and Conquer; Dynamic Programming; Greedy Algorithms; Backtracking; Branch and Bound.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Design Techniques questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-4"></a>

### 4. Lower-Bound Theory (9 questions)

**What to master:** Comparison Trees; Lower Bounds through Reductions.

**Exam lens:** Choose the data structure or invariant first, then derive the complexity rather than recalling it in isolation.

**Reusable method:** Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked.

**High-yield rules:** Master theorem applies only to suitable forms. BFS gives unweighted shortest paths; Dijkstra needs nonnegative edges; comparison sorting has an Omega(n log n) lower bound.

**Common traps:** Do not confuse tree height with node count, stable with in-place sorting, amortized with average complexity, or NP-hard with NP-complete.

---

#### Question 75

*UGC NET Dec 2013, Paper III, original Q57*

> Find the false statement : (A) The relationship construct known as the weak relationship type was defined by Dey, Storey & Barron (1999) (B) A weak relationship occurs when two relationship types are linked by either Event- Precedent sequence or Condition-Precedent sequence. (C) Conceptual model is not accurate representation of “Universe of interest”. (D) Ternary, Quaternary and Quintary relationships are shown through a series of application scenario’s and vignette’s.

**Chapter foundations**

This question belongs to the ideas covered by **Lower-Bound Theory**. Revise these foundations: Comparison Trees; Lower Bounds through Reductions.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Lower-Bound Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 76

*UGC NET Dec 2014, Paper III, original Q35*

> Consider the problem of a chain <A 1, A 2, A 3> of three matrices. Suppose that the dimensions of the matrices are 10 × 100, 100 × 5 and 5 × 50 respectively. There are two different ways of parenthesization : (i) ((A 1 A 2)A 3) and (ii) (A 1(A 2 A 3)). Computing the product according to the first parenthesization is ________ times faster in comparison to the second parenthesization. (A) 5 (B) 10 (C) 20 (D) 100

**Chapter foundations**

This question belongs to the ideas covered by **Lower-Bound Theory**. Revise these foundations: Comparison Trees; Lower Bounds through Reductions.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Lower-Bound Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 77

*UGC NET June 2015, Paper III, original Q32*

> The travelling salesman problem can be solved in: (1) Polynomial time using dynamic programming algorithm (2) Polynomial time using branch-and-bound algorithm (3) Exponential time using dynamic programming algorithm or branch-and-bound algorithm (4) Polynomial time using backtracking algorithm

**Chapter foundations**

This question belongs to the ideas covered by **Lower-Bound Theory**. Revise these foundations: Comparison Trees; Lower Bounds through Reductions.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Lower-Bound Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 78

*UGC NET June 2015, Paper III, original Q57*

> In propositional logic P « Q is equivalent to (Where ~ denotes NOT) : (1) ~ (Pv Q) 1 ~ (Qv P) (2) (~Pv Q) ^ (~@vP) (3) (PV Q) ^ (Qv P) (4) ~ (Pv Q) → ~ (Qv P) Which of the following statements is true for Branch - and - Bound search ? (1) Underestimates of remaining distance may cause deviation from optimal path. (2) Overestimates can't cause right path to be overlooked. (3) Dynamic programming principle can be used to discard redundant partial paths. (4) All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Lower-Bound Theory**. Revise these foundations: Comparison Trees; Lower Bounds through Reductions.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Lower-Bound Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 79

*UGC NET Jan 2017, Paper III, original Q31*

> The asymptotic upper bound solution of the recurrence relation given by T(n) = 2T ⎝⎜⎛ ⎠⎟⎞n 2 + n lg n is : (1) O(n 2) (2) O(n lg n) (3) O(n lg lg n) (4) O(lg lg n)

**Chapter foundations**

This question belongs to the ideas covered by **Lower-Bound Theory**. Revise these foundations: Comparison Trees; Lower Bounds through Reductions.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Lower-Bound Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 80

*UGC NET Dec 2019, original Q54*

> What are the greatest lower bound (GLB) and the least upper bound (LUB) of the sets A = (3,9, 12) and B = {1, 2, 4, 5, 10) if they exist in poset (z*,/)? (1) A(GLB-3. LUB-36): B(GLB - 1. LUB-20) (2) A(GLB - 3. LUB -12); B (GLB-1.LUB -10) (3) A (GLB - 1. LUB-36): B (GLB - 2. LUB-20) (4) A(GLB -1. LUB-12): B(GLB -2. LUB -10) 61547540914. 2 61547540915. 3 61547540916. 4

**Chapter foundations**

This question belongs to the ideas covered by **Lower-Bound Theory**. Revise these foundations: Comparison Trees; Lower Bounds through Reductions.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Lower-Bound Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 81

*UGC NET Dec 2019, original Q89*

> Give asymptotic upper and lower bound for T(n) given below. Assume T(n) is constant for n ≤2. I(n) = 4T (Vn) + Ig'n (1) (n) = 0(1g(lg? n)Ign) (2) T(n) = 0(1g? nlgn) (3) (4) T(n) = 0(1g (Ign)Ign) 61547541054. 2 61547541055. 3 61547541056. 4

**Chapter foundations**

This question belongs to the ideas covered by **Lower-Bound Theory**. Revise these foundations: Comparison Trees; Lower Bounds through Reductions.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Lower-Bound Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 82

*UGC NET June 2025, original Q77*

> The tight asymptotic bound for the recurrence T(n) = 2T(n/4) +Vn is (1) 0 (vn) (2) © (n log n) (4)e (nog Vn) 42558919361.2 42558919362. 3 42558919363.4

**Chapter foundations**

This question belongs to the ideas covered by **Lower-Bound Theory**. Revise these foundations: Comparison Trees; Lower Bounds through Reductions.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Lower-Bound Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 83

*UGC NET Dec 2025 session (Jan 2026), original Q97*

> Question Number : 97 using lower bound Choose the correct answer from the options given below: 1. A-II, B-III, C-IV, D-I 2. A-IV, B-III, C-II, D-I 3. A-I, B-II, C-III, D-IV 4. A-III, B-IV. C-I, D-II 6119878786.2 6119878787.3 6119878788.4

**Chapter foundations**

This question belongs to the ideas covered by **Lower-Bound Theory**. Revise these foundations: Comparison Trees; Lower Bounds through Reductions.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Lower-Bound Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-5"></a>

### 5. Graph Algorithms (33 questions)

**What to master:** BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam lens:** Choose the data structure or invariant first, then derive the complexity rather than recalling it in isolation.

**Reusable method:** Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked.

**High-yield rules:** Master theorem applies only to suitable forms. BFS gives unweighted shortest paths; Dijkstra needs nonnegative edges; comparison sorting has an Omega(n log n) lower bound.

**Common traps:** Do not confuse tree height with node count, stable with in-place sorting, amortized with average complexity, or NP-hard with NP-complete.

---

#### Question 84

*UGC NET Dec 2011, Paper III, original Q8*

> Show how a B – tree and B + tree can be used to implement a priority queue. Also show that any sequence of n insertion and minimum deletion can be perfor med in o(nlogn) steps. _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 85

*UGC NET Dec 2013, Paper II, original Q24*

> For any B-tree of minimum degree t ≥ 2, every node other than the root must have atleast ________ keys and every node can have at most ________ keys. (A) t – 1, 2t + 1 (B) t + 1, 2t + 1 (C) t – 1, 2t – 1 (D) t + 1, 2t – 1

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 86

*UGC NET Dec 2014, Paper III, original Q32*

> Match the following : List – I List – II a. Bucket sort i. O(n 3lgn) b. Matrix chain multiplication ii. O(n 3) c. Huffman codes iii. O(n lgn) d. All pairs shortest paths iv. O(n) Codes : a b c d (A) iv ii i iii (B) ii iv i iii (C) iv ii iii i (D) iii ii iv i

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 87

*UGC NET Dec 2015, Paper II, original Q36*

> In the following graph, discovery time stamps and finishing time stamps of Depth First Search (DFS) are shown as x/y, where x is discovery time stamp and y is finishing time stamp. 13/14 11/16 1/10 8/9 b 12/15 3/4 2/7 5/6 It shows which of the following depth first forest ? (1) fa, b, el ic, d, f, g, h} (2) fa, b, el fc, d, hi {f, g) (3) {a, b, el if, g) {c, d) (h} (4) {a, b, c, d} fe, f, g) {h} The number of disk pages access in B - tree search, where h is height, n is the number of keys, and t is the minimum degree, is : (1) 0 (logn h*t) (2) e (log+n*h) (3) e (logh n) (4) 0 (log, n)

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 88

*UGC NET Dec 2015, Paper III, original Q20*

> Floyd-Warshall algorithm utilizes . to solve the all-pairs shortest paths problem on a directed graph in time. (1) Greedy algorithm, 0(V3) (2) Greedy algorithm, o(V-Ign) (3) Dynamic programming, 0(V3) (4) Dynamic programming, O(V- Ign) D-8715 4 Paper-III

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 89

*UGC NET June 2015, Paper II, original Q4*

> Consider the following statements : (a) Depth - first search is used to traverse a rooted tree. (b) Pre - order, Post-order and Inorder are used to list the vertices of an ordered rooted tree. (c) Huffman's algorithm is used to find an optimal binary tree with given weights. (d) Topological sorting provides a labelling such that the parents have larger labels than their children. Which of the above statements are true ? (1) (a) and (b) (2) (c) and (d) (3) (a), (b) and (c) (4) (a), (b), (c) and (d) Consider a Hamiltonian Graph (G) with no loops and parallel edges. Which of the following is true with respect to this Graph (G) ? (a) deg (v) ≥ n/2 for each vertex of G (b) |E(G)| ≥1/2 (n-1) (n- 2) + 2 edges (c) deg (v) + deg (w) ≥n for every v and w not connected by an edge (1) (a) and (b) (b) and (c) (3) (a) and (c) (4) (a), (b) and (c) J-8715 2 Paper-Il

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 90

*UGC NET June 2015, Paper II, original Q21*

> Consider the given graph 10 28 142 25 24 16 5 18 3 22 12 Its Minimum Cost Spanning Tree is 1 28 10 16 14 16 (2) 25 22 12 22 28 10 (3) 25 16 16 3) 3 22 12

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 91

*UGC NET June 2015, Paper III, original Q31*

> An all-pairs shortest-paths problem is efficiently solved using (1) Dijkstra' algorithm (2) Bellman-Ford algorithm (3) Kruskal algorithm (4) Floyd-Warshall algorithm

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 92

*UGC NET July 2016, Paper II, original Q23*

> Suppose you are given a binary tree with n no des, such that each node has exactly either zero or two children. The maximum height of the tree will be (1) n 2 – 1 (2) n 2 + 1 (3) (n – 1)/2 (4) (n + 1)/2

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 93

*UGC NET Jan 2017, Paper II, original Q21*

> Which of the following is true for computation time in insertion, deleti on and finding maximum and minimum element in a sorted array ? (1) Insertion – 0(1), Deletion – 0(1), Maximum – 0(1), Minimum – 0(l) (2) Insertion – 0(1), Deletion – 0(1), Maximum – 0(n), Minimum – 0(n) (3) Insertion – 0(n), Deletion – 0(n), Maximum – 0(1), Minimum – 0(1) (4) Insertion – 0(n), Deletion – 0(n), Maximum – 0(n), Minimum – 0(n)

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 94

*UGC NET Jan 2017, Paper II, original Q25*

> Which of the following statements is false ? (A) Optimal binary search tree construction can be performed efficiently using dynamic programming. (B) Breadth-first search cannot be used to find connected components of a graph. (C) Given the prefix and postfix walks of a binary tree, the tre e cannot be re-constructed uniquely. (D) Depth-first-search can be used to find the connected components of a graph. (1) A (2) B (3) C (4) D

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 95

*UGC NET Jan 2017, Paper III, original Q56*

> Consider the following AO graph : Which is the best node to expand next by AO* algorithm ? (1) A (2) B (3) C (4) B and C

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 96

*UGC NET Nov 2017, Paper II, original Q5*

> Consider the graph given below : Use Kruskal’s algorithm to find a minimal spanning tree for the graph. The List of the edges of the tree in the order in which they are choosen is ? (1) AD, AE, AG, GC, GB, BF (2) GC, GB, BF, GA, AD, AE (3) GC, AD, GB, GA, BF, AE (4) AD, AG, GC, AE, GB, BF

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 97

*UGC NET Nov 2017, Paper II, original Q23*

> Let G be an undirected connected graph with distinct edge weight. Let E max be the edge with maximum weight and E min the edge with minimum weight. Which of the following statements is false ? (1) Every minimum spanning tree of G must contain E min. (2) If Emax is in minimum spanning tree, then its removal must disconnect G. (3) No minimum spanning tree contains E max. (4) G has a unique minimum spanning tree.

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 98

*UGC NET Dec 2018, original Q62*

> Consider the graph shown below : 2 4 3 2 1 1, 2 2 4 3 4 5 1 4 6 5 Use Kruskal's algorithm to find the minimum spanning tree of the graph. The weight of this minimum spanning tree is Options :

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 99

*UGC NET Dec 2018, original Q143*

> Consider the following terminology and match List I with List II and choose the correct inswer from the code given below. b = branching factor d = depth of the shallowest solution m = Maximum depth of the search tree 1 = depth limit List I List II (Algorithms) (Space Complexity) (a) BFS search (i) 0(bd) (d) Iterative deepening search (iv) O(bl) ur . Code : . (a) i), (b) (i), (c)-(iv), (d)-(i) 91394342570. 91394342571. (a)-(ili), (b)-(ii), (c)-(iv), (d)-(i) (a)-(i), (b)-(iii, (c)-(iv), (d) -(i) 91394342572. single line Ouestion Ontion • No Ontion Orientation: Vertical Duestion Number: 143 Ouestion Id: 91394310837 Ouestion Type : MCO

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 100

*UGC NET July 2018, Paper II, original Q81*

> E is the number of edges in the graph and f is maximum flow in the graph. Wh en the capacities are integers, the runtime of Ford-Fulberson algorithm is bounded by : (1) O (E ∗ f) (2) O (E 2∗ f) (3) O (E ∗ f2) (4) O (E 2∗ f2)

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 101

*UGC NET Dec 2019, original Q56*

> The weight of minimum spanning tree in graph G, calculated using Kruskal's algorithm is : 8 5 7 3 Graph G (1) 14 (2) 15 (3) 17 (4) 18 61547540922. 2 61547540923. 3 61547540924. 4 Single I he Question option No Option Orient On: Verticape: MCO Option Shuffing : No

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 102

*UGC NET Dec 2019, original Q86*

> A clique in an undirected graph G = (V. E) is a subset V' = V of vertices. such that (1) If (u, v) e E then u eV' and ueV' Guide (2) If (u. v) E E then u E V' or vEV' (3) Each pair of vertices in V' is connected by an edge (4) All pairs of vertices in V' are not connected by an edge 61547541042.2 61547541043.3 61547541044. 4

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 103

*UGC NET Dec 2019, original Q91*

> When using Dijkstra's algorithm to find shortest path in a graph, which of the following statement is not true? (1) It can find shortest path within the same graph data structure (2) Every time a new node is visited. we choose the node with smallest known distance/ cost (weight) to visit first (3) Shortest path always passes through least number of vertices (4) The graph needs to have a non-negative weight on every edge 61547541062.2 61547541063.3

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 104

*UGC NET Nov 2020, original Q128*

> Consider the undirected graph below: 8 9 2 a 11 14 / 10 1 2 Using Prim's algorithm to construct a minimum spanning tree starting with node a. which one of the following sequences of edges represents a possible order in which the edges would be added to construct the minimum spanning tree? (1) (a,b), (a,h). (g.h), (f.g), (c.f), (ci), (c.d), (d.e) (2) (a,b. (b.h). (g.h). (g.i), (ci), (c.f), (c,d), (d.e) (3) (a.b). (b.c). (c.i). (c.f), (f,g). (g.h), (c.d), (d,e) (4) (a,b), (g.h). (g.f). (c.f). (e.i), (fe), (b,e), (de) 53622817010.2

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 105

*UGC NET Nov 2020, original Q136*

> Let G be a simple undirected graph. To be a DFS tree on G. and T, be the BFS tree on G. Consider the following statements. Statement I: No edge of G is a cross with respect to To Statement II: For every edge (u, (u,v) of G, if u is at depth i and v is at depth j in Ta then li - jl = 1. In the light of the above statements, choose the correct answer from the options given below (1) Both Statement I and Statement II are true (2) Both Statement I and Statement Il are false (3) Statement I is correct but Statement II is false (4) Statement I is incorrect but Statement Il is true. 53622817042. 2 53622817043. 3 53622817044.4

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 106

*UGC NET Nov 2021, original Q45*

> A heap can be used but not a balanced binary search tree. Consider the following graph. * * * * * * * * * * * * 0 1 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1 1 1 1 1 2 a b + a b + b a + R + a b + 46) 47) 48) 49) 50) 51) 52) 53) 54) 55) 56) 57) 58) 59) Among the following sequences I. a b e g h f II. a b f e h g III. a b f h g e IV. a f g h b e Which are depth first traversals of the above graph? 1. I, II, and IV only 2. I and IV only 3. II, III, and IV only 4. I, III, and IV only

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 107

*UGC NET Nov 2021, original Q50*

> 3 In the following table, the left column contains the names of standard graph algorithms and the right column contains the time complexities of the algorithms. Here, n and m are number of vertices and edges, respectively. Match each algorithm with its time complexity. List I List II Standard graph algorithms Time complexities A. Bellman‐Ford algorithm I. O(m*log n) B. Kruskal’s algorithm II. O(n ) C. Floyd‐Warshall algorithm III. O(n*m) D. Topological sorting IV. O(n+m) Choose the correct answer from the options given below: 1. A ‐ III, B ‐ I, C ‐ II, D ‐ IV 2. A ‐ II, B ‐ IV, C ‐ III, D ‐ I 3. A ‐ III, B ‐ IV, C ‐ I, D ‐ II 4. A ‐ II, B ‐ I, C ‐ III, D ‐ IV

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 108

*UGC NET Oct 2022, original Q45*

> Consider a B-tree of height h. minimum degree 1 ≥ 2 that contains any n-key. where n≥1. Which of the following is correct? 1. h2 logg n +1 2 2. h≤log: n +1 2 3. h2 log.- n-1 2 4. h ≤logr n-1 2

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 109

*UGC NET Oct 2022, original Q63*

> Consider the following graph: For the graph; the following sequences of depth first search (DFS) are given (A) abcghf (B). abichg (C) abfhgo (D) afghbe Which of the following is correct? 1. (A). (B) and (D) only 2. (A). (B). (C) and (D) 3. (B). (C) and (D) only 4. (A), (C) and (D) only

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 110

*UGC NET Aug 2024, original Q135*

> Match List - I with List - II. List - I List - II (A) Dijkstra's Algorithms (1) Find the shortest path between all pairs of vertices in a graph with positive or negative edge weights. (B) Floyd-Warshall Algorithms (LI) Finds the shortest path in a weighted graph with non-negative edge weights. (C) Bellman-frod Algorithms (III) Sorts elements by repeatedly moving them post neighboring elements that are smaller. (D) Prim's Algorithms (IV) Determines the strongest connected components in a directed graph. Choose the correct answer from the options given below : (A) -(II, (B)-(I, (C)-(III, (D)-(IV) (2) (A) -(II), (B)-(I), (C)-(IV), (D)-(III) (3) (A)-(T), (B)-(II, (C)-(Ш), (D)-(IV) (4) (A)-(III), (B)-(ID), (C)-(IV), (D)-(I) 90/101

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 111

*UGC NET June 2025, original Q143*

> Which of the followings is the correct Flow graph for the TAC given in the passage? 0100000 0011000 0000110 0000001 0000001 010 000 00 00 0 0 0- 010000- 001000 010001 101000 00000 1 00000 000 0100000 1010 3. 000 01 0000001 001 0010 0100000 0100000 0100001 001000 010001 101000 000001 000001- 42558919624. 1 42558919626.3 42558919627.4 Mandion unher : 144

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 112

*UGC NET Dec 2025 session (Jan 2026), original Q89*

> Question Number : 89

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 113

*UGC NET Dec 2025 session (Jan 2026), original Q92*

> Question Number : 92 . Reason R: Every connected graph has a unique MST. In the light of the above statements, choose the most appropriate answer from the options given below 1. Both A and R are correct and R is the correct explanation of A 2. Both A and R are correct but R is NOT the correct explanation of A 3. A is correct but R is not correct 4. A is not correct but R is correct 6119878770.2 6119878771.3 6119878772.4

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 114

*UGC NET Dec 2025 session (Jan 2026), original Q93*

> Question Number: 93 . Reason R: Every connected graph has a unique MST. In the light of the above statements, choose the most appropriate answer from the options given below 1. Both A and R are correct and R is the correct explanation of A 2. Both A and R are correct but R is NOT the correct explanation of A 3. A is correct but R is not correct 4. A is not correct but R is correct 6119878770.2 6119878771.3 6119878772.4

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 115

*UGC NET Dec 2025 session (Jan 2026), original Q94*

> Question Number: 94 is a linear ordering of its vertices such that if G contain an edge (u, v) then u appears before v in the ordering. In the light of the above statements, choose the most appropriate answer from the options given below 1. Both A and R are correct and R is the correct explanation of A 2. Both A and R are correct but R is NOT the correct explanation of A 3. A is correct but R is not correct 4. A is not correct but R is correct 6119878774.2 6119878775.3 6119878776.4

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 116

*UGC NET Dec 2025 session (Jan 2026), original Q95*

> Question Number : 95

**Chapter foundations**

This question belongs to the ideas covered by **Graph Algorithms**. Revise these foundations: BFS; DFS; Shortest Paths; Maximum Flow; Minimum Spanning Trees.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Graph Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-6"></a>

### 6. Complexity Theory (10 questions)

**What to master:** P and NP; NP-Completeness; Reducibility.

**Exam lens:** Choose the data structure or invariant first, then derive the complexity rather than recalling it in isolation.

**Reusable method:** Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked.

**High-yield rules:** Master theorem applies only to suitable forms. BFS gives unweighted shortest paths; Dijkstra needs nonnegative edges; comparison sorting has an Omega(n log n) lower bound.

**Common traps:** Do not confuse tree height with node count, stable with in-place sorting, amortized with average complexity, or NP-hard with NP-complete.

---

#### Question 117

*UGC NET June 2010, Paper II, original Q46*

> The cost of the network is usually determined by (A) time complexity (B) switching complexity (C) circuit complexity (D) none of these

**Chapter foundations**

This question belongs to the ideas covered by **Complexity Theory**. Revise these foundations: P and NP; NP-Completeness; Reducibility.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Complexity Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 118

*UGC NET Dec 2013, Paper III, original Q35*

> Let A and B be two n × n matrices. The efficient algorithm to multiply the two matrices has the time complexity (A) O(n 3) (B) O(n 2.81) (C) O(n 2.67) (D) O(n 2)

**Chapter foundations**

This question belongs to the ideas covered by **Complexity Theory**. Revise these foundations: P and NP; NP-Completeness; Reducibility.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Complexity Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 119

*UGC NET Dec 2015, Paper II, original Q15*

> In general, in a recursive and non-recursive implementation of a problem (program) : (1) Both time and space complexities are better in recursive than in non-recursive program. (2) Both time and space complexities are better in non-recursive than in recursive program. (3) Time complexity is better in recursive version but space complexity is better in non-recursive version of the program. (4) Space complexity is better in recursive version but time complexity is better in non-recursive version of the program. D-8715 5 Paper-II

**Chapter foundations**

This question belongs to the ideas covered by **Complexity Theory**. Revise these foundations: P and NP; NP-Completeness; Reducibility.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Complexity Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 120

*UGC NET Dec 2018, original Q77*

> Match List I with List II and choose the correct answer from the code given below. List I List II (Graph Algorithm) (Time Complexity) (a) Dijkstra's algorithm (i) 0(ElgE) (b) Kruskal's algorithm (ii) o(V3) (c) Floyd-Warshall algorithm (iii) 0(V2) (d) Topological sorting (iv) 0(V + E) where V and E are the number of vertices and edges in graph respectively. Code: 'ersonal Exam Guidel . (a)-(i), (b)-(ili), (c)-(ii), (d)-(iv) 91394342306. (a)-(ii), (b)-(i), (c)-(iii, (d)-(iv) 91394342307. (a)-(i), (b)-(ili), (c)-(iv), (d)-(ii) 91394342308. (a)-(iii), (b)-(i), (c)-(iv), (d)-(i)

**Chapter foundations**

This question belongs to the ideas covered by **Complexity Theory**. Revise these foundations: P and NP; NP-Completeness; Reducibility.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Complexity Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 121

*UGC NET Dec 2018, original Q79*

> Consider a singly linked list. What is the worst case time complexity of the best-known algorithm to delete the node a, pointer to this node is q, from the list? (n lg n) 91394342314 O(n) 91394342315. 0(lg n) 91394342316. 0(1) uestion Number: 79

**Chapter foundations**

This question belongs to the ideas covered by **Complexity Theory**. Revise these foundations: P and NP; NP-Completeness; Reducibility.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Complexity Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 122

*UGC NET Dec 2018, original Q144*

> Match List I with List II and choose the correct answer from the code given below. List I List II (a) Greedy Best-First Search (i) Selects a node for expansion if optimal path to that node has been found. (b) A* Search (ii) Avoids substantial overhead associated with keeping the sorted queue of nodes. (c) Recursive Best-First Search (il) Suffers from excessive node generation. (d) Iterative-deepening A* Search (iv) Time complexity depends on the quality of heuristic. Code: . (a)-(i), (b)-(ii), (c)-(ill), (d)-(iv) Guide 91394342574. (a)-(iv), (b)-(i), (c)-(ii), (d)-(ili) rsonal Exam | 91394342575. (a)-(iv), (b)-(ili), (c)-(ii), (d)-(i) 91394342576. (a)-(i), (b)-(iv), (c)-(iti), (d) -(i)

**Chapter foundations**

This question belongs to the ideas covered by **Complexity Theory**. Revise these foundations: P and NP; NP-Completeness; Reducibility.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Complexity Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 123

*UGC NET Dec 2019, original Q92*

> The time complexity to multiply two polynomials of degree n using Fast Fourier transform method is : (1) e(nlgn) (2) 0(n?) (3) Đ(n) (4) e(lgn) 61547541066.2 61547541067.3 61547541068. 4

**Chapter foundations**

This question belongs to the ideas covered by **Complexity Theory**. Revise these foundations: P and NP; NP-Completeness; Reducibility.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Complexity Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 124

*UGC NET Nov 2021, original Q47*

> Both Statement I and Statement II are true. Which of the given options provides the increasing order of asymptotic complexity of functions f1, f2, f3 and f4? A. f1(n) = 2 B. f2(n) = n C. f3(n) = n log n D. f4(n) = n Choose the correct answer from the options given below 1. C, B, D, A 2. C, B, A, D 3. B, C, A, D 4. B, C, D, A

**Chapter foundations**

This question belongs to the ideas covered by **Complexity Theory**. Revise these foundations: P and NP; NP-Completeness; Reducibility.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Complexity Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 125

*UGC NET Nov 2021, original Q54*

> 3 Which among the following statement(s) is(are) FALSE? A. Greedy best‐first search is not optimal but is often efficient. B. A* is complete and optimal provided h(n) is admissible or consistent. C. Recursive best‐first search is efficient in terms of time complexity but poor in terms of space complexity. D. h(n) = 0 is an admissible heuristic for the 8‐puzzle. 1. A only 2. A and D only 3. C only 4. C and D only

**Chapter foundations**

This question belongs to the ideas covered by **Complexity Theory**. Revise these foundations: P and NP; NP-Completeness; Reducibility.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Complexity Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 126

*UGC NET Aug 2024, original Q128*

> Match List - I with List - II. List - I List - Il (Recurrence Relations) (Complexity) (A) T(n) = 2T(n/2) + n (I) T(n) = 0(n logn) (exact solution) (B) T(n) = T(n/2) +1 (II) O(n2) (C) T(n) = 2T(n/2) + 1 (III) T(n) = 0(n) (exact solution) (D) Tn) = T(n- 1) + 1 (IV) O(n) Choose the correct answer from the options given below : (1) (A)-(1), (B)-(IV), (C)-(III), (D)-(I) (2) (A)-(IV), (B)-(II, (C)-(I), (D) -(III) (3) (A)-(I), (B)-(III), (C)-(IV), (D) -(II) (4) (A) -(Ш), (B)-(I), (C)-(IV), (D)-(Il)

**Chapter foundations**

This question belongs to the ideas covered by **Complexity Theory**. Revise these foundations: P and NP; NP-Completeness; Reducibility.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Complexity Theory questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-7"></a>

### 7. Selected Topics (57 questions)

**What to master:** Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam lens:** Choose the data structure or invariant first, then derive the complexity rather than recalling it in isolation.

**Reusable method:** Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked.

**High-yield rules:** Master theorem applies only to suitable forms. BFS gives unweighted shortest paths; Dijkstra needs nonnegative edges; comparison sorting has an Omega(n log n) lower bound.

**Common traps:** Do not confuse tree height with node count, stable with in-place sorting, amortized with average complexity, or NP-hard with NP-complete.

---

#### Question 127

*UGC NET Dec 2009, Paper II, original Q21*

> If the number of leaves in a strictly binary tree is an odd num ber, then what can you say with full conviction about total number of nodes in the tree ? (A) It is an odd number. (B) It is an even number. (C) It cannot be equal to the number of leaves. (D) It is always greater than twice the number of lea ves.

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 128

*UGC NET June 2010, Paper II, original Q24*

> A chained hash table has an array size of 100. What is the maximum number of entries that can be placed in the table ? (A) 100 (B) 200 (C) 10000 (D) There is no upper limit

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 129

*UGC NET Dec 2013, Paper II, original Q25*

> Given two sorted list of size ‘m’ and ‘n’ respectively. The number of comparison needed in the worst case by the merge sort algorithm will be (A) m × n (B) max (m, n) (C) min (m, n) (D) m + n – 1

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 130

*UGC NET Dec 2013, Paper II, original Q46*

> Consider a preemptive priority based scheduling algorithm based on dynamically changing priority. Larger priority number implies higher priority. When the process is waiting for CPU in the ready queue (but not yet started execution), its priority changes at a rate a = 2. When it starts running, its priority changes at a rate b = 1. A ll the processes are assigned priority value 0 when they enter ready queue. Assume that the following processes want to execute : Process ID Arrival Time Service Time P1 0 4 P2 1 1 P3 2 2 P4 3 1 The time quantum q = 1. When two processes want to join ready queue simultaneously, the process which has not executed recently is given priority. The finish time of processes P1, P2, P3 and P4 will respectively be (A) 4, 5, 7 and 8 (B) 8, 2, 7 and 5 (C) 2, 5, 7 and 8 (D) 8, 2, 5 and 7

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 131

*UGC NET Dec 2013, Paper II, original Q48*

> Consider a disk queue with request for input/output to block on cylinders 98, 183, 37, 122, 14, 124, 65, 67 in that order. Assume that disk head is initially positioned at cylinder 53 and moving towards cylinder number

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 132

*UGC NET June 2013, Paper III, original Q13*

> In any n-element heap, the number of nodes of height h is (A) less than equal to ⎣⎢ ⎡ ⎦ ⎥ ⎤n 2 h (B) greater than ⎣ ⎢ ⎡ ⎦ ⎥ ⎤n 2 h (C) greater than ⎣ ⎢ ⎡ ⎦ ⎥ ⎤n 2 h + 1 (D) less than equal to ⎣ ⎢ ⎡ ⎦ ⎥ ⎤n 2 h + 1

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 133

*UGC NET June 2013, Paper III, original Q56*

> The number of distinct binary images which can be generated from a given binary image of right M × N are (A) M + N (B) M × N (C) 2 M + N (D) 2 MN

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 134

*UGC NET Dec 2014, Paper III, original Q50*

> How many disk blocks are required to keep list of free disk blocks i n a 16 GB hard disk with 1 kB block size using linked list of free disk blocks ? Assume t hat the disk block number is stored in 32 bits. (A) 1024 blocks (B) 16794 blocks (C) 20000 blocks (D) 1048576 blocks

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 135

*UGC NET June 2015, Paper III, original Q36*

> The number of nodes of height h in any n - element heap is (1) h (2) zh (3) ceil (f) (4)

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 136

*UGC NET July 2016, Paper II, original Q38*

> If the Disk head is locate d initially at track 32, find the number of disk moves required with FCFS scheduling criteria if the disk queue of I/O blocks requests are : 98, 37, 14, 124, 65, 67 (1) 320 (2) 322 (3) 321 (4) 319

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 137

*UGC NET July 2016, Paper III, original Q31*

> The number of different bina ry trees with 6 nodes is ______. (1) 6 (2) 42 (3) 132 (4) 256

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 138

*UGC NET Jan 2017, Paper II, original Q20*

> The order of a leaf node in a B + tree is the maximum number of children it can have. Suppose that block size is 1 kilobytes, the child pointer takes 7 bytes long and search field value takes 14 bytes long. The order of the leaf node is ________. (1) 16 (2) 63 (3) 64 (4) 65

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 139

*UGC NET Jan 2017, Paper II, original Q24*

> If h is chosen from a universal collection of hash functions and is use d to hash n keys into a table of size m, where n ≤ m, the expected number of collisions involving a particular key x is less than _______. (1) 1 (2) 1/n (3) 1/m (4) n/m

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 140

*UGC NET Jan 2017, Paper III, original Q50*

> Consider a disk queue with I/O requests on th e following cylinders in their arriving order : 6, 10, 12, 54, 97, 73, 128, 15, 44, 110, 34, 45 The disk head is assumed to be at cylinde r 23 and moving in the direction of decreasing number of cylinders. Total number of cylinde rs in the disk is 150. The disk head movement using SCAN-scheduling algorithm is : (1) 172 (2) 173 (3) 227 (4) 228

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 141

*UGC NET Dec 2018, original Q71*

> The solution of recurrence relation : T(n) = 2 T (sqrt(n)) + lg (n) is . O(lg (n)) 91394342282. O(n lg (n)) 91394342283. 0(lg (n) lg (n)) Guide 91394342284. 0(lg (n) Ig(lg (n)))

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 142

*UGC NET Dec 2018, original Q72*

> The elements 42, 25, 30, 40, 22, 35, 26 are inserted one by one in the given order into a max-heap. The resultant max-heap is stored in an array implementation as . <42, 40, 35, 25, 22, 30, 26> 91394342286. <42, 35, 40, 22, 25, 30, 26> 91394342287. <42, 40, 35, 25, 22, 26, 30> 91394342288. <42, 35, 40, 22, 25, 26, 30>

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 143

*UGC NET Dec 2018, original Q76*

> In a ternary tree, the number of internal nodes of degree 1, 2, and 3 is 4, 3, and 3 respectively. The number of leaf nodes in the ternary tree is 91394342302. 10 91394342303. 11 91394342304. 12

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 144

*UGC NET Dec 2018, original Q119*

> To overcome difficulties in Readers-Writers problem, which of the following statement/s is/are true? (i) Writers are given exclusive access to shared objects. (ii) Readers are given exclusive access to shared objects. (iti) Both Readers and Writers are given exclusive access to shared objects. Choose the correct answer from the code given below : Code : . (i) only 91394342474 (i) only Guide 91394342475. (i) only inal Exam 91394342476. Both (ii) and (ili)

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 145

*UGC NET Dec 2018, original Q146*

> Consider the following statements related to AND-OR Search algorithm. S1 A solution is a subtree that has a goal node at every leaf. S2 OR nodes are analogous to the branching in a deterministic environment. S3 AND nodes are analogous to the branching in a non-deterministic environment. Which one of the following is true referencing the above statements? Choose the correct answer from the code given below : Code: . S1 - False, S2 - True, S3 - True Guide 91394342582. S1 - True, S2 - True, S3 - False 91394342583. S1 - True, S2 - True, S3 - True 91394342584. S1 - False, S2 - True, S3 - False ngle Line Question Option: No

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 146

*UGC NET July 2018, Paper II, original Q28*

> The maximum number of comparisons needed to sort 9 items using radix sort is (assume each item is 5 digit octal number) : (1) 45 (2) 72 (3) 360 (4) 450

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 147

*UGC NET July 2018, Paper II, original Q29*

> A 5-ary tree is tree in which every internal node has exactly 5 children. The number o f left nodes in such a tree with 8 internal nodes will be : (1) 30 (2) 33 (3) 45 (4) 125

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 148

*UGC NET Dec 2019, original Q69*

> If we want to resize a 1024 x 768 pixels image to one that is 640 pixels wide with the same aspect ratio, what would be the height of the resized image? (1) 420 Pixels (2) 460 Pixels (3) 480 Pixels (4) 540 Pixels 61547540974.2 61547540975.3 61547540976.4 uestion Number: 70

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 149

*UGC NET Dec 2019, original Q79*

> Which of the following interprocess communication model is used to exchange messages among co-operative processes? (1) Shared memory model (2) Message passing model (3) Shared memory and message passing model (4) Queues 61547541014.2 61547541015. 3 61547541016. 4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 150

*UGC NET Dec 2019, original Q87*

> What is the worst case running time of Insert and Extract-min. in an implementation of a priority queue using an unsorted array? Assume that all insertions can be accomodated. (1) e(1). e(n) (2) 0(n). e(1) (3) e(1). e(1) (4) o(n). 0(n) 61547541046.2 61547541047.3 61547541048. 4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 151

*UGC NET Dec 2019, original Q88*

> In a B-Tree. each node represents a disk block. Suppose one block holds 8192 bytes. Each key uses 32 bytes. In a B-tree of order M there are M - 1 keys. Since each branch is on another disk block, we assume a branch is of 4 bytes. The total memory requirement for a non leaf node is (1) 32 M - 32 (2) 36 M - 32 (3) 36 M - 36 (4) 32 M - 36 61547541050.2 61547541051. 3 61547541052. 4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 152

*UGC NET Dec 2019, original Q105*

> Piconet is a basic unit of a bluetooth system consisting of - master node and up to - - active slave nodes. (1) one, five (2) one, seven (3) two. eight (4) one. eight Options : Guid 61547541117.1 61547541118.2 61547541119. 3 61547541120.4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 153

*UGC NET Dec 2019, original Q117*

> Consider the following statements with respect to duality in LPP: (a) The final simplex table giving optimal solution of the primal also contains optimal solution of its dual in itself. (b) If either the primal or the dual problem has a finite optimal solution. then the other problem also has a finite optimal solution. (c) If either problem has an unbounded optimum solution, then the other problem has no feasible solution at all. Which of the statements is (are) correct? (1) only (a) and (b) (2) only (a) and (c) (3) only (b) and (c) (4) (a), (b) and (c) 61547541166.2 61547541167.3 61547541168.4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 154

*UGC NET Dec 2019, original Q130*

> Consider the following : Guide (a) Trapping at local maxima (b) Reaching a plateau xam (c) Traversal along the ridge. Which of the following option represents shortcomings of the hill climbing algorithm? (1) (a) and (b) only (2) (a) and (c) only (3) (b) and (c) only (4) (a). (b) and (c) 61547541218.2 61547541219.3 61547541220. 4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 155

*UGC NET June 2019, original Q66*

> For a magnetic disk with concentric circular tracks, the seek latency is not linearly proportional to the seek distance due to 1. non-uniform distribution of requests 2. arm starting or stopping inertia 3. higher capacity of tracks on the periphery of the platter 4. use of unfair arm scheduling policies 64635085600.2 64635085601.3 64635085602. 4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 156

*UGC NET June 2019, original Q91*

> Consider a disk system with 100 cylinders. The requests to access the cylinders occur in the following sequence: 4,34, 10, 7, 19, 73, 2, 15, 6, 20 Assuming that the head is currently at cylinder 50, what is the time taken to satisfy all requests if it takes 1ms to move from the cylinder to adjacent one and the shortest seek time first policy is used? repp 357 ms Your . 2. 238 ms 3. 276 ms 4. 119 ms 64635085700.2 64635085701.3 64635085702.4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 157

*UGC NET June 2019, original Q94*

> Which of the following are NOT shared by the threads of the same process? (a) Stack (b) Registers (c) Address space (d) Message queue 1. (a) and (d) (b) and (c) 3. (a) and (b) 4. (a), (b) and (c) 64635085712. 2

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 158

*UGC NET June 2019, original Q114*

> Which of the following is best running time to sort n integers in the range 0 to n' -1? 1. 2. O(n) O(nlgn) O(n?) 64635085792. 2 64635085793. 3 64635085794. 4 Single One Question op on: No Opion Orients Vein ype: MCQ

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 159

*UGC NET June 2019, original Q115*

> Which of the following is application of depth-first search? 1. Only topological sort 2. Only strongly connected components 3. Both topological sort and strongly connected components 4. Neither topological sort nor strongly connected components 64635085796. 2 64635085797.3 64635085798.4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 160

*UGC NET Nov 2020, original Q54*

> Consider the following linear programming (LP): Max. 2 = 2x1 + 3x2 Such that 2x,+x≤4 x1 + 2x2 ≤ 5 *1. 72 20 The optimum value of the LP is (1) 23 (2) 9.5 (3) 13 (4) 8 53622816714.2 53622816715.3 53622816716.4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 161

*UGC NET Nov 2020, original Q58*

> What is the radix of the numbers if the solution to the quadratic equation x? -10x +26 = 0is x=4 and x = 7? (1) 8 (2) 9 (3) 10 (4) 11 53622816730. 2 53622816731.3 53622816732.4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 162

*UGC NET Nov 2020, original Q74*

> In a binary max heap containing n numbers, the smallest element can be found in . time. (1) O(n) (2) O(log: n) (3) O(1) (4) O(log: log2 n) 53622816794.2 53622816795.3 53622816796.4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 163

*UGC NET Nov 2020, original Q102*

> The running time of an algorithm is 0(g(n)) if and only if (A) its worst-case running time is 0(g(n)) and its best-case running time is n(g(n)). (0 = big 0) (B) its worst-case running time is 2(g(n)) and its best-case running time is o(g(n)). (O = big 0) (C) 0(g(n)) = n(g(n)) (0 = big 0) (D) 0(g(n)) n∞ (g(n)) is non-empty set. (o = small o) Choose the correct answer from the options given below: (1) (A) only (2) (B) only (3) (C) only (4) (D) only 53622816906.2 53622816907.3 53622816908, 4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 164

*UGC NET Nov 2020, original Q104*

> Which among the following statements) is (are) true? (A) A hash function takes a message of arbitrary length and generates a fixed length code. (B) A hash function takes a message of fixed length and generates a code of variable length. (C) A hash function may give same hash value for distinet messages. Choose the correct answer from the options given below: (1) (A) only (2) (B) and (C) only (3) (A) and (C) only (4) (B) only 53622816914.2 53622816915.3 53622816916.4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 165

*UGC NET Nov 2020, original Q114*

> Match List I with List II Let R_ = [(1.1). (2.2). (3,3)) and R¿ = ((1,1), (1,2), (1.3). (1.4)) List I List II (A) RUR2 (1) {(1.1).(1.2). (1.3), (1.4).(2.2).(8.3)) (B) (LI) {(1.1)} (C) R_nR2 (ILI) ((1,2).(1.3).(1.4)} (D) R2 - Ri (IV) {(2,2).(3,3)) Choose the correct answer from the options given below: (1) A-I, B-II. C-IV. D-III (2) A-I. B-IV. C-III, D-II (3): A-I. B-III, C-I. D-IV (4) A-I. B-IV. C-II, D-III 53622816954. 2 53622816955. 3 53622816956.4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 166

*UGC NET Nov 2020, original Q120*

> Match List I with List II List I List II (A) Topological sort of DAG (1 0(V + E) (B) Kruskal's MST algorithm (I) O(VE) (C) Bellman-Ford's single-source shortest (I) e(V+E) path algorithm (D) Floyd-Warshall's all pair shortest (IV) e(v3) path algorithm Choose the correct answer from the options given below: (1) A-I. B-III. C-IV. D-II (2) A-III. B-I. C-IV. D-II (3) A-II. B-I, C-II, D-IV (4) A-I. B-III. C-II, D.IV Options:

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 167

*UGC NET Oct 2022, original Q44*

> The number of nodes of height h in any n-element heap is atmost: 1. 21+1 2. 2i=] 3. 4. 21-

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 168

*UGC NET June 2025, original Q70*

> What shall be the average waiting time per process if we know that 10 processes (on average) arrive every second and there are normally 20 processes in the queue? 1. 03 seconds 1. 02 seconds 2. 18 seconds 3. 09 seconds 42558919333.2 42558919334. 3 42558919335.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 169

*UGC NET June 2025, original Q99*

> The correct sequence of constructing Huffman tree is A. Repeat until root formed B. Create leaf nodes C. Build priority queue D. Combine lowest frequency nodes Choose the correct answer from the options given below: 1. B, C, A, D 2. D, B, A, C 3. B, C, D, A 4. C, A, B, D 42558919449.2 42558919450. 3 42558919451.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 170

*UGC NET June 2025, original Q112*

> Once the process is allocated CPU and executing which of the following events could not occur? A. The process could issue an 1/0 request and then be placed in the Ready Queue B. The process could create new subprocesses & wait for the termination of the subprocesses C. The time slice of the process expires and it may join the waiting queue D. The process is forcibly removed from the CPU and is put in the Waiting queue due to arrival of an interrupt Choose the correct answer from the options given below: 1. B Only 2. D Only 3. A and C Only 4. A, C and D Only 42558919501.2 42558919502. 3 42558919503.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 171

*UGC NET June 2025, original Q135*

> Match List I with List I! List List Il A. Circular Queue I. Print Queue B. Priority Queue II. CPU Scheduling C. Double Ended Queue III. Dijkstra algorithm D. Simple Queue IV. Palindrome checking Choose the correct answer from the options given below: 1. A-II, B-II, C-I, D-IV 2. A-II, B-III, C-IV, D-1 3. A-III, B-II, C-I, D-IV 4. A-IV, B-II, C-I, D-III 42558919593.2 42558919594.3 42558919595.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 172

*UGC NET June 2025, original Q141*

> Which of the following is the correct High level code for the given TAC in the passage 1 t1 = y+2 2 init = x/(y+2); init = x/t1; limit=10; limit=10; while(i>j|| num>b) if 11 numb num = limit-1; num = limit-1; b = y+ 2; i = i-num; b = y + 2; i = i - num; } } j = i - num; j= i - num; k = k+b; k= k+b; 3 init = x/(y+2); 4 init = x/(y+2); limit=10; limit=10; if(i>j) while>&& num>b) While( num>b) num = limit-1; num = limit-1; b = y+ 2; else } i= i - num: } j= i - num; b = y +2; k = k+b; i = i - num; } j= i - num; k= k+b; 42558919617.2 42558919618.3 42558919619.4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 173

*UGC NET June 2025, original Q145*

> Which of the following is the Optimized version for the given TAC in the passage 1 100 : t1 = y+2 2 100 : t1 = y+2 101 : initial = x/t1 101 : initial = x/t1 102 : limit = 10 102 : limit = 10 103 : if i >j goto 105 103 : if i >j goto 105 104: goto 111 104 : if num ‹ b goto 111 105 : if num > b goto 107 105 : num = limit-1 106 : goto 111 106 : b = t1 107 : b = y+2 107: i = i-num 108 : i = i - limit-1 108: goto 103 109 : goto 103 109 : k= i+b 110: k= i+b 3 100 : t1 = y+2 4 100 : t1 = y+2 101 : initial = x/t1 101 : initial = x/t1 102 : limit = 10 102 : limit = 10 103 : num = 9 103 : if i>j goto 105 104 : if i >j goto 105 104 : goto 111 105 : goto 111 105 : if num < b goto 111 106 : if num > b goto 107 106 : num = limit-1 107 : goto 111 107 : b = t1 108: i = i - num 108 : i= i-num 109 : goto 103 109 : goto 103 110: j=i-num 110: k= i+b 111 : k= j+t1 42558919633.2 42558919634.3 42558919635.4 Sub-Section Id: Sub-Section Number : 3 425589204 Question Shuffling Allowed : No

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 174

*UGC NET June 2025, original Q146*

> What shall be the total head movement of cylinders if the FCFS disc scheduling method is used ? (1) 536 (2) 594 (3) 647 (4) 700 42558919637.2 42558919638.3 42558919639.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 175

*UGC NET June 2025, original Q148*

> What shall be the 2ºd request being processed by SCAN (LEFT) disc Scheduling technique for the already given request queue? 1. 81 2. 45 3. 33 4. 175 42558919644. 1 42558919646. 3 42558919647,4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 176

*UGC NET June 2025, original Q150*

> What shall be the 2°d request being processed by C-LOOK (Right) disc Scheduling technique for the already given request queue ? (1) 81 (2) 45 (3) 77 (4) 33 42558919653.2 42558919654. 3 42558919655.4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 177

*UGC NET Dec 2025 session (Jan 2026), original Q53*

> Question Number : 53 divides the order of the group (Z13, X) Reason R: The order of a subgroup of a group divides the order of the group. In the light of the above statements, choose the most appropriate answer from the options given below 1. Both A and R are correct and R is the correct explanation of A 2. Both A and R are correct but R is NOT the correct explanation of A 3. A is correct but R is not correct 4. A is not correct but R is correct 6119878610.2 6119878611.3 6119878612.4 Vumber : Yes

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 178

*UGC NET Dec 2025 session (Jan 2026), original Q83*

> Question Number : 83

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 179

*UGC NET Dec 2025 session (Jan 2026), original Q87*

> Question Number : 87

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 180

*UGC NET Dec 2025 session (Jan 2026), original Q88*

> Question Number : 88 = 3T(n/4) + n log n 1. e (n log n) 2. 0 (n? log n) 3. 0 (n (log n)-) 4. e (n log log n) 6119878750.2 6119878751.3 6119878752.4 Duestion Number : 88 = 3T(n/4) + n log n 1. e (n log n) 2. 0 (n2 log n) 3. 0 (n (log n)?) 4. e (n log log n) 6119878750.2 6119878751.3 6119878752.4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 181

*UGC NET Dec 2025 session (Jan 2026), original Q90*

> Question Number : 90 - 1 2. n1 + [log n] 3. [log n] 4. n + [log n] - 2 6119878758.2 6119878759.3 6119878760.4 Number : Yes

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 182

*UGC NET Dec 2025 session (Jan 2026), original Q106*

> Question Number: 106 * } D. L = {WE (a, b)*: na(w) = 16(W) } E.L= {a"b"c"™m : n≥0, m ≥ 0} Choose the correct answer from the options given below: 1. A. C & D Only 2. B, D & E Only 3. A & B Only 4. C & D Only 6119878822.2 6119878823.3 6119878824.4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 183

*UGC NET Dec 2025 session (Jan 2026), original Q141*

> Question Number : 141 before adding the contingency margin? 1. 240 PM 2. 260 PM 3. 180 PM 4. 200 PM 6119878962.2 6119878963.3 6119878964.4

**Chapter foundations**

This question belongs to the ideas covered by **Selected Topics**. Revise these foundations: Number-Theoretic Algorithms; Polynomial Arithmetic; FFT; String Matching.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Selected Topics questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-8"></a>

### 8. Advanced Algorithms (67 questions)

**What to master:** Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam lens:** Choose the data structure or invariant first, then derive the complexity rather than recalling it in isolation.

**Reusable method:** Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked.

**High-yield rules:** Master theorem applies only to suitable forms. BFS gives unweighted shortest paths; Dijkstra needs nonnegative edges; comparison sorting has an Omega(n log n) lower bound.

**Common traps:** Do not confuse tree height with node count, stable with in-place sorting, amortized with average complexity, or NP-hard with NP-complete.

---

#### Question 184

*UGC NET Dec 2009, Paper II, original Q11*

> Recursive functions are executed in a (A) First in first out-order (B) Last in first out-order (C) Parallel fashion (D) Load balancing

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 185

*UGC NET Dec 2009, Paper II, original Q25*

> A hash function f defined as f(key) = key mod 7, with linear probing used to resolve collisions. Insert the keys 37, 38, 72, 48, 98 and 11 into the table indexe d from 0 to 6. What will be the location of 11 ? (A) 3 (B) 4 (C) 5 (D) 6

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 186

*UGC NET June 2010, Paper II, original Q21*

> If we have six stack operations- pushing and popping each of A, B and C-such that push (A) must occur before push (B) which must occur before push (C), then A, C, B is a possible order for the pop operations, since this could be our sequence : push (A), pop (A), push (B), push (C), pop (C), pop (B). Which one of the following orders could not be the order the pop operations are run, if we are to satisfy the requirements described above ? (A) ABC (B) CBA (C) BAC (D) CAB

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 187

*UGC NET June 2010, Paper II, original Q25*

> In a B tree of order 5, the following keys are inserted as follows : 7, 8, 1, 4, 13, 20, 2, 6 and 5 How many elements are present in the root of the tree ? (A) 1 (B) 2 (C) 3 (D) 4

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 188

*UGC NET Dec 2012, Paper II, original Q26*

> A hash function f defined as f (key) =

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 189

*UGC NET June 2012, Paper II, original Q28*

> Mobile IP provides two basic functions. (A) Route discovery and registration (B) Agent discovery and registration (C) IP binding and registration (D) None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 190

*UGC NET Dec 2013, Paper II, original Q0*

> The total number of head movements using Shortest Seek Time First (SSTF) and SCAN algorithms are respectively (A) 236 and 252 cylinders (B) 640 and 236 cylinders (C) 235 and 640 cylinders (D) 235 and 252 cylinders

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 191

*UGC NET Dec 2013, Paper II, original Q35*

> Big – O estimate for f( x) = ( x + 1) log( x2 + 1) + 3 x2 is given as (A) O( x log x) (B) O( x2) (C) O( x3) (D) O( x2 log x)

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 192

*UGC NET Dec 2013, Paper II, original Q38*

> If n and r are non- negative integers and n ≥ r, then p(n + 1, r) equals to (A) p(n, r) (n + 1) (n + 1 – r) (B) p(n, r) (n + 1) (n – 1 + r) (C) p(n, r) (n – 1) (n + 1 – r) (D) p(n, r) (n + 1) (n + 1 + r)

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 193

*UGC NET Dec 2013, Paper III, original Q37*

> The longest common subsequence of the sequences X = <A, B, C, B, D, A, B> and Y = <B, D, C, A, B, A> has length (A) 2 (B) 3 (C) 4 (D) 5

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 194

*UGC NET Dec 2014, Paper II, original Q5*

> If we define the functions f, g and h that map R into R by : f( x) = x4, g( x) = x2 + 1, h( x) = x2 + 72, then the value of the composite functions ho(gof) and (hog)of are given as (A) x8 – 71 and x8 – 71 (B) x8 – 73 and x8 – 73 (C) x8 + 71 and x8 + 71 (D) x8 + 73 and x8 + 73

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 195

*UGC NET Dec 2014, Paper II, original Q22*

> You have to sort a list L, consisting of a sorted list followed b y a few ‘random’ elements. Which of the following sorting method would be most suitable for such a task ? (A) Bubble sort (B) Selection sort (C) Quick sort (D) Insertion sort

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 196

*UGC NET Dec 2014, Paper III, original Q21*

> Which of the following statements is not true ? (A) MPI_Isend and MPI_Irecv are non-blocking message passing routines of M PI. (B) MPI_Issend and MPI_Ibsend are non-blocking message passing routines of MPI. (C) MPI_Send and MPI_Recv are non-blocking message passing routines of MPI. (D) MPI_Ssend and MPI_Bsend are blocking message passing routines of MPI.

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 197

*UGC NET Dec 2014, Paper III, original Q31*

> Any decision tree that sorts n elements has height (A) Ω(n) (B) Ω(lgn) (C) Ω(n lgn) (D) Ω(n 2)

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 198

*UGC NET Dec 2014, Paper III, original Q33*

> We can show that the clique problem is NP-hard by proving that (A) CLIQUE ≤ P 3-CNF_SAT (B) CLIQUE ≤ P VERTEX_COVER (C) CLIQUE ≤ P SUBSET_SUM (D) None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 199

*UGC NET Dec 2015, Paper II, original Q38*

> The inorder traversal of the following tree is : 6)

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 200

*UGC NET Dec 2015, Paper III, original Q17*

> Given two sequences X and Y: X= (a, b, c, b, d, a, b) Y = (b, d, c, a, b, a). The longest common subsequence of X and Y is : (1) (b, c, a) (2) (c, a, b) (3) b,c, a, a) (4) (b, c, b, a)

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 201

*UGC NET Dec 2015, Paper III, original Q70*

> Consider a unit square centred at origin. The coordinates of the square are translated by a factor (5, 1) and rotated by an angle of 90°. What shall be the coordinates of the new square ?

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 202

*UGC NET June 2015, Paper II, original Q48*

> Which of the following algorithms sort n integers, having the range 0 to (n? - 1), in ascending order in O(n) time ? (1) Selection sort (2) Bubble sort (3) Radix sort (4) Insertion sort

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 203

*UGC NET June 2015, Paper III, original Q10*

> The Relation Vendor Order (V_no, V_ord_no, V_name, Qty_sup, unit_price) is in 2NF because : (1) Non_key attribute V_name is dependent on V_no which is part of composite key (2) Non_key attribute V_name is dependent on Qty_sup (3) Key attribute Qty_sup is dependent on primary_key unit price (4) Key attribute V_ord_no is dependent on primary_key unit price

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 204

*UGC NET June 2015, Paper III, original Q16*

> Which of the following is not a basic primitive of the Graphics Kernel System (GKS) ? (1) POLYLINE (2) POLYDRAW (3) FILL AREA (4) POLYMARKER

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 205

*UGC NET June 2015, Paper III, original Q33*

> Which of the following is asymptotically smaller ? (1) Ig(lg*n) (2) 1g*(Ign) (3) Ig(n!) (4) lg*(n!)

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 206

*UGC NET June 2015, Paper III, original Q34*

> Consider a hash table of size m = 100 and the hash function h(k) = floor (m(kA mod 1)) for A = (55-1) = 0.618033. Compute the location to which the key k=123456 is placed in hash table. (1) 77 (2) 82 (3) 88 (4) 89

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 207

*UGC NET June 2015, Paper III, original Q35*

> Let f(n) and g (n) be asymptotically non-negative functions. Which of the following is correct? (1) 0 (f(n)*g(n)) = min (f (n), g(n)) (2) 0 f(n)*g(n)) = max (f(n), g(n)) 3) o f(n) + g(n)) = min (f (n), g(n)) (4) 0 (f(n) + g(n)) = max (f (n), g(n))

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 208

*UGC NET June 2015, Paper III, original Q64*

> Given the symbols A, B, C, D, E, F, G and H with the probabilities 30'30 ' 30'30 ' 30'30 ' 30 and 13 respectively. The average Huffman code size in bils per symbol is : (1) 67 (2) 34 (3) 30 (4) 78 30

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 209

*UGC NET June 2015, Paper III, original Q69*

> Given the following statements with respect to linear programming problem: S1: The dual of the dual linear programming problem is again the primal problem S2: If either the primal or the dual problem has an unbounded objective function value, the other problem has no feasible solution. S3: If either the primal or dual problem has a finite optimal solution, the other one also possesses the same, and the optimal value of the objective functions of the two problems are equal. Which of the following is true? (1) S1 and S2 (2) S1 and S3 (3) S2 and S3 (4) S1, S2 and S3

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 210

*UGC NET July 2016, Paper II, original Q22*

> Consider the following operations performed on a stack of size 5 : Push (a); Pop() ; Push(b); Push(c); Pop(); Push(d); Pop();Pop(); Push (e) Which of the following st atements is correct ? (1) Underflow occurs (2) Stack operations are performed smoothly (3) Overflow occurs (4) None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 211

*UGC NET July 2016, Paper II, original Q30*

> Optical fiber uses reflection to guide light th rough a channel, in which angle of incidence is ________ the critical angle. (1) equal to (2) less than (3) greater than (4) less than or equal to

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 212

*UGC NET July 2016, Paper III, original Q34*

> Match the following : (a) Huffman codes (i) O(n 2) (b) Optimal polygon triangulation (ii) θ(n3) (c) Activity selection problem (iii) O(nlgn) (d) Quicksort (iv) θ(n) Codes : (a) (b) (c) (d) (1) (i) (ii) (iv) (iii) (2) (i) (iv) (ii) (iii) (3) (iii) (ii) (iv) (i) (4) (iii) (iv) (ii) (i)

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 213

*UGC NET July 2016, Paper III, original Q47*

> Which of the following sets represent five stages defined by Capability Maturity Model (CMM) in increasing order of maturity ? (1) Initial, Defined, Repeatable, Managed, Optimized. (2) Initial, Repeatable, Defined, Managed, Optimized. (3) Initial, Defined, Managed, Repeatable, Optimized. (4) Initial, Repeatable, Managed, Defined, Optimized.

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 214

*UGC NET July 2016, Paper III, original Q50*

> In Unix operating system, when a process creates a new process using the fork () system call, which of the following state is shared between the parent process and child process ? (1) Heap (2) Stack (3) Shared memory segments (4) Both Heap and Stack

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 215

*UGC NET July 2016, Paper III, original Q70*

> Consider the statement, “Either – 2 ≤ x ≤ – 1 or 1 ≤ x ≤2”. The negation of this statement is (1) x < – 2 or 2 < x or – 1 < x < 1 (2) x < – 2 or 2 < x (3) – 1 < x < 1 (4) x ≤ – 2 or 2 < x or – 1 < x < 1

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 216

*UGC NET Jan 2017, Paper II, original Q3*

> The functions mapping R into R are defined as : f( x) = x3 – 4x, g( x) = 1 x2 + 1 and h( x) = x4. Then find the value of the following composite functions : h og( x) and h ogof( x) (1) ( x2 + 1) 4 and [( x3 – 4x)2 + 1] 4 (2) ( x2 + 1) 4 and [( x3 – 4x)2 + 1] –4 (3) ( x2 + 1) –4 and [( x2 – 4x)2 + 1] 4 (4) ( x2 + 1) –4 and [( x3 – 4x)2 + 1] –4

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 217

*UGC NET Jan 2017, Paper II, original Q22*

> The seven elements A, B, C, D, E, F and G are pushed onto a stack i n reverse order, i.e., starting from G. The stack is popped five times and each element is inserted into a queue. Two elements are deleted from the queue and pushed back onto the stack. Now, one element is popped from the stack. The popped item is ________. (1) A (2) B (3) F (4) G

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 218

*UGC NET Jan 2017, Paper II, original Q23*

> Which of the following is a valid heap ? (A) (B) (C) (D) (1) A (2) B (3) C (4) D

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 219

*UGC NET Jan 2017, Paper II, original Q30*

> In link state routing algorithm after construction of link state packets, new routes are computed using : (1) DES algorithm (2) Dijkstra’s algorithm (3) RSA algorithm (4) Packets

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 220

*UGC NET Jan 2017, Paper III, original Q12*

> If following sequence of keys are insert ed in a B+ tree with K(=3) pointers : 8, 5, 1, 7, 3, 12, 9, 6 Which of the following sh all be correct B+ tree ? (1) (2) (3) (4)

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 221

*UGC NET Jan 2017, Paper III, original Q18*

> Consider a line AB with A = (0, 0) and B = (8, 4). Apply a si mple DDA algorithm and compute the first four plots on this line. (1) [(0, 0), (1, 1), (2, 1), (3, 2)] (2) [(0, 0), ( 1, 1.5), (2, 2), (3, 3)] (3) [(0, 0), (1, 1), (2, 2.5), (3, 3)] (4) [(0, 0), (1, 2) , (2, 2), (3, 2)]

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 222

*UGC NET Jan 2017, Paper III, original Q29*

> In RSA public key cryptosystem suppose n = p ∗ q where p and q are primes. (e, n) and (d, n) are public and private keys respectively. Let M be an integer such that o < M < n and φ(n) = (p – 1) (q – 1). Which of the following equations re present RSA public key cryptosystem ? I. C ≡ Me (mod n) II. ed ≡ 1(mod n) M ≡ (C)d (mod n) III. ed ≡ 1(mod φ(n)) IV. C ≡ Me(mod φ(n)) M ≡ Cd(mod φ(n)) Codes : (1) I and II (2) I and III (3) II and III (4) I and IV

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 223

*UGC NET Jan 2017, Paper III, original Q32*

> Any decision tree that sorts n elements has height ________. (1) Ω(lg n) (2) Ω(n) (3) Ω(n lg n) (4) Ω(n2)

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 224

*UGC NET Nov 2017, Paper II, original Q11*

> Use of any calculator or log table etc., is prohibited.

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 225

*UGC NET July 2018, Paper II, original Q22*

> Consider the array A=<4, 1, 3, 2, 16, 9, 10, 14, 8, 7>. After building heap from th e array A, the depth of the heap and the right child of max-heap are _________ and _________ respectively. (Root is at level 0). (1) 3, 14 (2) 3, 10 (3) 4, 14 (4) 4, 10

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 226

*UGC NET July 2018, Paper II, original Q23*

> A hash function h defined h(key)=key mod 7, with linear probing, is us ed to insert the keys 44, 45, 79, 55, 91, 18, 63 into a table indexed from 0 to 6. What will be the loca tion of key 18 ? (1) 3 (2) 4 (3) 5 (4) 6

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 227

*UGC NET July 2018, Paper II, original Q24*

> Which of the following algorithms solves the single-source short est paths ? (1) Prim’s algorithm (2) Floyd - Warshall algorithm (3) Johnson’s algorithm (4) Dijkstra’s algorithm

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 228

*UGC NET July 2018, Paper II, original Q70*

> Consider a hash table of size seven, with starting index zero, and a hash fun ction (7 x+3) mod 4. Assuming the hash table is initially empty, which of the follo wing is the contents of the table when the sequence 1, 3, 8, 10 is inserted into the table using closed has hing ? Here “__” denotes an empty location in the table. (1) 3, 10, 1, 8, __ , __ , __ (2) 1, 3, 8, 10, __ , __ , __ (3) 1, __ , 3, __ , 8, __ , 10 (4) 3, 10, __ , __ , 8, __ , __

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 229

*UGC NET Dec 2019, original Q131*

> Consider the following learning algorithms : Exam Guide (a) Logistic repression (b) Back propogation (c) Linear repression Which of the following option represents classification algorithms? (1) (a) and (b) only (2) (a) and (c) only (3) (b) and (c) only (4) (a). (b) and (c) 61547541222. 2 61547541223.3 61547541224. 4

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 230

*UGC NET June 2019, original Q112*

> There are many sorting algorithms based on comparison. The running time of heapsort algorithm is O(ngn). Like P, but unlike Q, heapsort sorts in place where (P, Q) is equal to 1. Merge sort, Quick sort 2. Quick sort, insertion sort Insertion sort, Quick sort Insertion sort, Merge sort 64635085784. 2 64635085785.3 64635085786.4

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 231

*UGC NET June 2019, original Q118*

> Consider the following steps : S, : Characterize the structure of an optimal solution S,: Compute the value of an optimal solution in bottom-up fashion Which of the step(s) is/are common to both dynamic programming and greedy algorithms? repp 1. Only S, 2. Only S, Personal Exam Guidel 3. Both S, and S 4. Neither S, nor S 64635085808. 2 64635085809. 3 64635085810.4

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 232

*UGC NET Nov 2020, original Q75*

> If algorithm A and another algorithm B take logan) and Vr microseconds, respectively, to solve a problem, then the largest size n of a problem these algorithms can solve, respectively, in one second are and (1) 210° and 10° (2) 210° and 1042 (3) 210° and 6.10° (4) 210° and 6.1012 53622816798.2 53622816799.3 53622816800.4

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 233

*UGC NET Nov 2021, original Q49*

> 63 A hash function h defined as h(key)=key mod 7, with linear probing, is used to insert the keys 44, 45, 79, 55, 91, 18, 63 into a table indexed from 0 to 6. What will be the location of key 18? 1. 3 2. 4 3. 5 4. 6

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 234

*UGC NET Nov 2021, original Q53*

> Both Statement I and Statement II are true Consider the given tree below. Calculate the value at the root of the tree using alpha‐beta pruning algorithm. 1. 3 2. 5 3. 6 4. 9

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 235

*UGC NET Oct 2022, original Q10*

> Consider the primal problem : Maximize 2 = 5x1+12x, + 4x3 Subject to x1 + 2x, + x3 =10 2xy - x2 + 3x3 = 8 its dual problem is Minimize w =101 + 8y Subject to 21 + 2y 25 231 - 2 = 12 4 + 3y2 ≥4 Which of the following is correct? 1. 1≥0, y= unrestricted 2. V1 20, N2 20 3. _is unrestricted, yz ≥0 4. Y_is unrestricted, yz restricted

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 236

*UGC NET Oct 2022, original Q19*

> The condition num! = 65 cannot be replaced by 1. num 65 || num <65 2. ! (num = = 65) 3. num - 65 4. ! (num - 65)

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 237

*UGC NET Oct 2022, original Q42*

> Assume that f (n) and g(n) are asymptotically positive. Which of the following is correct? 1. f(2) =0(g(r)) and g(a)= 0(1)) → /(v) = c(k(n)) 2. f(n) = 2(g(n)) and g(r) = 2(1(r)) = f(n) = O(li(2)) 3. f(1) = o(g()) and g(n1)=o(h()) = f(1)=o (h(x)) 4. f(n) = 0(g(n)) and g(n) = clh(n)) =/ (n)= 2(h(n))

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 238

*UGC NET Oct 2022, original Q43*

> The solution of the recunrence relation I (r) = 37(¼) -nIgn is 1. e(n?lgn) 2. e(n/gn) 3. Alnlgn) 4. Anlg lgn)

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 239

*UGC NET Oct 2022, original Q47*

> Consider the hash table of size 11 that uses open addressing with linear probing. Let h(k) = k mod 11 be the hash function. A sequence of records with keys 43. 36. 92, 87. 11. 47. 11. 13, 14 is inserted into an initially empty hash table. the bins of which are indexed from O to 10. What is the index of the bin into which the last record is inserted? 1. 8 2. 7 10 4. 4

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 240

*UGC NET Oct 2022, original Q48*

> Consider the traversal of a tree Preorder → ABCEIFJDGHKL Inorder → EICFJBGDKHLA Which of the following is correct post order traversal? 1. EIFJCKGLHDBA 2. FCGKLHDBUAE 3. FCGKLHDBAEIJ 4. IEJFCGKLHDBA

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 241

*UGC NET Oct 2022, original Q75*

> Consider the following algorithms and their running times : Algorithms Complexities (A) Breadth First Search o(v+E) (B) Rabin-Karp Algorithm (II) O(v+E) (C) Depth-First Search (III a((n-m-1)m) (D) Heap sort (worst case) (IV) O(1) (E) Quick sort (worst case) (V) O(77lg11) Which one of the following is correct? 1. (A)-III, (B)-II. (C)-D. (D) (IV). (E)-(V) 2. (A) -II, (B)-II, (C)-(I, (D)-(IV), (E)-(V) 3. (А)-I. (B)-(I. (C)-Д. (D)-(V). (E)-(IV) 4. (A)-II. (B)-I). (C)-(ID. (D)-(IV). (E)-(V)

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 242

*UGC NET Oct 2022, original Q77*

> Consider the following statements of approximation algorithm : Statement I: Vertex-cover is a polynomial time 2-approximation algorithm. Statement II: TSP-tour is a polynomial time 3-approximation algorithm for travelling salesman problem with the triangle inequality. Which of the following is correct? 1. Statement I true and Statement II false 2. Statement I and Statement II true Statement I false and Statement Il true 4. Statement I and Statement II false

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 243

*UGC NET June 2023, Paper II, original Q60*

> Suppose a circular queue of capacity (n - 1) elements is implemented with an (+2) array of n elements. Assume that the insertion and deletion operations are carried out using REAR and FRONT as array index variable respectively. Initially, REAR = FRONT = 0. The conditions to detect queue empty and queue full are a. EMPTY : REAR == FRONT FULL : (REAR + 1) mod n == FRONT b. EMPTY : (FRONT + 1) mod n == REAR FULL : (REAR + 1) mod n == FRONT al Exams Guid c. EMPTY (REAR + 1) mod n == FRONT FULL: REAR == FRONT d. EMPTY : REAR == FRONT FULL : (FRONT + 1) mod n == REAR

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 244

*UGC NET Dec 2022 session, 15 Mar 2023 Shift 1, original Q51*

> N0-87043 The relation R= ((1,3), (1, 1), (3, 1), (1,2), (3,3), (4,4)} defined in (1,2,3,4) is.

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 245

*UGC NET Aug 2024, original Q118*

> Select the Sorting Algorithms that are stable. (A) Quick Sort (B) Bubble Sort (C) Insertion Sort (D) Merge Sort (E) Shell Sort Choose the correct answer from the options given below : (1) (A), (B), (C) and (E) Only (2) (A), (D) and (E) Only (3) (B) and (C) Only (4) (B), (C) and (E) Only

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 246

*UGC NET June 2025, original Q116*

> Which of the following algorithms use Greedy strategy? A. Dijkstra's algorithm B. Kruskal's algorithm C. Huffman coding D. Bellman-Ford algorithm Choose the correct answer from the options given below: 1. A, B and D Only 2. A, B and C Only 3. C and D Only 4. Aand D Only 42558919516.1 42558919518. 3 42558919519.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 247

*UGC NET Dec 2025 session (Jan 2026), original Q74*

> Question Number : 74

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 248

*UGC NET Dec 2025 session (Jan 2026), original Q91*

> Question Number : 91

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 249

*UGC NET Dec 2025 session (Jan 2026), original Q96*

> Question Number : 96

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 250

*UGC NET Dec 2025 session (Jan 2026), original Q126*

> Question Number: 126

**Chapter foundations**

This question belongs to the ideas covered by **Advanced Algorithms**. Revise these foundations: Parallel Sorting, Searching and Merging; Approximation; Randomized Algorithms.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Advanced Algorithms questions: Trace a small instance, state the loop or recursion invariant, solve the recurrence, and report best/average/worst case only when asked. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

## Coverage and quality notes

- Recovered question blocks in this unit: **250**
- Chapter placements with direct keyword support: **200**
- Chapter placements needing manual review: **50**
- Questions with validated answers in this guide: **0**
- OCR may flatten mathematical notation, tables, code indentation, and figures. Full audit references are retained in the structured data.
- Some combined Paper 1/Paper 2 scans and older papers lack a trustworthy embedded key. Such questions remain pending rather than receiving guessed answers.

---

[Back to contents](#contents) · [All units](README.md) · [Project home](../README.md)

