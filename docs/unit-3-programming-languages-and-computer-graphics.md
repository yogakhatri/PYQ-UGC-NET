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

This guide contains all **189 question blocks currently recoverable and assigned to Unit 3** from the local UGC NET archive. Questions are arranged chapter-wise and numbered continuously through the unit.

> [!WARNING]
> This is a working extraction inventory, not a complete solved guide. **12 answers are validated and 177 remain pending** in this unit. Some unit and chapter placements use fallback routing, and OCR or missing figures can make questions incomplete.

Use this file for question discovery and broad chapter revision. The chapter notes and exam methods are general, not question-specific solutions. Full source paths, PDF pages and classification states remain in the structured data for auditing.

## Unit-wide exam playbook

- **Core idea:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.
- **Method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.
- **Rules/formulas:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.
- **Frequent traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

## Chapter-wise concepts and PYQs

<a id="chapter-1"></a>

### 1. Language Design and Translation Issues (22 questions)

**What to master:** Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 1

*UGC NET June 2012, Paper II, original Q25*

> Which of the following metric does not depend on the programming language used ?

**Options**

- **A.** Line of code
- **B.** Function count
- **C.** Member of token
- **D.** All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 2

*UGC NET Dec 2013, Paper II, original Q8*

> If you write your Name, Roll Number, Phone Number or put any mark on any part of the OMR Sheet, except for the space allotted for the relevant entries, which may disclose your identity, or use abusive language or employ any other unfair means such as change of response by scratching or using white fluid, you will render yourself liable to disqualification.

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 3

*UGC NET Dec 2013, Paper III, original Q8*

> If you write your Name, Roll Number, Phone Number or put any mark on any part of the OMR Sheet, except for the space allotted for the relevant entries, which may disclose your identity, or use abusive language or employ any other unfair means such as change of response by scratching or using white fluid, you will render yourself liable to disqualification.

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 4

*UGC NET June 2013, Paper III, original Q50*

> What will be the output of the following segment of the program ? main( ) { char *s = “hello world”; int i = 7; printf(“%, *s”, i, s); }

**Options**

- **A.** Syntax error
- **B.** hello w
- **C.** hello
- **D.** o world

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 5

*UGC NET June 2013, Paper III, original Q51*

> Trace the error : void main( ) { int *b, &a; *b = 20 printf(“%d, %d”, a, *b) }

**Options**

- **A.** No error
- **B.** Logical error
- **C.** Syntax error
- **D.** Semantic error

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 6

*UGC NET Dec 2014, Paper II, original Q8*

> If you write your Name, Roll Number, Phone Number or put any mark on any part of the OMR Sheet, except for the space allotted for the relevant entries, which may disclose your identity, or use abusive language or employ any other unfair means such as change of response by scratching or using white fluid, you will render yourself liable to disqualification.

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 7

*UGC NET Dec 2014, Paper III, original Q41*

> What is true about UML stereotypes ?

**Options**

- **A.** Stereotype is used for extending the UML language.
- **B.** Stereotyped class must be abstract
- **C.** The stereotype indicates that the UML element cannot be changed
- **D.** UML profiles can be stereotyped for backward compatibility

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 8

*UGC NET Dec 2015, Paper II, original Q8*

> If you write your Name, Roll Number, Phone Number or put any mark on any part of the OMR Sheet, except for the space allotted for the relevant entries, which may disclose your identity, or use abusive language or employ any other unfair means, such as change of response by scratching or white fluid, you will render yourself liable to You have to return the original OMR Sheet to the invigilators carry it with you outside the Examination Hall. You are at the end of the examination compulsorily and must not however, allowed to carry original question booklet and duplicate copy of OMR Sheet on conclusion of examination.

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 9

*UGC NET Dec 2015, Paper III, original Q8*

> If you write your Name, Roll Number, Phone Number or space allotted for the relevant entries, which may disclose put any mark on any part of the OMR Sheet, except for the your identity, or use abusive language or employ any other unfair means, such as change of response by scratching or disqualification. using white fluid, you will render yourself liable to You have to return the original OMR Sheet to the invigilators carry it with you outside the Examination Hall. You are at the end of the examination compulsorily and must not however, allowed to carry original question booklet and duplicate copy of OMR Sheet on conclusion of examination.

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 10

*UGC NET June 2015, Paper II, original Q8*

> If you write your Name, Roll Number, Phone Number or put any mark on any part of the OMR Sheet, except for the your identity, or use abusive language or employ any other space allotted for the relevant entries, which may disclose unfair means, such as change of response by scratching or white fluid, you will render yourself liable to You have to return the original OMR Sheet to the invigilators carry it with you outside the Examination Hall. You are at the end of the examination compulsorily and must not however, allowed to carry original question booklet and duplicate copy of OMR Sheet on conclusion of examination.

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 11

*UGC NET June 2015, Paper II, original Q11*

> What is the output of the following program? (Assume that the appropriate preprocessor directives are included and there is no syntax error) main () char S[ ]="ABCDEFGH"; printf (%C", * (& S[3])); printf ('%s", S+ 4); printf ("% u", S); /* Base address of S is 1000 */

**Options**

1. ABCDEFGH1000
2. CDEFGH1000
3. DDEFGHH1000
4. DEFGH1000

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 12

*UGC NET June 2015, Paper III, original Q42*

> Module design is used to maximize cohesion and minimize coupling. Which of the following is the key to implement this rule?

**Options**

1. Inheritance
2. Polymorphism
3. Encapsulation
4. Abstraction

**Correct answer**

**Option 3: Encapsulation**

*Verification: Final CBSE key matched through an archived transcription; independently verified from the information-hiding effect of encapsulation.*

**Step-by-step solution**

1. High cohesion means the responsibilities inside one module strongly belong together. Low coupling means a module depends as little as possible on other modules' internal details.
2. Encapsulation bundles related state and behaviour behind a controlled interface and hides the internal representation.
3. Bundling related responsibilities supports cohesion; hiding representation means clients depend on the interface instead of implementation details, which reduces coupling.
4. Therefore encapsulation is the option that most directly implements the stated module-design rule, so option 3 is correct.

**Why each option is right or wrong**

- **1. Inheritance — Incorrect.** Inheritance supports reuse and specialization, but it creates a dependency between subclass and superclass and does not by itself guarantee high cohesion or low coupling.
- **2. Polymorphism — Incorrect.** Polymorphism lets one interface represent several implementations and can reduce conditional logic, but it is not the primary rule that hides a module's internals.
- **3. Encapsulation — Correct.** It groups related data and operations and restricts access through a stable interface. This directly supports information hiding, high cohesion and low coupling.
- **4. Abstraction — Incorrect for this key.** Abstraction presents essential behaviour while suppressing unnecessary detail, so it also helps modular design. However, the implementation mechanism emphasized by the question is encapsulation: placing state and behaviour inside a boundary and controlling access.

**Conceptual lesson**

Cohesion looks inside a module: do its elements work toward one focused purpose? Higher cohesion is better. Coupling looks between modules: how much knowledge or dependency crosses their boundaries? Lower coupling is better.

Abstraction answers 'what service is offered?' Encapsulation answers 'where are the state and implementation kept, and who may access them?' They cooperate: abstraction gives a small interface; encapsulation protects the implementation behind it.

A useful design test is change impact. If a module's internal representation changes, well-encapsulated clients should not need changes. That limited ripple effect is evidence of low coupling. If the module contains only responsibilities needed for its single purpose, that is evidence of high cohesion.

**How to solve similar questions**

For exam questions, evaluate cohesion within a module and coupling across modules. Choose information hiding or encapsulation when the wording stresses controlled access, hiding implementation, or preventing ripple effects. Choose abstraction when it stresses essential features, a simplified view, or what an interface promises.

**Verification references**

