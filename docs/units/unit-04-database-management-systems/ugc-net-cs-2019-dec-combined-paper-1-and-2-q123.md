# Question 123

*UGC NET CS · 2019 Dec Paper 1 And 2 · Transactions and Concurrency Control · Dirty Reads, Lost Updates and Inconsistent States*

Transactions T1 and T2 update the same stock item A without concurrency control. Which problems may occur? (a) Dirty read, (b) lost update, (c) transaction failure, (d) inconsistent database state.

- **1.** (a), (b) and (c) only
- **2.** (c) and (d) only
- **3.** (a) and (b) only
- **4.** (a), (b) and (d) only

> [!TIP]
> **Correct answer: 4. (a), (b) and (d) only**

## Solution

Without isolation, T2 can read a value written but not committed by T1, causing a dirty read (a). If both read the same old stock and then write their separate results, the later write can overwrite the earlier one, causing a lost update (b). Such interleavings can violate inventory constraints or leave a value impossible under any serial order, producing an inconsistent database state (d). Concurrency alone does not inherently make a transaction fail, so (c) is not one of the anomalies. Option 4 is correct.

## Key Points

- Uncontrolled interleaving threatens isolation: uncommitted reads and overwritten writes can leave a nonserial, inconsistent result.

## Why the other options are incorrect

Options 1 and 2 wrongly include transaction failure as a necessary concurrency anomaly. Option 3 recognizes dirty reads and lost updates but omits their possible consequence—an inconsistent final database state. Control mechanisms exist to preserve isolation and serializability, not merely to prevent crashes.
