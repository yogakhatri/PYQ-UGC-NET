# Unit 6: Software Engineering

[Project home](../README.md) · [All units](README.md) · [Official syllabus](syllabus.md)

## Contents

- [How to use this guide](#status-and-use)
- [Unit-wide exam playbook](#unit-wide-exam-playbook)
- [1. Software Process Models](#chapter-1)
- [2. Software Requirements](#chapter-2)
- [3. Software Design](#chapter-3)
- [4. Software Quality](#chapter-4)
- [5. Estimation and Scheduling](#chapter-5)
- [6. Software Testing](#chapter-6)
- [7. Software Configuration Management](#chapter-7)
- [Coverage and quality notes](#coverage-and-quality-notes)

## Status and use

This guide contains all **178 question blocks currently recoverable and assigned to Unit 6** from the local UGC NET archive. Questions are arranged chapter-wise and numbered continuously through the unit.

> [!WARNING]
> This is a working extraction inventory, not a solved guide. All answers remain unvalidated. Some unit and chapter placements use fallback routing, and OCR or missing figures can make questions incomplete.

Use this file for question discovery and broad chapter revision. The chapter notes and exam methods are general, not question-specific solutions. Full source paths, PDF pages and classification states remain in the structured data for auditing.

## Unit-wide exam playbook

- **Core idea:** Identify the lifecycle artifact or metric being tested and map it to requirements, design, estimation, quality, testing, or configuration management.
- **Method:** Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics.
- **Rules/formulas:** Cyclomatic complexity V(G) = E-N+2P. Basic COCOMO effort is a(KLOC)^b and schedule is c(Effort)^d. Function points use weighted counts and an adjustment factor.
- **Frequent traps:** Verification asks whether the product is built right; validation asks whether the right product is built. Cohesion should rise while coupling should fall.

## Chapter-wise concepts and PYQs

<a id="chapter-1"></a>

### 1. Software Process Models (56 questions)

**What to master:** Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam lens:** Identify the lifecycle artifact or metric being tested and map it to requirements, design, estimation, quality, testing, or configuration management.

**Reusable method:** Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics.

**High-yield rules:** Cyclomatic complexity V(G) = E-N+2P. Basic COCOMO effort is a(KLOC)^b and schedule is c(Effort)^d. Function points use weighted counts and an adjustment factor.

**Common traps:** Verification asks whether the product is built right; validation asks whether the right product is built. Cohesion should rise while coupling should fall.

---

#### Question 1

*UGC NET Dec 2009, Paper II, original Q41*

> Software Engineering is a discipline that integrates _________ for th e development of computer software. (A) Process (B) Methods (C) Tools (D) All

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 2

*UGC NET Dec 2009, Paper II, original Q43*

> Recorded software attributes can be used in the following end eavours : (i) Cost and schedule estimates. (ii) Software product reliability predictions. (iii) Managing the development process. (iv) No where Codes : (A) (i) (ii) (iv) (B) (ii) (iii) (iv) (C) (i) (ii) (iii) (D) (i) (ii) (iii) (iv)

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 3

*UGC NET June 2010, Paper II, original Q41*

> Software engineering primarily aims on (A) reliable software (B) cost effective software (C) reliable and cost effective software (D) none of the above

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 4

*UGC NET June 2010, Paper II, original Q43*

> Which model is simplest model in Software Development ? (A) Waterfall model (B) Prototyping (C) Iterative (D) None of these

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 5

*UGC NET Dec 2011, Paper III, original Q2*

> (a) What do you mean by a software process ? What is the diffe rence between a methodology and a process ? What problem will a Software Developme nt house face if it does not follow any systematic process in its software development efforts ? (b) Which are the major phases in the waterfall model of softwa re development ? Which phase consumes the maximum effort ? OR (a) Show that a static two phase locking schedule satisfies t he condition for dynamic two phase locking. Is the converse true ? (b) Propose a multi version protocol base on locking. Prove that the protoc ol is safe. Compare the performance of this protocol with the one based on time stemp ordering. _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 6

*UGC NET Dec 2011, Paper III, original Q13*

> Compare the relative advantages of using the iterative waterf all model and the spiral model of software development. Explain with the help of few suitable examples, the types of problem for which you would adopt above models. _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 7

*UGC NET June 2012, Paper II, original Q20*

> Main aim of software engineering is to produce (A) program (B) software (C) within budget (D) software within budget in the given schedule

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 8

*UGC NET June 2012, Paper II, original Q23*

> If a process is under statistical control, then it is (A) Maintainable (B) Measurable (C) Predictable (D) Verifiable

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 9

*UGC NET June 2013, Paper III, original Q1*

> The Software Maturity Index (SMI) is defined as SMI = [M f – (Fa + Fc + Fd)] / Mf Where M f = the number of modules in the current release. F a = the number of modules in the current release that have been added. F c = the number of modules in the current release that have been changed. F d = the number of modules in the current release that have been deleted. The product begins to stabilize when (A) SMI approaches 1 (B) SMI approaches 0 (C) SMI approaches –1 (D) None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 10

*UGC NET June 2013, Paper III, original Q2*

> Match the following : a. Watson- Felix model i. Failure intensity b. Quick-Fix model ii. Cost estimation c. Putnam resource allocation model iii. Project planning d. Logarithmetic- Poisson Model iv. Maintenance Codes : a b c d (A) ii i iv iii (B) i ii iv iii (C) ii i iii iv (D) ii iv iii i 3. __________ is a process model that removes defects before they can precipitate serious hazards. (A) Incremental model (B) Spiral model (C) Cleanroom software engineering (D) Agile model

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 11

*UGC NET Dec 2014, Paper II, original Q42*

> Requirement Development, Organizational Process Focus, Organizationa l Training, Risk Management and Integrated Supplier Management are process areas re quired to achieve maturity level (A) Performed (B) Managed (C) Defined (D) Optimized

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 12

*UGC NET Dec 2014, Paper III, original Q45*

> Assume that the software team defines a project risk with 80% probability of occurrence of risk in the following manner : Only 70 percent of the software components scheduled for reuse will be integrat ed into the application and the remaining functionality will have to be custom deve loped. If 60 reusable components were planned with average component size as 100 LO C and software engineering cost for each LOC as $ 14, then the risk exposure would be (A) $ 25,200 (B) $ 20,160 (C) $ 17,640 (D) $ 15,120

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 13

*UGC NET Dec 2014, Paper III, original Q60*

> A computer based information system is needed : I. as it is difficult for administrative staff to process data. II. due to rapid growth of information and communication technology. III. due to growing size of organizations which need to process large volume of data. IV. as timely and accurate decisions are to be taken. Which of the above statement(s) is/are true ? (A) I and II (B) III and IV (C) II and III (D) II and IV

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 14

*UGC NET Dec 2015, Paper II, original Q47*

> Which of the following is not a software process model ? (1) Prototyping

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 15

*UGC NET June 2015, Paper II, original Q43*

> Which process model is also called as classic life cycle model ? (1) Waterfall model (2) RAD model (3) Prototyping model (4) Incremental model

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 16

*UGC NET June 2015, Paper III, original Q43*

> Verification: (1) refers to the set of activities that ensure that software correctly implements a specific function (2) gives answer to the question - Are we building the product right? (3) requires execution of software (4) both (1) and (2)

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 17

*UGC NET July 2016, Paper II, original Q42*

> The ________ model is preferred for software development when the requirements are not clear. (1) Rapid Application Development (2) Rational Unified Process (3) Evolutionary Model (4) Waterfall Model

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 18

*UGC NET July 2016, Paper III, original Q21*

> Which of the following is false regardi ng the evaluation of computer programming languages ? (1) Application oriented features (2) Efficiency and Readability (3) Software development (4) Hardware maintenance cost

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 19

*UGC NET Jan 2017, Paper II, original Q41*

> Software Engineering is an engineering discipline that is concerned with : (1) how computer systems work. (2) theories and methods that underlie computers and software systems. (3) all aspects of software production (4) all aspects of computer-based systems development, including har dware, software and process engineering.

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 20

*UGC NET Jan 2017, Paper II, original Q46*

> Match the following : List – I List – II a. Affiliate Marketing i. Vendors ask partners to place logos on partner’s site. If customers click, come to vendors and buy. b. Viral Marketing ii. Spread your brand on the net by word- of-mouth. Receivers will send your information to their friends. c. Group Purchasing iii. Aggregating the demands of small buyers to get a large volume. Then negotiate a price. d. Bartering Online iv. Exchanging surplus products and services with the process administered completely online by an intermediary. Company receives “points” for its contribution. Codes : a b c d (1) i ii iii iv (2) i iii ii iv (3) iii ii iv i (4) ii iii i iv

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 21

*UGC NET Jan 2017, Paper III, original Q15*

> Match the following : a. Glass i. Contains liquid cr ystal and serves as a bonding surface for a conductive coating. b. Conductive coating ii. Acts as a c onductor so that a voltage can be applied across the liquid crystal. c. Liquid crystal iii. A substance which will polarize light when a voltage is applied to it. d. Polarized film iv. A transparen t sheet that polarizes light. Codes : a b c d (1) i ii iii iv (2) i iii ii iv (3) iv iii ii i (4) iv ii i iii

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 22

*UGC NET Jan 2017, Paper III, original Q46*

> A software project was estimated at 352 Func tion Points (FP). A four person team will be assigned to this project consisting of an architect, two programmers, and a tester. The salary of the architect is ` 80,000 per month, the programmer ` 60,000 per month and the tester ` 50,000 per month. The average productivit y for the team is 8 FP per person month. Which of the following represents the projected cost of the project ? (1) ` 28,16,000 (2) ` 20,90,000 (3) ` 26,95,000 (4) ` 27,50,000

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 23

*UGC NET Jan 2017, Paper III, original Q48*

> A software company needs to develop a proj ect that is estimated as 1000 function points and is planning to use JAVA as the program ming language whose approximate lines of code per function point is accepted as 50. Consideri ng a = 1.4 as multiplicative factor, b = 1.0 as exponention factor for the basi c COCOMO effort equation and c = 3.0 as multiplicative factor, d = 0.33 as exponention factor for the basic COCOMO duration equation, approximately how long does the project take to complete ? (1) 11.2 months (2) 12.2 months (3) 13.2 months (4) 10.2 months

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 24

*UGC NET Nov 2017, Paper II, original Q41*

> Software does not wear-out in the traditional sense of the term, but sof tware does tend to deteriorate as it evolves, because : (1) Software suffers from exposure to hostile environments. (2) Defects are more likely to arise after software has been used often. (3) Multiple change requests introduce errors in component interactions . (4) Software spare parts become harder to order.

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 25

*UGC NET Nov 2017, Paper II, original Q42*

> Software re-engineering is concerned with : (1) Re-constructing the original source code from the existing machin e (low - level) code program and modifying it to make it more user - friendly. (2) Scrapping the source code of a software and re-writing it entirely fr om scratch. (3) Re-organising and modifying existing software systems to make them more maintainable. (4) Translating source code of an existing software to a new machine (low - level) language.

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 26

*UGC NET Dec 2018, original Q105*

> Which of the following statements is/are false? P: The clean-room strategy to software engineering is based on the incremental software process model. Q: The clean-room strategy to software engineering is one of the ways to overcome "unconscious" copying of copyrighted code. Choose the correct answer from the code given below : Code: . Ponly 91394342418. Qonly Guide 91394342419. Both Pand Q lal Exam 91394342420 Neither P nor Q ingle Line Question Option: No

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 27

*UGC NET Dec 2018, original Q107*

> A legacy software system has 940 modules. The latest release required that 90 of these modules be changed. In addition, 40 new modules were added and 12 old modules were removed. Compute the software maturity index for the system. -849 91394342426. 0-524 91394342427. 0-725 91394342428. 0-923 ingle Line Question Option : No

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 28

*UGC NET July 2018, Paper II, original Q11*

> Assume the following regarding the development of a software system P : - Estimated lines of code of P : 33, 480 LOC - Average productivity for P : 620 LOC per person-month - Number of software developers : 6 - Average salary of a software developer : ` 50,000 per month If E, D and C are the estimated development effort (in person-months), estimated development time (in months), and estimated development cost (in ` Lac) respectively, then (E, D, C) =_________. (1) (48, 8, 24) (2) (54, 9, 27) (3) (60, 10, 30) (4) (42, 7, 21)

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 29

*UGC NET July 2018, Paper II, original Q14*

> A software system crashed 20 times in the year 2017 and for each crash, it took 2 minutes to restart. Approximately, what was the software availability in tha t year ? (1) 96.9924% (2) 97.9924% (3) 98.9924% (4) 99.9924%

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 30

*UGC NET July 2018, Paper II, original Q15*

> Match the 5 CMM Maturity levels/CMMI staged representations in List- I with their characterizations in List-II : List - I List - II (a) Initial (i) Processes are improved quantitatively and continually. (b) Repeatable (ii) The plan for a project comes from a template for plans. (c) Defined (iii) The plan uses processes that can be measured quantitatively. (d) Managed (iv) There may not exist a plan or it may be abandoned. (e) Optimizing (v) There’s a plan and people stick to it. Code : (a) (b) (c) (d) (e) (1) (iv) (v) (i) (iii) (ii) (2) (i) (ii) (iv) (v) (iii) (3) (v) (iv) (ii) (iii) (i) (4) (iv) (v) (ii) (iii) (i)

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 31

*UGC NET July 2018, Paper II, original Q20*

> Which of the following statements is/are True ? P : Refactoring is the process of changing a software system in such a way that it does not alter the external behavior of the code yet improves the internal architect ure. Q : An example of refactoring is adding new features to satisfy a customer requirement discovered after a project is shipped. Code : (1) P only (2) Q only (3) Both P and Q (4) Neither P nor Q

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 32

*UGC NET Dec 2019, original Q111*

> ersonal Ex Consider the following models: M1: Mamdani model M2: Takagi - Sugeno-Kang model Mз: Kosko's additive model (SAM) Which of the following option contains examples of additive rule model? (1) Only Mi and M2 (2) Only Mo and M3 (3) Only Mi and M3 (4) Mi.M2. and Ma 61547541142.2 61547541143. 3 61547541144.4

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 33

*UGC NET Dec 2019, original Q134*

> Match the Agile Process models with the task performed during the model : List I List II (a) Scrum (i): CRC cards (b) Adaptive software development (ii) Sprint backlog (c) Extreme programming (iii) <action> the <result> <by/for/of/to> an) <object> Feature-driven development (iv) Time box release plan Choose the correct option from those given below : (1) (a) (ii), (b)-(iv), (c)-i). (d) (ili) (2) (a)-(i), (b)-(iii). (c)-(ii). (d)-(iv) (3) (a)-(ii), (b)-(i). (c)-(iv), (d) (ill) (4) (a)-(i), (b)-(iv), (c) -(ii), (d)-(iii) Options :

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 34

*UGC NET June 2019, original Q108*

> Software products need adaptive maintenance for which of the following reasons? 1. To rectify bugs observed while the system is in use 2. When the customers need the product to run on new platforms 3. To support the new features that users want it to support 4. To overcome wear and tear caused by the repeated use of the software 64635085768. 2 64635085769. 3 64635085770.4

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 35

*UGC NET Nov 2020, original Q70*

> Modifying the software by restructuring is called (1) Adaptive maintenance (2) Corrective maintenance (3) Perfective maintenance (4) Preventive maintenance ,1 53622816778.2 53622816779.3 53622816780.4

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 36

*UGC NET Nov 2020, original Q71*

> A Company has a choice of two languages 41 and L2 to develop a software for their chent. Number of LOC required to develop an application in L, is thrice the LOC in language L1. Also, software has to be maintained for next 10 years. Various parameters for two languages are given below to decide which language should be preferred for development. PARAMETER 5 Man-year needed for development LOC/1000 LOC/1000 Development cost Rs.70,000 Rs.90,000 Cost of Maintenance per year Rs. 1.00,000 Rs. 40,000 Total cost of project include cost of development and maintenance. What is the LOC for L1 for which cost of developing the software with both languages must be same? (1) 2000 (2) 6000 (3) 3000 (4) 5000 53622816782.2 53622816783.3 53622816784.4

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 37

*UGC NET Nov 2020, original Q72*

> A Software project was estimated at 864 Function Points. A six person team will be assigned to project consisting of a requirement gathering person, one designer. two programmers and two testers. The salary of the designer is *70.000 per month, requirement gatherer is 250,000 per month, programmer is t60,000 per month and a tester is 260.000 per month. Average productivity for the team is 12 FP per person month. Which of the following represents the projected cost of the project? (1) ·33,20,000 (2) ·48,20,000 (3) · 33,10,000 (4) · 22,10,000 53622816786.2 53622816787.3 53622816788.4

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 38

*UGC NET Nov 2020, original Q118*

> Match List I with List II With reference to CMM developed by Software Engineering Institute (SET) List I List II (A) INITIAL (I) Process measurement (B) REPEATABLE (I Process definition (C) DEFINED (I1) Project management (D) MANAGED (IV) ADHOC Choose the correct answer from the options given below: (1) A-III, B-IV. C-II, D-I (2) A-IV. B-III. C.I. D.II (3) A-IV. B-III, C-II, D-I (4) A-III. B-IV. C-I D-II 53622816970.2 53622816971.3

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 39

*UGC NET Nov 2021, original Q13*

> User interface. In software engineering, what kind of notation do formal methods predominantly use? 1. textual 14) 15) 16) 17) 18) 19) 20) 21) 22) 23) 24) 25) 26) 27) 28) 2. diagrammatic 3. mathematical 4. computer code

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 40

*UGC NET Nov 2021, original Q17*

> A and B only Match List I with List II List I List II (Software Process Model) (Decsription) A. Waterfall Model I. Software can be developed incrementally B. Evolutionary Model II. Requirement compromises are inevitable C. Component‐based Software Engineeering III. Explicit recognition of risk D. Spiral Development IV. Inflexible partitioning of the project into stages Choose the correct answer from the options given below: 1. A ‐ IV, B ‐ I, C ‐ III, D ‐ II 2. A ‐ I, B ‐ IV, C ‐ II, D ‐ III 3. A ‐ II, B ‐ III, C ‐ I, D ‐ IV 4. A ‐ IV, B ‐ I, C ‐ II, D ‐ III

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 41

*UGC NET Nov 2021, original Q18*

> A ‐ IV, B ‐ I, C ‐ III, D ‐ II Identify the correct order of the following five levels of Capability Maturity Model (from lower to higher) to measure the maturity of an organisation's software process. A. Defined B. Optimizing C. Initial D. Managed E. Repeatable Choose the correct answer from the options given below 1. C, A, E, D, B 2. C, E, A, B, D 3. C, B, D, E, A 4. C, E, A, D, B

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 42

*UGC NET Nov 2021, original Q19*

> C, A, E, D, B Given below are two statements Statement I: Cleanroom software process model incorporates the statistical quality certification of code increments as they accumulate into a system. Statement II: Cleanroom software engineering follows the classic analysis, design, code, test, and debug cycle to software development and focussing on defect removal rather than defect prevention. In light of the above statements, choose the correct answer from the options given below 1. Both Statement I and Statement II are true 2. Both Statement I and Statement II are false 3. Statement I is true but Statement II is false 4. Statement I is false but Statement II is true

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 43

*UGC NET Oct 2022, original Q25*

> Steganography 2. Relative Application Development 3. Rapid Application Desien 4. Recent Application Development

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 44

*UGC NET Oct 2022, original Q26*

> If every requirement can be checked by a cost - effective process, then SRS is called 1. Verifiable 2. Tracable 3. Modifiable 4. Complete

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 45

*UGC NET Oct 2022, original Q29*

> The process to gather the software requirements from client. analyze and document is known as - 1. Software Engineering Process 2. User Engineering Process 3. Requirement Elicitation Process 4. Requirement Engineering Process

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 46

*UGC NET Oct 2022, original Q30*

> Size and complexity are a part of 1. People Metrics 2. Project Metrics 3. Process Metrics 4. Product Metrics

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 47

*UGC NET Aug 2024, original Q60*

> If a software project has 2000 lines of code (LOC) and the average productivity rate is 10 LOC per person-hour, how many person-hours are required to complete the project? 100 (2) 150 (3) 200 (4) 250

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 48

*UGC NET Aug 2024, original Q96*

> Arrange the following phases of the Agile process in the correct sequence: (A) Design (B) Release (C) Testing (D) Development (E) Planning Choose the correct answer from the options given below : (1) (A), (B), (D), (E), (C) (2) (A), (D), (E), (B), (C) (3) (E), (A), (D), (C), (B) (4) (E), (D), (A), (C), (B)

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 49

*UGC NET Aug 2024, original Q97*

> Arrange the following steps of Feature Drive Development (FDD) process in the correct sequence : (A) Develop an overall model (B) Build by feature (C) Plan by feature (D) Design by feature (E) Build a feature list Choose the correct answer from the options given below : (1) (A), (C), (B), (E), (D) (2) (A), (E), (C), (D), (B) 3) (B), (A), (D), (E), (C) (4) (A), (B), (C), (E), (D)

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 50

*UGC NET Aug 2024, original Q119*

> Which of the following are typical activities in the software process lifecycle ? (A) Requirement Analysis (B) System Design (C) Code Refactoring (D) Deployment (E) Substructure Choose the correct answer from the options given below : (1) (A), (B), (C) Only (2) (B), (C), (D) Only (3) (A), (B), (D) Only (4) (A), (D), (E) Only

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 51

*UGC NET Aug 2024, original Q120*

> Which of the following are Agile Process Models? (A) Extreme Programming (XP) (B) Waterfall (C) Scrum (D) Spiral (E) Incremental Choose the correct answer from the options given below : (1) (A) and (C) Only (2) (B) and (C) Only (3) (A) and (D) Only (4) (B) and (E) Only

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 52

*UGC NET Aug 2024, original Q148*

> Which of the following is NOT a requirement for Banker's algorithm to grant a resource request? (1) The requested resources must be available. (2) The system must be in a safe state after granting the request. (3) The request must not exceed the maximum resources the process can request. (4) The process must be the only one requesting resources.

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 53

*UGC NET June 2025, original Q74*

> The process followed in order to find difficult, unknown and hidden information about a software system is called (1) Software Engineering (2) Software Re-Engineering (3) Reverse Engineering (4) Inverse Engineering 42558919349. 2 42558919350.3 42558919351.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 54

*UGC NET June 2025, original Q75*

> Which of the followings is NOT a software characteristic? (1) Software does not wear out (2) Software is flexible (3) Software is not manufactured (4) Software is always correct 42558919353.2 42558919354, 3 42558919355.4

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 55

*UGC NET Dec 2025 session (Jan 2026), original Q140*

> Question Number : 140

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 56

*UGC NET Dec 2025 session (Jan 2026), original Q142*

> Question Number : 142

**Chapter foundations**

This question belongs to the ideas covered by **Software Process Models**. Revise these foundations: Software Process; Generic Process Model; Framework Activities; Task Sets and Patterns; Lifecycle; Prescriptive Models; Project Management; Component-Based and Aspect-Oriented Development; Formal Methods; Agile Models - XP, Adaptive Software Development, Scrum, DSDM, Feature-Driven Development, Crystal; Web Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Process Models questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-2"></a>

### 2. Software Requirements (10 questions)

**What to master:** Functional and Non-Functional Requirements; Elicitation; Use Cases; Analysis and Modelling; Review; SRS.

**Exam lens:** Identify the lifecycle artifact or metric being tested and map it to requirements, design, estimation, quality, testing, or configuration management.

**Reusable method:** Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics.

**High-yield rules:** Cyclomatic complexity V(G) = E-N+2P. Basic COCOMO effort is a(KLOC)^b and schedule is c(Effort)^d. Function points use weighted counts and an adjustment factor.

**Common traps:** Verification asks whether the product is built right; validation asks whether the right product is built. Cohesion should rise while coupling should fall.

---

#### Question 57

*UGC NET Dec 2013, Paper III, original Q9*

> Which once of the following is not a software myth ? (A) Once we write the program and get it to work, our job is done. (B) Project requirements continually change, but change can be easily accommodated because software is flexible. (C) If we get behind schedule, we can add more programmers and catch up. (D) If an organization does not understand how to control software projects internally, it will invariably struggle when it outsources software projects.

**Chapter foundations**

This question belongs to the ideas covered by **Software Requirements**. Revise these foundations: Functional and Non-Functional Requirements; Elicitation; Use Cases; Analysis and Modelling; Review; SRS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Requirements questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 58

*UGC NET Dec 2014, Paper II, original Q44*

> Which one of the following set of attributes should not be encompassed by effective software metrics ? (A) Simple and computable (B) Consistent and objective (C) Consistent in the use of units and dimensions (D) Programming language dependent

**Chapter foundations**

This question belongs to the ideas covered by **Software Requirements**. Revise these foundations: Functional and Non-Functional Requirements; Elicitation; Use Cases; Analysis and Modelling; Review; SRS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Requirements questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 59

*UGC NET Dec 2015, Paper III, original Q74*

> Which one of the following statements, related to the requirements phase in Software Engineering, is incorrect ? (1) "Requirement validation" is one of the activities in the requirements phase. (2) "Prototyping" is one of the methods for requirement analysis. (3) "Modelling-oriented approach" is one of the methods for specifying the functional specifications. (4) "Function points" is one of the most commonly used size metric for requirements. 75. tag is an extension to HTML that can enclose any number of Javascript statements. (1) <SCRIPT> (2) < BODY> (3) < HEAD> (4) <TITLE> - 000- D-8715 15 Paper-III

**Chapter foundations**

This question belongs to the ideas covered by **Software Requirements**. Revise these foundations: Functional and Non-Functional Requirements; Elicitation; Use Cases; Analysis and Modelling; Review; SRS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Requirements questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 60

*UGC NET June 2015, Paper III, original Q45*

> Requirements prioritisation and negotiation belongs to : (1) Requirements validation (2) Requirements elicitation (3) Feasibility study (4) Requirements reviews

**Chapter foundations**

This question belongs to the ideas covered by **Software Requirements**. Revise these foundations: Functional and Non-Functional Requirements; Elicitation; Use Cases; Analysis and Modelling; Review; SRS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Requirements questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 61

*UGC NET July 2016, Paper III, original Q44*

> Match the software maintenance activities in List – I to its meaning in List – II. List – I List – II I. Corrective (a) Concerned with perfor ming activities to reduce the software complexity thereby improvi ng program understandability and increasing software maintainability. II. Adaptive (b) Concerned with fixing errors that are observed when the software is in use. III. Perfective (c) Concerned with the cha nge in the software that takes place to make the software adaptable to new environment (both hardware and software). IV. Preventive (d) Concerned with the change in the software that takes place to make the software adaptable to changing user requirements. Codes : I II III IV (1) (b) (d) (c) (a) (2) (b) (c) (d) (a) (3) (c) (b) (d) (a) (4) (a) (d) (b) (c)

**Chapter foundations**

This question belongs to the ideas covered by **Software Requirements**. Revise these foundations: Functional and Non-Functional Requirements; Elicitation; Use Cases; Analysis and Modelling; Review; SRS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Requirements questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 62

*UGC NET Jan 2017, Paper II, original Q44*

> The prototyping model of software development is : (1) a reasonable approach when requirements are well-defined. (2) a useful approach when a customer cannot define requirements clearly. (3) the best approach to use for projects with large development teams. (4) a risky model that rarely produces a meaningful product.

**Chapter foundations**

This question belongs to the ideas covered by **Software Requirements**. Revise these foundations: Functional and Non-Functional Requirements; Elicitation; Use Cases; Analysis and Modelling; Review; SRS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Requirements questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 63

*UGC NET June 2019, original Q110*

> Software validation mainly checks for inconsistencies between 1. use cases and user requirements 2. implementation and system design blueprints 3. detailed specifications and user requirements 4. functional specifications and use cases 64635085776. 2 64635085777.3 64635085778. 4

**Chapter foundations**

This question belongs to the ideas covered by **Software Requirements**. Revise these foundations: Functional and Non-Functional Requirements; Elicitation; Use Cases; Analysis and Modelling; Review; SRS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Requirements questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 64

*UGC NET Nov 2021, original Q14*

> textual If every requirement stated in the Software Requirement Specification (SRS) has only one interpretation, then SRS is said to be 1. correct 2. consistent 3. unambiguous 4. verifiable

**Chapter foundations**

This question belongs to the ideas covered by **Software Requirements**. Revise these foundations: Functional and Non-Functional Requirements; Elicitation; Use Cases; Analysis and Modelling; Review; SRS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Requirements questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 65

*UGC NET Oct 2022, original Q32*

> The model in which the requirements are implemented by its category is 1. Evolutionary Development Model 2. Waterfall Model 3. Prototyping Model 4. Iterative Enhancement Model

**Chapter foundations**

This question belongs to the ideas covered by **Software Requirements**. Revise these foundations: Functional and Non-Functional Requirements; Elicitation; Use Cases; Analysis and Modelling; Review; SRS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Requirements questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 66

*UGC NET June 2023, Paper II, original Q78*

> Given below are two statements: one is labelled as Assertion A and the other is (+2) labelled as Reason R. Assertion A: Validity checks real need of system users Reason R: Completeness checks system user defined requirements. In the light of the above statements, choose the correct answer from the options given below. a. Both A and R are true and R is the correct explanation of A b. Both A and R are true but R is NOT the correct explanation of A c. A is true but R is false d. A is false but R is true

**Chapter foundations**

This question belongs to the ideas covered by **Software Requirements**. Revise these foundations: Functional and Non-Functional Requirements; Elicitation; Use Cases; Analysis and Modelling; Review; SRS.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Requirements questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-3"></a>

### 3. Software Design (36 questions)

**What to master:** Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam lens:** Identify the lifecycle artifact or metric being tested and map it to requirements, design, estimation, quality, testing, or configuration management.

**Reusable method:** Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics.

**High-yield rules:** Cyclomatic complexity V(G) = E-N+2P. Basic COCOMO effort is a(KLOC)^b and schedule is c(Effort)^d. Function points use weighted counts and an adjustment factor.

**Common traps:** Verification asks whether the product is built right; validation asks whether the right product is built. Cohesion should rise while coupling should fall.

---

#### Question 67

*UGC NET June 2010, Paper II, original Q42*

> Top-down design does not require (A) step-wise refinement (B) loop invariants (C) flow charting (D) modularity

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 68

*UGC NET June 2010, Paper II, original Q44*

> Design phase will usually be (A) top-down (B) bottom-up (C) random (D) centre fringing

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 69

*UGC NET Dec 2011, Paper III, original Q17*

> How would you improve a software design that displays very low cohesion and high coupling ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ ______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 70

*UGC NET Dec 2012, Paper II, original Q39*

> Match the following with respect to (D) decreases Data Integrity. C+t data types : a. User defined type

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 71

*UGC NET Dec 2012, Paper II, original Q43*

> Data Encryption Techniques are (A) 1 particularly used for (B) 3 (A) protecting data in Data (C) 2 3 1 Communication System. (D) 2 1 3 (B) reduce Storage Space Requirement. (C) enhances Data Integrity.

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 72

*UGC NET June 2012, Paper II, original Q24*

> In a function oriented design, we (A) minimize cohesion and maximize coupling (B) maximize cohesion and minimize coupling (C) maximize cohesion and maximize coupling (D) minimize cohesion and minimize coupling

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 73

*UGC NET Dec 2013, Paper II, original Q7*

> The relationship of data elements in a module is called (A) Coupling (B) Modularity (C) Cohesion (D) Granularity

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 74

*UGC NET Dec 2013, Paper II, original Q9*

> Which one of the following is not a step of requirement engineering ? (A) Requirement elicitation (B) Requirement analysis (C) Requirement design (D) Requirement documentation COMPUTER SCIENCE AND APPLICATIONS Paper – II Note : This paper contains fifty (50) objective type questions of two (2) marks each. All questions are compulsory.

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 75

*UGC NET June 2013, Paper III, original Q5*

> The following three golden rules : (i) Place the user in control (ii) Reduce the user’s memory load (iii) Make the interface consistent are for (A) User satisfaction (B) Good interface design (C) Saving system’s resources (D) None of these

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 76

*UGC NET Dec 2014, Paper II, original Q43*

> The software _________ of a program or a computing system is the struc ture or structures of the system, which comprise software components, the externall y visible properties of those components, and the relationships among them. (A) Design (B) Architecture (C) Process (D) Requirement

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 77

*UGC NET Dec 2014, Paper III, original Q48*

> Temporal cohesion means (A) Coincidental cohesion (B) Cohesion between temporary variables (C) Cohesion between local variables (D) Cohesion with respect to time

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 78

*UGC NET June 2015, Paper II, original Q44*

> Cohesion is an extension of : (1) Abstraction concept

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 79

*UGC NET June 2015, Paper III, original Q44*

> Which design matric is used to measure the compactness of the program in terms of lines of code? (1) Consistency Conciseness (3) Efficiency (4) Accuracy

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 80

*UGC NET June 2015, Paper III, original Q47*

> A Design concept Refinement is a : (1) Top-down approach (2) Complementary of Abstraction concept (3) Process of elaboration (4) All of the above

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 81

*UGC NET June 2015, Paper III, original Q48*

> A software design is highly modular if : (1) cohesion is functional and coupling is data type. (2) cohesion is coincidental and coupling is data type. (3) cohesion is sequential and coupling is content type. (4) cohesion is functional and coupling is stamp type.

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 82

*UGC NET June 2015, Paper III, original Q55*

> Match the following : List - I List - II (a) Intelligence (i) Contextual, tacit, transfer needs learning (b) Knowledge (ii) Scattered facts, easily transferable (c) Information (iii) Judgemental (d) Data (iv) Codifiable, endorsed with relevance and purpose Codes : (a) (b) (c) (d) (1) (ili) (ii) (iv) (i) (2) (ili) (i) (iv) (ii) (3) (i) (ii) (iv) (4) (i) (Ill) (iv) (ii)

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 83

*UGC NET June 2015, Paper III, original Q60*

> Match the following for methods of MIS development : List - I List - II (a) Joint Application Design (JAD) (i) Delivers functionality in rapid iteration measured in weeks and needs frequent communication, development, testing and (b) Computer Aided Software Engg (ii) Reusable applications generally with one specific function. It is closely linked with idea of web services and service oriented architecture. (c) Agile development (iii) Tools to automate many tasks of SDLC (d) Component based technology (iv) Codes : (a) (b) (c) (d) (1) (i) (iii) (ii) (iv) (2) (iv) (ili) (i) (ii) (3) (iii) (iv) (i) (ii) (4) (iti) (i) (iv) (ii) J-8715 11 Paper-III

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 84

*UGC NET July 2016, Paper II, original Q41*

> If S 1 is total number of modules define d in the program architecture, S 3 is the number of modules whose correct function depends on prio r processing then th e number of modules not dependent on prior processing is : (1) 1 + S3 S1 (2) 1 – S3 S1 (3) 1 + S1 S3 (4) 1 – S1 S3

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 85

*UGC NET July 2016, Paper II, original Q43*

> Which of the following is not included in waterfall model ? (1) Requirement analysis (2) Risk analysis (3) Design (4) Coding

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 86

*UGC NET July 2016, Paper II, original Q46*

> An attacker sits between customer and Banker, and captures the information from the customer and retransmits to the banker by alteri ng the information. This attack is called as ______. (1) Masquerade Attack (2) Replay Attack (3) Passive Attack (4) Denial of Service Attack

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 87

*UGC NET July 2016, Paper III, original Q45*

> Match each application/software design concept in List – I to its definition in List – II. List – I List – II I. Coupling (a) Easy to visually inspect the design of the software and understand its purpose. II. Cohesion (b) Easy to add functional ity to a software without having to redesign it. III. Scalable (c) Focus of a code upon a single goal. IV. Readable (d) Reliance of a code module upon other code modules. Codes : I II III IV (1) (b) (a) (d) (c) (2) (c) (d) (a) (b) (3) (d) (c) (b) (a) (4) (d) (a) (c) (b)

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 88

*UGC NET Jan 2017, Paper II, original Q43*

> Which of the following statement(s) is/are true with respect to software architecture ? S1 : Coupling is a measure of how well the things grouped together i n a module belong together logically. S2 : Cohesion is a measure of the degree of interaction between software module s. S3 : If coupling is low and cohesion is high then it is easier to c hange one module without affecting others. (1) Only S1 and S2 (2) Only S3 (3) All of S1, S2 and S3 (4) Only S1

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 89

*UGC NET Jan 2017, Paper II, original Q45*

> A software design pattern used to enhance the functionality of an object at run-time is : (1) Adapter (2) Decorator (3) Delegation (4) Proxy

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 90

*UGC NET July 2018, Paper II, original Q12*

> Match the following in Software Engineering : List - I List - II (a) Product Complexity (i) Software Requirements Definition (b) Structured System Analysis (ii) Software Design (c) Coupling and Cohesion (iii) Validation Technique (d) Symbolic Execution (iv) Software Cost Estimation Code : (a) (b) (c) (d) (1) (ii) (iii) (iv) (i) (2) (iii) (i) (iv) (ii) (3) (iv) (i) (ii) (iii) (4) (iii) (iv) (i) (ii)

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 91

*UGC NET July 2018, Paper II, original Q16*

> Coupling is a measure of the strength of the interconnections between sof tware modules. Which of the following are correct statements with respect to module c oupling ? P : Common coupling occurs when one module controls the flow of another m odule by passing it information on what to do. Q : In data coupling, the complete data structure is passed from one modu le to another through parameters. R : Stamp coupling occurs when modules share a composite data structu re and use only parts of it. Code : (1) P and Q only (2) P and R only (3) Q and R only (4) All of P, Q and R

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 92

*UGC NET July 2018, Paper II, original Q17*

> A software design pattern often used to restrict access to an object is : (1) adapter (2) decorator (3) delegation (4) proxy

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 93

*UGC NET July 2018, Paper II, original Q18*

> Reasons to re-engineer a software include : P : Allow legacy software to quickly adapt to the changing requirement s Q : Upgrade to newer technologies/platforms/paradigm (for example, ob ject-oriented) R : Improve software maintainability S : Allow change in the functionality and architecture of the softwar e Code : (1) P, R and S only (2) P and R only (3) P, Q and S only (4) P, Q and R only

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 94

*UGC NET June 2019, original Q104*

> Software reuse is 1. the process of analysing software with the objective of recovering its design and specification the process of using existing software artifacts and knowledge to build new software 3. concerned with reimplementing legacy system to make them more maintainable the process of analysing software to create a representation of a higher level of abstraction and breaking software down into its parts to see how it works 64635085752. 2 64635085753. 3 64635085754. 4

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 95

*UGC NET Nov 2021, original Q5*

> A ‐ II , B ‐ III, C ‐ IV, D ‐ I Match List I with List II List I List II (Programming Paradigm) (Characteristic) A. Imperative I. Declarative, clausal representation, theorem proving B. Object‐oriented II. Side‐effect free, declarative, expression evaluation C. Logic III. Imperative, abstract data type D. Functional IV. Command‐based, procedural Choose the correct answer from the options given below: 1. A ‐ IV, B ‐ III, C ‐ I, D ‐ II 2. A ‐ III, B ‐ IV, C ‐ I, D ‐ II 3. A ‐ IV, B ‐ III, C ‐ II, D ‐ I 4. A ‐ II, B ‐ III, C ‐ I, D ‐ IV

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 96

*UGC NET Oct 2022, original Q34*

> Modules X and Y operate on the same input and output, then the cohesion is 1. Logical cohesion 2. Sequential cohesion 3. Procedural cohesion 4. Communicational cohesion

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 97

*UGC NET Aug 2024, original Q91*

> Arrange the following phases of database design in the correct order : (A) Physical Design (B) Conceptual Design (C) Logical Design (D) Requirement Analysis Choose the correct answer from the options given below : (1) (B), (D), (A), (C) (C), (A), (B), (D) (D), (B), (C), (A) (4) (A), (D), (C), (B)

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 98

*UGC NET Aug 2024, original Q136*

> Match List - I with List - II. List - I List - II (software design principles) (Definition) (A) Cohesion (1) Degree to which one module relies on another module. (B) Coupling (I1) Dividing a software system into distinct modules. (C) Abstration (III) Degree to which elements of a module belong together. (D) Modularity (IV) Simplifying complex reality by modeling classes appropriate to the problem. Choose the correct answer from the options given below : (1) (A)-(L), (B)-(II), (C)-(III, (D)-(IV) (2) (A)-(II), (B)-(III, (C)-(IV), (D)-(1) (3) (A)-(III), (B)-(I), (C)-(IV), (D)-(II) (4) (A)-(III), (B)-(IV), (C)-(II, (D) -(l)

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 99

*UGC NET June 2024, original Q68*

> (1) Type conversion (2) Tokenization (3) Loop optimization (4) Data flow Analysis ges which is not correct?

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 100

*UGC NET June 2025, original Q114*

> Which of the following cohesions are better than the Procedural Cohesion A. Functional Cohesion B. Sequential Cohesion C. Temporal Cohesion D. Communicational Cohesion E. Logical Cohesion Choose the correct answer from the options given below: 1. Aand D Only 2. A, B and D Only 3. C, D and E Only 4. A, D and E Only 42558919509.2 42558919510.3 42558919511.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 101

*UGC NET Dec 2025 session (Jan 2026), original Q136*

> Question Number : 136

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 102

*UGC NET Dec 2025 session (Jan 2026), original Q139*

> Question Number : 139

**Chapter foundations**

This question belongs to the ideas covered by **Software Design**. Revise these foundations: Abstraction; Architecture; Patterns; Separation of Concerns; Modularity; Information Hiding; Functional Independence; Cohesion and Coupling; Object-Oriented, Data, Architectural, UI and Component-Level Design.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Design questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-4"></a>

### 4. Software Quality (16 questions)

**What to master:** McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam lens:** Identify the lifecycle artifact or metric being tested and map it to requirements, design, estimation, quality, testing, or configuration management.

**Reusable method:** Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics.

**High-yield rules:** Cyclomatic complexity V(G) = E-N+2P. Basic COCOMO effort is a(KLOC)^b and schedule is c(Effort)^d. Function points use weighted counts and an adjustment factor.

**Common traps:** Verification asks whether the product is built right; validation asks whether the right product is built. Cohesion should rise while coupling should fall.

---

#### Question 103

*UGC NET June 2012, Paper II, original Q43*

> Reliability of software is directly dependent on (A) quality of the design (B) number of errors present (C) software engineers experience (D) user requirement 44. ______ is not an E-Commerce application. (A) House banking (B) Buying stocks (C) Conducting an auction (D) Evaluating an employee 45. ______ is a satellite based tracking system that enables the determination of person’s position. (A) Bluetooth (B) WAP (C) Short Message Service (D) Global Positioning System

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 104

*UGC NET June 2013, Paper III, original Q6*

> Software safety is a __________ activity that focuses on the identification and assessment of potential hazards that may affect software negatively and cause an entire system to fail. (A) Risk mitigation, monitoring and management (B) Software quality assurance (C) Software cost estimation (D) Defect removal efficiency COMPUTER SCIENCE AND APPLICATIONS PAPER – III Note : This paper contains seventy five (75) objective type questions of two (2) marks each. All questions are compulsory. The candida tes are required to select the most appropriate answer of each question.

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 105

*UGC NET Dec 2015, Paper III, original Q25*

> Which one of the following non-functional quality attributes is not highly affected by the architecture of the software ? (1) Performance

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 106

*UGC NET June 2015, Paper II, original Q41*

> Match the following : (a) Size-oriented metrics (i) uses number of external interfaces as one of the (b) Function-oriented measurement parameter. (ii) originally designed to be applied to business information metrics systems. Extended Function (iii) derived by normalizing quality and/ or productivity Point metrics measures by considering the size of the software. (d) Function point (iv) uses algorithm characteristics as one of the measurement parameter. Codes : (a) (b) (c) (d) (1) (iii) (iv) (i) (ii) (2) (i) (i) (iv) (iii) (3) (iv) (it) (iti) (i) (4) (iii) (i) (iv) (ii) J-8715 9 Paper-Il

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 107

*UGC NET July 2016, Paper II, original Q45*

> The extent to which a software tolerates the unexpected problems, is termed as : (1) Accuracy (2) Reliability (3) Correctness (4) Robustness

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 108

*UGC NET July 2016, Paper III, original Q43*

> A server crashes on the average once in 30 days , that is, the Mean Time Between Failures (MTBF) is 30 days. When this happens, it ta kes 12 hours to reboot it, that is, the Mean Time to Repair (MTTR) is 12 hours. The availability of server with these reliability data values is approximately : (1) 96.3% (2) 97.3% (3) 98.3% (4) 99.3%

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 109

*UGC NET July 2016, Paper III, original Q46*

> Software safety is quality assuranc e activity that focuses on hazards that (1) affect the reliability of a software component. (2) may cause an entire system to fail. (3) may result from user input errors. (4) prevent profitable mark eting of the final product.

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 110

*UGC NET Jan 2017, Paper II, original Q42*

> Which of the following is not one of three software product aspects addressed by McCall’s software quality factors ? (1) Ability to undergo change (2) Adaptiability to new environments (3) Operational characteristics (4) Production costs and scheduling

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 111

*UGC NET Dec 2019, original Q133*

> According to the ISO-9126 Standard Quality Model, match the attributes given in List-I with their definitions in List-II : List I List II (a) Functionality (1) Relationship between level of performance and amount of resources (b) Reliability (ii) Characteristics related with achievement of purpose (c) Efficiency (iii) Effort needed to make for improvement (d) Maintainability (iv) Capability of software to maintain performance of software Choose the correct option from the ones given below : (1) (a)-(i), (b)-(ii). (c)-(iii), (d) -(iv) (2) (a)-(ii). (b)-(i). (c)-(iv), (d)-(iii) (3) (a)-(ii), (b)-(iv), (c)-(i), (d)-(iii) (4) (a)-(i). (b) -(ii), (c)-(iv), (d)-(ili) 61547541230.2 61547541231.3 61547541232.4 Single Line Ouestion Option: No

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 112

*UGC NET Nov 2020, original Q99*

> Software reliability is described with respect to (A) Execution Time (B) Calendar Time (C) Clock Time Choose the correct answer from the options given below: (1) (A) and (B) only (2) (B) and (C) only (3) (A). (B) and (C) (4) (A) and (C) only 53622816894.2 53622816895.3 53622816896.4

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 113

*UGC NET Nov 2020, original Q135*

> Given below are two statements: Statement I: Quality control involves the series of inspections, reviews and tests used throughout the software process, to ensure each work product meets the requirements placed upon it. Statement II: Quality assurance consists of auditing and reporting functions of management. In the light of the above statements, choose the correct answer from the options given below (1) Both Statement I and Statement II are true (2) Both Statement I and Statement Il are false (3) Statement I is correct but Statement II is false (4) Statement I is incorrect but Statement Il is true. 53622817038.2 53622817039. 3 53622817040.4

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 114

*UGC NET Oct 2022, original Q31*

> Which Metrics are derived by normalizing quality and/or productivity measures by considering the size of the software that has been produced? 1. Function - Oriented Metrics 2. Function - Point Metrics 3. Line of Code Metrics 4. Size Oriented Metrics

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 115

*UGC NET Oct 2022, original Q33*

> Which of the following is an indirect measure of product? 1. Quality 2. Complexity 3. Reliability 4. All of these

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 116

*UGC NET Oct 2022, original Q84*

> A good software requirement specification does NOT have the characteristic 1. Completeness 2. Consistency 3. Clarity 4. Reliability

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 117

*UGC NET June 2025, original Q115*

> Which of the followings belongs to MaCall's quality factors? A. Maintainability B. Usability C. Integrity D. Functionality Choose the correct answer from the options given below: 1. Aand D Only 2. A, B and D Only 3. Cand D Only 4. A, B and C Only 42558919512. 1 42558919514.3 42558919515.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 118

*UGC NET June 2025, original Q133*

> Match List I with List I| List I (Software Quality Characteristic) List I (Description) A. Reliability I. Ability to transfer the software from one organization or hardware / software environment to another. II. Capability of software to maintain its level of B. Efficiency of time. performance under stated conditions for a stated period C. Maintainability III. Relationship between the level of performance of the software and the amount of resources used, under stated conditions. D. Portability IV. Effort needed to make modifications, including corrections, improvements or adaptation of software to changes in environment, requirements and functional specifications. Choose the correct answer from the options given below: 1. A-II, B-III, C-I, D-IV 2. A-II, B-III, C-IV, D-I 3. AIII, B-II, C-I, D-IV 4. A-IV, B-II, C-I, D-III 42558919585.2 42558919586.3 42558919587.4

**Chapter foundations**

This question belongs to the ideas covered by **Software Quality**. Revise these foundations: McCall and ISO 9126 Factors; Quality Control and Assurance; Risk Management; RMMM; Reliability.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Quality questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-5"></a>

### 5. Estimation and Scheduling (6 questions)

**What to master:** Software Sizing; LOC and FP Estimation; Cost and Effort; Estimation Models; COCOMO; Scheduling and Staffing; Timeline Charts.

**Exam lens:** Identify the lifecycle artifact or metric being tested and map it to requirements, design, estimation, quality, testing, or configuration management.

**Reusable method:** Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics.

**High-yield rules:** Cyclomatic complexity V(G) = E-N+2P. Basic COCOMO effort is a(KLOC)^b and schedule is c(Effort)^d. Function points use weighted counts and an adjustment factor.

**Common traps:** Verification asks whether the product is built right; validation asks whether the right product is built. Cohesion should rise while coupling should fall.

---

#### Question 119

*UGC NET Dec 2013, Paper III, original Q5*

> Function points can be calculated by (A) UFP ∗ CAF (B) UFP ∗ FAC (C) UFP ∗ Cost (D) UFP ∗ Productivity

**Chapter foundations**

This question belongs to the ideas covered by **Estimation and Scheduling**. Revise these foundations: Software Sizing; LOC and FP Estimation; Cost and Effort; Estimation Models; COCOMO; Scheduling and Staffing; Timeline Charts.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Estimation and Scheduling questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 120

*UGC NET July 2016, Paper III, original Q48*

> The number of function points of a proposed system is calculated as 500. Suppose that the system is planned to be developed in Java an d the LOC/FP ratio of Java is 50. Estimate the effort (E) required to complete the projec t using the effort formula of basic COCOMO given below : E = a(KLOC) b Assume that the values of a and b are 2.5 and 1.0 respectively. (1) 25 person months (2) 75 person months (3) 62.5 person months (4) 72.5 person months

**Chapter foundations**

This question belongs to the ideas covered by **Estimation and Scheduling**. Revise these foundations: Software Sizing; LOC and FP Estimation; Cost and Effort; Estimation Models; COCOMO; Scheduling and Staffing; Timeline Charts.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Estimation and Scheduling questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 121

*UGC NET Aug 2024, original Q61*

> Given a project that uses the COCOMO model with an estimated effort of 2000 person-months and a productivity rate of 5 person-month per KLOC, what is the estimated size of the project in KLOC ? (1) 200 (2) 400 (3) 100 (4) 50

**Chapter foundations**

This question belongs to the ideas covered by **Estimation and Scheduling**. Revise these foundations: Software Sizing; LOC and FP Estimation; Cost and Effort; Estimation Models; COCOMO; Scheduling and Staffing; Timeline Charts.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Estimation and Scheduling questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 122

*UGC NET Aug 2024, original Q62*

> Given a project with an estimated effort of 1500 person-hours and a team of 5 people, how many days will it take to complete the project, if each person works 8 hours a day? (1) 30 (2) 37.5 (3) 40 (4) 45.5

**Chapter foundations**

This question belongs to the ideas covered by **Estimation and Scheduling**. Revise these foundations: Software Sizing; LOC and FP Estimation; Cost and Effort; Estimation Models; COCOMO; Scheduling and Staffing; Timeline Charts.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Estimation and Scheduling questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 123

*UGC NET June 2025, original Q72*

> Which of the following is not a requirement elicitation Technique (1) Interviews (2) The use case approach (3) Facilitated Application Specification Technique (FAST) (4) Data Flow diagram 42558919341.2 42558919342. 3 42558919343,4 Mandatory: No Duestion Number : 73 Ouestion Id : 4255894978 Ouestion Tvpe : MCO

**Chapter foundations**

This question belongs to the ideas covered by **Estimation and Scheduling**. Revise these foundations: Software Sizing; LOC and FP Estimation; Cost and Effort; Estimation Models; COCOMO; Scheduling and Staffing; Timeline Charts.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Estimation and Scheduling questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 124

*UGC NET June 2025, original Q73*

> Estimation of software development effort for organic software in basic COCOMO is (1) E = 2.4 (KLOC)1.05 PM (2) E = 3.4 (KLOC)1.06 PM (3) E = 2.0 (KLOC)*.• PM (4) E = 2.4 (KLOC)1 PM 42558919345.2 42558919346. 3 42558919347.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Estimation and Scheduling**. Revise these foundations: Software Sizing; LOC and FP Estimation; Cost and Effort; Estimation Models; COCOMO; Scheduling and Staffing; Timeline Charts.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Estimation and Scheduling questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-6"></a>

### 6. Software Testing (31 questions)

**What to master:** Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam lens:** Identify the lifecycle artifact or metric being tested and map it to requirements, design, estimation, quality, testing, or configuration management.

**Reusable method:** Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics.

**High-yield rules:** Cyclomatic complexity V(G) = E-N+2P. Basic COCOMO effort is a(KLOC)^b and schedule is c(Effort)^d. Function points use weighted counts and an adjustment factor.

**Common traps:** Verification asks whether the product is built right; validation asks whether the right product is built. Cohesion should rise while coupling should fall.

---

#### Question 125

*UGC NET Dec 2009, Paper II, original Q42*

> Any error whose cause cannot be identified anywhere within the software system is called ________ (A) Internal error (B) External error (C) Inherent error (D) Logic error

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 126

*UGC NET Dec 2009, Paper II, original Q44*

> Black Box testing is done (A) to show that s/w is operational at its interfaces i.e . input and output. (B) to examine internal details of code. (C) at client side. (D) none of above.

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 127

*UGC NET Dec 2012, Paper II, original Q35*

> Which of the following is the most (A) system testing powerful parring method? (A) LL(D) (B) white box testing (B) Canonical LR (C) black box testing (C) SLR (D) unit testing (D) LALR D-87-12 5 Paper-ll

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 128

*UGC NET June 2012, Paper II, original Q22*

> Validation means (A) are we building the product right (B) are we building the right product (C) verification of fields (D) None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 129

*UGC NET Dec 2013, Paper II, original Q10*

> Testing of software with actual data and in actual environment is called (A) Alpha testing (B) Beta testing (C) Regression testing (D) None of the above

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 130

*UGC NET Dec 2013, Paper III, original Q6*

> Match the following : List – I List – II a. Data coupling i. Module A and Module B have shared data b. Stamp coupling ii. Dependency between modules is based on the fact they communicate by only passing of data c. Common coupling iii. When complete data structure is passed from one module to another d. Content coupling iv. When the control is passed from one module to the middle of another Codes : a b c d (A) iii ii i iv (B) ii iii i iv (C) ii iii iv i (D) iii ii iv i

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 131

*UGC NET Dec 2013, Paper III, original Q67*

> In Unix, how do you check that two given strings a and b are equal ? (A) test $a –eq $b (B) test $a –equal $b (C) test $a = $b (D) Sh –C test $a = = $b

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 132

*UGC NET June 2013, Paper III, original Q4*

> Equivalence partitioning is a __________ method that divides the input domain of a program into classes of data from which test cases can be derived. (A) White-box testing (B) Black-box testing (C) Orthogonal array testing (D) Stress testing

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 133

*UGC NET Dec 2015, Paper II, original Q2*

> This paper consists of fifty multiple-choice type of questions. 3. will be given to you. In the first 5 minutes, you are requested to open the booklet and compulsorily examine it as below : (i) To have access to the Question Booklet, tear off the paper seal on the edge of this cover page. Do not accept a booklet without sticker-seal and do not accept an open (ii) Tally the number of pages and number of questions in page. Faulty booklets due to pages/ questions missing the booklet with the information printed on the cover or duplicate or not in serial order or any other discrepancy should be got replaced immediately by a correct booklet from the invigilator within the period of 5 minutes. Afterwards, neither the Question Booklet will be replaced nor any extra time will be given. (iii) After this verification is over, the Test Booklet Number should be entered on the OMR Sheet and the OMR Sheet Number should be entered on this Test Booklet.

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 134

*UGC NET Dec 2015, Paper II, original Q46*

> In software testing, how the error, fault and failure are related to each other ? (1) Error leads to failure but fault is not related to error and failure. (2) Fault leads to failure but error is not related to fault and failure. (3) Error leads to fault and fault leads to failure. (4) Fault leads to error and error leads to failure. D-8715 10 Paper-Il

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 135

*UGC NET Dec 2015, Paper III, original Q72*

> Which one of the following statements is incorrect ? (1) Pareto analysis is a statistical method used for analyzing causes, and is one of the primary tools for quality management. (2) Reliability of a software specifies the probability of failure-free operation of that software for a given time duration. (3) The reliability of a system can also be specified as the Mean Time To Failure (MTTF). (4) In white-box testing, the test cases are decided from the specifications or the requirements.

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 136

*UGC NET June 2015, Paper II, original Q2*

> This paper consists of fifty multiple-choice type of questions. 3. will be given to you. In the first 5 minutes, you are requested to open the booklet and compulsorily examine it as below : (i) To have access to the Question Booklet, tear off the paper seal on the edge of this cover page. Do not accept a booklet without sticker-seal and do not accept an open (ii) Tally the number of pages and number of questions in page. Faulty booklets due to pages/ questions missing the booklet with the information printed on the cover or duplicate or not in serial order or any other discrepancy should be got replaced immediately by a correct booklet from the invigilator within the period of 5 minutes. Afterwards, neither the Question Booklet will be replaced nor any extra time will be given. (iii) After this verification is over, the Test Booklet Number should be entered on the OMR Sheet and the OMR Sheet Number should be entered on this Test Booklet.

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 137

*UGC NET June 2015, Paper II, original Q42*

> In which testing strategy requirements established during requirements analysis are validated against developed software? (1) Validation testing (2) Integration testing (3) Regression testing (4) System testing

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 138

*UGC NET June 2015, Paper III, original Q46*

> Adaptive maintenance is a maintenance which (1) correct errors that were not discovered till testing phase. (2) is carried out to port the existing software to a new environment. (3) improves the system performance. (4) both (2) and (3) J-8715 8 Paper-III

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 139

*UGC NET Jan 2017, Paper III, original Q43*

> Which of the following statement(s) is/are TRUE with regard to software testing ? I. Regression testing technique ensures that the software product runs correctly after the changes during maintenance. II. Equivalence partitioning is a white- box testing technique th at divides the input domain of a program into classes of data from which test cases can be derived. (1) only I (2) only II (3) both I and II (4) neither I nor II

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 140

*UGC NET Jan 2017, Paper III, original Q44*

> Which of the following are facts about a top-down software testing approach ? I. Top-down testing typically requir es the tester to build method stubs. II. Top-down testing typica lly requires the tester to build test drivers. (1) only I (2) Only II (3) Both I and II (4) Neither I nor II

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 141

*UGC NET Jan 2017, Paper III, original Q47*

> Complete each of the following sentences in List – I on the left hand side by filling in the word or phrase from the List – II on the right hand side that best completes the sentence : List – I List – II I. Determining whether you have built the right system is called ________ A. Software testing II. Determining whether you have built the system right is called ________ B. Software verification III. ________ is the process of demonstrating the existence of defects or providing confidence that they do not appear to be present. C. Software debugging IV. _______ is the process of discovering the cause of a defect and fixing it. D. Software validation Codes : I II III IV (1) B D A C (2) B D C A (3) D B C A (4) D B A C

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 142

*UGC NET Nov 2017, Paper II, original Q43*

> Which of the following is not a key issue stressed by an agile philosophy of software engineering ? (1) The importance of self-organizing teams as well as communication and collaboration between team members and customers. (2) Recognition that change represents opportunity. (3) Emphasis on rapid delivery of software that satisfies the customer . (4) Having a separate testing phase after a build phase.

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 143

*UGC NET Nov 2017, Paper II, original Q44*

> What is the normal order of activities in which traditional soft ware testing is organized ? (a) Integration Testing (b) System Testing (c) Unit Testing (d) Validation Testing Code : (1) (c), (a), (b), (d) (2) (c), (a), (d), (b) (3) (d), (c), (b), (a) (4) (b), (d), (a), (c)

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 144

*UGC NET Nov 2017, Paper II, original Q45*

> Which of the following testing techniques ensures that the software p roduct runs correctly after the changes during maintenance ? (1) Path Testing (2) Integration Testing (3) Unit Testing (4) Regression Testing

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 145

*UGC NET Dec 2018, original Q110*

> Software coupling involves dependencies among pieces of software called modules. Which of the following are correct statements with respect to module coupling? P: Common coupling occurs when two modules share the same global data. Q: Control coupling occurs when modules share a composite data structure and use only parts of it. R: Content coupling occurs when one module modifies or relies on the internal working of another module. Choose the correct answer from the code given below : Code : 'our . Pand Qonly 91394342438 Pand Ronly Qand Ronly 91394342439. All of P, Q and R 91394342440. Juestion Number: 110

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 146

*UGC NET July 2018, Paper II, original Q19*

> Which of the following is not a key strategy followed by the clean room approach to software development ? (1) Formal specification (2) Dynamic verification (3) Incremental development (4) Statistical testing of the system

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 147

*UGC NET June 2019, original Q103*

> In the context of software testing, which of the following statements is/are NOT correct? P: A minimal test set that achieves 100% path coverage will also achieve 100% statement coverage. Q: A minimal test set that achieves 100% path coverage will generally detect more faults than one that achieves 100% statement coverage. R: A minimal test set that achieves 100% statement coverage will generally detect more faults than one that achieves 100% branch coverage. 1. R only 2. Q only 3. P and Qonly 4. Q and R only 64635085748. 2

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 148

*UGC NET Nov 2021, original Q11*

> Both Statement I and Statement II are true. In software testing, beta testing is the testing performed by _______________. 1. potential customers at the developer's location 2. potential customers at their own locations 3. product developers at the customer's location 4. product developers at their own locations

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 149

*UGC NET Nov 2021, original Q20*

> Both Statement I and Statement II are true Given below are two statements, one is labelled as Assertion A and the other is labelled as Reason R Assertion A : Software developers donot do exhaustive software testing in practice. Reason R : Even for small inputs, exhaustive testing is too computationally intensive (e.g., takes too long) to run all the tests. In light of the above statements, choose the correct answer from the options given below 1. Both A and R are true and R is the correct explanation of A 2. Both A and R are true but R is NOT the correct explanation of A 3. A is true but R is false 4. A is false but R is true

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 150

*UGC NET Oct 2022, original Q27*

> Fault base testing technique is 1. Unit testing 2. Beta testing 3. Stress testing 4. Mutation testing

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 151

*UGC NET Oct 2022, original Q28*

> Alpha and Beta testing are forms of 1. White - Box Testing 2. Black - Box Testing 3. Acceptance Testing 4. System Testing

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 152

*UGC NET Aug 2024, original Q137*

> Match List - I with List - II. List - I List - II (Testing Type) (Description) (A) Unit testing (I) Testing individual components of the software. (B) Integrating testing (IL) Testing the interaction between integrated components. (C) System testing (Ш) Testing to verify the system meets business needs. (D) Acceptance testing (IV) Testing the complete system to ensure it meets requirements. Choose the correct answer from the options given below : (1) (A)-(L), (B)-(II), (C)-(III), (D)-(IV) (2) (A)-(I, (B)-(I), (C)-(IV), (D) -(III) (3) (A)-(I), (B)-(III), (C)-(I), (D)-(IV) (4) (A)-(I), (B)-(IV), (C)-(I), (D)-(IL)

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 153

*UGC NET June 2024, original Q121*

> Match List-l with List-ll : List - Il List - I White box Testing A. Verification Il. Black box Testing C. Internal logic exercise B. Validation Ill. Quality Control IV. Quality Assurance Choose the correct answer from the options given below: D. Software requirement exercise (2) A-I, B-II, C-III, D-IV (1) A-IV, B-III, C-I, D-II (4) A-III, B-IV, C-I, D-П (3) A-IV, B-III, C-II, D-I

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 154

*UGC NET June 2025, original Q98*

> Arrange the following types of testing in the order they are usually performed in the software Development life cycle. A. Integration testing B. Unit testing C. System Testing D. Acceptance Testing Choose the correct answer from the options given below: 1. B, C, A, D 2. B, A, C, D 3. C, B, A, D 4. C, B, D, A , 1 42558919445. 2 42558919446. 3 42558919447.4

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 155

*UGC NET Dec 2025 session (Jan 2026), original Q137*

> Question Number : 137

**Chapter foundations**

This question belongs to the ideas covered by **Software Testing**. Revise these foundations: Verification and Validation; Error, Fault, Bug and Failure; Unit and Integration Testing; White-Box and Black-Box Testing; Basis-Path and Control-Structure Testing; Test-Case Derivation; Alpha, Beta, Regression, Performance and Stress Testing.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Testing questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

<a id="chapter-7"></a>

### 7. Software Configuration Management (23 questions)

**What to master:** Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam lens:** Identify the lifecycle artifact or metric being tested and map it to requirements, design, estimation, quality, testing, or configuration management.

**Reusable method:** Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics.

**High-yield rules:** Cyclomatic complexity V(G) = E-N+2P. Basic COCOMO effort is a(KLOC)^b and schedule is c(Effort)^d. Function points use weighted counts and an adjustment factor.

**Common traps:** Verification asks whether the product is built right; validation asks whether the right product is built. Cohesion should rise while coupling should fall.

---

#### Question 156

*UGC NET June 2010, Paper II, original Q7*

> Advantage of synchronous sequential circuits over asynchronous ones is (A) faster operation (B) ease of avoiding problems due to hazard (C) lower hardware requirement (D) better noise immunity

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 157

*UGC NET Dec 2012, Paper II, original Q19*

> The maturity levels used to measure a

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 158

*UGC NET Dec 2013, Paper III, original Q7*

> A process which defines a series of tasks that have the following four primary objectives is known as 1. to identify all items that collectively define the software configuration. 2. to manage chan ges to one or more of these items. 3. to facilitate the construction of different versions of an application. 4. to ensure that software quality is maintained as the configuration evolves over time. (A) Software Qu ality Management Process (B) Software Configuration Management Process (C) Software Version Management Process (D) Software Change Management Process COMPUTER SCIENCE & APPLICATIONS Paper – III Note : This paper contains seventy five (75) objective type questions of two (2) marks each. All questions are compulsory.

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 159

*UGC NET June 2013, Paper III, original Q11*

> The golden ratio ϕ and its conjugate –ϕ both satisfy the equation (A) x3 – x – 1 = 0 (B) x3 + x – 1 = 0 (C) x2 – x – 1 = 0 (D) x2 + x – 1 = 0

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 160

*UGC NET Dec 2014, Paper II, original Q45*

> Which one of the following is used to compute cyclomatic complexity ? (A) The number of regions – 1 (B) E – N + 1, where E is the number of flow graph edges and N is the number of flow graph nodes. (C) P – 1, where P is the number of predicate nodes in the flow graph G. (D) P + 1, where P is the number of predicate nodes in the flow graph G.

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 161

*UGC NET Dec 2014, Paper III, original Q43*

> Which one of the following is not a source code metric ? (A) Halstead metric (B) Function point metric (C) Complexity metric (D) Length metric

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 162

*UGC NET Dec 2014, Paper III, original Q59*

> Match the following components of an expert system : a. I/O interface i. Accepts user’s queries and responds to question through I/O interface b. Explanation module ii. Contains facts and rules about the domain c. Inference engine iii. Gives the user, the ability to follow inferencing steps at any time during consultation d. Knowledge base iv. Permits the user to communicate with the system in a natural way Codes : a b c d (A) i iii iv ii (B) iv iii i ii (C) i iii ii iv (D) iv i iii ii

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 163

*UGC NET Dec 2015, Paper II, original Q39*

> An ideal sort is an in-place-sort whose additional space requirement is (1) O (log2 n) (2) 0 (nlog2 n) (3) O (1) (4) O(n)

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 164

*UGC NET Dec 2015, Paper III, original Q48*

> As compared to rental and leasing methods to acquire computer systems for a Management Information System (MIS), purchase method has following advantage : (1) It has high level of flexibility (2) It doesn't require cash up-front (3) It is a business investment (4) Little risk of obsolescence

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 165

*UGC NET Dec 2015, Paper III, original Q71*

> Which of the following is/are the components of a CRT ? (a) Electron Gun (b) Control Electrode (c) Focusing Electrode (d) Phosphor Coated Screen Codes : (1) (a) and (d) (2) (a), (b) and (d) (3) (a), (b), (c) and (d) (4) (a), (c) and (d) D-8715 14 Paper-Ill

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 166

*UGC NET June 2015, Paper II, original Q26*

> Which of the following protocols is an application layer protocol that establishes, manages and terminates multimedia sessions ? (1) Session Maintenance Protocol (2) Real - time Streaming Protocol (3) Real - time Transport Control Protocol (4) Session Initiation Protocol

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 167

*UGC NET July 2016, Paper II, original Q44*

> The cyclomatic complexity of a flow gr aph V(G), in terms of predicate nodes is : (1) P + 1 (2) P – 1 (3) P – 2 (4) P + 2 Where P is number of predicate nodes in flow graph V(G).

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 168

*UGC NET July 2016, Paper III, original Q2*

> This paper consists of seventy five multiple-choice type of questions.

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 169

*UGC NET July 2016, Paper III, original Q75*

> A software program that infe rs and manipulates existing know ledge in order to generate new knowledge is known as : (1) Data dictionary (2) Reference mechanism (3) Inference engine (4) Control strategy _______________

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 170

*UGC NET Jan 2017, Paper III, original Q45*

> Match the terms related to Software Confi guration Management (SCM ) in List – I with the descriptions in List – II. List – I List – II I. Version A. An instance of a system that is distributed to customers. II. Release B. An instance of a system which is functionally identical to other instances, but designed for different hardware/software configurations. III. Variant C. An instance of a system that differs, in some way, from other instances. Codes : I II III (1) B C A (2) C A B (3) C B A (4) B A C

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 171

*UGC NET July 2018, Paper II, original Q13*

> Which one of the following is not typically provided by Source Code Management Software ? (1) Synchronisation (2) Versioning and Revision history (3) Syntax highlighting (4) Project forking

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 172

*UGC NET July 2018, Paper II, original Q47*

> In Challenge-Response authentication the claimant ________. (1) Proves that she knows the secret without revealing it (2) Proves that she doesn’t know the secret (3) Reveals the secret (4) Gives a challenge

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 173

*UGC NET Dec 2019, original Q142*

> What is the cyclomatic complexity of flowgraph F? (1) 2 (2) 3 (3) 4 (4) 61547541266.2 61547541267. 3 61547541268. 4

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 174

*UGC NET Oct 2022, original Q73*

> (A)-D. (B) -(IL), (C)-II. (D)-(TV) 2. (А)-(Ш. В-ІІ). (С)-Д. (D)-(IV) 3. (А)-II), (B)-(IT. (C)-. (D)-(IV) 4. (A)-. (B)-II). (C)-Ш), (D)-(IV)

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 175

*UGC NET Aug 2024, original Q59*

> In Software configuration management, what is the primary purpose of version control? (1) To control the changes made to software (2) To document user requirements (3) To estimate project cost (4) To design the software architecture

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 176

*UGC NET June 2024, original Q18*

> Which of the following, is not the goal of reverse Engineering? (1) Cope with complexity (2) Recover lost information (3) Detect side effect (4) Data flow

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 177

*UGC NET June 2025, original Q97*

> Arrange the following in the increasing order of coupling from lowest coupling to highest coupling. A. Common Coupling B. Stamp Coupling C. Control Coupling D. External Coupling E. Content Coupling Choose the correct answer from the options given below: 1. E, A, C, B, D 2. D, B, A, E, C 3. B, C, D, A, E 4. C, A, B, D, E 42558919441.2 42558919442. 3 42558919443.4 Mandatory: No

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

---

#### Question 178

*UGC NET Dec 2025 session (Jan 2026), original Q144*

> Question Number : 144

**Chapter foundations**

This question belongs to the ideas covered by **Software Configuration Management**. Revise these foundations: Change and Version Control; Reuse; Re-engineering; Reverse Engineering.

**Exam method**

1. Identify the exact definition, formula, algorithm or system property being tested.
2. For Software Configuration Management questions: Write the model formula before substitution. For testing construct the control-flow graph or equivalence/boundary classes; for process models match risk and change characteristics. Use the chapter rules below and eliminate options that violate definitions, units, or boundary cases.
3. Check units, boundary cases and every statement before selecting an option.

**Answer status**

This item has not yet passed reliable answer-key matching and independent derivation, so no option is printed here. The omission is intentional: an unverified answer would make the guide unsafe for revision.

## Coverage and quality notes

- Recovered question blocks in this unit: **178**
- Chapter placements with direct keyword support: **165**
- Chapter placements needing manual review: **13**
- Questions with validated answers in this guide: **0**
- OCR may flatten mathematical notation, tables, code indentation, and figures. Full audit references are retained in the structured data.
- Some combined Paper 1/Paper 2 scans and older papers lack a trustworthy embedded key. Such questions remain pending rather than receiving guessed answers.

---

[Back to contents](#contents) · [All units](README.md) · [Project home](../README.md)

