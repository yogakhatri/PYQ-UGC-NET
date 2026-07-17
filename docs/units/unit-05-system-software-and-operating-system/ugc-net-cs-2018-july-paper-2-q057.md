# Question 57

*UGC NET CS · 2018 July Paper 2 · Memory Management · Paging and Page Tables*

Page information in memory is also called as Page Table. The essential contents in each entry of a page table is/are _________.

- **1.** Page Access information
- **2.** Virtual Page number
- **3.** Page Frame number
- **4.** Both virtual page number and Page Frame Number

> [!TIP]
> **Correct answer: 3. Page Frame number**

## Solution

A virtual page number is used as the index that selects a page-table entry, so it need not be stored again inside an ordinary linear page-table entry. The entry's essential translation result is the physical page-frame number. Real systems also attach valid, protection, reference, and dirty bits, but the frame number is the indispensable item among the choices. Hence option 3 is correct.

## Key Points

- Virtual page number indexes the page table; the selected PTE supplies the physical frame number and status bits.

## Why the other options are incorrect

Access information is useful metadata but does not by itself translate an address. Storing the virtual page number is unnecessary in the standard indexed table, so option 4 also adds a nonessential field. In hashed or inverted tables the layout differs, but the question asks the conventional page table.
