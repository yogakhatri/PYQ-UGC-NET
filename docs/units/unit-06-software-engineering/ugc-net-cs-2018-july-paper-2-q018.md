# Question 18

*UGC NET CS · 2018 July Paper 2 · Software Maintenance · Reasons for Software Re-engineering*

Which are reasons to re-engineer software? P: Help legacy software adapt to changing requirements. Q: Upgrade to newer technologies, platforms or paradigms. R: Improve maintainability. S: Change the functionality and architecture of the software.

- **1.** P, R and S only
- **2.** P and R only
- **3.** P, Q and S only
- **4.** P, Q and R only

> [!TIP]
> **Correct answer: 4. P, Q and R only**

## Solution

P is a valid reason: re-engineering makes a rigid legacy system easier to evolve as requirements change. Q is valid because migration can move a system to a supported platform, language, database, or paradigm. R is a central goal—improving structure, documentation, and maintainability. S is not accepted as stated because re-engineering normally preserves the system's externally visible functionality while restructuring or migrating it; deliberate functional change belongs to enhancement/forward engineering. Hence P,Q,R only, option 4.

## Key Points

- Re-engineering modernizes and restructures an existing asset, usually preserving behavior while making future change cheaper and safer.

## Why the other options are incorrect

Options 1 and 3 include S while omitting a valid reason, and option 2 omits technology/platform modernization. Architecture may be reorganized internally, but coupling that claim with a change of functionality makes S false in the standard definition.
