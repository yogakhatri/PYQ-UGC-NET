# Question 15

*UGC NET CS · 2013 Dec Paper 2 · Database Integrity · Numeric Range Validation*

Data Integrity control uses _______

- **A.** Upper and lower limits on numeric data.
- **B.** Passwords to prohibit unauthorised access to files.
- **C.** Data dictionary to keep the data
- **D.** Data dictionary to find last access of data

> [!TIP]
> **Correct answer: A. Upper and lower limits on numeric data.**

## Solution

Data-integrity controls keep stored values valid and consistent. Upper and lower bounds validate a numeric value against its permitted domain, rejecting entries outside the range. This directly protects correctness of the data.

## Key Points

- Integrity controls validate values and relationships; security controls govern authorization and access.

## Why the other options are incorrect

Passwords are access-security controls: they restrict who can reach data but do not ensure an authorized user enters valid values. A data dictionary stores metadata, not the data itself, and it is not primarily an access-history log.
