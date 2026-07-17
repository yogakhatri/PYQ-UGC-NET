# Question 58

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Pipeline and Vector Processing · Instruction Pipeline*

stoption 1D-30320 SEND:187008 Consider an unpipelined machine with 10nsec clock cycles which uses four cycles for ALU operations and branches where as five cycles tor memory operation. Assume that the relative frequencies of these operations are: 40%, 20% and 40%, respectively. Due to clock skew and setup pipeline let us consider that the machine adds one nsec overhead to the clock. How much speedup is observed in the instruction execution rate when a pipelined machine is considered.

- **1.** 2 times
- **2.** 4 times
- **3.** 6 times
- **4.** 8 times

> [!TIP]
> **Correct answer: 2. 4 times**

## Solution

The unpipelined average instruction time is [0.40(4)+0.20(4)+0.40(5)]×10 ns = 4.4×10 ns = 44 ns. With pipelining, the clock period is the original 10 ns stage time plus 1 ns pipeline overhead, or 11 ns. In steady state the pipeline completes about one instruction per clock, so the speedup in instruction rate is 44/11=4.

## Key Points

- Pipeline throughput speedup = unpipelined average instruction time ÷ pipelined clock period, after the pipeline fills.

## Why the other options are incorrect

The alternatives 2, 6, and 8 do not follow from the weighted CPI and the 11 ns pipeline clock. Ignoring the one-nanosecond overhead would give 4.4, which is also not any of those alternatives.
