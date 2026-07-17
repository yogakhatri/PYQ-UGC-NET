# Question 12

*UGC NET CS · 2013 Dec Paper 2 · Database File Navigation · GO BOTTOM and SKIP Commands*

GO BOTTOM and SKIP-3 commands are given one after another in a databa se file of 30 records. It shifts the control to

- **A.** 28 th record
- **B.** 27 th record
- **C.** 3 rd record
- **D.** 4 th record

> [!TIP]
> **Correct answer: B. 27 th record**

## Solution

GO BOTTOM positions the record pointer on the last record, number 30. SKIP -3 then moves backward three record positions: 30 to 29 is one, to 28 is two, and to 27 is three. Control therefore reaches the 27th record.

## Key Points

- GO BOTTOM selects the last record; SKIP n moves relatively from the current record, with negative n moving backward.

## Why the other options are incorrect

28 results from moving back only two positions. Records 3 and 4 would come from treating -3 as an absolute record number or wrapping around, neither of which is how the relative SKIP command works.
