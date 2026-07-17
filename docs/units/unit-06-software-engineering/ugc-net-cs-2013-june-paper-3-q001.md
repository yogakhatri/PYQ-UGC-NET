# Question 1

*UGC NET CS · 2013 June Paper 3 · Software Maintenance · Software Maturity Index*

The Software Maturity Index (SMI) is defined as SMI = [M f – (Fa + Fc + Fd)] / Mf Where M f = the number of modules in the current release. F a = the number of modules in the current release that have been added. F c = the number of modules in the current release that have been changed. F d = the number of modules in the current release that have been deleted. The product begins to stabilize when

- **A.** SMI approaches 1
- **B.** SMI approaches 0
- **C.** SMI approaches –1
- **D.** None of the above

> [!TIP]
> **Correct answer: A. SMI approaches 1**

## Solution

SMI=1-(Fa+Fc+Fd)/Mf. The numerator subtracted from 1 counts the relative amount of change in the current release: added, changed and deleted modules. As a product stabilizes, fewer modules require such changes, so (Fa+Fc+Fd)/Mf tends toward 0 and SMI tends toward 1. A value near 1 therefore indicates maturity/stability, while a lower value indicates substantial churn.

## Key Points

- Software Maturity Index is one minus the fraction of modules added, changed or deleted; stability pushes it toward 1.

## Why the other options are incorrect

SMI near 0 means the counted changes are roughly as large as the release's module count, which signals instability rather than stabilization. A negative value would indicate even heavier change under the formula. Hence B and C reverse the interpretation, and D is unnecessary.
