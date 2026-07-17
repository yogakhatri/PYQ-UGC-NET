# Question 61

*UGC NET CS · 2019 Dec Paper 1 And 2 · Microprogrammed Control · Microinstruction Format and Field Sizing*

A micro instruction format has microoperation field which is divided into 2 subfields F1 and F2. each having 15 distinct microoperations, condition field CD for four status bits, branch field BR having four options used in conjunction with address field AD. The address space is of 128 memory words. The size of micro instruction is :

- **1.** 19
- **2.** 18
- **3.** 17
- **4.** 20

> [!TIP]
> **Correct answer: 1. 19**

## Solution

Each F field must encode 15 microoperations (and conventionally the no-operation choice), requiring 4 bits; thus F1+F2 uses 8 bits. Selecting one of four status conditions needs 2 bits, the four branch choices need 2 bits, and 128=2^7 control-memory addresses need 7 bits. Total size=4+4+2+2+7=19 bits, option 1.

## Key Points

- Size every encoded field with ceil(log2 choices), then add the address width.

## Why the other options are incorrect

Seventeen or eighteen bits under-allocate at least one field. Twenty includes an unnecessary extra bit: all stated alternatives and 128 addresses fit exactly in nineteen bits. Even ignoring the explicit no-operation code, fifteen choices still require ceil(log2 15)=4 bits per F field.
