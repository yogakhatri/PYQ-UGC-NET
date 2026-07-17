# Question 133

*UGC NET CS · 2018 Dec Paper 1 And 2 · Transaction Processing · Undo-Redo Crash Recovery*

Consider the log: (i) T1 start; (ii) T1 updates A from 20,000 to 15,000; (iii) T1 updates B from 12,000 to 17,000; (iv) T1 commit; (v) T2 start; (vi) T2 updates A from 15,000 to 16,500; (vii) T2 commit. The database crashes just before log record (vii) is written. Which statement about recovery is true?

- **1.** We must redo log record (vi) to set A to 16,500.
- **2.** We must redo log record (vi) to set A to 16,500 and then redo log records (ii) and (iii).
- **3.** We need not redo log records (ii) and (ill) because transaction T1 has committed.
- **4.** We can apply redo and undo operations in arbitrary order because they are idempotent.

> [!TIP]
> **Correct answer: No printed option is correct. Standard undo/redo recovery must undo record (vi), restoring A to 15,000, and redo committed T1's records (ii) and (iii). Option 2 would be correct if its first word ‘redo’ were ‘undo’.**

## Solution

T1 has a commit record, so it is a winner; without a checkpoint/force guarantee, recovery redoes its logged updates to ensure durability. T2 has no commit record, so it is a loser; its possible update must be undone using the old value in record (vi), changing A from 16,500 back to 15,000. The correct recovery action is therefore UNDO (vi) and REDO (ii),(iii). The source PDF clearly prints REDO in option 2, making the item defective rather than providing the standard answer.

## Key Points

- Crash recovery classifies winners and losers: redo committed transactions as needed for durability; undo uncommitted transactions for atomicity.

## Why the other options are incorrect

Options 1 and 2 wrongly redo T2's uncommitted interest update. Option 3 assumes that a commit record proves T1's data pages were already forced to disk; standard no-force recovery cannot assume that and may need redo. Option 4 confuses idempotence with commutativity: repeated redo/undo may be safe, but arbitrary ordering on the same item can leave the wrong final value.
