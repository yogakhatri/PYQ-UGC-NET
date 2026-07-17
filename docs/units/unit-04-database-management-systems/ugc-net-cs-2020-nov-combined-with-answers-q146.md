# Question 146

*UGC NET CS · 2020 Nov With Answers · SQL · DISTINCT and IN Predicates*

Which query retrieves the distinct employee IDs of all employees working on project numbers 20, 30 and 40?

- **1.** SELECT EMPID FROM PROJECTWORK WHERE PROJNO=(20,30,40)
- **2.** SELECT EMPID FROM PROJECTWORK WHERE PROJNO IN (20,30,40)
- **3.** SELECT DISTINCT EMPID FROM PROJECTWORK WHERE PROJNO IN (20,30,40)
- **4.** SELECT DISTINCT EMPID FROM PROJECTWORK WHERE PROJNO=20,30,40

> [!TIP]
> **Correct answer: 3. SELECT DISTINCT EMPID FROM PROJECTWORK WHERE PROJNO IN (20,30,40)**

## Solution

The predicate PROJNO IN (20,30,40) selects rows for any of the three listed project numbers. Because PROJECTWORK's key is (EMPID,PROJNO), one employee can have several selected rows—one for each project—and selecting EMPID alone can therefore produce duplicates. DISTINCT removes those repetitions. The correct query is SELECT DISTINCT EMPID FROM PROJECTWORK WHERE PROJNO IN (20,30,40), option 3.

## Key Points

- Use IN for membership in a value list and DISTINCT when projection can collapse different source rows to the same selected value.

## Why the other options are incorrect

Options 1 and 4 use invalid equality syntax for a list. Option 2 uses IN correctly but omits DISTINCT, so an employee assigned to more than one listed project can appear more than once.
