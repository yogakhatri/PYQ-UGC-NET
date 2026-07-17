# Question 32

*UGC NET CS · 2017 Nov Paper 2 · Microprocessor Programming · Rotate, Shift, Multiply and Carry Flag*

Consider the following assembly program fragment : stc mov al, 11010110b mov cl, 2 rcl al, 3 rol al, 4 shr al, cl mul cl The contents of the destination register ax (in hexadecimal) and the status of Carry Flag (CF) after the execution of above instructions, are :

- **1.** ax=003CH; CF=0
- **2.** ax=001EH; CF=0
- **3.** ax=007BH; CF=1
- **4.** ax=00B7H; CF=1

> [!TIP]
> **Correct answer: 1. ax=003CH; CF=0**

## Solution

Begin with AL=D6h=11010110₂ and CF=1. Three rotate-through-carry-left steps give (ADh,CF=1), then (5Bh,1), then (B7h,0). Rotating AL left four bits turns B7h into 7Bh and leaves CF=1. Shifting 7Bh right by CL=2 gives AL=1Eh; the intermediate low bits make the shift carry 1. Finally unsigned `mul cl` computes AL×CL=1Eh×02h=003Ch in AX. For 8-bit `MUL`, CF and OF are cleared because the high byte AH is zero. Thus AX=003Ch and CF=0, option 1.

## Key Points

- Trace both the data byte and CF after every rotate/shift; remember that 8-bit `MUL` writes the 16-bit product to AX and then sets CF/OF from AH.

## Why the other options are incorrect

Option 2 stops at AL=1Eh before multiplication. Options 3 and 4 reflect intermediate rotate values rather than the final product, and they retain a carry that `MUL` recomputes from whether the product's upper half is nonzero.
