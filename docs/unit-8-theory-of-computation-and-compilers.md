# Unit 8: Theory of Computation and Compilers

[Project home](../README.md) · [All units](README.md) · [Official syllabus](syllabus.md)

## Contents

- [How to use this guide](#status-and-use)
- [Unit-wide exam playbook](#unit-wide-exam-playbook)
- [1. Theory of Computation](#chapter-1)
- [2. Regular Language Models](#chapter-2)
- [3. Context-Free Language](#chapter-3)
- [4. Turing Machines](#chapter-4)
- [5. Unsolvable Problems and Computational Complexity](#chapter-5)
- [6. Syntax Analysis](#chapter-6)
- [7. Semantic Analysis](#chapter-7)
- [8. Runtime System](#chapter-8)
- [9. Intermediate Code Generation](#chapter-9)
- [10. Code Generation and Optimization](#chapter-10)
- [Coverage and quality notes](#coverage-and-quality-notes)

## Status and use

This guide contains all **220 question blocks currently recoverable and assigned to Unit 8** from the local UGC NET archive. Questions are arranged chapter-wise and numbered continuously through the unit.

> [!WARNING]
> This is a working extraction inventory, not a complete solved guide. **0 answers are validated and 220 remain pending** in this unit. Some unit and chapter placements use fallback routing, and OCR or missing figures can make questions incomplete.

Use this file for question discovery and broad chapter revision. The chapter notes and exam methods are general, not question-specific solutions. Full source paths, PDF pages and classification states remain in the structured data for auditing.

## Unit-wide exam playbook

- **Core idea:** Classify the language or grammar before selecting DFA/NFA, PDA/CFG, TM, parser, or compiler analysis.
- **Method:** For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments.
- **Rules/formulas:** Regular languages are closed under union, intersection and complement. LL(1) table entries must be conflict-free. LR items encode viable prefixes.
- **Frequent traps:** The pumping lemma proves non-regularity but not regularity; ambiguity differs from left recursion; recursive languages differ from recursively enumerable languages.

## Chapter-wise concepts and PYQs

<a id="chapter-1"></a>

### 1. Theory of Computation (1 questions)

**What to master:** Formal Language; Non-Computational Problems; Diagonal Argument; Russell's Paradox.

**Exam lens:** Classify the language or grammar before selecting DFA/NFA, PDA/CFG, TM, parser, or compiler analysis.

**Reusable method:** For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments.

**High-yield rules:** Regular languages are closed under union, intersection and complement. LL(1) table entries must be conflict-free. LR items encode viable prefixes.

**Common traps:** The pumping lemma proves non-regularity but not regularity; ambiguity differs from left recursion; recursive languages differ from recursively enumerable languages.

---

#### Question 1

*UGC NET Dec 2019, original Q108*

> According to Dempster-Shafer theory for uncertainty management. Personal Exam Guic

**Options**

1. Bel(A) + Bel(-A) ≤1
2. Bel(A) + Bel(-A) ≥1
3. Bel(A) + Bel(-A) =1
4. Bel(A) + Bel(-A) = 0 Where Bel(A) denotes Belief of event A. 61547541130. 2 61547541131.3 61547541132. 4

**Chapter foundations**

This question belongs to the ideas covered by **Theory of Computation**. Revise these foundations: Formal Language; Non-Computational Problems; Diagonal Argument; Russell's Paradox.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Theory of Computation questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-2"></a>

### 2. Regular Language Models (30 questions)

**What to master:** DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam lens:** Classify the language or grammar before selecting DFA/NFA, PDA/CFG, TM, parser, or compiler analysis.

**Reusable method:** For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments.

**High-yield rules:** Regular languages are closed under union, intersection and complement. LL(1) table entries must be conflict-free. LR items encode viable prefixes.

**Common traps:** The pumping lemma proves non-regularity but not regularity; ambiguity differs from left recursion; recursive languages differ from recursively enumerable languages.

---

#### Question 2

*UGC NET June 2010, Paper II, original Q3*

> “My Lafter Machin (MLM) recognizes the following strings : (i) a (ii) aba (iii) abaabaaba (iv) abaabaabaabaabaabaabaabaaba Using this as an information, how would you compare the following regular expressions ? (i) (aba) 3x (ii) a.(baa)3 x–1. ba (iii) ab.(aab). 3x–1.a

**Options**

- **A.** (ii) and (iii) are same, (i) is different.
- **B.** (ii) and (iii) are not same.
- **C.** (i), (ii) and (iii) are different.
- **D.** (i), (ii) and (iii) are same.

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 3

*UGC NET Dec 2013, Paper II, original Q28*

> Given the following statements : S 1 : If L is a regul ar language then the language {uv | u ∈ L, v ∈ LR} is also regular. S 2 : L = {ww R} is regular language. Which of the following is true ?

**Options**

- **A.** S 1 is not correct and S 2 is not correct.
- **B.** S 1 is not correct and S2 is correct.
- **C.** S 1 is correct and S2 is not correct.
- **D.** S 1 is correct and S2 is correct.

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 4

*UGC NET Dec 2013, Paper III, original Q16*

> Match the following with respect to programming languages : List – I List – II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Structured Language i. JAVA
> - **B.** Non-structured Language ii. BASIC
> - **C.** Object Oriented Programming Language iii. PASCAL
> - **D.** Interpreted Programming Language iv. FORTRAN Codes : a b c d

**Options**

- **A.** iii iv i ii
- **B.** iv iii ii i
- **C.** ii iv i iii
- **D.** ii iii iv i

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 5

*UGC NET Dec 2014, Paper III, original Q23*

> Given two languages : L 1 = {(ab) n a k | n > k, k ≥ 0} L 2 = {a n b m | n ≠ m} Using pumping lemma for regular language, it can be shown that

**Options**

- **A.** L 1 is regular and L 2 is not regular.
- **B.** L 1 is not regular and L 2 is regular.
- **C.** L 1 is regular and L 2 is regular.
- **D.** L 1 is not regular and L 2 is not regular.

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 6

*UGC NET Dec 2014, Paper III, original Q24*

> Regular expression for the complement of language L = {a n b m | n ≥ 4, m ≤ 3} is

**Options**

- **A.** (a + b)* ba(a + b)*
- **B.** a* bbbbb*
- **C.** ( λ + a + aa + aaa)b* + (a + b)* ba(a + b)*
- **D.** None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 7

*UGC NET June 2015, Paper III, original Q20*

> The regular expression corresponding to the language L where I = x € 10, 1)* | x ends with 1 and does not contain substring 00 is :

**Options**

1. (1 + 01)* (10 + 01)
2. (1 + 01)* 01
3. (1 + 01)* (1 + 01)
4. (10 + 01)* 01

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 8

*UGC NET July 2016, Paper II, original Q31*

> The number of strings of length 4 that are generated by the regular expression (0|∈)1+2* (3| ∈), where | is an alternation characte r, {+, *} are quantif ication characters, and ∈ is the null string, is :

**Options**

1. 08
2. 10
3. 11
4. 12

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 9

*UGC NET July 2016, Paper III, original Q22*

> The symmetric difference of two sets S 1 and S2 is defined as S 1 s S2 = {x|x ∈ S1 or x ∈ S2, but x is not in both S1 and S2} The nor of two languages is defined as nor (L 1, L2) = {w|w |∈L1 and w |∈ L2}. Which of the following is correct ?

**Options**

1. The family of regular languages is clos ed under symmetric difference but not closed under nor.
2. The family of regular languages is cl osed under nor but not closed under symmetric difference.
3. The family of regular languages are cl osed under both symmetric difference and nor.
4. The family of regular languages are not closed under both symmetric difference and nor.

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 10

*UGC NET July 2016, Paper III, original Q24*

> Consider the following two languages : L 1 = {0i1j| gcd (i, j) = 1} L 2 is any subset of 0*. Which of the following is correct ?

**Options**

1. L 1 is regular and L*2 is not regular
2. L 1 is not regular and L*2 is regular
3. Both L 1 and L*2 are regular languages
4. Both L 1 and L*2 are not regular languages

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 11

*UGC NET Jan 2017, Paper II, original Q31*

> Which of the following strings would match the regular expression : p+ [3 – 5] ∗ [xyz] ? I. p443y II. p6y III. 3 xyz IV. p35z V. p353535 x VI. ppp5

**Options**

1. I, III and VI only
2. IV, V and VI only
3. II, IV and V only
4. I, IV and V only

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 12

*UGC NET Jan 2017, Paper III, original Q19*

> Which of the following are not regular ?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Strings of even number of a’s.
> - **B.** Strings of a’s, whose length is a prime number.
> - **C.** Set of all palindromes made up of a’s and b’s.
> - **D.** Strings of a’s whose le ngth is a perfect square.

**Options**

1. (A) and (B) only
2. (A), (B) and (C) only
3. (B), (C) and (D) onl y
4. (B) and (D) only

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 13

*UGC NET Dec 2018, original Q82*

> Consider the language L given by L = (2nk | k> 0, and n is non-negative integer number) The minimum number of states of finite automaton which accepts the language L is . n +1 n(n+1) 91394342327. 2 91394342328. 2n Single Die Question pion No 0,730 Orientaion Vetype: MCQ

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 14

*UGC NET Dec 2018, original Q88*

> Which of the following problems is decidable for recursive languages (L) ? . Is L=$? 91394342350 Is w e L, where w is a string? Is L= 2*? 91394342351. 91394342352. Is L = R, where R is a given regular set ? Single in Duet 0 pies No 009130 031078 on Vent Type: MCQ Option Sinfling: Yes Display Question Namber: Yes Correct Marks: 2 Wrong Marks: 0 Which of the following problems is decidable for recursive languages (L)? . Is L=$? 91394342350. Is w e L, where w is a string?

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 15

*UGC NET Dec 2019, original Q94*

> Consider the language L = fa"b*-3 | n > on on 2= {a, b}. Which one of the following grammars generates the language L?

**Options**

1. S→aAla. A →aAb|6
2. S A → aAb |2
3. S → aaaA|a. A → aAb | 2
4. S → aaaA. A → aAb|2 61547541074.2 61547541075. 3 61547541076.4

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 16

*UGC NET Dec 2019, original Q96*

> Consider [ = {w. x} and T = {x. y. z}. Define homomorphism h by : h(x) = xzy h(w) = zxyy If L is the regular language denoted by r = (w +x*)(ww)*, then the regular language h(L) is given by

**Options**

1. (2x yy +xzy) (2x yy)
2. zyy + (azy)* )(zxyy zxyy)*
3. (zxyy + xzy) (zxyy)*
4. zxyy + (xzy) (zxyy zxyy) 61547541082. 2 61547541083. 3 61547541084. 4

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 17

*UGC NET Dec 2019, original Q98*

> Consider the following languages : [y = {a"b"*}u {a"b™ c™}. n. m 20 Iz = suw" [w e {a. b} +) Where R represents reversible operation. Which one of the following is (are) inherently ambiguous language(s)?

**Options**

1. only Ly
2. only In
3. both Ly and La
4. neither L, nor Lz 61547541090. 2 61547541091. 3 61547541092.4

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 18

*UGC NET June 2019, original Q125*

> How many states are there in a minimum state automata equivalent to regular expression given below? Regular expression is a *b(a+b) 1. 1 2. 2 3. 3 4

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 19

*UGC NET Nov 2020, original Q78*

> Let Ly and L2 be languages over 2 = (a, b) represented by the regular expressions (a' + b)" and (a +b)* respectively. Which of the following is true with respect to the two languages?
>
> **Additional extracted choices — check the source page:**
>
> 1. 4 Ch
> 2. 42 CL
> 3. _Missing in extracted text_
> 4. 404g = ф 53622816810.2 53622816811.3 53622816812. 4

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 20

*UGC NET Nov 2020, original Q129*

> Consider the following regular expressions: (a) r = a(b + a)* (b) s= a(a + b)* (e) t = aa b Choose the correct answer from the options given below based on the relation between the languages generated by the regular expressions above:

**Options**

1. L(r)c L(s) c L(t)
2. L(r) = L(s) = L(t)
3. L(r) = L(t) = L(s)
4. (s) = L(t) = L(r) 53622817014.2 53622817015.3 53622817016. 4

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 21

*UGC NET Nov 2021, original Q31*

> Which of the following languages are not regular? A. L={ (01) 0 | n > k, k>=0 } B. L={ c b a | n >= 0, k>=0 } C. L={ 0 1 | n≠k } Choose the correct answer from the options given below:

**Options**

1. A and B only
2. A and C only
3. B and C only
4. A, B and C

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 22

*UGC NET Nov 2021, original Q36*

> Find the regular expression for the language accepted by the automata given below. n k n k n+k n k 1 n n m 2 n m m 3 n n n 3 1 2 1 2 3 1 2 3 1 3

**Options**

1. (aa (a+b)ab)
2. (a+b)ab(ab+bb+ aa (a+b)ab)
3. a ab(ab+bb+ aa (a+b)ab)
4. a (a+b)ab(ab+bb+ aa (a+b)ab)

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 23

*UGC NET Dec 2022 session, 11 Mar 2023 Shift 2, original Q1*

> No.2 The transition function '8' in multi-tape Turing machine is defined as: 1.8:20× Fk → 2º× [k× {L, R, S}k 2.8:Q×Q×k→Q×Qx[*×(L,R,S}k 4.8:Q×[K×29→Q×[*×29×(L,R,S}k

**Options**

1. 1
2. 2
3. 3
4. 4 1 3[Option ID=394151 SID: 187030 In Pumping Lemma for regular languages, to say a language is satisfying pumping lemma, what is the minimum length of 'y' if you consider the string as 'xyz'. 1. n 2.2 3.1 4. 0 (1) 1 (2) 2 (4) 4 (3) 3 i Option 10-39418

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 24

*UGC NET Aug 2024, original Q84*

> 40 software professionals were interviewed for a job. 25 knew PYTHON 20 knew JAVA and 7 knew neither language. How many knew both languages?

**Options**

1. 20
2. 53
3. 10
4. 88

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 25

*UGC NET Aug 2024, original Q113*

> Which of the following languages can be recognized by Non-Deterministic Finite Automata (NFA) but cannot be recognized by Deterministic Finite Automata (DFA) ?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** L, = (we (0, 1)* | the length of w is even)
> - **B.** L2 = (we (0, 1)* | the length of w is odd}
> - **C.** L3 = (we (0, 1)* | all O's come before all I's in w}
> - **D.** L4 = (wE (0, 1)* | w contains an equal number of O's and 1's] (E) L5 = (we (0, 1)* | all I's come before all O's in wj Choose the correct answer from the options given below :

**Options**

1. (A) and (B) Only
2. (B) and (C) Only
3. (C) and (D) Only
4. (D) and (E) Only 73/101

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 26

*UGC NET June 2025, original Q82*

> Consider the following DFA Which of the following NFA is valid for the given DFA? 1 2 3 42558919381.2 42558919382. 3 42558919383.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 27

*UGC NET Dec 2025 session (Jan 2026), original Q99*

> Question Number : 99

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 28

*UGC NET Dec 2025 session (Jan 2026), original Q101*

> Question Number : 101

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 29

*UGC NET Dec 2025 session (Jan 2026), original Q103*

> Question Number : 103

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 30

*UGC NET Dec 2025 session (Jan 2026), original Q105*

> Question Number: 105 = L(r]) UL(12) C. L(11))=L(11) D. L(1 *) = (L(ry))* Choose the correct answer from the options given below:

**Options**

1. A & B Only
2. B, C & D Only
3. A, C & D Only
4. A, B, C & D 6119878818.2 6119878819.3 6119878820.4

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 31

*UGC NET Dec 2025 session (Jan 2026), original Q108*

> Question Number: 108 and y € (VUT)* D. Greibach Normal Form IV. A → BC or A → a, where A, B, C are in V and a is in T. Choose the correct answer from the options given below:
>
> **Additional extracted choices — check the source page:**
>
> 1. A-II, B-III, C-I, D-IV
> 2. A-I, B-III, C-II, D-IV
> 3. A-II, B-III, C-IV, D-I
> 4. A-II, B-IV, C-1, D-III 6119878830.2 6119878831.3 6119878832.4 uestion Number : 108 * and y € (VUT)* D. Greibach Normal Form IV. A → BC or A → a, where A, B, C are in V and a is in T. Choose the correct answer from the options given below:

**Options**

1. A-II, B-III, C-1, D-IV
2. A-I, B-III, C-II, D-IV
3. A-II, B-III, C-IV, D-I
4. A-II, B-IV, C-I, D-III 6119878830.2 6119878831.3 6119878832.4

**Chapter foundations**

This question belongs to the ideas covered by **Regular Language Models**. Revise these foundations: DFA; NFA; Equivalence; Regular Languages, Grammars and Expressions; Properties; Pumping Lemma; Non-Regular Languages; Lexical Analysis.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Regular Language Models questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-3"></a>

### 3. Context-Free Language (69 questions)

**What to master:** PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam lens:** Classify the language or grammar before selecting DFA/NFA, PDA/CFG, TM, parser, or compiler analysis.

**Reusable method:** For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments.

**High-yield rules:** Regular languages are closed under union, intersection and complement. LL(1) table entries must be conflict-free. LR items encode viable prefixes.

**Common traps:** The pumping lemma proves non-regularity but not regularity; ambiguity differs from left recursion; recursive languages differ from recursively enumerable languages.

---

#### Question 32

*UGC NET Dec 2009, Paper II, original Q34*

> Contex-free Grammar (CFG) can be recognized by

**Options**

- **A.** Finite state automata
- **B.** 2-way linear bounded automata
- **C.** push down automata
- **D.** both (B) and (C)

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 33

*UGC NET June 2010, Paper II, original Q34*

> Which of the following is the most general phase structured grammar ?

**Options**

- **A.** Regular
- **B.** Context-sensitive
- **C.** Context free
- **D.** None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 34

*UGC NET Dec 2013, Paper II, original Q26*

> Given the following statements : S 1 : SLR uses follow information to guide reductions. In case of LR and LALR parsers, the look- aheads are associated with the items and they make use of the left context available to the parser. S 2 : LR grammar is a larger sub- class of context free grammar as compared to that SLR and LALR grammars. Which of the following is true ?

**Options**

- **A.** S 1 is not correct and S 2 is not correct.
- **B.** S 1 is not correct and S 2 is correct.
- **C.** S 1 is correct and S 2 is not correct.
- **D.** S 1 is correct and S2 is correct.

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 35

*UGC NET Dec 2013, Paper II, original Q27*

> The context free grammar for the language L = {a n bm | n ≤ m + 3, n ≥ 0, m ≥ 0} is

**Options**

- **A.** S → aaa A; A → aAb | B, B → Bb | λ
- **B.** S → aaaA| λ, A → aAb | B, B → Bb | λ
- **C.** S → aaaA | aa A | λ, A → aAb | B, B → Bb| λ
- **D.** S → aaaA | aa A | aA | λ, A → aAb | B, B → Bb | λ

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 36

*UGC NET Dec 2013, Paper III, original Q40*

> Pumping lemma for context-free languages states : Let L be an infinite context free language. Then there exists some positive integer m such that any w ∈ L with |w| ≥ m can be decomposed as w = uv xy Z with |v xy| _________ and |vy| _________ such that uv .z xy .z Z ∈ L for all .z = 0, 1, 2, ....... .

**Options**

- **A.** ≤ m, ≤ 1
- **B.** ≤ m, ≥ 1
- **C.** ≥ m, ≤ 1
- **D.** ≥ m, ≥ 1

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 37

*UGC NET Dec 2013, Paper III, original Q41*

> The Greibach normal form grammar for the language L = {an bn + 1 | n ≥ 0} is

**Options**

- **A.** S → a SB, B → bB | λ
- **B.** S → a SB, B → bB | b
- **C.** S → a SB | b, B → b
- **D.** S → a Sb | b

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 38

*UGC NET Dec 2013, Paper III, original Q42*

> Given the following statements : S 1 : Every context-sensitive language L is recursive. S 2 : There exists a recursive language that is not context sensitive. Which statement is correct ?

**Options**

- **A.** S 1 is not correct and S 2 is not correct.
- **B.** S 1 is not correct and S 2 is correct.
- **C.** S 1 is correct and S 2 is not correct.
- **D.** S 1 is correct and S2 is correct.

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 39

*UGC NET June 2013, Paper III, original Q36*

> The grammar with production rules S → aSb |SS|λ generates language L given by :

**Options**

- **A.** L = {w ∈{a, b}* | na(w) = nb(w) and n a(v) ≥ n b(v) where v is any prefix of w}
- **B.** L = {w ∈{a, b}* | na(w) = nb(w) and n a(v) ≤ n b(v) where v is any prefix of w}
- **C.** L = {w ∈{a, b}* | n a(w) ≠ nb(w) and na(v) ≥ nb(v) where v is any prefix of w}
- **D.** L = {w ∈{a, b}* | na(w) ≠ nb(w) and n a(v) ≤ n b(v) where v is any prefix of w}

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 40

*UGC NET June 2013, Paper III, original Q38*

> For every context free grammar (G) there exists an algorithm that passes any w ∈ L ( G ) i n n u m b e r o f s t e p s proportional to

**Options**

- **A.** ln|w
- **B.** w
- **C.** w| 2
- **D.** w| 3

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 41

*UGC NET June 2013, Paper III, original Q39*

> Match the following :
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Context sensitive language i. Deterministic finite automation
> - **B.** Regular grammar ii. Recursive enumerable
> - **C.** Context free grammar iii. Recursive language
> - **D.** Unrestricted grammar iv. Pushdown automation Codes : a b c d

**Options**

- **A.** ii i iv iii
- **B.** iii iv i ii
- **C.** iii i iv ii
- **D.** ii iv i iii

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 42

*UGC NET June 2013, Paper III, original Q40*

> The statements s1 and s2 are given as : s1 : Context sensitive languages are closed under intersection, concatenation, substitution and inverse homomorphism. s2 : Context free languages are closed under complementation, substitution and homomorphism. Which of the following is correct statement ?

**Options**

- **A.** Both s1 and s2 are correct.
- **B.** s1 is correct and s2 is not correct.
- **C.** s1 is not correct and s2 is correct.
- **D.** Both s1 and s2 are not correct.

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 43

*UGC NET Dec 2014, Paper II, original Q35*

> The following Context-Free Grammar (CFG) : S → aB | bA A → a | as | bAA B → b | bs | aBB will generate

**Options**

- **A.** odd numbers of a’s and odd numbers of b’s
- **B.** even numbers of a’s and even numbers of b’s
- **C.** equal numbers of a’s and b’s
- **D.** different numbers of a’s and b’s

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 44

*UGC NET Dec 2014, Paper III, original Q22*

> The pushdown automation M = ({q 0, q 1, q 2}, {a, b}, {0, 1}, δ, q 0, 0, {q 0}) with δ(q 0, a, 0) = {(q 1, 10)} δ(q 1, a, 1) = {(q 1, 11)} δ(q 1, b, 1) = {(q 2, λ)} δ(q 2, b, 1) = {(q 2, λ)} δ(q 2, λ, 0) = {(q 0, λ)} Accepts the language

**Options**

- **A.** L = {a n b m | n, m ≥ 0}
- **B.** L = {a n b n | n ≥ 0}
- **C.** L = {a n b m | n, m > 0}
- **D.** L = {a n b n | n > 0}

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 45

*UGC NET Dec 2014, Paper III, original Q61*

> Given the recursively enumerable language (L RE ), the context sensitive language (L CS ), the recursive language (L REC ), the context free language (L CF ) and deterministic context free language (L DCF ). The relationship between these families is given by

**Options**

- **A.** L CF ⊆ L DCF ⊆ L CS ⊆ L RE ⊆ L REC
- **B.** L CF ⊆ L DCF ⊆ L CS ⊆ L REC ⊆ L RE
- **C.** L DCF ⊆ L CF ⊆ L CS ⊆ L RE ⊆ L REC
- **D.** L DCF ⊆ L CF ⊆ L CS ⊆ L REC ⊆ L RE

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 46

*UGC NET Dec 2014, Paper III, original Q63*

> According to pumping lemma for context free languages : Let L be an infinite context free language, then there exists s ome positive integer m such that any w ∈ L with | w | ≥ m can be decomposed as w = u v x y z

**Options**

- **A.** with | v xy | ≤ m such that uv i xyi z ∈ L for all i = 0, 1, 2
- **B.** with | v xy | ≤ m, and | vy | ≥ 1, such that uv i xyi z ∈ L for all i = 0, 1, 2, …….
- **C.** with | v xy | ≥ m, and | vy | ≤ 1, such that uv i xyi z ∈ L for all i = 0, 1, 2, …….
- **D.** with | v xy | ≥ m, and | vy | ≥ 1, such that uv i xyi z ∈ L for all i = 0, 1, 2, …….

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 47

*UGC NET Dec 2015, Paper II, original Q43*

> Which of the following statements is false?

**Options**

1. Top-down parsers are LL parsers where first L stands for left - to - right scan and second L stands for a leftmost derivation.
2. (000)* is a regular expression that matches only strings containing an odd number of zeroes, including the empty string.
3. Bottom-up parsers are in the LR family, where L stands for left - to - right scan and R stands for rightmost derivation.
4. The class of context - free languages is closed under reversal. That is, if L is any context - free language, then the language LR = (WR: weL) is context - free.

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 48

*UGC NET Dec 2015, Paper III, original Q22*

> The family of context sensitive languages is under union and _under reversal.

**Options**

1. closed, not closed
2. not closed, not closed
3. closed, closed
4. not closed, closed

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 49

*UGC NET Dec 2015, Paper III, original Q23*

> Match the following : List - I List - II (a) {a" b" | n > 0} is a deterministic (i) but not recursive language context free language The complement of (a" braIn >03 (ii) but not context free language is a context free language (c) {a" b" an) is context sensitive language (ili) but can not be accepted by a deterministi pushdown automation (d) L is a recursive language (iv) but not regular Codes: (a) (b)(c) d)

**Options**

1. (i) (ii) (iii) (iv)
2. (ii) (iv) (iti)
3. (iv) (iii) (ii) (i)
4. (iv) (iii) (i) (ii)

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 50

*UGC NET Dec 2015, Paper III, original Q24*

> The language of all non-null strings of a's can be defined by a context free grammar as follow: S → a S|S a l a The word a can be generated by different trees.

**Options**

1. Two
2. Three
3. Four
4. Five D-8715 5 Paper-III

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 51

*UGC NET Dec 2015, Paper III, original Q26*

> The context free grammar given by S → XYX x→ aX|bX|^ Y → bbb generates the language which is defined by regular expression : (1) (a+b)*bbb (2) abbb(a +b)*

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 52

*UGC NET Dec 2015, Paper III, original Q28*

> Given the following two languages : Ly = fa"ba"|n> 0} L2= (a"ba"bn+1/n> o Which of the following is correct?
>
> **Additional extracted choices — check the source page:**
>
> 1. Ly is context free language and Lz is not context free language
> 2. Ly is not context free language and L, is context free language
> 3. _Missing in extracted text_
> 4. Both Ly and Lz are not context free languages Both Ly and L2 are context free languages

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 53

*UGC NET Dec 2015, Paper III, original Q73*

> Consider a language A defined over the alphabet 2 = 10, 1) as A = 0|21 1^ : n> =0. The expression [n/2| means the floor of n/2, or what you get by rounding n/ 2 down to the nearest integer. Which of the following is not an example of a string in A ?

**Options**

1. 011
2. 0111
3. 0011
4. 001111

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 54

*UGC NET June 2015, Paper II, original Q33*

> If all the production rules have single non - terminal symbol on the left side, the grammar defined is :

**Options**

1. context free grammar
2. context sensitive grammar
3. unrestricted grammar
4. phrase grammar

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 55

*UGC NET June 2015, Paper III, original Q19*

> Minimal deterministic finite automaton for the language L= (0"|n ≥ 0, n = 4} will have :

**Options**

1. 1 final state among 5 states
2. 4 final states among 5 states
3. 1 final state among 6 states
4. 5 final states among 6 states

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 56

*UGC NET June 2015, Paper III, original Q21*

> The transition function for the language L = (w|n, (W) and n(W) are both odd} is given by : 8 (90, a) = 91 ; § (90, b) = 92 8 (91, a) = 90 ; 8 (91, b) = 93 б (92, а) = 93 ; б (92, b) = 90 8 (93, a) = 92 ; 8 (93, b) = 91 The initial and final states of the automata are :

**Options**

1. 9o and go respectively
2. 9o and q1 respectively
3. 9o and 92 respectively
4. 9o and q3 respectively J-8715 5 Paper-II

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 57

*UGC NET June 2015, Paper III, original Q61*

> A context free grammar for I = \ W|no (W) > n1 (W)} is given by :

**Options**

1. S→0 0S 1SS
2. 5→0515 055155|01
3. S→00S 1SS S15 SS1
4. S→0S|1S|0|1

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 58

*UGC NET July 2016, Paper II, original Q11*

> Given i = 0, j = 1, k = –1 x = 0.5, y = 0.0 What is the output of the following expression in C language ? x * y < i + j || k

**Options**

1. – 1
2. 0
3. 1
4. 2

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 59

*UGC NET July 2016, Paper III, original Q55*

> Let L be the language generated by re gular expression 0*10* and accepted by the deterministic finite automata M. Consider the relation R M defined by M. As all states are reachable from the start state, RM has _____ equivalence classes.

**Options**

1. 2
2. 4
3. 5
4. 6

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 60

*UGC NET July 2016, Paper III, original Q56*

> Let L = {0 n1n|n ≥ 0} be a context free language. Which of the following is correct ?

**Options**

1. –L is context free and Lk is not context free for any k ≥ 1.
2. –L is not context free and Lk is context free for any k ≥ 1.
3. Both –L and Lk is for any k ≥ 1 are context free.
4. Both –L and Lk is for any k ≥ 1 are not context free.

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 61

*UGC NET Jan 2017, Paper III, original Q22*

> Let G = (V, T, S, P) be a context-free gramma r such that every one of its productions is of the form A → v, with | v| = K > 1. The deriva tion tree for any W ∈ L(G) has a height h such that

**Options**

1. log K|W| ≤ h ≤ logK⎝⎜ ⎛ ⎠⎟ ⎞ |W| – 1 K – 1
2. log K|W| ≤ h ≤ logK(K|W|)
3. log K|W| ≤ h ≤ K logK|W
4. log K|W| ≤ h ≤ ⎝⎜ ⎛ ⎠⎟ ⎞ |W| – 1 K – 1

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 62

*UGC NET Jan 2017, Paper III, original Q23*

> Given the following two languages : L 1 = {an bn | n ≥ 0, n ≠ 100} L 2 = {w ∈ {a, b, c}*| na(w) = nb(w) = nc(w)} Which of the following options is correct ?

**Options**

1. Both L 1 and L2 are not context free language
2. Both L 1 and L2 are context free language.
3. L 1 is context free language, L2 is not context free language.
4. L 1 is not context free language, L2 is context free language.

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 63

*UGC NET Jan 2017, Paper III, original Q61*

> Given the following two statements : A. L = {w|n a(w) = nb(w)} is deterministic context free language, but not linear. B. L = {a n bn} ∪ {an b2n} is linear, but not deterministic context free language. Which of the following options is correct ?

**Options**

1. Both (A) and (B) are false.
2. Both (A) and (B) are true.
3. (A) is true, (B) is false.
4. (A) is false, (B) is true.

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 64

*UGC NET Jan 2017, Paper III, original Q63*

> Which of the following statements is false ?

**Options**

1. Every context-sensitiv e language is recursive.
2. The set of all languages that are no t recursively enumerable is countable.
3. The family of recursively enumer able languages is closed under union.
4. The families of recursively enumerable a nd recursive languages are closed under reversal.

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 65

*UGC NET Nov 2017, Paper II, original Q34*

> Which of the following statements is/are TRUE ? (a) The grammar S → SS /c4994 a is ambiguous. (Where S is the start symbol) (b) The grammar S → 0S1 /c4994 01S /c4994 /c=27 is ambiguous. (The special symbol /c=27 represents the empty string) (Where S is the start symbol) (c) The grammar (Where S is the start symbol) S → T/U T → x S y /c4994 xy /c4994 /c=27 U → yT generates a language consisting of the string yxxyy.

**Options**

1. Only (a) and (b) are TRUE.
2. Only (a) and (c) are TRUE.
3. Only (b) and (c) are TRUE.
4. All of (a), (b) and (c) are TRUE.

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 66

*UGC NET Dec 2018, original Q84*

> Consider the following two languages : L1 = {× | for some y with |y| = 2Ix, x e Land Lis regular languagel Lz = ix | for some y such that |x| = |y|, xy e L and L is regular language) Which one of the following is correct? Code: . Only Ly is regular language Exam Guide Only Lz is regular language 91394342334. Both L1 and La are regular languages 91394342335. 91394342336. Both Ly and Lz are not regular languages Single One Question gion No Digion Orient on: Vet Type: MCQ

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 67

*UGC NET Dec 2018, original Q85*

> Consider the following languages : Which one of the following is correct? Code: Options: Only Ly is context free language 91394342337. Guide 91394342338 Only Lz is context free language Both Ly and Lz are context free languages 91394342339. 91394342340. Both Ly and Lz are not context free languages Single Line Onetion option No On Oriense On: Ven Type: MCQ

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 68

*UGC NET Dec 2018, original Q86*

> Consider R to be any regular language and L1, Lz be any two context-free languages. Which one of the following is correct? . Li is context free (Ly U Lz) - Ris context free 91394342342. 91394342343. Ly n Lz is context free 91394342344. Ly - R is context free

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 69

*UGC NET Dec 2018, original Q87*

> Consider the following problems: Exam (i) Whether a finite state automaton halts on all inputs ? (ii) Whether a given context free language is regular ? (i) Whether a Turing machine computes the product of two numbers? Which one of the following is correct? Code: . Only (i) and (ill) are undecidable problems Only (ii) and (iii) are undecidable problems 91394342346. Only (i) and (il) are undecidable problems 91394342347. 91394342348 (i), (i) and (ili) are undecidable problems ingle Line Question Option: No

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 70

*UGC NET July 2018, Paper II, original Q34*

> Pushdown automata can recognize language generated by_________.

**Options**

1. Only context free grammar
2. Only regular grammar
3. Context free grammar or regular grammar
4. Only context sensitive grammar

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 71

*UGC NET July 2018, Paper II, original Q35*

> To obtain a string of n Terminals from a given Chomsky normal form grammar, the number of productions to be used is :

**Options**

1. 2n−1
2. 2n
3. n+1
4. n2

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 72

*UGC NET July 2018, Paper II, original Q37*

> Context sensitive language can be recognized by a :

**Options**

1. Finite state machine
2. Deterministic finite automata
3. Non-deterministic finite automata
4. Linear bounded automata

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 73

*UGC NET July 2018, Paper II, original Q38*

> The set A = { 0n 1n 2n | n = 1, 2, 3, ......... } is an example of a grammar that is :

**Options**

1. Context sensitive
2. Context free
3. Regular
4. None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 74

*UGC NET Dec 2019, original Q95*

> Consider the following grammar: S → 0A |0BB A → 00A |1 B →1B|11C C → B Which language does this grammar generate?

**Options**

1. L((00) * 0 + (11)*1)
2. I(0(11)*+1(00) *)
3. L((00) * 0)
4. L(0(11) *1) 61547541078.2 61547541079.3 61547541080. 4

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 75

*UGC NET Dec 2019, original Q97*

> Consider the following statements with respect to the language I = fa"b"In ≥ 0} S,: L' is context free language Sz: L* is conext-free language for any given k ≥1 Sy: I and L* are context free languages Which one of the following is correct?

**Options**

1. only S, and Sa
2. only S, and S
3. only S, and S3
4. S. S2 and S 61547541086. 2 61547541087.3 61547541088. 4

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 76

*UGC NET Dec 2019, original Q99*

> Let G= (V.T. S. P) be any context-free grammar without any -productions or unit productions. Let K be the maximum number of symbols on the right of any production in P. The maximum number of production rules for any equivalent grammar in Chomsky normal form is given by:

**Options**

1. (K -1)|P|+|T I-1
2. (K-1)|P|+ IT
3. K|PI+|TI-1
4. K|PI+|TI Where I-I denotes the cardinality of the set. 61547541094.2 61547541095. 3 61547541096. 4

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 77

*UGC NET Dec 2019, original Q100*

> Consider the following language families: Ly = The context - free languages L, = The context - sensitive languages Iz = The recursively enumerable languages Ly = The recursive languages Which one of the following options is correct? (3) 61547541098. 2

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 78

*UGC NET June 2019, original Q126*

> Match List-I with List-II : where L: Regular language Iz: Context-free language Iz: Recursive language 14: Recursively enumerable language List-I List-II (a) LULA (i) Context-fiee language (b) LUL, (ii) Recursively enumerable language (iii) Recursive language Choose the correct option from those given below : (a)-(ii); (b)-(i); (c)-(ii) (a) (ii; (b)-(iii); (c) (i) 3. (a)-(ii); (b)-(i); (c)-(ii) (a)-(i); (b)-(ii); (c)-(iii) 64635085840.2 64635085841. 3 64635085842. 4

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 79

*UGC NET Nov 2020, original Q77*

> Consider L = LyN La Where 41 = [0™1"20"1" (m, n≥ 0) 12 = (0"1"2* | m,n, k ≥ 0) Then, the language L is

**Options**

1. Recursively enumerable but not context free
2. Regular
3. Context free but not regular
4. Not recursive 53622816806.2 53622816807.3 53622816808.4

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 80

*UGC NET Nov 2020, original Q79*

> Which of the following statements is true?

**Options**

1. The union of two context free languages is contest free.
2. The intersection of two context free languages is context free.
3. The complement of a context free language is context free.
4. If a language is context free, it can always be accepted by a deterministic pushdown automaton. 53622816814.2 53622816815.3 53622816816.4

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 81

*UGC NET Nov 2020, original Q105*

> Let Gi and G2 be arbitrary context free languages and R an arbitrary regular language. Consider the following problems: (A) Is L(G]) = L(Gz)? (B) Is L(Gz) ≤ L(G,)? (C) Is L(G) = R? Which of the problems are undecidable? Choose the correct answer from the options given below:

**Options**

1. (A) only
2. (B) only
3. (A) and (B) only
4. (A). (B) and (C) 53622816918.2 53622816919,3 53622816920.4 Questiory ner: 105 Question td: 5362284342 Question Type : MCQ Option Shuring : No Is Question Correct Marks: 2 Wrong Marks: 0

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 82

*UGC NET Nov 2020, original Q121*

> Match List I with List II: La: Regular language. LF: Context free language LREc: Recursive language, LRE: Recursively enumerable language. List I List II (A) Recursively Enumerable language D IRECULRE (B) Recursive language (ID IcF ULREC (C) Context Free language Choose the correct answer from the options given below:

**Options**

1. A-II, B-III. C-I
2. A-II, B-I, C-II
3. A-I. B-II, C-III
4. A-II. B-I, C-I 53622816982.2 53622816983.3 53622816984.4

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 83

*UGC NET Nov 2020, original Q137*

> Given below are two statements: Statement I: The problem "Is 41 1L2 =ф? " is undecidable for context sensitive languages Ly and La. Statement II: The problem "Is WeL?" is decidable for context sensitive language L, (where Wis a string). In the light of the above statements, choose the correct answer from the options given below

**Options**

1. Both Statement I and Statement Il are true
2. Both Statement I and Statement II are false
3. Statement I is correct but Statement II is false
4. Statement I is incorrect but Statement Il is true. 53622817046.2 53622817047.3 53622817048.4

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 84

*UGC NET Nov 2021, original Q33*

> Let L = { 0 1 0 | n>=1, m>=1 } L = { 0 1 0 | n>=1, m>=1 } L = { 0 1 0 | n>=1} Which of the following are correct statements?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** L =L L
> - **B.** L and L are context free languages but L is not a context free language
> - **C.** L and L are not context free languages but L is a context free language
> - **D.** L is a subset of L Choose the correct answer from the options given below:

**Options**

1. A and B only
2. A and C only
3. A and D only
4. A only

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 85

*UGC NET Nov 2021, original Q34*

> Given below are two statements Statement I: The family of context free languages is closed under homomorphism Statement II: The family of context free languages is closed under reversal In light of the above statements, choose the correct answer from the options given below

**Options**

1. Both Statement I and Statement II are true
2. Both Statement I and Statement II are false
3. Statement I is true but Statement II is false
4. Statement I is false but Statement II is true

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 86

*UGC NET Nov 2021, original Q37*

> What language is accepted by the pushdown automaton M=({q , q , q2}, {a, b}, {a, b, z}, δ, q , z, {q }) with δ(q , a, a) ={ (q , aa) }; δ(q , b, a) ={(q , ba)} δ(q , a, b) ={ (q , ab) }; δ(q , b, b) ={ (q , bb) } δ(q , a, z) ={ (q , az) }; δ(q , b, z) ={ (q , bz) } δ(q , λ, b) ={ (q , b) }; δ(q , λ, a) ={ (q , a) } δ(q , a, a) ={ (q , λ) }; δ(q , b, b) ={ (q , λ) } δ(q , λ, z) ={ (q , z) }?

**Options**

1. L = { w | n (w) = n (w), w Є {a, b} }}
2. L = { w | n (w) <= n (w), w Є {a, b} }}
3. L = { w | n (w) <= n (w), w Є {a, b} }}
4. L= {ww | w Є {a, b} }

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 87

*UGC NET Oct 2022, original Q13*

> Consider the production rules of grammer G: S→ AbB A → aAb |X B→ bB| A Which of the following language L is generated by grammer G?

**Options**

1. L= (a*b™: ≥0,m >n}
2. I=@"2™: n≥0, m ≥0}
3. I = a"b":n≥m}
4. LI = la"b™: n≥ m.m > 0}

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 88

*UGC NET Oct 2022, original Q16*

> Consider the following NPDA = (go-4-9, \{a.b), (1.=). 5, 40. = (9-3) б(до, а, г) = ((g1, 112)) 5(g1, a, 1) = (g1.111); Which of the following Language L is accepted by NPDA? 1. I = la"b":n≥0} 2. L= a"b?:n ≥0} 3. hE = 10b": n> 0}

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 89

*UGC NET Oct 2022, original Q56*

> Consider the properties of recursively enumerable sets : (A) Finiteness Context Freedom (C) Emptiness Which of the following is true?

**Options**

1. Only (A) and (B) are not decidable
2. Only (B) and (C) are not decidable
3. Only (C) and (A) are not decidable
4. All (A). (B) and (C) are not decidable

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 90

*UGC NET Oct 2022, original Q59*

> Consider the grammer S → sSla. Consider the following statements: The string abababa has (A) two parse trees (B) two left most derivations (C) two right most derivations Which of the following is correct?

**Options**

1. AIl (A). (B) and (C) are true
2. Only (B) is true
3. Only (C) is true
4. Only (A) is true

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 91

*UGC NET Oct 2022, original Q82*

> Consider the following statements about Context Free Language (CFL): Statement I: CFL is closed under homomorphism. Statement II: CFL is closed under complement. Which of the following is correct?

**Options**

1. Statement I is true and Statement II is false
2. Statement II is true and Statement I is false
3. Both Statement I and Statement II are true
4. Neither Statement I nor Statement Il is true

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 92

*UGC NET June 2023, Paper II, original Q33*

> Consider the following language: (+2) L= {wE {a, b,c}*: na(w) + nb/w) = nc(w)} L is

**Options**

- **A.** Context free but not linear
- **B.** Not context free
- **C.** Context free and linear
- **D.** Linear

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 93

*UGC NET June 2023, Paper II, original Q87*

> A. The set of turning machine codes for TM's that accept all inputs that are (+2) palindromes (possible along with some other inputs) is decidable B. The language of codes for TM's M that when started with blank tape, eventually write a 1 somewhere on the tape is undecidable C. The language accepted by a TM M is L (M) is always recursive D. Post's correspondence problem is undecidable Choose the correct answer from the options given below:

**Options**

- **A.** A, B and C only
- **B.** B, C and D only
- **C.** A and C only
- **D.** B and D only

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 94

*UGC NET Aug 2024, original Q53*

> If Ly and Lz are context free languages, which of the following is True about LynLz?

**Options**

1. LynL is context free
2. LynLy is Regular
3. Ly^L_ is Recursively Enumerable
4. LynL, is Context Sensitive

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 95

*UGC NET Aug 2024, original Q102*

> Arrange the following Language Classes in ascending order according to their expressive power, as defined by Chomsky hierarchy :
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Context-free languages
> - **B.** Context-sensitive languages
> - **C.** Regular languages
> - **D.** Unrestricted Grammars Choose the correct answer from the options given below :

**Options**

1. (C), (A), (B), (D)
2. (C), (A), (D), (B)
3. (A), (C), (B), (D)
4. (A), (D), (B), (C)

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 96

*UGC NET Aug 2024, original Q106*

> Which of the following are context free language ?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** (w'xykz'|i+k=j+1, where i, j, k, 1≥ 0}
> - **B.** [w xykz |i=j and k=1, where i, j, k, 1≥ 0)
> - **C.** [w' xyk z'|i=j=k and k#l, where i, j, k, 1≥ 0}
> - **D.** [w xyk z'|i=j=k+1, where i, j, k, 1≥ 0) (E) [wxy* z|i=j=l and k#l, where i, j, k, 1≥ 0} Choose the correct answer from the options given below :

**Options**

1. (A), (B) Only
2. (B), (C) Only
3. (C), (D) Only
4. (D), (E) Only

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 97

*UGC NET Aug 2024, original Q116*

> Which of the following properties correctly describe a Regular Grammar ?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** All production rules are of the form A→xB or A→x, where A and B are non terminal symbols and x is a terminal symbol.
> - **B.** Regular grammars are more powerful than context-free grammars and can express any type of language.
> - **C.** There is a direct correspondence between regular grammar and finite automata.
> - **D.** Regular grammars can generate languages that are not recognised by any type of automata. Choose the correct answer from the options given below :

**Options**

1. (A) and (B) Only
2. (B) and (C) Only
3. (C) and (D) Only
4. (A) and (C) Only

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 98

*UGC NET June 2024, original Q69*

> For the regular languages and context free languages which is not correct ?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** both are closed under union operation
> - **B.** both are closed under concatenation operation
> - **C.** both are closed under intersection operation
> - **D.** both are closed under complementation operation E. both are closed under kleen star operation Choose the most appropriate answer from the options given below :

**Options**

1. A and B Only
2. Band COnly
3. Cand D Only
4. Dand E only

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 99

*UGC NET June 2025, original Q122*

> Which of the following Grammars is/are only Context Free? A S → Ab S → Ab as → aA A → Sa A → a A → a C S → AS D 5 → Ab s → aA S → aA A → a A → a E S → Sb A → Aa A → E Choose the correct answer from the options given below:

**Options**

1. A, B Only
2. C, D Only
3. C, E Only
4. A, B, D, E Only 42558919541.2 42558919542.3 42558919543.4

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 100

*UGC NET Dec 2025 session (Jan 2026), original Q102*

> Question Number : 102

**Chapter foundations**

This question belongs to the ideas covered by **Context-Free Language**. Revise these foundations: PDA and NPDA; CFG; Chomsky and Greibach Normal Forms; Ambiguity; Parse/Derivation Trees; PDA-CFG Equivalence; CFL Properties.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Context-Free Language questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-4"></a>

### 4. Turing Machines (16 questions)

**What to master:** Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam lens:** Classify the language or grammar before selecting DFA/NFA, PDA/CFG, TM, parser, or compiler analysis.

**Reusable method:** For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments.

**High-yield rules:** Regular languages are closed under union, intersection and complement. LL(1) table entries must be conflict-free. LR items encode viable prefixes.

**Common traps:** The pumping lemma proves non-regularity but not regularity; ambiguity differs from left recursion; recursive languages differ from recursively enumerable languages.

---

#### Question 101

*UGC NET June 2012, Paper II, original Q40*

> Consider the following statements : I. Recursive languages are closed under complementation. II. Recursively enumerable languages are closed under union. III. Recursively enumerable languages are closed under complementation. Which of the above statements are true ?

**Options**

- **A.** I only
- **B.** I and II
- **C.** I and III
- **D.** II and III

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 102

*UGC NET Dec 2014, Paper III, original Q11*

> Consider the following statements : I. Re-construction operation used in mixed fragmentation satisfies commuta tive rule. II. Re-construction operation used in vertical fragmentation satisfies c ommutative rule Which of the following is correct ?

**Options**

- **A.** I
- **B.** II
- **C.** Both are correct
- **D.** None of the statements are correct.

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 103

*UGC NET Dec 2014, Paper III, original Q13*

> Which of the following categories of languages do not refer to animation languages ?

**Options**

- **A.** Graphical languages
- **B.** General-purpose languages
- **C.** Linear-list notations
- **D.** None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 104

*UGC NET Dec 2014, Paper III, original Q62*

> Match the following : List – I List – II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Context free grammar i. Linear bounded automaton
> - **B.** Regular grammar ii. Pushdown automaton
> - **C.** Context sensitive grammar iii. Turing machine
> - **D.** Unrestricted grammar iv. Deterministic finite automaton Codes : a b c d

**Options**

- **A.** ii iv iii i
- **B.** ii iv i iii
- **C.** iv i ii iii
- **D.** i iv iii ii

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 105

*UGC NET Dec 2015, Paper III, original Q65*

> Consider a standard additive model consisting of rules of the form of If x is A; AND y is B; THEN z is Ci. Given crisp inputs x= X0, y= Yo, the output of the model is : (1) == EMA, (40) MB, (0) MC, 12) (2) == EMA, (30) MB. (40)

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 106

*UGC NET June 2015, Paper III, original Q62*

> Given the following two statements: Sy: If Ly and Lz are recursively enumerable languages over I, then LyU L, and Lyn Lz are also recursively enumerable. S2: The set of recursively enumerable languages is countable. Which of the following is correct?

**Options**

1. S, is correct and S, is not correct
2. S, is not correct and S2 is correct
3. Both S, and S, are not correct
4. Both S, and S2 are correct

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 107

*UGC NET Jan 2017, Paper III, original Q20*

> Consider the languages L 1 = φ and L2 = {1}. Which one of the following represents L * 1 ∪ L* 2 L* 1 ?

**Options**

1. { ∈}
2. { ∈, 1}
3. φ
4. 1*

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 108

*UGC NET Jan 2017, Paper III, original Q21*

> Given the following statements : (A) A class of languages that is closed under union and complementation has to be closed under intersection. (B) A class of languages that is closed unde r union and intersection has to be closed under complementation. Which of the following options is correct ?

**Options**

1. Both (A) and (B) are false.
2. Both (A) and (B) are true.
3. (A) is true, (B) is false.
4. (A) is false, (B) is true.

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 109

*UGC NET Jan 2017, Paper III, original Q62*

> Which of the following pairs have different expressive power ?

**Options**

1. Single-tape-turing machine and multi-dimensional turing machine.
2. Multi-tape turing machine and multi-dimensional turing machine.
3. Deterministic push down automata and non-deterministic pushdown automata.
4. Deterministic finite automata and Non-deterministic finite automata

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 110

*UGC NET July 2018, Paper II, original Q31*

> Two finite state machines are said to be equivalent if they :

**Options**

1. Have the same number of edges
2. Have the same number of states
3. Recognize the same set of tokens
4. Have the same number of states and edges

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 111

*UGC NET July 2018, Paper II, original Q33*

> A pushdown automata behaves like a Turing machine when the number of auxiliary memory is :

**Options**

1. 0
2. 1
3. 1 or more
4. 2 or more

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 112

*UGC NET July 2018, Paper II, original Q40*

> Consider the following statements( ) : S1 : There exists no algorithm for deciding if any two Turing machines M 1 and M 2 accept the same language. S2 : The problem of determining whether a Turing machine halts on any input is undecidable. Which of the following options is correct ?

**Options**

1. Both S1 and S2 are correct
2. Both S1 and S2 are not correct
3. Only S1 is correct
4. Only S2 is correct

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 113

*UGC NET Dec 2019, original Q101*

> Consider the following statements: S,: These exists no algorithm for deciding if any two Turing machines My and M accept the same language. Sz: Let M, and M2 be arbitrary Turing machines. The problem to determine L(M,) sL(M,) is undecidable. Which of the statements is (are) correct?

**Options**

1. Only Sy
2. Only S
3. Both S, and S
4. Neither S, nor S, 61547541102.2 61547541103.3 61547541104.4

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 114

*UGC NET June 2019, original Q130*

> For a statement A language L c 2* is recursive if there exists some turing machine M. Which of the following conditions is satisfied for any string co?

**Options**

1. If @ eL, then M accepts o and M will not halt
2. If weL, then M accepts c and M will halt by reaching at final state
3. If ceL, then M halts without reaching to acceptable state
4. If ceL, then M halts without reaching to an acceptable state 64635085856. 2 64635085857.3 64635085858. 4

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 115

*UGC NET Aug 2024, original Q100*

> Arrange the following stages of a Turing Machine (TM) operation in the correct order as they occur during computation.
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Writing a symbol on the tape
> - **B.** Moving the tape head left to right
> - **C.** Reading a symbol from the tape
> - **D.** Transitioning to a new state based on the current state and symbol read (E) Halting and accepting or rejecting the input Choose the correct answer from the options given below : (1) (C), (A), (B), (D), (E) (2) (C), (B), (A), (D), (E) (3) (C), (D),

**Options**

- **A.** ,
- **B.** , (E) (4)
- **C.** ,
- **D.** , (B), (A), (E) 64/101

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 116

*UGC NET June 2024, original Q55*

> Match List-l with List-I1 : List - I List - Il
>
> **Additional extracted choices — check the source page:**
>
> - **A.** A-aB|a, ae T, A, BEV
> - **B.** A→BC|a, ae T, A, B, CE V Recursive Descent Parser
> - **C.** LL (1) grammar II. Turing Machine
> - **D.** Halting problem II. Choamsky Normal Form IV. Finite Automate Choose the correct answer from the options given below :

**Options**

1. A-IV, B-III, C-I, D-II
2. A-I, B-I, C-II, D-IV
3. A-II, B-IV, C-II, D-I
4. A-IV, B-HI. C-II, D-I

**Chapter foundations**

This question belongs to the ideas covered by **Turing Machines**. Revise these foundations: Standard TM and Variants; Universal TM; Models of Computation; Church-Turing Thesis; Recursive and Recursively Enumerable Languages; Context-Sensitive Languages; Unrestricted Grammars; Chomsky Hierarchy; TM Construction.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Turing Machines questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-5"></a>

### 5. Unsolvable Problems and Computational Complexity (3 questions)

**What to master:** Halting and Post Correspondence Problems; Unsolvable CFL Problems; Complexity Measurement and Classification; Tractable and Intractable Problems.

**Exam lens:** Classify the language or grammar before selecting DFA/NFA, PDA/CFG, TM, parser, or compiler analysis.

**Reusable method:** For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments.

**High-yield rules:** Regular languages are closed under union, intersection and complement. LL(1) table entries must be conflict-free. LR items encode viable prefixes.

**Common traps:** The pumping lemma proves non-regularity but not regularity; ambiguity differs from left recursion; recursive languages differ from recursively enumerable languages.

---

#### Question 117

*UGC NET Dec 2014, Paper II, original Q21*

> Convert the following infix expression into its equivalent post fix expression (A + B^ D) / (E – F) + G

**Options**

- **A.** ABD^ + EF – / G+
- **B.** ABD + ^EF – / G+
- **C.** ABD + ^EF / – G+
- **D.** ABD^ + EF / – G+

**Chapter foundations**

This question belongs to the ideas covered by **Unsolvable Problems and Computational Complexity**. Revise these foundations: Halting and Post Correspondence Problems; Unsolvable CFL Problems; Complexity Measurement and Classification; Tractable and Intractable Problems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Unsolvable Problems and Computational Complexity questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 118

*UGC NET Nov 2020, original Q125*

> Arrange the following types of machine in descending order of complexity. (A) SISD (B) MIMD (C) SIMD Choose the correct answer from the options given below:

**Options**

1. A. B. C
2. C. B.A
3. B. C.A
4. C, A, B 53622816998.2 53622816999.3 53622817000.4

**Chapter foundations**

This question belongs to the ideas covered by **Unsolvable Problems and Computational Complexity**. Revise these foundations: Halting and Post Correspondence Problems; Unsolvable CFL Problems; Complexity Measurement and Classification; Tractable and Intractable Problems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Unsolvable Problems and Computational Complexity questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 119

*UGC NET June 2024, original Q70*

> Match List-l with List-ll : List - I1 List - 1 Automata A. Back Tracking Undecidable Problem Infinite languages with matching numbers Predictive Parser C. Canonical LR Parser Large number of states Choose the correct answer from the options given below i D. Post Correspondence Problem A-II, B-V, C1, D-III
>
> **Additional extracted choices — check the source page:**
>
> 1. A-I, B-II, C-III, D-IV
> 2. A-III, B-I, C-IV, D-IT
> 3. A-IV, B-III, C-II, D-I
> 4. _Missing in extracted text_

**Chapter foundations**

This question belongs to the ideas covered by **Unsolvable Problems and Computational Complexity**. Revise these foundations: Halting and Post Correspondence Problems; Unsolvable CFL Problems; Complexity Measurement and Classification; Tractable and Intractable Problems.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Unsolvable Problems and Computational Complexity questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-6"></a>

### 6. Syntax Analysis (17 questions)

**What to master:** Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam lens:** Classify the language or grammar before selecting DFA/NFA, PDA/CFG, TM, parser, or compiler analysis.

**Reusable method:** For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments.

**High-yield rules:** Regular languages are closed under union, intersection and complement. LL(1) table entries must be conflict-free. LR items encode viable prefixes.

**Common traps:** The pumping lemma proves non-regularity but not regularity; ambiguity differs from left recursion; recursive languages differ from recursively enumerable languages.

---

#### Question 120

*UGC NET Dec 2009, Paper II, original Q17*

> Specialization is __________ process.
>
> **Additional extracted choices — check the source page:**
>
> - **A.** top-down
> - **B.** bottom up
> - **C.** both (A) and (B)
> - **D.** none of these

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 121

*UGC NET Dec 2009, Paper II, original Q32*

> Which of the following grammar is LR (1) ?

**Options**

- **A.** A → a A b, A → b A b, A → a , A → b
- **B.** A → a A a, A → a A b, A → c
- **C.** A → A + A, A → a
- **D.** Both (A) and (B)

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 122

*UGC NET June 2010, Paper II, original Q17*

> Generalization is _______ process.
>
> **Additional extracted choices — check the source page:**
>
> - **A.** top-down
> - **B.** bottom up
> - **C.** both (A) & (B)
> - **D.** None of these

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 123

*UGC NET Dec 2012, Paper II, original Q13*

> Which of the following is true ? grammar
>
> **Additional extracted choices — check the source page:**
>
> - **A.** A relation in BCNF is always in E→E*F/F+E/F 3NF. F→F-F/ id
> - **B.** A relation in 3NF is always in Which of the following is true ? BCNF. (A) * has higher precedence than +
> - **C.** BCNF and 3NF are same. (B) - has higher precedence than *
> - **D.** A relation in BCNF is not in (C) + and - have same precedence 3NF. (D) + has higher precedence than * D-87-12 3 Paper-ll

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 124

*UGC NET Dec 2012, Paper II, original Q27*

> Which of the following is true while RG-59 with impedance 75 & used for converting CFG to LL(I) grammar?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Cable TV (A) Remove left recursion alone
> - **B.** Ethernet (B) Factoring grammar alone
> - **C.** Thin Ethernet (C) Both of the above
> - **D.** Thick Ethernet (D) None of the above Paper-ll 4 D-87-12

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 125

*UGC NET Dec 2013, Paper II, original Q30*

> Which of the following derivations does a top-down parser use while parsing an input string ? The input is scanned from left to right.

**Options**

- **A.** Leftmost derivation
- **B.** Leftmost derivation traced out in reverse
- **C.** Rightmost derivation traced out in reverse
- **D.** Rightmost derivation

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 126

*UGC NET June 2015, Paper II, original Q34*

> Which one from the following is false?
>
> **Additional extracted choices — check the source page:**
>
> 1. LALR parser is Bottom - Up parser
> 2. A parsing algorithm which performs a left to right scanning and a right most deviation is RL (1).
> 3. LR parser is Bottom - Up parser.
> 4. In LL(1), the 1 indicates that there is a one - symbol look - ahead.

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 127

*UGC NET July 2016, Paper II, original Q35*

> Which of the following is FALSE ?

**Options**

1. The grammar S → a Sb |bSa|SS| ∈, where S is the only non-terminal symbol and ∈ is the null string, is ambiguous.
2. SLR is powerful than LALR.
3. An LL(1) parser is a top-down parser.
4. YACC tool is an LALR (1) parser generator.

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 128

*UGC NET Jan 2017, Paper II, original Q33*

> Consider the following statements related to compiler construction : I. Lexical Analysis is specified by context-free gramm ars and implemented by pushdown automata. II. Syntax Analysis is specified by regular expressions and implemented by finite-state machine. Which of the above statement(s) is/are correct ?

**Options**

1. Only I
2. Only II
3. Both I and II
4. Neither I nor II

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 129

*UGC NET Dec 2018, original Q90*

> The grammar S → (S) | SS | E is not suitable for predictive parsing because the grammar is . Right recursive 91394342358 Left recursive 91394342359. Ambiguous 91394342360. An operator grammar Single in Questio20 pios: No 0713 Oriens On: Vo Type: MCQ Option Shufling: Xes Display Quesion Number: Xes Correct Marks: 2 Wrong Marks: 0

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 130

*UGC NET July 2018, Paper II, original Q39*

> A bottom-up parser generates :

**Options**

1. Left-most derivation in reverse
2. Right-most derivation in reverse
3. Left-most derivation
4. Right-most derivation

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 131

*UGC NET Nov 2021, original Q40*

> Given below are two statements Statement I: LL(1) and LR are examples of Bottom‐up parsers. Statement II: Recursive descent parser and SLR are examples of Top‐down parsers In light of the above statements, choose the correct answer from the options given below

**Options**

1. Both Statement I and Statement II are true
2. Both Statement I and Statement II are false
3. Statement I is true but Statement II is false
4. Statement I is false but Statement II is true

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 132

*UGC NET Oct 2022, original Q12*

> The reduced grammar equivalent to the grammar, whose production rules are given below. is S → ABI CA B → BC|AB A → a C → a BIb

**Options**

1. S → CA, A → a, C → b
2. 8 → CA| B. B → BC|B. A → a, C → aB|b
3. S → CA|B. B → BC. A → a. C → aB|b
4. S → ABIAC. B → BC|BA, A → a, C → aB|b

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 133

*UGC NET Oct 2022, original Q81*

> Consider the following statements: Statement I: LALR parser is more powerful than canonical LR Parser: Statement II: SLR parser is more powerful than LALR Which of the following is correct?

**Options**

1. Statement I true and Statement Il false
2. Statement I false and Statement II true
3. Both Statement I and Statement II false
4. Both Statement I and Statement II true

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 134

*UGC NET June 2023, Paper II, original Q27*

> Which of the following parser is most powerful parser? (+2)

**Options**

- **A.** Operator precedence
- **B.** SLR
- **C.** Canonical LR
- **D.** LALR

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 135

*UGC NET June 2024, original Q52*

> Shift-Reduce conflicts are resolved by : (1) Left recurssion (3) Ambiguity (2) Left factoring (4) Associativity and Precedence

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 136

*UGC NET June 2024, original Q82*

> An ambiguous grammar is one which has
>
> **Additional extracted choices — check the source page:**
>
> - **A.** More than one derivations
> - **B.** More than one left most derivations
> - **C.** More than one right most derivations
> - **D.** More than one Parse tree More than one syntax tree Choose the correct answer from the options given below :

**Options**

1. A and D Only
2. Band COnly
3. Dand EOnly
4. A and E Only

**Chapter foundations**

This question belongs to the ideas covered by **Syntax Analysis**. Revise these foundations: Associativity; Precedence; Grammar Transformations; Top-Down, Recursive-Descent, Predictive and LL(1) Parsing; Bottom-Up, LR and LALR(1) Parsing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Syntax Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-7"></a>

### 7. Semantic Analysis (30 questions)

**What to master:** Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam lens:** Classify the language or grammar before selecting DFA/NFA, PDA/CFG, TM, parser, or compiler analysis.

**Reusable method:** For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments.

**High-yield rules:** Regular languages are closed under union, intersection and complement. LL(1) table entries must be conflict-free. LR items encode viable prefixes.

**Common traps:** The pumping lemma proves non-regularity but not regularity; ambiguity differs from left recursion; recursive languages differ from recursively enumerable languages.

---

#### Question 137

*UGC NET Dec 2009, Paper II, original Q35*

> Synthesized attribute can be easily simulated by a

**Options**

- **A.** LL grammar
- **B.** Ambiguous grammar
- **C.** LR grammar
- **D.** None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 138

*UGC NET June 2010, Paper II, original Q33*

> Consider the following left associative operators in decreasing order of precedence : – subtraction (highest precedence) * multiplication $ exponentiation (lowest precedence) What is the result of the following expression ? 3 – 2 * 4 $ | * 2 ** 3

**Options**

- **A.** – 61
- **B.** 64
- **C.** 512
- **D.** 4096

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 139

*UGC NET Dec 2012, Paper II, original Q2*

> Union deterministic finite automaton. The c. Derived type

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 140

*UGC NET Dec 2012, Paper II, original Q44*

> Let L be a set accepted by a non- b. Built in type

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 141

*UGC NET Dec 2013, Paper III, original Q21*

> Given the following statements : S 1 : The grammars S → asb | bsa | ss | a and S → asb | bsa | a are not equivalent. S 2 : The grammars S → ss | sss | asb | bsa | λ and S → ss | asb | bsa | λ are equivalent. Which of the following is true ?

**Options**

- **A.** S 1 is correct and S 2 is not correct.
- **B.** Both S 1 and S2 are correct.
- **C.** S 1 is not correct and S2 is correct.
- **D.** Both S 1 and S2 are not correct.

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 142

*UGC NET June 2015, Paper III, original Q63*

> Given the following grammars: G1: S → AB aaB A → aA | € B → bB € G2: S→ A B A → a Ab ab B→a bB € Which of the following is correct?

**Options**

1. Gy is ambiguous and G2 is unambiguous grammars
2. Gy is unambiguous and G, is ambiguous grammars
3. both Gy and G2 are ambiguous grammars
4. both Gy and G, are unambiguous grammars

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 143

*UGC NET Nov 2017, Paper II, original Q35*

> Match the description of several parts of a classic optimizing co mpiler in List - I , with the names of those parts in List - II : List - I List - II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** A part of a compiler that is responsible for recognizing (i) Optimizer syntax.
> - **B.** A part of a compiler that takes as input a stream of (ii) Semantic Analysis characters and produces as output a stream of words along with their associated syntactic categories.
> - **C.** A part of a compiler that understand the meanings of (iii) Parser variable names and other symbols and checks that they are used in ways consistent with their definitions.
> - **D.** An IR-to-IR transformer that tries to improve the IR (iv) Scanner program in some way (Intermediate Representation). Code : (a) (b) (c) (d)

**Options**

1. (iii) (iv) (ii) (i)
2. (iv) (iii) (ii) (i)
3. (ii) (iv) (i) (iii)
4. (ii) (iv) (iii) (i)

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 144

*UGC NET July 2018, Paper II, original Q36*

> Consider the following two Grammars : G1 : S → SbS|a G2 : S → aB|ab, A → GAB|a, B→ ABb|b Which of the following option is correct ?

**Options**

1. Only G1 is ambiguous
2. Only G2 is ambiguous
3. Both G1 and G2 are ambiguous
4. Both G1 and G2 are not ambiguous

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 145

*UGC NET Dec 2019, original Q93*

> Personal Exam Consider the following grammars: G,: S → aSb | bSa laa G2: S → aSb | bSa | SS | 2 G3: S→ aSb| bSa | SS la G,: S → aSb | 6Sa | SS | SSS | 2 Which of the following is correct w.r.t. the above grammars?

**Options**

1. Gy and G3 are equivalent
2. G, and G are equivalent
3. Go and Gy are equivalent
4. Gz and G, are equivalent 61547541070. 2 61547541071. 3 61547541072.4

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 146

*UGC NET Dec 2019, original Q107*

> The full form of ICANN is

**Options**

1. Internet Corporation for Assigned Names and Numbers
2. Internet Corporation for Assigned Numbers and Names
3. Institute of Cooperation for Assigned Names and Numbers
4. Internet Connection for Assigned Names and Numbers 61547541126.2 61547541127.3 61547541128.4

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 147

*UGC NET Dec 2019, original Q109*

> Consider the following statements: S1: Vx P(x)v VxQ(x) and Vx (P(x) v Q(x)) are not logically equivalent. S2: 3x P(x) ^ Ix Q(x) and Ix (P(x)л Q(x)) are not logically equivalent Which of the following statements is/are correct?

**Options**

1. Only S1
2. Only S2
3. Both S1 and S2
4. Neither Si nor S2 61547541134.2 Guide 61547541135.3 61547541136. 4

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 148

*UGC NET June 2019, original Q120*

> Consider the following statements : S,: For any integer n>1, a = 1(modn) for all aeZ* 'n, where on) 1s Euler's phi function. S, : If p is prime, then a" = 1(mod p) for all a e Z Which one of the following is/are correct? repp

**Options**

1. Only s,
2. Only s, ersonal Exam Guide
3. Both S, and Sa
4. Neither S, nor S 64635085816.2 64635085817.3 64635085818. 4

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 149

*UGC NET Nov 2020, original Q107*

> Which of the following grammars is (are) ambiguous? (A) s → ss |asb | bsa | 2 (B) s → asbs | bsas | 2 (C) s → aAB A → bBb B → Al& where 1 denotes empty string Choose the correct answer from the options given below:

**Options**

1. (A) and (C) only
2. (B only
3. (B) and (C) only
4. (A) and (B) only 53622816926.2 53622816927.3 53622816928.4

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 150

*UGC NET Nov 2020, original Q148*

> Which of the following query/queries return the employee ID and name of employees whose salary is greater than the salary of all employees in department number 20 of university. Order result by employee ID (refer table structures given above). (A) SELECT BID, NAME FROM EMPLOYEE WHERE SALARY»(SELECT SALARY FROM EMPLOYEE WHERE DEPTNO=20) ORDER BY EID: (B) SELECT EID. NAME FROM EMPLOYEE WHERE SALARY (SELECT SALARY FROM EMPLOYEE WHERE DEPTNO=20): (C) SELECT EID, NAME FROM EMPLOYEE WHERE SALARY>ALL(SELECT SALARY FROM EMPLOYEE WHERE DEPTNO=20) ORDER BY EID Choose the correct answer from the options given below:

**Options**

1. (A) and (B) only
2. (A) and (C) only
3. (B) only
4. (C) only 53622817090. 2 53622817091.3 53622817092.4

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 151

*UGC NET Aug 2024, original Q51*

> Consider the Grammar : S → A A → $B$ | id B → B, A|A If 1o = CLOSURE (IIS → All then, how many items be in the set for GOTO(oS)

**Options**

1. 3
2. 4
3. 5
4. 6

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 152

*UGC NET Aug 2024, original Q52*

> Consider the Grammar : T → Qx Q → RS S → z|€ Here x, y, z are terminals and T, Q, R, S are non terminals. What will be the follow set of the non terminal R?

**Options**

1. ix, yi
2. (y, z)
3. (z, x)
4. 18)

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 153

*UGC NET Aug 2024, original Q87*

> Translate Vxay(x<y) in English. Consider domain as a real number for both the variables. (1) For all real numbers x, there exists a real number y such that x is less than y For every real numbers y, there exists a real number x such that x is less than y 3) For some real numbers x, there exists a real number y such that r is less than y (4) For each and every real numbers x and y, x is less than y

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 154

*UGC NET Aug 2024, original Q125*

> Consider the following if p and q are two statements.
>
> **Additional extracted choices — check the source page:**
>
> - **A.** ~(p/q) = ~pV~q
> - **B.** ~(pq) =~p/~q
> - **C.** p/-p= T
> - **D.** ~(p→q) = p^~q (E) pVq=~pV~q Choose the correct answer from the options given below :

**Options**

1. (A), (B) and (D) Only
2. (A), (C) and (D) Only
3. (C), (D) and (E) Only
4. (A), (B) and (C) Only

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 155

*UGC NET June 2024, original Q100*

> Arrange in appropriate order, the construction of a fartle apr Ragular Expeussion A. Minimum State DFA D. Protices titatement

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 156

*UGC NET June 2025, original Q76*

> Consider the following infix expression Q: ((A+B) * D) 1 (E - F). The equivalent postfix expression of Q is

**Options**

1. AB+D * EFT -
2. AB+D * -1 EF
3. AB + D E* F-1
4. AB+D * EF-1 42558919356. 1 42558919358.3 42558919359.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 157

*UGC NET June 2025, original Q87*

> Which of the followings is not a valid property over two fuzzy relations R and Š which must be obeyed for performing 1-cut defuzzifications? 3. (R)) + R, except when 1 = 1 4. For any ≤ B, where 0 ≤ B ≤ 1, it is true that Ra S Ra 42558919400. 1 ptions: 42558919401.2 42558919402.3 42558919403.4

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 158

*UGC NET June 2025, original Q101*

> Arrange the following parsers in increasing order of their power of handling grammars i.e. from the least powerful parser to the most powerful parser.
>
> **Additional extracted choices — check the source page:**
>
> - **A.** LR(O)
> - **B.** LR(1)
> - **C.** LALR(1)
> - **D.** LL(O) E. SLR Choose the correct answer from the options given below:

**Options**

1. LL(O) →LR(0) → SLR→LR(1) →LALR(1)
2. SLR →LR(0) →LL(0) →LR(1) →LALR(1)
3. LL(0) →LR(0) →SLR→LALR(1) →LR(1)
4. LR(0) →LL(0) →SLR → LR(1) →LALR(1) 42558919456.1 42558919458. 3 42558919459.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 159

*UGC NET June 2025, original Q109*

> Which of the following gates do not give output 1 when both the inputs are O-
>
> **Additional extracted choices — check the source page:**
>
> - **A.** NAND gate
> - **B.** NOR gate
> - **C.** X-OR gate
> - **D.** X-NOR gate Choose the correct answer from the options given below:

**Options**

1. A, B Only
2. B, C Only
3. C, D Only
4. C Only 42558919489.2 42558919490.3 42558919491.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 160

*UGC NET June 2025, original Q127*

> Match List I with List I! List I List II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Type 3 Grammar 1. V → (VU 2)*
> - **B.** Type 2 Grammar lI. AVB → N(VU 2)*B , where (2,B)E(VU 2)*
> - **C.** Type 1 Grammar III. (VU [* → (VU 2)*
> - **D.** Type 0 Grammar IV. V → V[I2 Choose the correct answer from the options given below:
>
> **Additional extracted choices — check the source page:**
>
> 1. A→II, B→III, C→IV, D→1
> 2. A→III, B→I, C→IV, D→>II
> 3. A→IV, B→I, C→II, D→>III
> 4. A→III, B→II, C→I, D→IV 42558919560.1 42558919562. 3 42558919563.4 Manditory enDer: 127 * B. Type 2 Grammar II. AVB → X(VU 2)*B , where (2,B)E(V U S)* C. Type 1 Grammar III. (VU []* → (VUS]* D. Type 0 Grammar IV. V → V212 Choose the correct answer from the options given below:

**Options**

1. A>II, B→III, C>IV, D→I
2. A→III, B→I, C→IV, D→II
3. A→IV, B→I, C→II, D→III
4. A→III, B>II, C→1, D>IV 42558919561.2 42558919562.3 42558919563.4

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 161

*UGC NET June 2025, original Q142*

> What are the various LEADERS (leading statements) for the TAC given in the passage?

**Options**

1. 100, 102, 103, 104, 105, 107, 110
2. 100, 103, 105, 107, 111, 112
3. 100, 103, 105, 106, 107, 111
4. 100, 103, 104, 105, 106, 107, 111 42558919620. 1 42558919622. 3 42558919623.4

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 162

*UGC NET Dec 2025 session (Jan 2026), original Q55*

> Question Number : 55 B. Зn]m(n+m=4лn-т=2) C. En Im (n? + m? = 5) D. ImVn(m+n=0) E. Vm 3n(m+n= 0) Choose the correct answer from the options given below:

**Options**

1. A. B & C Only
2. A, B, C & D Only
3. A, B, C & E Only
4. B, C, E & D Only 6119878618.2 6119878619.3 6119878620.4

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 163

*UGC NET Dec 2025 session (Jan 2026), original Q69*

> Question Number : 69

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 164

*UGC NET Dec 2025 session (Jan 2026), original Q70*

> Question Number : 70

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 165

*UGC NET Dec 2025 session (Jan 2026), original Q127*

> Question Number : 127

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 166

*UGC NET Dec 2025 session (Jan 2026), original Q130*

> Question Number : 130

**Chapter foundations**

This question belongs to the ideas covered by **Semantic Analysis**. Revise these foundations: Attribute Grammars; Syntax-Directed Definitions; Inherited and Synthesized Attributes; Dependency Graphs; Evaluation Order; S- and L-Attributed Definitions; Type Checking.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Semantic Analysis questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-8"></a>

### 8. Runtime System (7 questions)

**What to master:** Storage Organization; Activation Tree and Records; Stack Allocation; Parameter Passing; Symbol Table.

**Exam lens:** Classify the language or grammar before selecting DFA/NFA, PDA/CFG, TM, parser, or compiler analysis.

**Reusable method:** For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments.

**High-yield rules:** Regular languages are closed under union, intersection and complement. LL(1) table entries must be conflict-free. LR items encode viable prefixes.

**Common traps:** The pumping lemma proves non-regularity but not regularity; ambiguity differs from left recursion; recursive languages differ from recursively enumerable languages.

---

#### Question 167

*UGC NET Dec 2009, Paper II, original Q5*

> In a MIU puzzle, either of the letters M, I or U could go as a start symbol. Production rules are given below : R 1 : U → IU R 2 : M. x → M. x.x where . .. is string concatenation operator. Given this, which of the following holds for (i) MIUIUIUIUIU (ii) MIUIUIUIUIUIUIUIU

**Options**

- **A.** Either (i) or (ii) but not both of these are valid words .
- **B.** Both (i) and (ii) are valid words and they take identical number of transformations for the production.
- **C.** Both (i) and (ii) are valid words but they involve differe nt number of transformations in the production.
- **D.** None of these

**Chapter foundations**

This question belongs to the ideas covered by **Runtime System**. Revise these foundations: Storage Organization; Activation Tree and Records; Stack Allocation; Parameter Passing; Symbol Table.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Runtime System questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 168

*UGC NET June 2010, Paper II, original Q32*

> Which of the following expression is represented by the parse tree ?

**Options**

- **A.** (A + B) * C
- **B.** A + * BC
- **C.** A + B * C
- **D.** A * C + B

**Chapter foundations**

This question belongs to the ideas covered by **Runtime System**. Revise these foundations: Storage Organization; Activation Tree and Records; Stack Allocation; Parameter Passing; Symbol Table.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Runtime System questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 169

*UGC NET Dec 2014, Paper II, original Q31*

> Shift-Reduce parsers perform the following :

**Options**

- **A.** Shift step that advances in the input stream by K(K > 1) s ymbols and Reduce step that applies a completed grammar rule to some recent parse tree s, joining them together as one tree with a new root symbol.
- **B.** Shift step that advances in the input stream by one symbol and Reduce step that applies a completed grammar rule to some recent parse trees, joining them together as one tree with a new root symbol.
- **C.** Shift step that advances in the input stream by K(K = 2) s ymbols and Reduce step that applies a completed grammar rule to form a single tree.
- **D.** Shift step that does not advance in the input stream and Reduce s tep that applies a completed grammar rule to form a single tree.

**Chapter foundations**

This question belongs to the ideas covered by **Runtime System**. Revise these foundations: Storage Organization; Activation Tree and Records; Stack Allocation; Parameter Passing; Symbol Table.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Runtime System questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 170

*UGC NET Dec 2014, Paper II, original Q33*

> In a two-pass assembler, symbol table is

**Options**

- **A.** Generated in first pass
- **B.** Generated in second pass
- **C.** Not generated at all
- **D.** Generated and used only in second pass

**Chapter foundations**

This question belongs to the ideas covered by **Runtime System**. Revise these foundations: Storage Organization; Activation Tree and Records; Stack Allocation; Parameter Passing; Symbol Table.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Runtime System questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 171

*UGC NET Nov 2020, original Q91*

> Which of the following are applications of symbol table? (A) Storage allocation (B) Checking type compatability (C) Suppressing duplicate error messages Choose the correct answer from the options given below: (-) (A) and (B) only (2) (A) and (C) only (3) (B) and (C) only (4) (A). (B) and (C) 53622816862.2 53622816863.3 53622816864.4

**Chapter foundations**

This question belongs to the ideas covered by **Runtime System**. Revise these foundations: Storage Organization; Activation Tree and Records; Stack Allocation; Parameter Passing; Symbol Table.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Runtime System questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 172

*UGC NET Nov 2021, original Q74*

> Match List I with List II List I List II System calls Description
>
> **Additional extracted choices — check the source page:**
>
> - **A.** fork() I. Sends a signal from one process to another process
> - **B.** exec() II. Indicates termination of the current process
> - **C.** kill() III. Loads the specified program in the memory
> - **D.** exit() IV. Creates a child process Choose the correct answer from the options given below:

**Options**

1. A ‐ II , B ‐ III , C ‐ IV , D ‐ I
2. A ‐ IV , B ‐ III , C ‐ I , D ‐ II
3. A ‐ IV , B ‐ I , C ‐ II , D ‐ III
4. A ‐ IV , B ‐ III , C ‐ II, D ‐ I

**Chapter foundations**

This question belongs to the ideas covered by **Runtime System**. Revise these foundations: Storage Organization; Activation Tree and Records; Stack Allocation; Parameter Passing; Symbol Table.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Runtime System questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 173

*UGC NET June 2025, original Q118*

> Which of the following are controlled-access protocols
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Reservation
> - **B.** Polling
> - **C.** TDMA
> - **D.** Token Passing E. CSMA/CA Choose the correct answer from the options given below:

**Options**

1. A and D Only
2. A, Band D Only
3. C, D and E Only
4. A, D and E Only 42558919525.2 42558919526. 3 42558919527.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Runtime System**. Revise these foundations: Storage Organization; Activation Tree and Records; Stack Allocation; Parameter Passing; Symbol Table.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Runtime System questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-9"></a>

### 9. Intermediate Code Generation (6 questions)

**What to master:** Representations; Translation of Declarations, Assignments, Control Flow, Boolean Expressions and Procedure Calls.

**Exam lens:** Classify the language or grammar before selecting DFA/NFA, PDA/CFG, TM, parser, or compiler analysis.

**Reusable method:** For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments.

**High-yield rules:** Regular languages are closed under union, intersection and complement. LL(1) table entries must be conflict-free. LR items encode viable prefixes.

**Common traps:** The pumping lemma proves non-regularity but not regularity; ambiguity differs from left recursion; recursive languages differ from recursively enumerable languages.

---

#### Question 174

*UGC NET Dec 2009, Paper II, original Q33*

> A shift-reduce parser carries out the actions specified within braces immediately after reducing with the corresponding rule of the grammar. S → x x W [ print “1”] S → y [print “2”] W → S 2 [print “3”], what is the translation of “ x x x x y z z” ?

**Options**

- **A.** 1 1 2 3 1
- **B.** 1 1 2 3 3
- **C.** 2 3 1 3 1
- **D.** 2 3 3 2 1

**Chapter foundations**

This question belongs to the ideas covered by **Intermediate Code Generation**. Revise these foundations: Representations; Translation of Declarations, Assignments, Control Flow, Boolean Expressions and Procedure Calls.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Intermediate Code Generation questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 175

*UGC NET Dec 2012, Paper II, original Q18*

> Given the following expressions of a

**Chapter foundations**

This question belongs to the ideas covered by **Intermediate Code Generation**. Revise these foundations: Representations; Translation of Declarations, Assignments, Control Flow, Boolean Expressions and Procedure Calls.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Intermediate Code Generation questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 176

*UGC NET Nov 2020, original Q80*

> Which of the following is not an intermediate code form?

**Options**

1. Svntax trees
2. Three address codes
3. Quadrupules
4. Post fix Notation. 53622816818.2 53622816819.3 53622816820,4

**Chapter foundations**

This question belongs to the ideas covered by **Intermediate Code Generation**. Revise these foundations: Representations; Translation of Declarations, Assignments, Control Flow, Boolean Expressions and Procedure Calls.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Intermediate Code Generation questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 177

*UGC NET Nov 2020, original Q87*

> It f(x) = x is my friend, and p(x) =x is perfect, then correct logical translation of the statement "some of my friends are not perfect" is _

**Options**

1. Vx (f(x) A -p(x))
2. 3, (f(x) A → p(x))
3. - (f(x) A -P(x))
4. 3, (-f(x) ^ →p(x)) 53622816846. 2 53622816847.3 53622816848.4

**Chapter foundations**

This question belongs to the ideas covered by **Intermediate Code Generation**. Revise these foundations: Representations; Translation of Declarations, Assignments, Control Flow, Boolean Expressions and Procedure Calls.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Intermediate Code Generation questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 178

*UGC NET Oct 2022, original Q80*

> A top down approach to programming calls for : Statement I: Working from the general to the specific. Statement II: Postpone the minor decisions. Statement III: A systematic approach. Statement IV: Intermediate coding of the problem Which of the following is true?

**Options**

1. Statement I only
2. Statement I and Statement II only
3. Statement I, Statement II and Statement III only
4. Statement I. Statement II and Statement IV only

**Chapter foundations**

This question belongs to the ideas covered by **Intermediate Code Generation**. Revise these foundations: Representations; Translation of Declarations, Assignments, Control Flow, Boolean Expressions and Procedure Calls.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Intermediate Code Generation questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 179

*UGC NET Dec 2025 session (Jan 2026), original Q107*

> Question Number : 107

**Chapter foundations**

This question belongs to the ideas covered by **Intermediate Code Generation**. Revise these foundations: Representations; Translation of Declarations, Assignments, Control Flow, Boolean Expressions and Procedure Calls.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Intermediate Code Generation questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-10"></a>

### 10. Code Generation and Optimization (41 questions)

**What to master:** Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam lens:** Classify the language or grammar before selecting DFA/NFA, PDA/CFG, TM, parser, or compiler analysis.

**Reusable method:** For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments.

**High-yield rules:** Regular languages are closed under union, intersection and complement. LL(1) table entries must be conflict-free. LR items encode viable prefixes.

**Common traps:** The pumping lemma proves non-regularity but not regularity; ambiguity differs from left recursion; recursive languages differ from recursively enumerable languages.

---

#### Question 180

*UGC NET June 2010, Paper II, original Q11*

> The statement print f (“ % d”, 10 ? 0 ? 5 : 1 : 12); will print

**Options**

- **A.** 10
- **B.** 0
- **C.** 12
- **D.** 1

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 181

*UGC NET June 2010, Paper II, original Q35*

> Which of the following is used for grouping of characters into tokens (in a computer) ?

**Options**

- **A.** A parser
- **B.** Code optimizer
- **C.** Code generator
- **D.** Scanner

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 182

*UGC NET Dec 2012, Paper II, original Q4*

> Pointer finite automaton is Q. The maximum number of states in equivalent finite Code: automaton that accepts L is a b d
>
> **Additional extracted choices — check the source page:**
>
> - **A.** 2 4 1 (A) IQ/
> - **B.** 3 (B) 2|0/
> - **C.** 4 1 (C) 2191- 1 2
> - **D.** 3 1 2 (D) 2191 Paper-ll 6 D-87-12

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 183

*UGC NET Dec 2012, Paper II, original Q38*

> Match the following IC families with (A) ios:: app their basic circuits: (B) in : : ios a. TTL

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 184

*UGC NET Dec 2012, Paper II, original Q49*

> Identify the operation which is expression ? commutative but not associative ? (1 & 2) + (3 & 4)
>
> **Additional extracted choices — check the source page:**
>
> - **A.** OR (A) 1
> - **B.** NOR (B) 3
> - **C.** EX-OR (C) 2
> - **D.** NAND (D) O

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 185

*UGC NET June 2013, Paper III, original Q37*

> A pushdown automation M = (Q, Σ, Γ, δ, q 0, z, F) is set to be deterministic subject to which of the following condition(s), for every q ∈ Q, a ∈ Σ ∪ {λ} and b ∈ Γ (s1) δ(q, a, b) contains at most one element (s2) if δ(q, λ, b) is not empty then δ(q, c, b) must be empty for every c ∈ Σ

**Options**

- **A.** only s1
- **B.** only s2
- **C.** both s1 and s2
- **D.** neither s1 nor s2

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 186

*UGC NET June 2013, Paper III, original Q67*

> Which one of the following is a correct implementation of the meta- predicate “not” in PROLOG (Here G represents a goal) ?

**Options**

- **A.** not(G):– !, call(G), fail. not(G).
- **B.** not(G):– call(G), !, fail. not(G).
- **C.** not(G):– call(G), fail, !. not(G).
- **D.** not(G):– call(G), fail. not(G):– !.

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 187

*UGC NET Dec 2014, Paper II, original Q32*

> Which of the following is true ?
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Canonical LR parser is LR (1) parser with single look ahead terminal
> - **B.** All LR(K) parsers with K > 1 can be transformed into LR(1) parser s.
> - **C.** Both (A) and (B)
> - **D.** None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 188

*UGC NET Dec 2014, Paper III, original Q20*

> How many tokens will be generated by the scanner for the following statement ? x = x ∗ (a + b) – 5;

**Options**

- **A.** 12
- **B.** 11
- **C.** 10
- **D.** 07

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 189

*UGC NET Dec 2015, Paper II, original Q41*

> Loop unrolling is a code optimization technique : that avoids tests at every iteration of the loop. (2) that improves performance by decreasing the number of instructions in a basic block. (3) that exchanges inner loops with outer loops. (4) that reorders operations to allow multiple computations to happen in parallel.

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 190

*UGC NET Dec 2015, Paper III, original Q27*

> There are exactly. . different finite automata with three states x, y and z over the alphabet {a, b} where x is always the start state.

**Options**

1. 64
2. 256
3. 1024
4. 5832

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 191

*UGC NET June 2015, Paper II, original Q35*

> Which phase of compiler generates stream of atoms?

**Options**

1. Syntax Analysis
2. Lexical Analysis
3. Code Generation
4. Code Optimization J-8715 8 Paper-Il

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 192

*UGC NET July 2016, Paper II, original Q25*

> In how many ways can the string A ∩ B – A ∩ B – A be fully parenthesized to yi eld an infix expression ?

**Options**

1. 15
2. 14
3. 13
4. 12

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 193

*UGC NET July 2016, Paper II, original Q33*

> In _______, the bodies of the two loops are me rged together to form a single loop provided that they do not make any references to each other.

**Options**

1. Loop unrolling
2. Strength reduction
3. Loop concatenation
4. Loop jamming

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 194

*UGC NET July 2016, Paper III, original Q74*

> Consider a 3-puzzle where, like in the usua l 8-puzzle game, a tile can only move to an adjacent empty space. Given the initial state 1 2 3 , which of the following state cannot be reached ?

**Options**

1. 3 1 2
2. 2 3 1
3. 1 3 2
4. 1 2 3

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 195

*UGC NET Jan 2017, Paper II, original Q2*

> Match the following : List – I List – II
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Absurd i. Clearly impossible being contrary to some evident truth.
> - **B.** Ambiguous ii. Capable of more than one interpretation or meaning.
> - **C.** Axiom iii. An assertion that is accepted and used without a proof.
> - **D.** Conjecture iv. An opinion preferably based on some experience or wisdom. Codes : a b c d

**Options**

1. i ii iii iv
2. i iii iv ii
3. ii iii iv i
4. ii i iii iv

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 196

*UGC NET Jan 2017, Paper II, original Q12*

> Which one of the following is correct for overloaded functions in C++ ?

**Options**

1. Compiler sets up a separate function for every definition of function.
2. Compiler does not set up a separate function for every definition of function.
3. Overloaded functions cannot handle different types of objects.
4. Overloaded functions cannot have same number of arguments.

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 197

*UGC NET Jan 2017, Paper III, original Q65*

> A t-error correcting q-nary linear code must satisfy : M t Σ i = 0⎝ ⎛ ⎠ ⎞n i (q – 1)i ≤ X Where M is the number of code words and X is

**Options**

1. q n
2. q t
3. q –n
4. q –t

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 198

*UGC NET July 2018, Paper II, original Q32*

> The finite state machine given in figure below recognizes :

**Options**

1. any string of odd number of a’s
2. any string of odd number of b’s
3. any string of even number of a’s and odd number of b’s
4. any string of odd number of a’s and odd number of b’s

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 199

*UGC NET July 2018, Paper II, original Q76*

> Consider the following statements : (a) False /c4994= True (b) If α /c4994= (β ∧ γ) then α /c4994= β and α /c4994= γ. Which of the following is correct with respect to the above statements ?

**Options**

1. Both statement (a) and statement (b) are false.
2. Statement (a) is true but statement (b) is false.
3. Statement (a) is false but statement (b) is true.
4. Both statement (a) and statement (b) are true.

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 200

*UGC NET Nov 2021, original Q21*

> A only 2. A and B only 3. B and C only 4. A and C only

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 201

*UGC NET Nov 2021, original Q22*

> Both Statement I and Statement II are true 2. Both Statement I and Statement II are false 3. Statement I is true but Statement II is false 4. Statement I is false but Statement II is true

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 202

*UGC NET Nov 2021, original Q23*

> How many ways are there to assign 5 different jobs to 4 different employees if every employee is assigned at least 1 job?

**Options**

1. 1024
2. 625
3. 240
4. 20

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 203

*UGC NET Nov 2021, original Q27*

> A and B only 2. B and C only 3. A only 4. B only

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 204

*UGC NET Nov 2021, original Q35*

> What is the minimum number of states required to the finite automaton equivalent to the transition diagram given below?

**Options**

1. 3
2. 4
3. 5
4. 6

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 205

*UGC NET Nov 2021, original Q41*

> The postfix form of the expression (A + B) * (C * D ‐ E) * F / G is _______ .

**Options**

1. A B + C D * E – F G / * *
2. A B + C D * E – F * * G /
3. A B + C D * E – * F * G /
4. A B + C D E * – * F * G /

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 206

*UGC NET Oct 2022, original Q6*

> The number of gate inputs. required to realize expression ABC + ABCD + EF +AD is 12 2. 13 3. 14 4. 15

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 207

*UGC NET Oct 2022, original Q15*

> Consider L = (ab. aa, baa) Which of the following string is NOT in L*? 1. baaaaabaaaaa 2. abaabaaabaa

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 208

*UGC NET Oct 2022, original Q58*

> (A) and (B) only 2. (B) and (C) only 3. (C) and (A) only 4. AII (A). (B) and (C)

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 209

*UGC NET Oct 2022, original Q60*

> (B) and (C) only 2. (A) and (B) only 3. (A), (B) and (C) only

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 210

*UGC NET Oct 2022, original Q61*

> (A) and (D) only 2. B) and (C) only 3. (A) and (C) only 4. (B) and (D) only

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 211

*UGC NET Oct 2022, original Q62*

> Let ({a.b).*) be a semigroup, where a*a = b. (A) (B) b*b =6 Choose the most appropriate answer from the options given below:

**Options**

1. (A) only true
2. (B) only true
3. Both (A) and (B) true
4. Neither (A) nor (B) true

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 212

*UGC NET Oct 2022, original Q64*

> (A) and (B) only true 2. (B) and (C) only true 3. (A) and (C) only true 4. (A). (B) and (C) true

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 213

*UGC NET Oct 2022, original Q85*

> Both (A) and (R) are true and (R) is the correct explanation of (A) 2. Both (A) and (R) are true but (R) is NOT the correct explanation of (A) 3. (A) is true but (R) is false 4. (A) is false but (R) is true

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 214

*UGC NET Oct 2022, original Q87*

> Both (A) and (R) are true and (R) is the correct explanation of (A) 2. Both (A) and (R) are true but (R) is NOT the correct explanation of (A) 3. (A) is true but (R) is false 4. (A) is false but (R) is true

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 215

*UGC NET Aug 2024, original Q101*

> Arrange the following stages of parsing in the correct order as they typically occur in the compilation process.
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Lexical Analysis
> - **B.** Sematic Analysis
> - **C.** Syntax Analysis
> - **D.** Intermediate Code Generation (E) Code Optimization Choose the correct answer from the options given below : (1)

**Options**

- **A.** ,
- **B.** ,
- **C.** ,
- **D.** , (E) (2) (A), (C), (B), (D), (E) (3) (A), (D), (B), (C), (E) (4) (A), (C), (D), (B), (E) 65/101

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 216

*UGC NET Aug 2024, original Q117*

> Which of the following tasks could be attained using syntax trees in compiler design?

**Options**

- **A.** Type Checking
- **B.** Code Generation
- **C.** Code Optimization
- **D.** Error Handling Choose the correct answer from the options given below : (1) (A), (B), (C) Only (2) (B), (C), (D) Only 3) (A), (C), (D) Only (4) (A), (B), (D) Only

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 217

*UGC NET June 2024, original Q102*

> The following code: stmt → if expr then stant else stmt I if expr then stmt suffers from: CO (1) Ambiguity (2) Left factoring MLeft Recurssion (4) A-moves

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 218

*UGC NET June 2025, original Q134*

> Match List I with List II List I List lI
>
> **Additional extracted choices — check the source page:**
>
> - **A.** Equivalence Partitioning 1. Measures independent paths in code
> - **B.** Boundary Value Analysis II. Divides input into valid/invalid sets
> - **C.** Cyclomatic Complexity III. Focuses on limits of input ranges
> - **D.** Decision Table Testing IV. In which a number of combinations of actions are tested under varying sets of conditions. Choose the correct answer from the options given below:

**Options**

1. A-II, B-III, C-I, D-IV
2. A-II, B-III, C-IV, D-1
3. A-III, B-II, C-I, D-IV
4. A-IV, B-II, C-I, D-III 42558919589.2 42558919590. 3 42558919591.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 219

*UGC NET Dec 2025 session (Jan 2026), original Q100*

> Question Number : 100

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 220

*UGC NET Dec 2025 session (Jan 2026), original Q104*

> Question Number: 104

**Chapter foundations**

This question belongs to the ideas covered by **Code Generation and Optimization**. Revise these foundations: Control-Flow and Data-Flow Analysis; Local, Global, Loop and Peephole Optimization; Instruction Scheduling.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Code Generation and Optimization questions: For automata trace states or build a product machine; for grammars compute FIRST/FOLLOW and items; for decidability use closure or reduction arguments. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

## Coverage and quality notes

- Recovered question blocks in this unit: **220**
- Chapter placements with direct keyword support: **191**
- Chapter placements needing manual review: **29**
- Questions with validated answers in this guide: **0**
- OCR may flatten mathematical notation, tables, code indentation, and figures. Full audit references are retained in the structured data.
- Some combined Paper 1/Paper 2 scans and older papers lack a trustworthy embedded key. Such questions remain pending rather than receiving guessed answers.

---

[Back to contents](#contents) · [All units](README.md) · [Project home](../README.md)