- [Final-answer-key archive](https://www.cbse-net.in/2015/08/net-answer-key-of-computer-science-june-2015.html)
- [Independent concept reference](https://docs.oracle.com/javase/tutorial/java/concepts/object.html)

---

#### Question 13

*UGC NET July 2016, Paper II, original Q8*

> If you write your Name, Roll Number, Phone Number or put any mark on any part of the OMR Sheet, except for the space allotted for the relevant entries, which may disclose your identity, or use abusive language or employ any other unfair means, such as change of response by scratching or using white fluid, you will render yourself liable to disqualification.

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 14

*UGC NET July 2016, Paper III, original Q8*

> If you write your Name, Roll Number, Phone Number or put any mark on any part of the OMR Sheet, except for the space allotted for the relevant entries, which may disclose your identity, or use abusive language or employ any other unfair means, such as change of response by scratching or using white fluid, you will render yourself liable to disqualification.

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 15

*UGC NET Jan 2017, Paper II, original Q8*

> If you write your Name, Roll Number, Phone Number or put any mark on any part of the OMR Sheet, except for the space allotted for the relevant entries, which may disclose your identity, or use abusive language or employ any other unfair means, such as change of response by scratching or using white fluid, you will render yourself liable to disqualification.

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 16

*UGC NET Jan 2017, Paper III, original Q8*

> If you write your Name, Roll Number, Phone Number or put any mark on any part of the OMR Sheet, except for the space allotted for the relevant entries, which may disclose your identity, or use abusive language or employ any other unfair means, such as change of response by scratching or using white fluid, you will render yourself liable to disqualification.

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 17

*UGC NET Nov 2017, Paper II, original Q8*

> If you write your Name, Roll Number, Phone Number or put any mark on any part of the OMR Sheet, except for the space allotted for the relevant entries, which may disclos e your identity, or use abusive language or employ any other unfair means, such as change of response by scratching or using white fluid, you will render yourself liable to disqualification.

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 18

*UGC NET July 2018, Paper II, original Q7*

> Which of the following statements is/are True ? P : C programming language has a weak type system with static types. Q : Java programming language has a strong type system with static ty pes.

**Options**

1. P only
2. Q only
3. Both P and Q
4. Neither P nor Q

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 19

*UGC NET July 2018, Paper II, original Q8*

> If you write your Name, Roll Number, Phone Number or put any mark on any part of the OMR Sheet, except for the space allotted for the relevant entries, which may disclos e your identity, or use abusive language or employ any other unfair means, such as change of response by scratching or using white fluid, you will render yourself liable to disqualification.

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 20

*UGC NET Dec 2019, original Q122*

> Which of the following are legal statements in C programming language?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** int *P=&44:
> - **B.** int * P = &r: ional
> - **C.** int P= &a: 'our Pers
> - **D.** int P= a: Choose the correct

**Options**

1. (a) and b)
2. (b) and (c)
3. (b) and (d)
4. (a) and (d) 61547541186.2 61547541187.3 61547541188.4 Single Line Ouestion Ontion : No

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 21

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

---

#### Question 22

*UGC NET Aug 2024, original Q58*

> Consider the function in C code: Cal(a, b) ( if (b! = 1) / if (a ! = 1) | printf("*"); Cal(a/ 2, b); else ( b=b-1; Cal (10, b); How many times * is going to be printed, if the function is called with Cal(10, 10); ? 1) 25 (2) 23 (3) 24 (4) 27

**Chapter foundations**

This question belongs to the ideas covered by **Language Design and Translation Issues**. Revise these foundations: Programming-Language Concepts, Paradigms and Models; Programming Environments; Virtual Computers and Binding Times; Programming-Language Syntax; Stages in Translation; Formal Transition Models.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Language Design and Translation Issues questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-2"></a>

### 2. Elementary Data Types (6 questions)

**What to master:** Properties of Types and Objects; Scalar and Composite Data Types.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 23

*UGC NET Dec 2009, Paper II, original Q14*

> Encapsulation is

**Options**

- **A.** Dynamic binding
- **B.** A mechanism to associate the code and data.
- **C.** Data abstraction
- **D.** Creating new class

**Chapter foundations**

This question belongs to the ideas covered by **Elementary Data Types**. Revise these foundations: Properties of Types and Objects; Scalar and Composite Data Types.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Elementary Data Types questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 24

*UGC NET June 2010, Paper II, original Q15*

> The data type created by the data abstraction process is called

**Options**

- **A.** class
- **B.** structure
- **C.** abstract data type
- **D.** user defined data type

**Chapter foundations**

This question belongs to the ideas covered by **Elementary Data Types**. Revise these foundations: Properties of Types and Objects; Scalar and Composite Data Types.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Elementary Data Types questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 25

*UGC NET Dec 2013, Paper III, original Q14*

> Which of the following concepts means adding new concepts to a program as it runs ?

**Options**

- **A.** Data hiding
- **B.** Dynamic loading
- **C.** Dynamic typing
- **D.** Dynamic binding

**Chapter foundations**

This question belongs to the ideas covered by **Elementary Data Types**. Revise these foundations: Properties of Types and Objects; Scalar and Composite Data Types.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Elementary Data Types questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 26

*UGC NET June 2015, Paper II, original Q12*

> Which of the following, in Ct+, is inherited in a derived class from base class ? (1) constructor 2) destructor (3) data members (4) virtual methods

**Chapter foundations**

This question belongs to the ideas covered by **Elementary Data Types**. Revise these foundations: Properties of Types and Objects; Scalar and Composite Data Types.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Elementary Data Types questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 27

*UGC NET Nov 2020, original Q61*

> Suppose you are compiling on a machine with 1-byte chars, 2-byte shorts, 4-byte ints, and S-byte doubles, and with alignment rules that require the address of every primitive data element to be an integer multiple of the element's size. Suppose further that the compiler is not permitted to reorder fields; padding is used to ensure alignment. How much space will be consumed by the following array? struct ( short s; char c: short ti chard: double r: int i: ) A[10]: /*10 element array of structs*/

**Options**

1. 150 bytes
2. 320 bytes
3. 240 bytes
4. 200 bytes 53622816742. 2 53622816743.3 53622816744.4

**Chapter foundations**

This question belongs to the ideas covered by **Elementary Data Types**. Revise these foundations: Properties of Types and Objects; Scalar and Composite Data Types.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Elementary Data Types questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 28

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

### 3. Programming in C (7 questions)

**What to master:** Tokens; Identifiers; Data Types; Sequence Control; Subprogram Control; Arrays; Structures; Unions; Strings; Pointers; Functions; File Handling; Command-Line Arguments; Preprocessors.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 29

*UGC NET Dec 2009, Paper II, original Q12*

> What would be the output of the following program, if run from the command line as “myprog 1 2 3” ? main (int argc, char ∗ argv[ ]) { int i ; i = argv[1] + argv[2] + argv[3] ; printf (“% d”, i) ; }

**Options**

- **A.** 123
- **B.** 6
- **C.** Error
- **D.** “123”

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C**. Revise these foundations: Tokens; Identifiers; Data Types; Sequence Control; Subprogram Control; Arrays; Structures; Unions; Strings; Pointers; Functions; File Handling; Command-Line Arguments; Preprocessors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 30

*UGC NET June 2012, Paper II, original Q26*

> A / B + tree index is to be built on the name attribute of the relation STUDENT. Assume that all students names are of length 8 bytes, disk block are of size 512 bytes and index pointers are of size 4 bytes. Given this scenario what would be the best choice of the degree (i.e. the number of pointers per node) of the B + tree ?

**Options**

- **A.** 16
- **B.** 42
- **C.** 43
- **D.** 44 www.solutionsadda.in

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C**. Revise these foundations: Tokens; Identifiers; Data Types; Sequence Control; Subprogram Control; Arrays; Structures; Unions; Strings; Pointers; Functions; File Handling; Command-Line Arguments; Preprocessors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 31

*UGC NET Dec 2013, Paper II, original Q16*

> What does the following declaration mean ? int (*ptr) [10];

**Options**

- **A.** ptr is an array of pointers of 10 integers.
- **B.** ptr is a pointer to an array of 10 integers.
- **C.** ptr is an array of 10 integers.
- **D.** none of the above.

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C**. Revise these foundations: Tokens; Identifiers; Data Types; Sequence Control; Subprogram Control; Arrays; Structures; Unions; Strings; Pointers; Functions; File Handling; Command-Line Arguments; Preprocessors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 32

*UGC NET Dec 2014, Paper II, original Q12*

> What does the following expression means ? char ∗(∗(∗ a[N]) ( )) ( );

**Options**

- **A.** a pointer to a function returning array of n pointers to function returning character pointers.
- **B.** a function return array of N pointers to functions returning pointers to charact ers
- **C.** an array of n pointers to function returning pointers to characters
- **D.** an array of n pointers to function returning pointers to functions returning pointe rs to characters.

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C**. Revise these foundations: Tokens; Identifiers; Data Types; Sequence Control; Subprogram Control; Arrays; Structures; Unions; Strings; Pointers; Functions; File Handling; Command-Line Arguments; Preprocessors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 33

*UGC NET July 2016, Paper II, original Q12*

> The following statement in ‘C’ int (*f())[ ]; declares

**Options**

1. a function returning a point er to an array of integers.
2. a function returning an ar ray of pointers to integers.
3. array of functions retu rning pointers to integers.
4. an illegal statement.

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C**. Revise these foundations: Tokens; Identifiers; Data Types; Sequence Control; Subprogram Control; Arrays; Structures; Unions; Strings; Pointers; Functions; File Handling; Command-Line Arguments; Preprocessors.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 34

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

#### Question 35

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

### 4. Object-Oriented Programming (24 questions)

**What to master:** Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 36

*UGC NET Dec 2009, Paper II, original Q13*

> A __________ is a special method used to initialize the instance v ariable of a class.

**Options**

- **A.** Member function
- **B.** Destructor
- **C.** Constructor
- **D.** Structure

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 37

*UGC NET June 2010, Paper II, original Q13*

> Member of a class specified as _______ are accessible only to method of the class.

**Options**

- **A.** private
- **B.** public
- **C.** protected
- **D.** derive

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 38

*UGC NET Dec 2013, Paper III, original Q10*

> Match the following with respect to relationship between objects and classes : List – I List – II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** State diagram i. Useful for both abstract modelling and for designing actual program
> - **B.** Object diagram ii. Describes object classes
> - **C.** Class diagram iii. Useful for documenting test cases
> - **D.** Instance diagram iv. Describing the behaviour of a single class of objects. Codes : a b c d

**Options**

- **A.** iv i ii iii
- **B.** ii iii iv i
- **C.** iii iv ii i
- **D.** ii iv i iii

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 39

*UGC NET Dec 2013, Paper III, original Q44*

> In IPV 4, the IP address 200.200.200.200 belongs to

**Options**

- **A.** Class A
- **B.** Class B
- **C.** Class C
- **D.** Class D

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 40

*UGC NET June 2013, Paper III, original Q26*

> An actor in an animation is a small program invoked _______ per frame to determine the ch aracteristics of some object in the animation.

**Options**

- **A.** once
- **B.** twice
- **C.** 30 times
- **D.** 60 times

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 41

*UGC NET Dec 2015, Paper III, original Q1*

> Pickinpiboth perata and attributes with operations (b) Inheritance i Hiding implementation details of methods from users of (c) Encapsulation (iii) Using similar operations to do similar things (d) Abstraction (iv) Create new classes from existing class Codes:
>
> **Additional extracted choices — check the source page:**
>
> - **A.** _Missing in extracted text_
> - **B.** _Missing in extracted text_
> - **C.** _Missing in extracted text_
> - **D.** _Missing in extracted text_

**Options**

1. (iv) (iti) (i) (i)
2. (iii) (iv) (i) (i)
3. (iii) (i) (ii) (iv)
4. (iv) (iii) (ii) (i) D-8715 6 Paper-III

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 42

*UGC NET Dec 2015, Paper III, original Q2*

> Making atleast one member function as virtual function (3) Declaring as Abstract class using virtual keyword (4) Declaring as Abstract class using static keyword

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 43

*UGC NET Dec 2015, Paper III, original Q29*

> Which of the following is used to make an Abstract class ? (1) Making atleast one member function as pure virtual function

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 44

*UGC NET Dec 2015, Paper III, original Q30*

> Match the following with reference to object oriented modelling: List - I List - II (a) Polymorphism

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 45

*UGC NET Dec 2015, Paper III, original Q36*

> Which of the following is/ are correct with reference to Abstract class and interface ? A class can inherit only one Abstract class but may inherit several interfaces. (b) An Abstract class can provide complete and default code but an interface has no code. Codes :

**Options**

1. (a) is true
2. (b) is true
3. Both (a) and (b) are true
4. Neither (a) nor (b) is true D-8715 7 Paper-IlI

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 46

*UGC NET Dec 2015, Paper III, original Q46*

> Lan age mondal used in MiSt is Logic programming (3) Object oriented programming (4) All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 47

*UGC NET July 2016, Paper III, original Q37*

> Implicit return type of a class constructor is :

**Options**

1. not of class type its elf
2. class type itself
3. a destructor of class type
4. a destructor not of class type

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 48

*UGC NET July 2016, Paper III, original Q40*

> Which of the following statements is correct ?

**Options**

1. Every class containi ng abstract method must not be declared abstract.
2. Abstract class cannot be direc tly initiated with ‘new’ operator.
3. Abstract class cannot be initiated.
4. Abstract class contains definition of implementation.

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 49

*UGC NET July 2016, Paper III, original Q42*

> When one object reference vari able is assigned to another object reference variable then

**Options**

1. a copy of the object is created.
2. a copy of the reference is created.
3. a copy of the reference is not created.
4. it is illegal to assign one object refe rence variable to another object reference variable.

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 50

*UGC NET Jan 2017, Paper III, original Q14*

> A segment is any object described by GKS co mmands and data that start with CREATE SEGMENT and Terminates with CLOSE SE GMENT command. What functions can be performed on these segments ?

**Options**

1. Translation and Rotation
2. Panning and Zooming
3. Scaling and Shearing
4. Translation, Rotation, Panning and Zooming

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 51

*UGC NET Jan 2017, Paper III, original Q37*

> Abstraction and encapsulation are fundamental principles that underlie the object oriented approach to software development. What can you say about the following two statements ? I. Abstraction allows us to focus on what something does without considering the complexities of how it works. II. Encapsulation allows us to consider co mplex ideas while ignoring irrelevant detail that would confuse us.

**Options**

1. Neither I nor II is correct.
2. Both I and II are correct.
3. Only II is correct.
4. Only I is correct.

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 52

*UGC NET Nov 2017, Paper II, original Q13*

> A member function can always access the data in __________ , (in C++) .

**Options**

1. the class of which it is member
2. the object of which it is a member
3. the public part of its class
4. the private part of its class

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 53

*UGC NET Dec 2019, original Q65*

> Let A be the base class in C++ and B be the derived class from A with protected inheritance. Which of the following statement is false for class B?

**Options**

1. Member function of class B can access protected data of class A
2. Member function of Class B can access public data of class A
3. Member function of class B cannot access private data of class A
4. Object of derived class B can access public base class data 61547540958.2 61547540959. 3 61547540960.4

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 54

*UGC NET Dec 2019, original Q121*

> Which of the following statements are true regarding C++?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Overloading gives the capability to an existing operator to operate on other data types.
> - **B.** Inheritance in object oriented programming provides support to reusability.
> - **C.** When object of a derived class is defined, first the constructor of derived class is executed then constructor of a base class is executed.
> - **D.** Overloading is a type of polymorphism. Choose the correct option from those given below :

**Options**

1. (a) and (b) only
2. (a). (b) and (c) only
3. (a), (b) and (d) only
4. (b), (c) and (d) only 61547541182.2 61547541183.3 61547541184.4

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 55

*UGC NET Aug 2024, original Q129*

> Match List - I with List - II. List - I List - Il (IP Address) (Class)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** 10.20.30.40 (1) Class E
> - **B.** 210.20.30.3 (II) Class B
> - **C.** 180.30.100.10 (III) Class A
> - **D.** 252.5.15.11 (IV) Class C Choose the correct answer from the options given below : (1)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(LI),
> - **B.** -(III),
> - **C.** -(L),
> - **D.** -(IV) (2)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(I),
> - **B.** -(IV),
> - **C.** -(I),
> - **D.** -(III) (3)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(I),
> - **B.** -(II),
> - **C.** -(IV),
> - **D.** -(II) (4)

**Options**

- **A.** -(III),
- **B.** -(IV),
- **C.** -(IL),
- **D.** -(t) ComE are 2 - 2ng Meals 10

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 56

*UGC NET June 2024, original Q51*

> Which of the following is not an object Oriented Programming language?

**Options**

1. Pearl
2. Python
3. Smail talk
4. SOL Plus

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 57

*UGC NET Dec 2025 session (Jan 2026), original Q62*

> Question Number : 62

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 58

*UGC NET Dec 2025 session (Jan 2026), original Q64*

> Question Number : 64

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 59

*UGC NET Dec 2025 session (Jan 2026), original Q67*

> Question Number : 67

**Chapter foundations**

This question belongs to the ideas covered by **Object-Oriented Programming**. Revise these foundations: Class; Object; Instantiation; Inheritance; Encapsulation; Abstract Class; Polymorphism.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Object-Oriented Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-5"></a>

### 5. Programming in C++ (27 questions)

**What to master:** Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 60

*UGC NET Dec 2009, Paper II, original Q15*

> Which of the statements are true ? I. Function overloading is done at compile time. II. Protected members are accessible to the member of derived class. III. A derived class inherits constructors and destructors. IV. A friend function can be called like a normal function. V. Nested class is a derived class.

**Options**

- **A.** I, II, III
- **B.** II, III, V
- **C.** III, IV, V
- **D.** I , II, IV

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 61

*UGC NET Dec 2012, Paper II, original Q29*

> Which of the following are two special functions that are meant for handling exception, that occur during exception handling itself? d
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Void terminate ( ) and Void g m unexpected ()
> - **B.** Non void terminate () and void Using the property of eccentricity of a unexpected () vertex, find every vertex that is the
> - **C.** Void terminate () and non void centre of the given tree. unexpected () (A) d & h
> - **D.** Non void terminate ( ) and non (B) c&k void unexpected () (C) g, b, c, h, i, m (D) c & h

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 62

*UGC NET Dec 2013, Paper II, original Q18*

> Which of the following operators can not be overloaded in C+ + ?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** ∗
> - **B.** + =
> - **C.** = =
> - **D.** : : 19. _________ allows to create classes which are derived from other classes, so that they automatically include some of its “parent’s” members, plus its own members.

**Options**

- **A.** Overloading
- **B.** Inheritance
- **C.** Polymorphism
- **D.** Encapsulation

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 63

*UGC NET Dec 2013, Paper III, original Q15*

> Which of the following correctly describes overloading of functions ?

**Options**

- **A.** Virtual polymorphism
- **B.** Transient polymorphism
- **C.** Ad-hoc polymorphism
- **D.** Pseudo polymorphism

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 64

*UGC NET Dec 2013, Paper III, original Q18*

> C++ actually supports the following two complete dynamic systems :

**Options**

- **A.** One defined by C++ and the other not defined by C.
- **B.** One defined by C and one specific to C++
- **C.** Both are specific to C++
- **D.** Both of them are improvements of C

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 65

*UGC NET Dec 2013, Paper III, original Q19*

> Important advantage of using new and delete operators in C++ is

**Options**

- **A.** Allocation of memory
- **B.** Frees the memory previously allocated
- **C.** Initialization of memory easily
- **D.** Allocation of memory and frees the memory previously allocated.

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 66

*UGC NET Dec 2014, Paper II, original Q13*

> Which of the following is not a member of class ?

**Options**

- **A.** Static function
- **B.** Friend function
- **C.** Const function
- **D.** Virtual function

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 67

*UGC NET Dec 2015, Paper II, original Q12*

> Consider the following two statements: (a) A publicly derived class is a subtype of its base class. (b) Inheritance provides for code reuse. Which one of the following statements is correct ?

**Options**

1. Both the statements (a) and (b) are correct.
2. Neither of the statements (a) and (b) are correct.
3. Statement (a) is correct and (b) is incorrect.
4. Statement (a) is incorrect and (b) is correct. D-8715 4 Paper-ll

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 68

*UGC NET June 2015, Paper II, original Q14*

> Which of the following is incorrect in C++?

**Options**

1. When we write overloaded function we must code the function for each usage.
2. When we write function template we code the function only once.
3. It is difficult to debug macros
4. Templates are more efficient than macros When the inheritance is private, the private methods in base class are in the derived class (in C++). (1) inaccessible 2) accessible (3) protected (4) public J-8715 4 Paper-Il

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 69

