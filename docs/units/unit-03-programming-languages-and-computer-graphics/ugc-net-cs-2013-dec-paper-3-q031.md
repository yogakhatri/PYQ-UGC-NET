# Question 31

*UGC NET CS · 2013 Dec Paper 3 · Computer Graphics and Image Processing · Compression Ratio and Data Redundancy*

In image processing, RD=1-1/CR where CR=n1/n2 is the compression ratio and n1,n2 are the information-carrying units in two datasets representing the same information. RD is the relative ______ of the first dataset.

- **A.** Data Compression
- **B.** Data Redundancy
- **C.** Data Relation
- **D.** Data Representation

> [!TIP]
> **Correct answer: B. Data Redundancy**

## Solution

The compression ratio is CR=n1/n2, where n1 is the size of the original representation and n2 is the size after compression. Therefore 1/CR=n2/n1 is the fraction of the original data that remains. Subtracting it from 1 gives RD=1-n2/n1, the fraction removed because it was redundant. RD consequently means the relative data redundancy of the first dataset.

## Key Points

- CR tells how much smaller the compressed data is; RD=1-1/CR tells what fraction of the original representation was redundant.

## Why the other options are incorrect

Data compression is the process, while CR measures its ratio; RD measures the redundant fraction eliminated. Data relation and data representation are not the quantities defined by this standard formula.
