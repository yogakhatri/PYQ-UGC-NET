# Question 18

*UGC NET CS · 2017 Nov Paper 2 · Database Integrity · Entity, Domain, Referential and User-Defined Integrity*

Match the following with respect to RDBMS : (a) Entity integrity (i) enforces some specific business rule that do not fall into entity or domain (b) Domain integrity (ii) Rows can’t be deleted which are used by other records (c) Referential integrity (iii) enforces valid entries for a column (d) Userdefined integrity (iv) No duplicate rows in a table Code : (a) (b) (c) (d)

- **1.** (iii) (iv) (i) (ii)
- **2.** (iv) (iii) (ii) (i)
- **3.** (iv) (ii) (iii) (i)
- **4.** (ii) (iii) (iv) (i)

> [!TIP]
> **Correct answer: 2. (iv) (iii) (ii) (i)**

## Solution

Entity integrity requires a valid unique primary-key identity, matching the option's simplified 'no duplicate rows' description (iv). Domain integrity restricts a column to permitted values and types, so b→iii. Referential integrity prevents a referenced parent row from being deleted while dependent foreign-key rows remain, so c→ii. User-defined integrity implements additional business rules, so d→i. The sequence (iv),(iii),(ii),(i) is option 2.

## Key Points

- Entity identifies rows; domain validates column values; referential preserves foreign-key links; user-defined constraints encode business rules.

## Why the other options are incorrect

The other codes interchange domain, referential, and user-defined constraints. More precisely, entity integrity says every primary-key component is non-NULL, while key uniqueness prevents duplicate entity identifiers; the paper compresses these ideas into item (iv).
