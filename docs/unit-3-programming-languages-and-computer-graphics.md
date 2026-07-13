# Unit 3: Programming Languages and Computer Graphics

[Project home](../README.md) · [All units](README.md) · [Official syllabus](syllabus.md)

## Contents

- [How to use this guide](#status-and-use)
- [Unit-wide exam playbook](#unit-wide-exam-playbook)
- [1. Language Design and Translation Issues](#chapter-1)
- [2. Elementary Data Types](#chapter-2)
- [3. Programming in C](#chapter-3)
- [4. Object-Oriented Programming](#chapter-4)
- [5. Programming in C++](#chapter-5)
- [6. Web Programming](#chapter-6)
- [7. Computer Graphics](#chapter-7)
- [8. 2-D Geometrical Transforms and Viewing](#chapter-8)
- [9. 3-D Object Representation, Geometric Transformations and Viewing](#chapter-9)
- [Coverage and quality notes](#coverage-and-quality-notes)

## Status and use

This guide contains all **17 question blocks currently recoverable and assigned to Unit 3** from the local UGC NET archive. Questions are arranged chapter-wise and numbered continuously through the unit.

> [!WARNING]
> This is a working extraction inventory, not a complete solved guide. **9 answers are validated and 8 remain pending** in this unit. Some unit and chapter placements use fallback routing, and OCR or missing figures can make questions incomplete.

Use this file for question discovery and broad chapter revision. The chapter notes and exam methods are general, not question-specific solutions. Full source paths, PDF pages and classification states remain in the structured data for auditing.

## Unit-wide exam playbook

- **Core idea:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.
- **Method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.
- **Rules/formulas:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.
- **Frequent traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

## Chapter-wise concepts and PYQs

<a id="chapter-1"></a>

### 1. Language Design and Translation Issues (1 questions)

**What to master:** Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 1

*UGC NET Nov 2021, original Q5*

> Match List I with List II List I List II (Programming Paradigm) (Characteristic)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Imperative I. Declarative, clausal representation, theorem proving
> - **B.** Object‐oriented II. Side‐effect free, declarative, expression evaluation
> - **C.** Logic III. Imperative, abstract data type
> - **D.** Functional IV. Command‐based, procedural Choose the correct answer from the options given below:

**Options**

1. A ‐ IV, B ‐ III, C ‐ I, D ‐ II
2. A ‐ III, B ‐ IV, C ‐ I, D ‐ II
3. A ‐ IV, B ‐ III, C ‐ II, D ‐ I
4. A ‐ II, B ‐ III, C ‐ I, D ‐ IV

**Correct answer**

**Option 1: A-IV, B-III, C-I, D-II**

*Verification: Official NTA final key matched by Question ID 2335 and Option ID 9337; independently verified from the defining properties of the four paradigms.*

**Step-by-step solution**

1. Imperative programming describes computation through commands that change state, so A matches IV, command-based and procedural.
2. Object-oriented programming organizes mutable state and operations into objects and supports abstract data types, so B matches III.
3. Logic programming states facts and clauses and derives answers through inference or theorem proving, so C matches I.
4. Functional programming emphasizes expression evaluation and avoiding side effects, so D matches II. Therefore option 1 is correct.

**Why each option is right or wrong**

- **1. A-IV, B-III, C-I, D-II — Correct.** It matches each paradigm to its defining computational model.
- **2. A-III, B-IV, C-I, D-II — Incorrect.** It swaps imperative command-based programming with the object-oriented abstract-data-type description.
- **3. A-IV, B-III, C-II, D-I — Incorrect.** It swaps logic programming with functional programming.
- **4. A-II, B-III, C-I, D-IV — Incorrect.** It assigns functional characteristics to imperative programming and procedural commands to functional programming.

**Conceptual lesson**

A programming paradigm is a model for expressing computation. Imperative programs say how state changes; functional programs evaluate expressions; logic programs state relations to be proved; object-oriented programs coordinate objects that combine state and behaviour.

Declarative is a broad family containing functional and logic styles, but their mechanisms differ. Functional programming uses functions and expression values, while logic programming uses facts, rules, unification and inference.

Real languages are often multi-paradigm. Exam questions normally ask for the characteristic most strongly associated with each paradigm, not a claim that a language can use only one style.

**How to solve similar questions**

Look for signature words: command/state means imperative; objects and abstract data types mean object-oriented; clauses and theorem proving mean logic; expressions and side-effect freedom mean functional.

**Verification references**

- [Final-answer-key archive](https://cdnbbsr.s3waas.gov.in/s301eee509ee2f68dc6014898c309e86bf/uploads/2022/04/2022040888.pdf)
- [Independent concept reference](https://docs.python.org/3/howto/functional.html)

<a id="chapter-2"></a>

### 2. Elementary Data Types (1 questions)

**What to master:** Properties of Types and Objects; Scalar and Composite Data Types.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 2

*UGC NET Nov 2021, original Q48*

> The order of a leaf node in a B+ tree is the maximum number of (value, data record pointer) pairs it can hold. Given that the block size is 1K bytes, data record pointer is 7 bytes long, the value field is 9 bytes long and a block pointer is 6 bytes long, what is the order of the leaf node?

**Options**

1. 63
2. 64
3. 67
4. 68

**Chapter foundations**

This question belongs to the ideas covered by **Elementary Data Types**. Revise these foundations: Properties of Types and Objects; Scalar and Composite Data Types.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Elementary Data Types questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-3"></a>

### 3. Programming in C (2 questions)

**What to master:** Tokens; Identifiers; Data Types; Sequence Control; Subprogram Control; Arrays; Structures; Unions; Strings; Pointers; Functions; File Handling; Command-Line Arguments; Preprocessors.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 3

*UGC NET Nov 2021, original Q2*

> What does the following function f() in 'C' return? int f(unsigned int N) { unsigned int counter = 0; while(N > 0) { counter += N & 1; N = N >> 1;} return counter == 1;}

**Options**

1. 1 if N is odd, otherwise 0
2. 1 if N is a power of 2, otherwise 0
3. 1 if the binary representation of N is all 1's, otherwise 0
4. 1 if the binary representation of N has any 1's, otherwise 0

**Correct answer**

**Option 2: 1 if N is a power of 2, otherwise 0**

*Verification: Official NTA final key matched by Question ID 2332 and Option ID 9326; independently verified by tracing the bit-count loop.*

**Step-by-step solution**

1. `N & 1` extracts the least-significant bit: it is 1 when that bit is set and 0 otherwise.
2. `N = N >> 1` shifts the next binary bit into the least-significant position. Repeating until `N` becomes zero visits every bit.
3. Therefore `counter` becomes the population count: the number of 1-bits in the original unsigned integer.
4. The return expression is `counter == 1`. A positive unsigned integer has exactly one 1-bit precisely when it is a power of two, so option 2 is correct.

**Why each option is right or wrong**

- **1. N is odd — Incorrect.** Oddness checks only the least-significant bit. For example, 3 is odd but has two 1-bits, so the function returns 0.
- **2. N is a power of 2 — Correct.** Powers of two have binary forms such as `1`, `10`, `100` and contain exactly one set bit.
- **3. All bits are 1 — Incorrect.** Values such as 3 (`11`) and 7 (`111`) have more than one set bit and make `counter == 1` false.
- **4. Any bit is 1 — Incorrect.** That condition would be true for every positive `N`; this function requires exactly one set bit.

**Conceptual lesson**

Bitwise AND with 1 reads the rightmost bit, while a right shift moves through the remaining bits. Together they form the standard bit-by-bit traversal of an unsigned integer.

The loop computes a count, not merely a Boolean test. Always identify the loop invariant: after k iterations, `counter` equals the number of 1-bits removed from the original value, and `N` contains the unprocessed higher bits.

A faster power-of-two test often used in exams is `N != 0 && (N & (N - 1)) == 0`, because subtracting one changes the only set bit and all lower bits. The explicit counting version here is easier to prove by tracing.

**How to solve similar questions**

Trace one example from each option class—such as 8, 7, 3 and 0—in a table with columns for `N`, `N & 1`, and `counter`. Then state the invariant and generalize.

**Verification references**

- [Final-answer-key archive](https://cdnbbsr.s3waas.gov.in/s301eee509ee2f68dc6014898c309e86bf/uploads/2022/04/2022040888.pdf)
- [Independent concept reference](https://www.gnu.org/software/c-intro-and-ref/manual/html_node/Bitwise-Operations.html)

---

#### Question 4

*UGC NET Nov 2021, original Q66*

> Suppose a B tree is used for indexing a database file. Consider the following information: size of the search key field= 10 bytes, block size = 1024 bytes, size of the record pointer= 9 bytes, size of the block pointer= 8 bytes. Let K be the order of internal node and L be the order of leaf node of B tree, then (K, L)=______.

**Options**

1. (57, 53)
2. (50, 52)
3. (60, 64)
4. (34, 31)

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C**. Revise these foundations: Tokens; Identifiers; Data Types; Sequence Control; Subprogram Control; Arrays; Structures; Unions; Strings; Pointers; Functions; File Handling; Command-Line Arguments; Preprocessors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-4"></a>

### 4. Object-Oriented Programming (0 questions)

**What to master:** Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._

<a id="chapter-5"></a>

### 5. Programming in C++ (0 questions)

**What to master:** Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

_No question was confidently routed here in the automated pass; keep the chapter in revision because it is in the official syllabus._

<a id="chapter-6"></a>

### 6. Web Programming (3 questions)

**What to master:** HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 5

*UGC NET Nov 2021, original Q1*

> Which of the statements given below is/are correct? It is always important and useful to include an 'alt' attribute on 'img' tag in HTML because A. users who cannot see the image due to vision impairment can have a textual description of the image (which can be spoken aloud by a screenreader). B. If the image fails to load (slow connection, broken path, etc.) then alt text is displayed instead. C. SEO (Search Engine Optimization) benefits. Choose the correct answer from the options given below:

**Options**

1. A only
2. B and C only
3. C only
4. A, B, and C

**Correct answer**

**Option 4: A, B, and C**

*Verification: Official NTA final key matched by Question ID 2331 and Option ID 9324; independently verified against the HTML standard.*

**Step-by-step solution**

1. Statement A is true: useful alternative text gives a text equivalent when a user cannot perceive the image, including users of screen readers.
2. Statement B is true: when an image cannot be fetched or displayed, user agents can present its alternative text instead.
3. Statement C is true in the intended exam sense: meaningful alternative text helps search systems understand image content and context; it must describe the image rather than repeat keywords artificially.
4. Because A, B and C are all correct, the complete combination is option 4.

**Why each option is right or wrong**

- **1. A only — Incorrect.** Accessibility is a major reason, but it is not the only valid reason; B and C are also true.
- **2. B and C only — Incorrect.** It wrongly excludes the accessibility benefit in A.
- **3. C only — Incorrect.** It wrongly excludes both accessibility and fallback rendering.
- **4. A, B, and C — Correct.** It includes all three valid benefits of meaningful `alt` text.

**Conceptual lesson**

The `alt` attribute supplies a textual replacement for an image. Think of it as content equivalence, not a tooltip. It matters when the visual is unavailable because of disability, a failed request, text-only processing, or automated indexing.

Context determines the value. An informative image needs a concise description of its purpose. A decorative image normally uses an empty value, `alt=""`, so assistive technology can ignore it. An image used as a link or button needs text describing the action.

For statement-combination questions, judge A, B and C independently before looking at the combined options. This prevents one familiar benefit, such as accessibility, from making you select an incomplete combination.

**How to solve similar questions**

Create a small truth table for the labelled statements. Mark each statement true or false from the standard concept, form the set of true labels, and only then match that set to an option.

**Verification references**

- [Final-answer-key archive](https://cdnbbsr.s3waas.gov.in/s301eee509ee2f68dc6014898c309e86bf/uploads/2022/04/2022040888.pdf)
- [Independent concept reference](https://html.spec.whatwg.org/multipage/images.html#alt)

---

#### Question 6

*UGC NET Nov 2021, original Q3*

> Consider the following recursive function F() in Java that takes an integer value and returns a string value: public static String F( int N) { if ( N <= 0) return "‐"; return F(N ‐ 3) + N + F(N ‐ 2) + N; } The value of F(5) is:

**Options**

1. ‐2‐25‐3‐135
2. ‐2‐25‐1‐3‐135
3. ‐1‐145‐2‐245
4. ‐2‐25‐3‐1‐135

**Correct answer**

**Option 4: -2-25-3-1-135**

*Verification: Official NTA final key matched by Question ID 2333 and Option ID 9332; independently verified by expanding the recursion in Java evaluation order.*

**Step-by-step solution**

1. Use the base case first: `F(0)`, `F(-1)` and every non-positive argument return `"-"`.
2. Expand `F(2)`: `F(-1) + 2 + F(0) + 2`, which concatenates to `"-2-2"`.
3. Expand `F(1)` as `"-1-1"`, then `F(3) = F(0) + 3 + F(1) + 3 = "-3-1-13"`.
4. Finally, `F(5) = F(2) + 5 + F(3) + 5 = "-2-25-3-1-135"`, which is option 4.

**Why each option is right or wrong**

- **1. `-2-25-3-135` — Incorrect.** It loses the two recursive `F(1)` contributions inside `F(3)`.
- **2. `-2-25-1-3-135` — Incorrect.** It places the `F(1)` output before the first `3`, contrary to the expression order `F(0) + 3 + F(1) + 3`.
- **3. `-1-145-2-245` — Incorrect.** It does not follow the argument reductions by 3 and 2 from `F(5)`.
- **4. `-2-25-3-1-135` — Correct.** It preserves both the recursive-call order and every appended value.

**Conceptual lesson**

Recursive string questions test both the call tree and concatenation order. The two calls are not interchangeable: the function completely evaluates `F(N-3)`, appends `N`, evaluates `F(N-2)`, and appends `N` again.

When one operand of Java `+` is already a string, later additions in that left-associative chain perform string concatenation. Thus the integers become text rather than being arithmetically added.

Memoizing small values such as `F(1)`, `F(2)` and `F(3)` avoids redrawing repeated subtrees and reduces transcription errors.

**How to solve similar questions**

Write the base values, compute the required smaller calls bottom-up, and keep every intermediate result inside quotation marks. Concatenate strictly from left to right.

**Verification references**

- [Final-answer-key archive](https://cdnbbsr.s3waas.gov.in/s301eee509ee2f68dc6014898c309e86bf/uploads/2022/04/2022040888.pdf)
- [Independent concept reference](https://docs.oracle.com/javase/specs/jls/se17/html/jls-15.html#jls-15.18.1)

---

#### Question 7

*UGC NET Nov 2021, original Q4*

> Match List I with List II List I List II (Programming Term) (Meaning)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** JNDI I. Runtime support for running Java programs
> - **B.** RMI II. The API in support of naming and directory services
> - **C.** JDK III. The methods provided by the Java development kit and runtime support for calling remote methods
> - **D.** JRE IV. The compiler and class libraries to develop Java applications Choose the correct answer from the options given below:

**Options**

1. A ‐ II , B ‐ III, C ‐ IV, D ‐ I
2. A ‐ II, B ‐ IV, C ‐ III, D ‐ I
3. A ‐ I, B ‐ III, C ‐ IV, D ‐ II
4. A ‐ III, B ‐ II, C ‐ IV, D ‐ I

**Correct answer**

**Option 1: A-II, B-III, C-IV, D-I**

*Verification: Official NTA final key matched by Question ID 2334 and Option ID 9333; independently verified from Oracle Java platform definitions.*

**Step-by-step solution**

1. JNDI is the Java Naming and Directory Interface, so A matches II, the API for naming and directory services.
2. RMI means Remote Method Invocation and supplies Java mechanisms for calling methods on remote objects, so B matches III.
3. The JDK is the development kit containing development tools such as the compiler together with libraries, so C matches IV.
4. The JRE supplies the runtime environment needed to run Java programs, so D matches I. The complete mapping is option 1.

**Why each option is right or wrong**

- **1. A-II, B-III, C-IV, D-I — Correct.** Every acronym is paired with its standard role.
- **2. A-II, B-IV, C-III, D-I — Incorrect.** It incorrectly assigns application-development tools to RMI and remote invocation to the JDK.
- **3. A-I, B-III, C-IV, D-II — Incorrect.** It swaps the roles of JNDI and the JRE.
- **4. A-III, B-II, C-IV, D-I — Incorrect.** It swaps JNDI naming services with RMI remote-method services.

**Conceptual lesson**

Separate platform packaging from service APIs. JDK and JRE describe what is installed for development or execution; JNDI and RMI are APIs for particular distributed-programming tasks.

JDK is the broader development package: it includes tools needed to build Java software and the runtime needed to execute it. JRE focuses on execution. Modern Java distributions may package runtimes differently, but this classic distinction is what older UGC NET questions test.

JNDI locates named resources such as directory entries. RMI invokes behaviour on a remote Java object. The mnemonic is N for naming and R for remote.

**How to solve similar questions**

Expand every acronym before matching. Fix the two easiest pairs first—JNDI/naming and RMI/remote invocation—then distinguish development (JDK) from runtime (JRE).

**Verification references**

- [Final-answer-key archive](https://cdnbbsr.s3waas.gov.in/s301eee509ee2f68dc6014898c309e86bf/uploads/2022/04/2022040888.pdf)
- [Independent concept reference](https://docs.oracle.com/javase/8/docs/technotes/guides/jndi/)

<a id="chapter-7"></a>

### 7. Computer Graphics (1 questions)

**What to master:** Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 8

*UGC NET Nov 2021, original Q7*

> Which of the statements given below are correct? The midpoint (or Bresenham) algorithm for rasterizing lines is optimized relative to DDA algorithm in that
>
> **Additional extracted choices — check the source page:**
>
> - **A.** it avoids round‐off operations.
> - **B.** it is incremental.
> - **C.** it uses only integer arithmetic.
> - **D.** all straight lines can be displayed as straight (exact). Choose the correct answer from the options given below:

**Options**

1. A and B only
2. A and C only
3. A, B, C, and D
4. A, B, and C only

**Correct answer**

**Option 4: A, B, and C only**

*Verification: Official NTA final key matched by Question ID 2337 and Option ID 9348; independently verified from the Bresenham line algorithm.*

**Step-by-step solution**

1. A is true: Bresenham chooses the next raster pixel with a decision parameter, avoiding the repeated floating-point rounding used by the basic DDA formulation.
2. B is true: the decision value is updated from the previous step, so the method is incremental.
3. C is true: the standard line algorithm updates the decision parameter using integer addition and subtraction.
4. D is false: a finite square pixel grid cannot represent every mathematical straight line exactly. Therefore A, B and C only are correct, which is option 4.

**Why each option is right or wrong**

- **1. A and B only — Incorrect.** It omits the integer-arithmetic advantage in C.
- **2. A and C only — Incorrect.** It omits the incremental nature in B.
- **3. A, B, C, and D — Incorrect.** D is false because rasterization approximates a continuous line with discrete pixels.
- **4. A, B, and C only — Correct.** These are the three relevant properties; D overclaims exact display.

**Conceptual lesson**

DDA advances using a slope-related real-valued increment and rounds generated coordinates to pixels. Bresenham instead tracks the sign of an integer decision expression to choose between two candidate pixels.

Incremental means the next result is computed cheaply from the current state rather than re-evaluating the line equation from scratch. Both DDA and Bresenham are incremental, but Bresenham's integer decision update is its key optimization.

Raster accuracy means selecting the best discrete approximation. It does not mean that a mathematical line with arbitrary slope becomes an exact continuous straight line on a pixel grid.

**How to solve similar questions**

Evaluate each claimed advantage separately. Reject any statement containing an absolute such as 'all lines exactly' when a continuous object is represented on a discrete raster.

**Verification references**

- [Final-answer-key archive](https://cdnbbsr.s3waas.gov.in/s301eee509ee2f68dc6014898c309e86bf/uploads/2022/04/2022040888.pdf)
- [Independent concept reference](https://doi.org/10.1147/sj.41.0025)

<a id="chapter-8"></a>

### 8. 2-D Geometrical Transforms and Viewing (1 questions)

**What to master:** Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 9

*UGC NET Nov 2021, original Q8*

> What is the transformation matrix M that transforms the square in the xy-plane defined by (1,1)^T, (-1,1)^T, (-1,-1)^T and (1,-1)^T to a parallelogram whose corresponding vertices are (2,1)^T, (0,1)^T, (-2,-1)^T and (0,-1)^T?

**Options**

1. M = [[1,1,0],[0,1,0],[0,0,1]]
2. M = [[1,0,0],[1,1,0],[0,0,1]]
3. M = [[1,1,1],[0,1,0],[0,0,1]]
4. M = [[1,1,0],[1,1,0],[0,0,1]]

**Correct answer**

**Option 1: M = [[1,1,0],[0,1,0],[0,0,1]]**

*Verification: Official NTA final key matched by Question ID 2338 and Option ID 9349; source matrices visually recovered and independently verified on all four vertex pairs.*

**Step-by-step solution**

1. Compare corresponding vertices. Their y-coordinates do not change, so `y'=y`.
2. The target x-values are obtained by adding the source coordinates: `x'=x+y`. For example, `(1,1)` maps to `(2,1)` and `(-1,-1)` maps to `(-2,-1)`.
3. There is no constant translation. In homogeneous column-vector form, `x'=1x+1y+0`, `y'=0x+1y+0`, and the last coordinate stays 1.
4. Thus `M=[[1,1,0],[0,1,0],[0,0,1]]`. Checking the other two vertices gives `(0,1)` and `(0,-1)`, so option 1 is correct.

**Why each option is right or wrong**

- **1. `[[1,1,0],[0,1,0],[0,0,1]]` — Correct.** It implements `x'=x+y` and `y'=y` for every listed pair.
- **2. `[[1,0,0],[1,1,0],[0,0,1]]` — Incorrect.** It implements `x'=x`, `y'=x+y`; `(1,1)` would become `(1,2)`.
- **3. `[[1,1,1],[0,1,0],[0,0,1]]` — Incorrect.** Its extra x-translation gives `(1,1)→(3,1)`.
- **4. `[[1,1,0],[1,1,0],[0,0,1]]` — Incorrect.** It makes both output coordinates `x+y`; `(1,1)` would become `(2,2)`.

**Conceptual lesson**

A 2-D affine transform in homogeneous column-vector form is `[[a,b,tx],[c,d,ty],[0,0,1]]`. The first row determines x, the second determines y, and the last column contains translation.

When point correspondences are supplied, derive coordinate equations before multiplying matrices. Changes shared by every point indicate translation; dependence of one coordinate on another indicates scaling, rotation or shear.

The matrix here is an x-shear: y stays fixed while x changes by an amount proportional to y. Always confirm the candidate on more than one point because a wrong matrix can accidentally map one vertex correctly.

**How to solve similar questions**

Solve `x'=ax+by+tx` and `y'=cx+dy+ty` from corresponding points, build the homogeneous matrix, and verify every listed pair in the stated row- or column-vector convention.

**Verification references**

- [Final-answer-key archive](https://cdnbbsr.s3waas.gov.in/s301eee509ee2f68dc6014898c309e86bf/uploads/2022/04/2022040888.pdf)
- [Independent concept reference](https://www.w3.org/TR/css-transforms-1/#mathematical-description)

<a id="chapter-9"></a>

### 9. 3-D Object Representation, Geometric Transformations and Viewing (8 questions)

**What to master:** Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 10

*UGC NET Nov 2021, original Q9*

> Suppose a Bezier curve P(t) is defined by the four control points P0=(-2,0), P1=(-2,4), P2=(2,4), and P3=(2,0). Which statements are correct? A. Bezier curve P(t) has degree 3. B. P(1/2)=(0,3). C. Bezier curve P(t) may extend outside the convex hull of its control points.

**Options**

1. A and B only
2. A and C only
3. B and C only
4. A, B, and C

**Correct answer**

**Option 1: A and B only**

*Verification: Official NTA final key matched by Question ID 2339 and Option ID 9353; missing source text visually recovered and independently verified from the cubic Bezier equation.*

**Step-by-step solution**

1. A is true: four control points define a Bezier curve of degree at most 3; these control points produce the intended cubic curve.
2. At `t=1/2`, the cubic Bernstein weights are `1/8, 3/8, 3/8, 1/8`.
3. The weighted x-coordinate is `(-2)(1/8+3/8)+(2)(3/8+1/8)=0`; the y-coordinate is `0(1/8)+4(3/8)+4(3/8)+0(1/8)=3`. Therefore B is true.
4. C is false because a Bezier curve lies inside the convex hull of its control points. Hence A and B only are correct, which is option 1.

**Why each option is right or wrong**

- **1. A and B only — Correct.** The curve is cubic and its midpoint parameter evaluates to `(0,3)`, while C is false.
- **2. A and C only — Incorrect.** It rejects the correct midpoint and accepts the false convex-hull claim.
- **3. B and C only — Incorrect.** It omits the correct degree statement and accepts C.
- **4. A, B, and C — Incorrect.** The convex-hull property directly contradicts C.

**Conceptual lesson**

An n-degree Bezier curve normally uses n+1 control points and Bernstein basis polynomials. For four points, `P(t)=(1-t)^3P0+3(1-t)^2tP1+3(1-t)t^2P2+t^3P3`.

The Bernstein weights are nonnegative and sum to 1 for `0≤t≤1`. Therefore every curve point is a convex combination of the controls, which proves the convex-hull property.

Symmetric control points often make `t=1/2` calculations fast: pair equal weights and use coordinate symmetry before doing full arithmetic.

**How to solve similar questions**

Count control points for the degree, write the Bernstein weights at the requested parameter, and remember endpoint interpolation, symmetry and the convex-hull property for eliminating statements.

**Verification references**

- [Final-answer-key archive](https://cdnbbsr.s3waas.gov.in/s301eee509ee2f68dc6014898c309e86bf/uploads/2022/04/2022040888.pdf)
- [Independent concept reference](https://www.w3.org/TR/SVG/paths.html#PathDataCubicBezierCommands)

---

#### Question 11

*UGC NET Nov 2021, original Q10*

> Given below are two statements Statement I: The maximum number of sides that a triangle might have when clipped to a rectangular viewport is 6. Statement II: In 3D graphics, the perspective transformation is nonlinear in z. In light of the above statements, choose the correct answer from the options given below

**Options**

1. Both Statement I and Statement II are true.
2. Both Statement I and Statement II are false
3. Statement I is true but Statement II is false
4. Statement I is false but Statement II is true

**Correct answer**

**Option 4: Statement I is false but Statement II is true**

*Verification: Official NTA final key matched by Question ID 2340 and Option ID 9360; independently verified from convex-polygon clipping and perspective division.*

**Step-by-step solution**

1. Clipping a triangle means intersecting a convex 3-vertex polygon with a convex 4-vertex rectangular window.
2. The intersection can have as many as `3+4=7` boundary vertices. Therefore the claimed maximum of 6 in Statement I is false.
3. Perspective projection uses a homogeneous divide. A depth-related coordinate is divided by a term depending on z, so the final normalized relationship is not linear in z. Statement II is true.
4. The truth pattern is false/true, which corresponds to option 4.

**Why each option is right or wrong**

- **1. Both statements true — Incorrect.** Statement I understates the possible clipped polygon by one side.
- **2. Both statements false — Incorrect.** Statement II correctly identifies the nonlinearity introduced by perspective division.
- **3. I true, II false — Incorrect.** It reverses both truth values.
- **4. I false, II true — Correct.** A clipped triangle can be a heptagon, and perspective depth after division is nonlinear.

**Conceptual lesson**

Polygon clipping produces the geometric intersection of the subject polygon and clip window. New vertices arise where edges cross, and clip-window corners can also become vertices of the result. For convex polygons with m and n vertices, the intersection has at most m+n vertices.

A matrix multiplication in homogeneous coordinates is linear before normalization. Perspective appearance arises after dividing by the homogeneous coordinate; that division makes screen coordinates and normalized depth rational, rather than linear, functions of original depth.

In two-statement questions, determine each truth value independently. Do not let a familiar true statement about perspective make the less familiar clipping bound seem true.

**How to solve similar questions**

For clipping bounds, count possible boundary contributions from both convex polygons. For perspective questions, separate the homogeneous matrix step from the nonlinear divide that produces Cartesian coordinates.

**Verification references**

- [Final-answer-key archive](https://cdnbbsr.s3waas.gov.in/s301eee509ee2f68dc6014898c309e86bf/uploads/2022/04/2022040888.pdf)
- [Independent concept reference](https://doi.org/10.1145/360767.360802)
- [Additional verification source](https://www.w3.org/TR/css-transforms-2/#perspective-matrix-computation)

---

#### Question 12

*UGC NET Nov 2021, original Q21*

> A only 2. A and B only 3. B and C only 4. A and C only

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 13

*UGC NET Nov 2021, original Q27*

> A and B only 2. B and C only 3. A only 4. B only

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 14

*UGC NET Nov 2021, original Q28*

> Match List I with List II n List I List II Identity Name
>
> **Additional extracted choices — check the source page:**
>
> - **A.** x + x =x I. Identity Law
> - **B.** x + 0 = x II. Absorption Law
> - **C.** x +1 = 1 III. Idempotent law
> - **D.** x + xy = x IV. Domination Law Choose the correct answer from the options given below:

**Options**

1. A ‐ III, B ‐I , C ‐ II, D ‐ IV
2. A ‐ I, B ‐III , C ‐ IV, D ‐ II
3. A ‐ III, B ‐I , C ‐ IV, D ‐ II
4. A ‐ III, B ‐IV , C ‐ I, D ‐ II

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 15

*UGC NET Nov 2021, original Q38*

> A ‐ III, B ‐I , C ‐ IV, D ‐ II 2. A ‐ III, B ‐II , C ‐ I, D ‐ IV 3. A ‐ III, B ‐IV, C ‐ I, D ‐ II 4. A ‐ IV, B ‐III , C ‐ I, D ‐ II

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 16

*UGC NET Nov 2021, original Q45*

> Consider the following graph. * * * * * * * * * * * * 0 1 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1 1 1 1 1 2 a b + a b + b a + R + a b + Among the following sequences I. a b e g h f II. a b f e h g III. a b f h g e IV. a f g h b e Which are depth first traversals of the above graph?

**Options**

1. I, II, and IV only
2. I and IV only
3. II, III, and IV only
4. I, III, and IV only

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 17

*UGC NET Nov 2021, original Q81*

> Match List I with List II List I List II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Odd Function I. NAND gate
> - **B.** Universal Gate II. XOR gate
> - **C.** 2421 code III. Amplification
> - **D.** Buffer IV. Self‐Complementing Choose the correct answer from the options given below:

**Options**

1. A ‐ I, B ‐ II, C ‐ III, D ‐ IV
2. A ‐ II, B ‐ I, C ‐ IV, D ‐ III
3. A ‐ I, B ‐ III, C ‐ II, D ‐ IV
4. A ‐ IV, B ‐ II, C ‐ III, D ‐ I

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

## Coverage and quality notes

- Recovered question blocks in this unit: **17**
- Chapter placements with direct keyword support: **11**
- Chapter placements needing manual review: **6**
- Questions with validated answers in this guide: **9**
- OCR may flatten mathematical notation, tables, code indentation, and figures. Full audit references are retained in the structured data.
- Some combined Paper 1/Paper 2 scans and older papers lack a trustworthy embedded key. Such questions remain pending rather than receiving guessed answers.

---

[Back to contents](#contents) · [All units](README.md) · [Project home](../README.md)

