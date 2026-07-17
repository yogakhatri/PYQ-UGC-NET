# Question 47

*UGC NET CS · 2013 June Paper 3 · Database Security, Integrity and Triggers · Foreign Keys, Encryption and ECA Rules*

Match the following : a. Foreign keys i. Domain constraint b. Private key ii. Referential integrity c. Event control action model iii. Encryption d. Data security iv. Trigger Codes : a b c d

- **A.** iii ii i iv
- **B.** ii i iv iii
- **C.** iii iv i ii
- **D.** i ii iii iv

> [!TIP]
> **Correct answer: Intended answer: B (ii, i, iv, iii), but the printed pairing 'Private key → Domain constraint' is conceptually defective.**

## Solution

Three matches are direct: a foreign key enforces referential integrity (a→ii); an event-condition-action model is implemented by a trigger (c→iv); and encryption is a principal database-security mechanism (d→iii). These force sequence ii, i, iv, iii, which is option B. The remaining forced match is 'private key→domain constraint,' but a cryptographic private key belongs with encryption, not a database domain constraint. The source likely contains a wording error, so B is only the intended elimination-based answer, not a fully valid four-pair mapping.

## Key Points

- Use certain pairs first in a matching question, but flag the item when elimination forces a conceptually false leftover pair.

## Why the other options are incorrect

A and C map foreign keys to encryption instead of referential integrity. D maps foreign keys to domain constraints and ECA to encryption. B alone contains the three defensible matches, although its leftover private-key pairing exposes the question defect.
