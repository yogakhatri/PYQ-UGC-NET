# Question 45

*UGC NET CS · 2014 Dec Paper 3 · Software Project Management · Risk Exposure*

A project risk has an 80% probability: only 70% of components scheduled for reuse will be integrated, and the remaining functionality must be custom-developed. If 60 reusable components were planned, their average size is 100 LOC, and development costs $14 per LOC, what is the risk exposure?

- **A.** $ 25,200
- **B.** $ 20,160
- **C.** $ 17,640
- **D.** $ 15,120

> [!TIP]
> **Correct answer: B. $ 20,160**

## Solution

If only 70% are reusable, 30% of 60 components must be custom-developed: 0.30×60=18 components. Their size is 18×100=1,800 LOC, so the loss if the risk occurs is 1,800×$14=$25,200. Risk exposure equals probability × loss, giving 0.80×$25,200=$20,160.

## Key Points

- Risk exposure is probability of occurrence multiplied by the monetary impact if the risk occurs.

## Why the other options are incorrect

$25,200 is the impact before multiplying by the 80% probability. $17,640 corresponds to multiplying the loss by 70%, which is the reuse success fraction rather than the risk probability. $15,120 applies another incorrect factor. Option B follows RE=P(risk)×cost consequence.
