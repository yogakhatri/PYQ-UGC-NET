# Question 107

*UGC NET CS · 2018 Dec Paper 1 And 2 · Software Maintenance · Software Maturity Index*

A legacy software system has 940 modules. The latest release required 90 of these modules to be changed. In addition, 40 new modules were added and 12 old modules were removed. Compute the software maturity index for the system.

- **1.** 0.849
- **2.** 0.524
- **3.** 0.725
- **4.** 0.923

> [!TIP]
> **Correct answer: 1. 0.849**

## Solution

The software maturity index is SMI=[M_T-(F_a+F_c+F_d)]/M_T, where M_T is the module count and F_a, F_c, and F_d are modules added, changed, and deleted in the release. Substituting the stated values gives [940-(40+90+12)]/940=(940-142)/940=798/940≈0.84894. Rounded to three decimals, the SMI is 0.849, option 1.

## Key Points

- SMI is one minus the fraction of modules added, changed, or deleted in the release.

## Why the other options are incorrect

Options 2–4 do not result from the standard SMI substitution. A value near 1 indicates relatively little change; here 142 of 940 modules are affected, leaving about 84.9% as the maturity/stability fraction.