*UGC NET July 2016, Paper III, original Q19*

> Given the following statements : (A) To implement Abstract Data Type, a programming language require a syntactic unit to encapsulate type definition. (B) To implement ADT, a programming language requires some primitive operations that are built in the language processor. (C) C++, Ada, Java 5.0, C #2005 provide support for parameterised ADT. Which one of the following options is correct ?

**Options**

1. (A), (B) and (C) are false.
2. (A) and (B) are true; (C) is false.
3. (A) is true; (B) and (C) are false.
4. (A), (B) and (C) are true.

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 70

*UGC NET July 2016, Paper III, original Q38*

> It is possible to define a cl ass within a class termed as ne sted class. There are _____ types of nested classes.

**Options**

1. 2
2. 3
3. 4
4. 5

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 71

*UGC NET Jan 2017, Paper II, original Q11*

> Which of the following cannot be passed to a function in C++ ?

**Options**

1. Constant
2. Structure
3. Array
4. Header file

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 72

*UGC NET Jan 2017, Paper II, original Q13*

> Which of the following storage classes have global visibility in C/C++ ?

**Options**

1. Auto
2. Extern
3. Static
4. Register

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 73

*UGC NET Jan 2017, Paper II, original Q14*

> Which of the following operators cannot be overloaded in C/C++ ?

**Options**

1. Bitwise right shift assignment
2. Address of
3. Indirection
4. Structure reference

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 74

*UGC NET Jan 2017, Paper III, original Q40*

> Which of the following statement(s) with regard to an abstract class in JAVA is/are TRUE ? I. An abstract class is one that is not used to create objects. II. An abstract class is designed only to act as a base class to be inherited by other classes.

**Options**

1. Only I
2. Only II
3. Neither I nor II
4. Both I and II

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 75

*UGC NET Nov 2017, Paper II, original Q12*

> The associativity of which of the following operators is Left to Right, in C++ ?

**Options**

1. Unary Operator
2. Logical not
3. Array element access
4. addressof

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 76

*UGC NET Nov 2017, Paper II, original Q14*

> Which of the following is not correct for virtual function in C++ ?

**Options**

1. Must be declared in public section of class.
2. Virtual function can be static.
3. Virtual function should be accessed using pointers.
4. Virtual function is defined in base class.

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 77

*UGC NET Nov 2017, Paper II, original Q15*

> Which of the following is not correct (in C++) ?

**Options**

1. Class templates and function templates are instantiated in the same wa y.
2. Class templates differ from function templates in the way they are initi ated.
3. Class template is initiated by defining an object using the template ar gument.
4. Class templates are generally used for storage classes.

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 78

*UGC NET Nov 2017, Paper II, original Q16*

