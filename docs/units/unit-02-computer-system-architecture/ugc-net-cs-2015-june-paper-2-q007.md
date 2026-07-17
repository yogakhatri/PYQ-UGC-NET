# Question 7

*UGC NET CS · 2015 June Paper 2 · Digital Logic Circuits and Components · Full-Adder Sum and Carry*

For a full adder, compute (S,Cₒ) for (a) x=1,y=0,Cᵢ=0 and (b) x=0,y=1,Cᵢ=1.

- **1.** (a) S=1,Cₒ=0; (b) S=0,Cₒ=1
- **2.** (a) S=0,Cₒ=0; (b) S=1,Cₒ=1
- **3.** (a) S=1,Cₒ=1; (b) S=0,Cₒ=0
- **4.** (a) S=0,Cₒ=1; (b) S=1,Cₒ=0

> [!TIP]
> **Correct answer: 1. (a) S=1,Cₒ=0; (b) S=0,Cₒ=1**

## Solution

For a full adder, S=x⊕y⊕Cᵢ and Cₒ=xy+xCᵢ+yCᵢ. In (a), 1+0+0=1, so S=1 and Cₒ=0. In (b), 0+1+1=2 in binary, so the low bit S=0 and the carry Cₒ=1. This is option 1.

## Key Points

- A full adder outputs the least significant bit and carry of x+y+Cᵢ.

## Why the other options are incorrect

The other options contradict one or both binary sums. The quickest check is arithmetic: the sum output is the parity bit of the three inputs, while carry is 1 whenever at least two inputs are 1.
