# Question 67

*UGC NET CS · 2017 Jan Paper 3 · Data Compression · LZW Dictionary Construction*

From the given data below : abbaabbaab which one of the following is not a word in the dictionary created by LZ-coding (the initial words are a, b) ?

- **1.** ab
- **2.** bb
- **3.** ba
- **4.** baab

> [!TIP]
> **Correct answer: 4. baab**

## Solution

Use LZW-style dictionary growth with initial entries a and b. Reading `abbaabbaab`: `ab` is new, so add it; then add `bb`; then `ba`; then `aa`. The next longest known phrase is `ab`, and extending it with b adds `abb`. Later the known phrase `ba` extended with a adds `baa`. The dictionary therefore contains ab, bb, and ba, but never baab. Option 4 is the word not created.

## Key Points

- LZW adds previous matched phrase + next symbol; trace phrase boundaries, not every substring of the input.

## Why the other options are incorrect

Options 1–3 are exactly the first three new two-symbol dictionary entries encountered during parsing. `baab` would require that full extension to occur as the first unseen phrase, but the parsing boundaries generate `baa` instead.