> Which of the following is/are true with reference to ‘view’ in DBMS ? (a) A ‘view’ is a special stored procedure executed when certain event occurs. (b) A ‘view’ is a virtual table, which occurs after executing a pre-compi led query.

**Options**

1. Only (a) is true
2. Only (b) is true
3. Both (a) and (b) are true
4. Neither (a) nor (b) are true

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 79

*UGC NET Dec 2018, original Q97*

> Consider the following two C++ programs P1 and P2 and two statements S1 and S2 about these programs : P1 P2 void f (int a, int b, int &e) double a = 1, b = 2; | a = 1; double &f(double &d) *b = 2; { d = 1; Exam Guide C = 3; return b; int main() int main ( / int i = 0; fli, &i, i); f(a) = 5; cout << 1; cout << a <<"." << b; S1: P1 prints out 3 S2: P2 prints out 4: 2 What can you say about the statements S1 and S2? Code: . Only S1 is true. Only S2 is true. 91394342386. 91394342387. Both S1 and S2 are true. 91394342388 Neither S1 nor S2 is true. Single Dine Question pion No digion Orient on: Ventype: MCQ Option Shufling : Yes

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 80

*UGC NET Dec 2018, original Q101*

> Consider the C/C++ function f0 given below : 'our . void f(char wl) int x = strlen(w); //length of a string char c; for (int i = 0; i < x; i++) c = w[i]; w[i] = w[x-i-1); w[x-i-1) = c; Which of the following is the purpose of fl)? . It outputs the contents of the array in reverse order. 91394342402. It outputs the contents of the array in the original order. 91394342403. It outputs the contents of the array with the characters shifted over by one position. It outputs the contents of the array with the characters rearranged so they are no longer recognized as the words in the original phrase. 91394342404.

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 81

*UGC NET July 2018, Paper II, original Q5*

> Given below are three implementations of the swap( ) function in C++ : (a) (b) (c) void swap (int a, int b) void swap (int &a, int &b) v oid swap (int *a, int *b) { { { int temp; int temp; int *temp; temp = a; temp = a; temp = a; a = b; a = b; a = b; b = temp; b = temp; b = temp; } } } int main( ) int main( ) int main( ) { { { int p = 0, q = 1; int p = 0, q = 1; int p = 0, q = 1; swap (p, q); swap (p, q); swap (&p, &q); } } } Which of these would actually swap the contents of the two integer var iables p and q ?

**Options**

1. (a) only
2. (b) only
3. (c) only
4. (b) and (c) only

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 82

*UGC NET July 2018, Paper II, original Q6*

> In Java, which of the following statements is/are True ? S1 : The ‘final’ keyword applied to a class definition prevents the class from being extended through derivation. S2 : A class can only inherit one class but can implement multiple interf aces. S3 : Java permits a class to replace the implementation of a method that it h as inherited. It is called method overloading.

**Options**

1. S1 and S2 only
2. S1 and S3 only
3. S2 and S3 only
4. All of S1, S2 and S3

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 83

*UGC NET Aug 2024, original Q121*

> Which of the following statements about pointers in C are TRUE.
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Pointers can be used to access array elements
> - **B.** Pointers can store the address of another pointer
> - **C.** Pointers are automatically deferenced in expression
> - **D.** Pointers cannot be used to access structure members Choose the correct answer from the options given below :

**Options**

1. (A) and (C) Only
2. (A) and (B) Only
3. (B) and (C) Only
4. (C) and (D) Only

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 84

*UGC NET Aug 2024, original Q122*

> Which of the following are TRUE about constructors in C++?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** A constructor can be overloaded.
> - **B.** A constructor does not have a return type.
> - **C.** A constructor must be declared as a friend function.
> - **D.** A constructor is called when an object is destroyed. Choose the correct answer from the options given below :

**Options**

1. (B), (C), (D) Only
2. (B), (C) Only
3. (A), (B), (C) Only
4. (A), (B) Only

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 85

*UGC NET June 2024, original Q71*

> The output of the following C++ Program is : #include <stdio.h» int main (void) 85305 x - 30; int x, "p; print f ("%d, *p); return 0;
>
> **Additional extracted choices — check the source page:**
>
> 1. 30
> 2. value of I
> 3. address of x
> 4. Error 72. wruch of the rollowing have truth values l universe of discourse consists of all integers ?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** n3m (n°<m)
> - **B.** 3nm (n<m?)
> - **C.** 3n3m (nº+m? =5) E. 3n3m (m+n=4/n-m=1)
> - **D.** 3n3m (n? +m?-6) Choose the correct answer from the options given below :

**Options**

1. A, B, C Only
2. B, C, E Only
3. C. D, B Only
4. B, D Oniy

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 86

*UGC NET June 2024, original Q73*

> Multiple Inheritance le permitted directly in..... A C++ B. lava C. Python E. BASIC D. VENET Choose the most appropriate answer from the options given below :

**Options**

1. A and BOnly
2. A and COnly
3. Band D Only
4. A, C and E Only

**Chapter foundations**

This question belongs to the ideas covered by **Programming in C++**. Revise these foundations: Tokens; Identifiers; Variables and Constants; Data Types; Operators; Control Statements; Functions and Parameter Passing; Virtual Functions; Classes and Objects; Constructors and Destructors; Overloading; Inheritance; Templates; Exception and Event Handling; Streams and Files; Multifile Programs.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Programming in C++ questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-6"></a>

### 6. Web Programming (32 questions)

**What to master:** HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 87

*UGC NET Dec 2013, Paper III, original Q13*

> The document that is used by XSLT to indicate, how to transform the elements of the XML document to another format is

**Options**

- **A.** HTML page
- **B.** DOC type procedure
- **C.** Style sheet
- **D.** Stored procedure

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 88

*UGC NET Dec 2014, Paper III, original Q40*

> The behaviour of the document elements in XML can be defined by

**Options**

- **A.** Using document object
- **B.** Registering appropriate event handlers
- **C.** Using element object
- **D.** All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 89

*UGC NET Dec 2014, Paper III, original Q42*

> Which method is called first by an applet program ?

**Options**

- **A.** start( )
- **B.** run( )
- **C.** init( )
- **D.** begin( )

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 90

*UGC NET Dec 2015, Paper III, original Q34*

> Javascript and Java has similar name because _ _is/are true. (a) Javascripts syntax is loosely based on Java's syntax (b) Javascript is stripped down version of Java (c) Java and Javascript are originated from Island of Java Codes :

**Options**

1. (a) only
2. (a), (b) and (c)
3. (a) and (b)
4. (a) and (c)

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 91

*UGC NET Dec 2015, Paper III, original Q35*

> Which of the following statements are true with reference to the way of describing XML data ? (a) XML uses DTD to describe the data (b) XML uses XSL to describe the data (c) XML uses a description node to describe the data Codes: (1) (a) only

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 92

*UGC NET June 2015, Paper III, original Q37*

> In Java, when we implement an interface method, it must be declared as : (1) Private (2) Protected

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 93

*UGC NET June 2015, Paper III, original Q38*

> The Servlet Response interface enables a servlet to formulate a response for a client using the method

**Options**

1. void log(Exception e, String s)
2. void destroy()
3. int get ServerPort()
4. void set ContextType(String type) J-8715 7 Paper-II

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 94

*UGC NET June 2015, Paper III, original Q39*

> Which one of the following is correct?

**Options**

1. Java applets can not be written in any programming language
2. An applet is not a small program
3. An applet can be run on its own
4. Applets are embedded in another applications

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 95

*UGC NET June 2015, Paper III, original Q40*

> In XML we can specify the frequency of an element by using the symbols
>
> **Additional extracted choices — check the source page:**
>
> 1. +*!
> 2. #*!
> 3. _Missing in extracted text_
> 4. -*?

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 96

*UGC NET June 2015, Paper III, original Q41*

> In XML, DOCTYPE declaration specifies to include a reference to ______ file.

**Options**

1. Document Type Definition
2. Document type declaration
3. Document transfer definition
4. Document type language

**Correct answer**

**Option 1: Document Type Definition**

*Verification: Final CBSE key matched through an archived transcription; independently verified against the W3C XML specification.*

**Step-by-step solution**

1. Read the tested keyword: DOCTYPE. It means document type declaration; it is the declaration written in the XML document.
2. Ask what that declaration may contain or point to. The grammar supplied by those markup declarations is called a Document Type Definition, abbreviated DTD.
3. For an external DTD, the declaration uses SYSTEM or PUBLIC followed by an external identifier, for example `<!DOCTYPE greeting SYSTEM "hello.dtd">`.
4. Therefore the missing file type is a Document Type Definition file, so option 1 is correct.

**Why each option is right or wrong**

- **1. Document Type Definition — Correct.** A DTD declares the permitted document structure, including elements, attributes, entities and notations. A DOCTYPE declaration can point to an external DTD.
- **2. Document type declaration — Incorrect.** This expands DOCTYPE itself, not the external grammar file to which the declaration refers.
- **3. Document transfer definition — Incorrect.** This is not an XML standard term.
- **4. Document type language — Incorrect.** This is also not the name of the XML grammar resource; the standard term is Document Type Definition.

**Conceptual lesson**

Keep three ideas separate: XML carries data, a DOCTYPE declaration appears in an XML document, and a DTD supplies grammar-like rules for a class of XML documents.

A DTD may be internal, external, or both. An internal subset is written inside square brackets in the DOCTYPE. An external subset is referenced with `SYSTEM` or `PUBLIC`; `.dtd` is the conventional filename extension.

Well-formed and valid are not synonyms. A well-formed XML document obeys XML syntax, such as one root element and correctly nested tags. A valid XML document is well-formed and also obeys its declared DTD constraints.

**How to solve similar questions**

Expand the acronym first, then distinguish the declaration from the resource it declares or references. If an option invents words such as transfer or language, reject it unless that phrase is a defined XML term.

**Verification references**

- [Final-answer-key archive](https://www.cbse-net.in/2015/08/net-answer-key-of-computer-science-june-2015.html)
- [Independent concept reference](https://www.w3.org/TR/xml/#sec-prolog-dtd)

---

#### Question 97

*UGC NET July 2016, Paper III, original Q41*

> Which of the following statements is not correct ?

**Options**

1. HTML is not screen precise formatting language.
2. HTML does not specify a logic.
3. DHTML is used for developing highly interactive web pages.
4. HTML is a programming language.

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 98

*UGC NET Jan 2017, Paper III, original Q38*

> Given the array of intege rs ‘array’ shown below : 13 7 27 2 18 33 9 11 22 8 What is the output of th e following JAVA statements ? int [ ] p = new int [10]; int [ ] q = new int [10]; for (int k = 0; k < 10; k ++) p[k] = array [k]; q = p; p[4] = 20; System.out.println(array [4] + “:” + q[4]);

**Options**

1. 20 : 20
2. 18 : 18
3. 18 : 20
4. 20 : 18

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 99

*UGC NET Jan 2017, Paper III, original Q39*

> Consider the following JAVA program : public class First { public static int CBSE (int x) { if ( x < 100) x = CBSE (x + 10); return ( x – 1); } public static void main (String[] args){ System.out.print(First.CBSE(60)); } } What does this program print ?

**Options**

1. 59
2. 95
3. 69
4. 99

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 100

*UGC NET Jan 2017, Paper III, original Q41*

> Which of the following HTML c ode will affect the vertical alignment of the table content ?

**Options**

1. <td style = “vertical-align : middle”> Text Here </td>
2. <td valign = “centre”> Text Here </td>
3. <td style = “text-align : center”> Text Here </td>
4. <td align = “middle”> Text Here </td>

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 101

*UGC NET Jan 2017, Paper III, original Q42*

> What can you say about the following statements ? I. XML tags are case-insensitive. II. In JavaScript, identifier names are case-sensitive. III. Cascading Style Sheets (CSS) cannot be used with XML. IV. All well-formed XML documents must contain a document type definition.

**Options**

1. only I and II are false.
2. only III and IV are false.
3. only I and III are false.
4. only II and IV are false.

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 102

*UGC NET July 2018, Paper II, original Q1*

> The definitions in an XML document are said to be __________ when the t agging system and definitions in the DTD are all in compliance.

**Options**

1. well-formed
2. reasonable
3. valid
4. logical

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 103

*UGC NET July 2018, Paper II, original Q2*

> Consider the JavaScript Code : var y= ’’12”; function f( ) { var y=’’6”; alert (this.y); function g( ) {alert (y); } g( ); } f( ); If M is the number of alert dialog boxes generated by this JavaScript c ode and D1, D2, ...., DM represents the content displayed in each of the M dialog boxes, then :

**Options**

1. M=3; D1 displays ”12”; D2 displays ”6”; D3 displays ”12”.
2. M=3; D1 displays ”6”; D2 displays ”12”; D3 displays ”6”.
3. M=2; D1 displays ”6”; D2 displays ”12”.
4. M=2; D1 displays ”12”; D2 displays ”6”.

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 104

*UGC NET July 2018, Paper II, original Q3*

> What is the output of the following JAVA program ? class simple { public static void main(String[ ] args) { simple obj = new simple( ); obj.start( ); } void start( ) { long [ ] P= {3, 4, 5}; long [ ] Q= method (P); System.out.print (P[0] + P[1] + P[2]+”:”); System.out.print (Q[0] + Q[1] + Q[2]); } long [ ] method (long [ ] R) { R [1]=7; return R; } } //end of class

**Options**

1. 12 : 15
2. 15 : 12
3. 12 : 12
4. 15 : 15

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 105

*UGC NET Dec 2019, original Q66*

> Which tag is used to enclose any number of javascript statements in HTML document?

**Options**

1. ‹code>
2. <script>
3. <title>
4. <body> 61547540962.2 61547540963. 3 61547540964. 4

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 106

*UGC NET Dec 2019, original Q135*

> Match List-I with List-II: List I List II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Frame attribute (i) to create link in HTML
> - **B.** str» tag (ii) for vertical alignment of content in cell
> - **C.** Valign attribute (iii) to enclose each row in table
> - **D.** <a> tag (iv) to specify the side of the table frame that display border Choose the correct option from those given below : rsonal Exam Guide (1)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(i).
> - **B.** -(il),
> - **C.** -(ili),
> - **D.** -(iv) (2)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(ii),
> - **B.** -(i),
> - **C.** -(iii),
> - **D.** (iv) (3)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(iv),
> - **B.** -(iii),
> - **C.** -(ii).
> - **D.** -(i) (4)

**Options**

- **A.** -(iii).
- **B.** -(iv),
- **C.** -(ii),
- **D.** -(i) 61547541238. 2 61547541239.3 61547541240.4

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 107

*UGC NET June 2019, original Q75*

> Which of the following statements is/are true? P: In a scripting language like JavaScript, types are typically associated with values, not variables. : It is not possible to show images on a web page without the <img> tag of HTML. Select the correct answer from the options given below : 1. P only 2. Qonly Both Pand Q 4. Neither P nor Q

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 108

*UGC NET June 2019, original Q76*

> Which of the following statements is/are true? P: An XML document with correct syntax as specified by W3C is called "Well Formed". Q: An XML documented validated against a DTD is both "Well formed" and "Valid". R: <xml version="1•0" encoding="UTF-8"> is syntactly correct declaration for the version of an XML document. Select the correct answer from the options given below : .

**Options**

1. Pand Qonly
2. Pand R only
3. Q and Ronly
4. All of P, Q and R 64635085640.2 64635085641.3 64635085642. 4

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 109

*UGC NET Nov 2020, original Q60*

> In HTML, <map> tag is used for

**Options**

1. defining a path between two nodes in an image
2. defining clickable region in an image
3. highlighting an area in an image
4. defining the site-map of a web-site 53622816738.2 53622816739.3 53622816740.4

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 110

*UGC NET Nov 2020, original Q95*

> Which of the following statements regarding XML is/are True? (A) XML is a set of tags designed to tell browsers how to display text and images in a web page. (B) XML defines a syntax for representing data, but the meaning of data varies from application to application. (C) < Letter >, < LETTER > and < letter > are three different tags in XML. Choose the correct answer from the options given below:

**Options**

1. (A) and (B) only
2. (A) and (C) only
3. (B) and (C) only
4. (A). (B) and (C) 53622816878.2 53622816879,3 53622816880.4

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 111

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

#### Question 112

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

#### Question 113

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

---

#### Question 114

*UGC NET Oct 2022, original Q21*

> Which mechanism in XML allows organizations to specify globally unique names as element tags in documents?

**Options**

1. root
2. header
3. schema
4. namespace

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 115

*UGC NET Aug 2024, original Q139*

> Match List - I with List - II. List - I List - II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** HIML (1) Allow for dynamic and interactive web pages.
> - **B.** DHTML (I) Defines the structure of web pages.
> - **C.** XML (III) Object-oriented programming language for web applications.
> - **D.** JAVA (IV) Used for data storage and transport. Choose the correct answer from the options given below : (1)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(L),
> - **B.** -(III,
> - **C.** -(II),
> - **D.** -(IV) (2)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(LI),
> - **B.** -(III),
> - **C.** -(IV),
> - **D.** -(l) (3)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** -(II,
> - **B.** -(I),
> - **C.** -(IV),
> - **D.** -(III) (4)

**Options**

- **A.** -(III),
- **B.** -(I),
- **C.** -(IV),
- **D.** -(II)

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 116

*UGC NET June 2024, original Q78*

> Which of the following is the Markup language? A. HTML B. XML e. DHTML D. LML E. PN Choose the correct answer from the options given below :

**Options**

1. B, C, D Only
2. A, C, D Only
3. A, C, D, E Only
4. A, B, C Only

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 117

*UGC NET June 2025, original Q110*

> Consider the following statements for XML (Extensible Markup Language) :
>
> **Additional extracted choices — check the source page:**
>
> - **A.** The number of tags decreases and users can define their own tags.
> - **B.** Its is used for Presentation.
> - **C.** It is case sensitive.
> - **D.** It is dynamic. Which of the above statements are true ?

**Options**

1. B, C, D Only
2. A, B, D Only
3. A, C, D Only
4. B, D Only 42558919493.2 42558919494. 3 42558919495.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 118

*UGC NET Dec 2025 session (Jan 2026), original Q66*

> Question Number : 66 B. paintO C. init( D. stop( Choose the correct answer from the options given below:

**Options**

1. A, B, C, D
2. C, A, B, D
3. A. C, B, D
4. B,A, C, D 6119878662.2 6119878663.3 6119878664.4

**Chapter foundations**

This question belongs to the ideas covered by **Web Programming**. Revise these foundations: HTML; DHTML; XML; Scripting; Java; Servlets; Applets.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Web Programming questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-7"></a>

### 7. Computer Graphics (25 questions)

**What to master:** Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 119

*UGC NET June 2013, Paper III, original Q30*

> If 40 black lines interleaved with 40 white lines can be distinguished across one inch, the resolution is

**Options**

- **A.** 40 line-pairs per inch
- **B.** 80 line-pairs per inch
- **C.** 1600 lines per inch
- **D.** 40 lines per inch

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 120

*UGC NET Dec 2014, Paper III, original Q17*

> In Cyrus-Beck algorithm for line clipping the value of t paramet er is computed by the relation : (Here P 1 and P 2 are the two end points of the line, f is a point on the boundary, n 1 is inner normal)

**Options**

- **A.** (P1 – f i) ⋅ n i (P2 – P 1) ⋅ n i
- **B.** (fi – P 1) ⋅ n i (P2 – P 1) ⋅ n i
- **C.** (P2 – f i) ⋅ n i (P1 – P 2) ⋅ n i
- **D.** (fi – P 2) ⋅ n i (P1 – P 2) ⋅ n i

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 121

*UGC NET Dec 2014, Paper III, original Q64*

> Given two spatial masks S 1 =    0 1 0 1 –4 0 0 1 0 and S 2 =    1 1 1 1 –8 1 1 1 1 The Laplacian of an image at all points (x, y) can be implement ed by convolving the image with spatial mask. Which of the following can be used as the spatial mask ?

**Options**

- **A.** only S 1
- **B.** only S 2
- **C.** Both S 1 and S 2
- **D.** None of these

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 122

*UGC NET Dec 2015, Paper III, original Q33*

> Which of the following graphic primitives are considered as the basic building blocks of computer graphics? (a) Points (b) Lines Polylines (d) Polygons Codes:

**Options**

1. (a) only
2. (a) and (b)
3. (a), (b) and (c)
4. (a), (b), (c) and (d)

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 123

*UGC NET Dec 2015, Paper III, original Q69*

> Which raster locations would be chosen by Bresenham's algorithm when scan converting a line from (1, 1) to (8, 5)?
>
> **Additional extracted choices — check the source page:**
>
> 1. У
> 2. _Missing in extracted text_
> 3. У
> 4. У 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 3 3 2 2 4 3 4 3 4 3 4 3 5 4 5 4 3 5 5 6 4 6 5 5 7 6 7 5 8 6 8 | 7_ 8 8 5

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 124

*UGC NET Jan 2017, Paper III, original Q17*

> Which of the following is/are si de effects of scan conversion ?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Aliasing
> - **B.** Unequal intensity of diagonal lines
> - **C.** Overstriking in photographic applications
> - **D.** Local or Global aliasing

**Options**

1. a and b
2. a, b and c
3. a, c and d
4. a, b, c and d

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 125

*UGC NET Dec 2018, original Q94*

> In 3D Graphics, which of the following statements about perspective and parallel projection is/are true? P: In a perspective projection, the farthest an object is from the centre of projection, the smaller it appears. Q: Parallel projection is equivalent to a perspective projection where the viewer is standing infinitely far away. R: Perspective projections do not preserve straight lines. Choose the correct answer from the code given below : Code: . Pand Qonly 91394342374 Pand R only 91394342375. Q and R only P, Q and R 91394342376.

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 126

*UGC NET July 2018, Paper II, original Q9*

> Which of the following statements is/are True regarding the solution to the visibility problem in 3D graphics ? S1 : The Painter’s algorithm sorts polygons by depth and then paints ( scan - converts) each Polygon on to the screen starting with the most nearest polygon. S2 : Backface Culling refers to eliminating geometry with backfacing no rmals.

**Options**

1. S1 only
2. S2 only
3. Both S1 and S2
4. Neither S1 nor S2

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 127

*UGC NET Dec 2019, original Q67*

> A rectangle is bound by the lines x = 0: y = 0:x = 5and y=3. The line segment joining (-1, O) and (4. 5), if clipped against this window will connect the points -

**Options**

1. (0. 1) and (3. 3)
2. (0, 1) and (2. 3)
3. (0. 1) and (4, 5)
4. (0. 1) and (3. 5) Options : Guid 61547540965. 1 61547540966.2 61547540967. 3 61547540968. 4

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 128

*UGC NET Dec 2019, original Q68*

> Which of the following algorithms is not used for line clipping?

**Options**

1. Cohen-Sutherland algorithm
2. Southerland-Hodgeman algorithm
3. Liang-Barsky algorithm
4. Nicholl-Lee-Nicholl algorithm 61547540970.2 61547540971. 3 61547540972. 4

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 129

*UGC NET Dec 2019, original Q103*


**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 130

*UGC NET Dec 2019, original Q120*

> Consider the following statements with respect to approaches to fill area on raster systems : P: To determine the overlap intervals for scan lines that cross the area. Q: To start from a given interior position and paint outward from this point until we encounter the specified boundary conditions. Select the correct answer from the options given below :

**Options**

1. P only
2. Q only
3. Both Pand Q
4. Neither P nor Q 61547541178.2 61547541179.3 61547541180.4

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 131

*UGC NET June 2019, original Q77*

> Consider a raster system with resolution 640 by 480. What size is frame buffer (in bytes) for this system to store 12 bits per pixel?

**Options**

1. 450 kilobytes
2. 500 kilobytes
3. 350 kilobytes
4. 400 kilobytes 64635085644. 2 64635085645. 3 64635085646.4 Single Line Ouestion Option: No

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 132

*UGC NET Nov 2021, original Q6*

> Suppose you have eight 'black and white' images taken with a 1‐megapixel camera and one '8‐color' image taken by an 8‐megapixel camera. How much hard disk space in total do you need to store these images on your computer?

**Options**

1. 1 GB
2. 4 MB
3. 3 MB
4. 3 GB

**Correct answer**

**Option 2: 4 MB**

*Verification: Official NTA final key matched by Question ID 2336 and Option ID 9342; independently verified by bits-per-pixel calculation.*

**Step-by-step solution**

1. A black-and-white image has two possible pixel values, so it requires log2(2)=1 bit per pixel. Each 1-megapixel image therefore needs about 1 megabit before compression.
2. Eight such images need 8 megabits, which is 1 megabyte because 8 bits make one byte.
3. An 8-color image needs log2(8)=3 bits per pixel. At 8 megapixels, it needs 24 megabits, or 3 megabytes.
4. The total is 1 MB + 3 MB = 4 MB, so option 2 is correct.

**Why each option is right or wrong**

- **1. 1 GB — Incorrect.** This is roughly 256 times larger than the uncompressed bit count in the question.
- **2. 4 MB — Correct.** The monochrome images contribute 1 MB and the 8-color image contributes 3 MB.
- **3. 3 MB — Incorrect.** It counts only the 8-color image and omits the eight black-and-white images.
- **4. 3 GB — Incorrect.** It confuses megabytes with gigabytes and is about three orders of magnitude too large.

**Conceptual lesson**

For an indexed or fixed-palette image with C possible colors, the theoretical storage per pixel is `ceil(log2 C)` bits. Two colors need 1 bit; 8 colors need 3 bits; 256 colors need 8 bits.

Image size before compression is `width × height × bits per pixel`. A megapixel is approximately one million pixels. Convert bits to bytes by dividing by 8, and convert units only after the bit calculation.

Real files may also contain headers, palettes, padding and compression. Unless the question supplies such overhead, UGC NET expects the ideal raw pixel-data calculation.

**How to solve similar questions**

Write `pixels × bits/pixel` for every image group, add all bit totals, then divide by 8. Never treat the number of colors itself as bits per pixel.

**Verification references**

- [Final-answer-key archive](https://cdnbbsr.s3waas.gov.in/s301eee509ee2f68dc6014898c309e86bf/uploads/2022/04/2022040888.pdf)
- [Independent concept reference](https://www.w3.org/TR/png-3/#11IHDR)

---

#### Question 133

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

---

#### Question 134

*UGC NET June 2025, original Q60*

> Consider the following piece of C programming code: int x=128, y=110; do If(x > y) x= x - y; else y = y - x; ) while(x! =y) printf("d", x); Which one will be the output?

**Options**

1. 18
2. 2
3. 92
4. 74 42558919293.2 42558919294. 3 42558919295.4

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 135

*UGC NET June 2025, original Q62*

> What will be the output of the following C programming code: int i, j; for(i=1; i<5; i+=2) for(j=1; j<i; j+=2) printf"%d", j);

**Options**

1. 1
2. 1 2
3. 1 3
4. 1 1 42558919301.2 42558919302.3 42558919303.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 136

*UGC NET June 2025, original Q63*

> What would be the equivalent pointer expression for referring the array element ar[m][n][o]

**Options**

1. * (* (* (ar) + m + n) + o)
2. (* (* (* ar + m) + n) + o)
3. (* (* (ar + m) + n) + o)
4. * (* (* (ar + m) + n) + o) 42558919305.2 42558919306. 3 42558919307.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 137

*UGC NET June 2025, original Q80*

> What will be the output of the following C Programming code : void main () int *i, a=12, b=2, c; c= (a=a+b, b=a/b, a=a *b, b=a-b) i = &c; printf("d", - (*i)); }

**Options**

1. 91
2. 90
3. 98
4. 92 42558919372.1 42558919374.3 42558919375.4

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 138

*UGC NET June 2025, original Q94*

> Consider the operators used in C Programming given below: A. && B. += C.>> D. >= E. ?: Choose among the following the correct order of precedence of the operators given above (higher to lower):
>
> **Additional extracted choices — check the source page:**
>
> 1. C, D, E, B, A
> 2. C, A, D, E, B
> 3. C, D, A, E, B
> 4. D, C, A, B, E 42558919428. 1 42558919430. 3 42558919431.4 Mansion ry mber: 24 :

**Options**

1. C, D, E, B, A
2. C, A, D, E, B
3. C, D, A, E, B
4. D, C, A, B, E 42558919428. 1 42558919430.3 42558919431,4

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 139

*UGC NET June 2025, original Q111*

> only legal pointer operations: 1. pointer + number > pointer B. pointer - number → number C. pointer + pointer → pointer D. pointer - pointer → pointer E. pointer - pointer → number Choose the most appropriate answer from the options given below:

**Options**

1. A, B, C Only
2. A, B, D Only
3. A, B Only
4. A, E Only 42558919497.2 42558919498. 3 42558919499.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 140

*UGC NET June 2025, original Q129*

> Match List I with List Il List I List I
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Overloading 1. Since function call is resolved during run time, the execution is Slow.
> - **B.** Early binding II. Since function call is resolved during compilation time, the execution is much faster.
> - **C.** Overriding III. Supports compile-time polymorphism.
> - **D.** Late Binding IV. Supports run-time polymorphism. Choose the correct answer from the options given below:

**Options**

1. A-III, B-II, C-I, D-IV
2. A-IV, B-II, C-III, D-I
3. A-III, B-I, C-IV, D-lI
4. A-IV, B-I, C-III, D-II 42558919569.2 42558919570.3 42558919571.4

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 141

*UGC NET June 2025, original Q130*

> Match List I with List I! List I
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Oblique Projection I. When the direction of projection is so chosen that the lines perpendicular to the plane of projection are foreshortened.
> - **B.** Cavelier Projection II. When the direction of projection is so chosen that there is no foreshortening of lines perpendicular to the plane of projection.
> - **C.** Cabinet Projection III. When the direction of projection is perpendicular to the plane of projection.
> - **D.** Orthographic Projection IV. When the angle between the projectors and the plane of projection is not equal to 90°. Choose the correct answer from the options given below:

**Options**

1. A-III, B-II, C-IV, D-I
2. A-IV, B-II, C-I, D-III
3. A-III, B-I, C-IV, D-II
4. A-IV, B-I, C-III, D-II 42558919573.2 42558919574. 3 42558919575.4

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 142

*UGC NET Dec 2025 session (Jan 2026), original Q63*

> Question Number : 63

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 143

*UGC NET Dec 2025 session (Jan 2026), original Q65*

> Question Number : 65

**Chapter foundations**

This question belongs to the ideas covered by **Computer Graphics**. Revise these foundations: Video-Display Devices; Raster-Scan and Random-Scan Systems; Graphics Monitors; Input Devices; Points and Lines; Line-Drawing Algorithms; Midpoint Circle and Ellipse Algorithms; Scan-Line Polygon Fill; Boundary-Fill and Flood-Fill.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Computer Graphics questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-8"></a>

### 8. 2-D Geometrical Transforms and Viewing (15 questions)

**What to master:** Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 144

*UGC NET Dec 2013, Paper II, original Q22*

> If the queue is implemented with a linked list, keeping track of a front pointer and a rear pointer, which of these pointers will change during an insertion into a non-empty queue ?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Neither of the pointers change
> - **B.** Only front pointer changes
> - **C.** Only rear pointer changes
> - **D.** Both of the pointers changes 23. _______ is often used to prove the correctness of a recursive function.

**Options**

- **A.** Diagonalization
- **B.** Communitivity
- **C.** Mathematical Induction
- **D.** Matrix Multiplication

**Chapter foundations**

This question belongs to the ideas covered by **2-D Geometrical Transforms and Viewing**. Revise these foundations: Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 2-D Geometrical Transforms and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 145

*UGC NET Dec 2013, Paper III, original Q11*

> Match the following style rules for reusability : List – I List – II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Keep methods coherent i. Write a method to get the last element of a list
> - **B.** Keep methods small ii. Maintain parallel structure when possible
> - **C.** Keep methods consistent iii. Breaking a method into smaller parts
> - **D.** Provide uniform coverage iv. Performs a single function or a group of closely related functions. Codes : a b c d

**Options**

- **A.** iv iii ii i
- **B.** ii i iv iii
- **C.** iii iv ii i
- **D.** ii iii iv i

**Chapter foundations**

This question belongs to the ideas covered by **2-D Geometrical Transforms and Viewing**. Revise these foundations: Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 2-D Geometrical Transforms and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 146

*UGC NET Dec 2013, Paper III, original Q64*

> Which of the following points lies on the same side as the origin, with reference to the line 3x + 7y = 2 ?

**Options**

- **A.** (3, 0)
- **B.** (1, 0)
- **C.** (0.5, 0.5)
- **D.** (0.5, 0)

**Chapter foundations**

This question belongs to the ideas covered by **2-D Geometrical Transforms and Viewing**. Revise these foundations: Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 2-D Geometrical Transforms and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 147

*UGC NET Dec 2013, Paper III, original Q65*

> The transformation matrix required for conversion of CMY colour model to RGB colour model is given as :

**Options**

- **A.** ⎣⎢ ⎢⎡ ⎦ ⎥ ⎥⎤R G B = ⎣ ⎢ ⎢⎡ ⎦ ⎥ ⎥⎤C M Y – ⎣ ⎢ ⎢⎡ ⎦ ⎥ ⎥⎤1 1 1
- **B.** ⎣⎢ ⎢⎡ ⎦ ⎥ ⎥⎤R G B = ⎣ ⎢ ⎢⎡ ⎦ ⎥ ⎥⎤C M Y – ⎣ ⎢ ⎢⎡ ⎦ ⎥ ⎥⎤1 2 3
- **C.** ⎣⎢ ⎢⎡ ⎦ ⎥ ⎥⎤R G B = ⎣ ⎢ ⎢⎡ ⎦ ⎥ ⎥⎤1 1 1 – ⎣⎢ ⎢⎡ ⎦ ⎥ ⎥⎤C M Y
- **D.** ⎣ ⎢ ⎢⎡ ⎦ ⎥ ⎥⎤R G B = ⎣ ⎢ ⎢⎡ ⎦ ⎥ ⎥⎤C M Y – ⎣ ⎢ ⎢⎡ ⎦ ⎥ ⎥⎤0.5 0.5 0.5

**Chapter foundations**

This question belongs to the ideas covered by **2-D Geometrical Transforms and Viewing**. Revise these foundations: Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 2-D Geometrical Transforms and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 148

*UGC NET Dec 2014, Paper II, original Q15*

> Which of the following differentiates between overloaded functions and overridden functions ?

**Options**

- **A.** Overloading is a dynamic or runtime binding and overridden is a static or compile time binding.
- **B.** Overloading is a static or compile time binding and overridi ng is dynamic or runtime binding.
- **C.** Redefining a function in a friend class is called overloading , while redefining a function in a derived class is called as overridden function.
- **D.** Redefining a function in a derived class is called function ove rloading, while redefining a function in a friend class is called function overriding.

**Chapter foundations**

This question belongs to the ideas covered by **2-D Geometrical Transforms and Viewing**. Revise these foundations: Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 2-D Geometrical Transforms and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 149

*UGC NET June 2015, Paper III, original Q13*

> Give the number of principal vanishing point(s) along with their direction for the standard perspective transformation:
>
> **Additional extracted choices — check the source page:**
>
> 1. Only one in the direction K
> 2. Two in the directions I and J
> 3. Three in the directions I, J and K
> 4. Only two in the directions J and K ° about the point P(- 1, - 1). What shall be the coordinates of the new triangle

**Options**

1. A = (1, 52 - 1), B'= (-1,252 - 1) and C'= 352 - 1, = N2 - 1)
2. A'= (1, N2 - 1), B'= (252-1, - 1) and C'= (352-1, 2 52-1)
3. A'= (-1, N2 - 1), B'= (-1,252-1) and C'= (302 - 1, 2 52-1)
4. A'= (VE - 1, - 1), B= (-1,252 - 1) and C'= (352 - 1, = 52 - 1)

**Chapter foundations**

This question belongs to the ideas covered by **2-D Geometrical Transforms and Viewing**. Revise these foundations: Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 2-D Geometrical Transforms and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 150

*UGC NET July 2016, Paper II, original Q13*

> Which one of the following is correct, when a class grants friend status to another class ?

**Options**

1. The member functions of the class ge nerating friendship can access the members of the friend class.
2. All member functions of the class gran ted friendship have unrestricted access to the members of the class granting the friendship.
3. Class friendship is reciprocal to each other.
4. There is no such concept.

**Chapter foundations**

This question belongs to the ideas covered by **2-D Geometrical Transforms and Viewing**. Revise these foundations: Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 2-D Geometrical Transforms and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 151

*UGC NET July 2016, Paper III, original Q14*

> A point P(5, 1) is rotated by 90 ° about a pivot point (2, 2). What is the coordinate of new transformed point P′ ?

**Options**

1. (3, 5)
2. (5, 3)
3. (2, 4)
4. (1, 5)

**Chapter foundations**

This question belongs to the ideas covered by **2-D Geometrical Transforms and Viewing**. Revise these foundations: Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 2-D Geometrical Transforms and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 152

*UGC NET July 2016, Paper III, original Q15*

> Let R be the rectangular window against wh ich the lines are to be clipped using 2D Sutherland-Cohen line clipping algorithm. Th e rectangular window has lower left-hand corner at (– 5, 1) and upper ri ght-hand corner at (3, 7). Cons ider the following three lines for clipping with the given end point co-ordinates : Line AB : A (– 6, 2) and B (–1, 8) Line CD : C (– 1, 5) and D (4, 8) Line EF : E (–2, 3) and F (1, 2) Which of the following line(s) is/are candidate for clipping ?

**Options**

1. AB
2. CD
3. EF
4. AB and CD

**Chapter foundations**

This question belongs to the ideas covered by **2-D Geometrical Transforms and Viewing**. Revise these foundations: Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 2-D Geometrical Transforms and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 153

*UGC NET June 2019, original Q78*

> Consider the following statements regarding 2D transforms in computer graphies : S1 1 0 : is a 2x2 matrix that reflects (mirrors) only 2D point about 0 -1 the X-axis. S2 : A 2x2 matrix which mirrors any 2D point about the X-axis, is a rotation matrix. repp What can you say about the statements S1 and S2? Your 1. Both Sl and S2 are true 2. Only S1 is true Only S2 is true 4. Both S1 and S2 are false 64635085648. 2 64635085649. 3 64635085650.4

**Chapter foundations**

This question belongs to the ideas covered by **2-D Geometrical Transforms and Viewing**. Revise these foundations: Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 2-D Geometrical Transforms and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 154

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

---

#### Question 155

*UGC NET Oct 2022, original Q17*

> Hidden surface removal problem with minimal 3D pipeline can be solved with

**Options**

1. Painter's algorithm
2. Window Clipping algorithm
3. Brute force rasterization algorithm
4. Flood fill algorithm

**Chapter foundations**

This question belongs to the ideas covered by **2-D Geometrical Transforms and Viewing**. Revise these foundations: Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 2-D Geometrical Transforms and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 156

*UGC NET Oct 2022, original Q24*

> This transformation is called dy = = g 1 1. Scaling 2. Shear 3. Homography

**Chapter foundations**

This question belongs to the ideas covered by **2-D Geometrical Transforms and Viewing**. Revise these foundations: Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 2-D Geometrical Transforms and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 157

*UGC NET June 2025, original Q61*

> Which of the following technique is used for Clipping?

**Options**

1. Stack based Seed
2. Scan Line Seed
3. Sutherland-Cohen
4. Inverse Scaling 42558919297.2 42558919298.3 42558919299.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **2-D Geometrical Transforms and Viewing**. Revise these foundations: Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 2-D Geometrical Transforms and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 158

*UGC NET Dec 2025 session (Jan 2026), original Q61*

> Question Number : 61 and (4, 5, 6) on to a viewport specified by coordinates (2, 4, 2) and (8, 10, 8) is 2 0 0 0 0

**Options**

1. 2 niN. 0 0 6 5 + V 0 0 0 1 2 0 0 0
2. 0 3 0 5 0 0 6 4 0 0 101
3. 1 3 4 5 0 2 4 0 1 0 0 11 0 0 1
4. 2 3 0 5 1 0 4 5 0 0 0 - 6119878642.2 6119878643.3 6119878644.4

**Chapter foundations**

This question belongs to the ideas covered by **2-D Geometrical Transforms and Viewing**. Revise these foundations: Translation; Scaling; Rotation; Reflection; Shear; Matrix Representations and Homogeneous Coordinates; Composite Transforms; Transformations Between Coordinate Systems; Viewing Pipeline; Viewing Coordinate Reference Frame; Window-to-Viewport Transformation; Viewing Functions; Line and Polygon Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 2-D Geometrical Transforms and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-9"></a>

### 9. 3-D Object Representation, Geometric Transformations and Viewing (31 questions)

**What to master:** Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam lens:** Trace program state or transform coordinates explicitly; language questions usually test scope, binding, parameter passing, OOP dispatch, or C semantics.

**Reusable method:** For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order.

**High-yield rules:** Matrix composition is order-sensitive. Translation is represented in homogeneous coordinates. Pointer arithmetic advances in units of the pointed type.

**Common traps:** Watch undefined or implementation-dependent C behavior, pass-by-value aliases, constructor order, integer division, and reversed matrix multiplication.

---

#### Question 159

*UGC NET June 2010, Paper II, original Q12*

> What will be the output of the following c-code ? void main ( ) { char *P = "ayqm" ; char c; c = ++ *p ; printf ("%c", c); }

**Options**

- **A.** a
- **B.** c
- **C.** b
- **D.** q

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 160

*UGC NET Dec 2011, Paper III, original Q18*

> What are the types of collision resolution techniques and the method used in each of these types ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ ______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 161

*UGC NET Dec 2013, Paper II, original Q17*

> Which of the following has compilation error in C ?

**Options**

- **A.** int n = 32
- **B.** char ch = 65
- **C.** float f = (float) 3.2
- **D.** none of the above

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 162

*UGC NET June 2013, Paper III, original Q9*

> You have to return the original OMR Sheet to the invigilators at the end of the examination compulsorily and must not carry it with you outside the Examination Hall. You are however, allowed to carry duplicate copy of OMR Sheet on conclusion of examination.

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 163

*UGC NET June 2013, Paper III, original Q32*

> Arrays in C language can have _________ with reference to memory representation.

**Options**

- **A.** n-subscripts
- **B.** two-subscripts
- **C.** only one subscript
- **D.** three subscripts only

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 164

*UGC NET Dec 2014, Paper II, original Q11*

> What will be the output of the following ‘C’ code ? main ( ) { int x = 128; printf (“\n%d”, 1 + x ++); }

**Options**

- **A.** 128
- **B.** 129
- **C.** 130
- **D.** 131

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 165

*UGC NET Dec 2014, Paper III, original Q15*

> A technique used to approximate halftones without reducing spatial resolution i s known as _________.

**Options**

- **A.** Halftoning
- **B.** Dithering
- **C.** Error diffusion
- **D.** None of the above

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 166

*UGC NET Dec 2014, Paper III, original Q18*

> Match the following :
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Cavalier Projection i. The direction of projection is chosen so that there is no foreshortening of lines perpendicular to the xy plane.
> - **B.** Cabinet Projection ii. The direction of projection is chosen so that lines perpendicular to the xy planes are foreshortened by half their lengths.
> - **C.** Isometric Projection iii. The direction of projection makes equal angles with all of the principal axis.
> - **D.** Orthographic Projection iv. Projections are characterized by the fact that the direction of projection is perpendicular to the view plane. Codes : a b c d

**Options**

- **A.** i iii iv ii
- **B.** ii iii i iv
- **C.** iv ii iii i
- **D.** i ii iii iv

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 167

*UGC NET Dec 2015, Paper II, original Q11*

> Consider the following program : #include<stdio.h> main() int i, inp; float x, term=1, sum=0; scanf(" %d %f", & inp, &x); for(i=1; i<=inp; i++) term = term * x/i; sum = sum + term ; printf("Result = %f\n", sum); } The program computes the sum of which of the following series?

**Options**

1. x+x/2+23/3+244+...
2. * + x2/2! + x/3! + x/4! +...
3. 1+X12+2/3+x4/4+...
4. 1+ X/2! +23/3! + x*/4! +...

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 168

*UGC NET Dec 2015, Paper III, original Q66*

> A bell-shaped membership function is specified by three parameters (a, b, c) as follows : 1) 17(7=9"1 e) 17=9 0) 117=9) 0 1-17=9 1 1

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 169

*UGC NET July 2016, Paper II, original Q9*

> You have to return the Original OMR Sheet to the invigilators at the end of the examination compulsorily and must not carry it with you outside the Examination Hall. You are, however, allowed to carry original question booklet and duplicate copy of OMR Sheet on conclusion of examination.

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 170

*UGC NET July 2016, Paper III, original Q16*

> In perspective projection, if a line segment join ing a point which lies in front of the viewer to a point in back of the viewer is projected to a broken line of infinite extent. This is known as _______.

**Options**

1. View confusion
2. Vanishing point
3. Topological distortion
4. Perspective foreshortening

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 171

*UGC NET July 2016, Paper III, original Q18*

> Which of the following statement(s) is/are correct with reference to curve generation ? I. Hermite curves are generated us ing the concepts of interpolation. II. Bezier curves are generated using the concepts of approximation. III. The Bezier curve lies entirely with in the convex hull of its control points. IV. The degree of Bezier curve does not depend on the number of control points.

**Options**

1. I, II and IV only
2. II and III only
3. I and II only
4. I, II and III only

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 172

*UGC NET July 2016, Paper III, original Q60*

> Which of the following is used for the bounda ry representation of an image object ?

**Options**

1. Quad Tree
2. Projections
3. Run length coding
4. Chain codes

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 173

*UGC NET Jan 2017, Paper II, original Q9*

> You have to return the Original OMR Sheet to the invigilators at the end of the examination compulsorily and must not carry it with you outside the Examination Hall. You are, however, allowed to carry original question booklet on conclusion of examination.

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 174

*UGC NET Jan 2017, Paper III, original Q9*

> You have to return the Original OMR Sheet to the invigilators at the end of the examination compulsorily and must not carry it with you outside the Examination Hall. You are, however, allowed to carry original question booklet on conclusion of examination.

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 175

*UGC NET Nov 2017, Paper II, original Q9*

> You have to return the original OMR Sheet to the invigilators at the end of the examination compulsorily and must not carry it with you outside the Examination Hall. You a re however, allowed to carry original question booklet and duplicate copy of OMR Sheet on conclusion of examination.

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 176

*UGC NET July 2018, Paper II, original Q4*

> What is the output of the following ‘C’ program ? (Assuming little - endian representation of multi-byte data in which Least Significant Byte (LSB) is stored at the lowest memory address.) #include <stdio.h> #include <stdlib.h> /* Assume short int occupies two bytes of storage */ int main ( ) { union saving { short int one; char two[2]; }; union saving m; m.two [0] = 5; m.two [1] = 2; printf(’’%d, %d, %d\n”, m.two [0], m.two [1], m.one); }/* end of main */

**Options**

1. 5, 2, 1282
2. 5, 2, 52
3. 5, 2, 25
4. 5, 2, 517

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 177

*UGC NET Nov 2020, original Q96*

> In the context of SD Computer graphics, which of the following statements is/are correct? Under perspective projection, each set of parallel lines in the object do not stay parallel in the image (except those that are parallel to the viewplane to start with). Applying a perspective transformation in the graphics pipeline to a vertex involves dividing by its'z' coordinate. (C) Perspective transformation is a linear transformation. Choose the correct answer from the options given below:

**Options**

1. (A) and (B) only
2. (A) and (C) only
3. (B) and (C) only
4. (A), (B) and (C) 53622816882.2 53622816883.3 53622816884.4

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 178

*UGC NET Nov 2020, original Q126*

> Given below are different properties of 3D projections from A-D. Identify the correct order on the basis of property true of (1) a perspective projection only, (11) an orthographic projection only, (il) both orthographic and projective transformations and (iv) neither orthographic nor projective transformation, respectively.
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Straight lines are mapped to straight lines.
> - **B.** Distances and angles are (in general) preserved
> - **C.** Far away objects appear the same size as closer ones.
> - **D.** Requires homogeneous coordinates in order for it to be encoded into a linear transformation. Choose the correct answer from the options given below:

**Options**

1. D. C. B. A
2. B.C. D. A
3. D. C. A. B
4. C. D. B. A 53622817002.2 53622817003.3 53622817004.4

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 179

*UGC NET Nov 2020, original Q132*

> Given below are two statements: Statement I: Bezier curves are curves that interpolate all of their control points. Statement II: A cubic bezier curve has four control points. In the light of the above statements, choose the correct answer from the options given below

**Options**

1. Both Statement I and Statement II are true
2. Both Statement I and Statement Il are false
3. Statement I is correct but Statement Il is false
4. Statement I is incorrect but Statement Il is true. 53622817026.2 53622817027.3 53622817028.4

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 180

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

#### Question 181

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

#### Question 182

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

#### Question 183

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

#### Question 184

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

#### Question 185

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

---

#### Question 186

*UGC NET Aug 2024, original Q55*

> #include<stdio.h> void main() int arr|] = (1, 2, 3, 4, 5); int *p= arr; printf(" %d", , *p++); printf(" %d", *(p+1)); Find the output of the above code?

**Options**

1. 1,2
2. 1, 3
3. 2, 3
4. 14

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 187

*UGC NET Aug 2024, original Q57*

> #include<iostream.h> using namespace std; void swap(int &x, int &y) int temp=x; x = y; y = temp; int main() int a = 5, b=10; swap(a,b); swap(a,b); cout<<a<<" " <<b; return 0; What will be the output of above code?

**Options**

1. 5, 10
2. 10,5
3. 5,5
4. 10, 10 39/101

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 188

*UGC NET Aug 2024, original Q70*

> Which of the following is correct way to declare a functional pointer in C ?

**Options**

1. int *func (int, int)
2. int (*func) (int, int)
3. int (func*) (int, int)
4. int *func* (int, int)

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 189

*UGC NET Aug 2024, original Q71*

> What will be the output of the following C code? #include<stdio.h> void main() int arr[5] = (10, 20, 30, 40, 50); int *p= (int) (&arr+ 1); printf(" %d%d", *(arr + 1), *(p -1));

**Options**

1. 10 50
2. 20 50
3. 30 40
4. 20 40

**Chapter foundations**

This question belongs to the ideas covered by **3-D Object Representation, Geometric Transformations and Viewing**. Revise these foundations: Polygon and Quadric Surfaces; Spline Representation; Bezier and B-Spline Curves and Surfaces; Illumination Models; Polygon Rendering; Viewing Pipeline and Coordinates; Projection Transforms; Clipping.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For 3-D Object Representation, Geometric Transformations and Viewing questions: For code, make a variable-and-memory table and evaluate sequence points carefully. For graphics, use homogeneous matrices and preserve transformation order. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

## Coverage and quality notes

- Recovered question blocks in this unit: **189**
- Chapter placements with direct keyword support: **169**
- Chapter placements needing manual review: **20**
- Questions with validated answers in this guide: **12**
- OCR may flatten mathematical notation, tables, code indentation, and figures. Full audit references are retained in the structured data.
- Some combined Paper 1/Paper 2 scans and older papers lack a trustworthy embedded key. Such questions remain pending rather than receiving guessed answers.

---

[Back to contents](#contents) · [All units](README.md) · [Project home](../README.md)

