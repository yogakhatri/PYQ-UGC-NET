# Question 63

*UGC NET CS · 2019 Dec Paper 1 And 2 · Basic Computer Organization and Design · Accumulator Program Execution*

The following program is stored in the memory unit of the basic computer. Give the content of accumulator register in hexadecimal after the execution of the program. Location Instruction 010 CLA 011 ADD 016 012 BUN 014 013 HLT 014 AND 017 015 BUN 013 Guide 016 C1A5 017 93C6

- **1.** A1B4
- **2.** 81B4
- **3.** A184
- **4.** 8184 Single Line Ouestion Option: No

> [!TIP]
> **Correct answer: 4. 8184 Single Line Ouestion Option: No**

## Solution

CLA clears AC to 0000. ADD 016 loads the word at location 016 into the sum, so AC=C1A5. BUN 014 skips HLT and transfers control to AND 017. The bitwise hexadecimal AND is C1A5 AND 93C6: C&9=8, 1&3=1, A&C=8, and 5&6=4, giving 8184. BUN 013 then reaches HLT. Therefore option 4.

## Key Points

- Trace control flow before calculating data: branch to 014, perform a nibblewise AND, branch back to HLT.

## Why the other options are incorrect

A1B4, 81B4, and A184 each contain at least one nibble that is not the AND of the corresponding source nibbles. The ADD does not combine C1A5 with 93C6; only the later AND instruction uses 93C6.
