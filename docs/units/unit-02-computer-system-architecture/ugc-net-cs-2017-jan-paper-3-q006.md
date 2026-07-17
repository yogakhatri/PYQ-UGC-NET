# Question 6

*UGC NET CS · 2017 Jan Paper 3 · Microprocessors · 8085 Data-Transfer Instructions*

In 8085, which of the following performs : load register pair immediate operation ?

- **1.** LDAX rp
- **2.** LHLD addr
- **3.** LXI rp, data
- **4.** INX rp

> [!TIP]
> **Correct answer: 3. LXI rp, data**

## Solution

LXI means 'load register pair immediate.' In `LXI rp, data16`, the two bytes following the opcode are copied into the selected register pair, such as BC, DE, HL, or SP. Therefore option 3 directly performs the requested operation.

## Key Points

- In 8085 mnemonics, LXI = Load register pair eXtended/Immediate with a 16-bit constant.

## Why the other options are incorrect

`LDAX rp` loads the accumulator indirectly through BC or DE. `LHLD addr` loads L and H from two consecutive memory locations. `INX rp` increments a register pair; it does not load immediate data.
