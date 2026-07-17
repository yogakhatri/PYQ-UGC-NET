# Question 28

*UGC NET CS · 2015 June Paper 3 · Network Security · Columnar Transposition Cipher*

The message "COMPUTERNETWORK" is encrypted using a columnar transposition cipher with key "LAYER". What is the ciphertext?

- **1.** CTTOEWMROPNRUEK
- **2.** MROUEKCTTPNROEW
- **3.** OEWPNRCTTUEKMRO
- **4.** UEKPNRMROOEWCTT

> [!TIP]
> **Correct answer: 3. OEWPNRCTTUEKMRO**

## Solution

Write the plaintext row-wise under the five-letter key: `L A Y E R / C O M P U / T E R N E / T W O R K`. The column strings are L→CTT, A→OEW, Y→MRO, E→PNR, R→UEK. Read columns in alphabetical key order A, E, L, R, Y: `OEW + PNR + CTT + UEK + MRO = OEWPNRCTTUEKMRO`.

## Key Points

- Fill rows under the key, alphabetically rank key columns, then read each ranked column top to bottom.

## Why the other options are incorrect

The other strings read columns in a different order. Columnar transposition does not sort columns by their original positions; it uses the alphabetical ranking of the key letters, which uniquely yields option 3.
