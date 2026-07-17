# Question 37

*UGC NET CS · 2017 Jan Paper 2 · Memory Management · TLB Effective Access Time*

In a paging system, it takes 30 ns to search translation Look-a-side Buffer (TLB) and 90 ns to access the main memory. If the TLB hit ratio is 70%, the effective memory access time is :

- **1.** 48ns
- **2.** 147ns
- **3.** 120ns
- **4.** 84ns

> [!TIP]
> **Correct answer: 2. 147ns**

## Solution

A TLB hit costs the 30 ns lookup plus one 90 ns memory access, totaling 120 ns. On a miss, the system pays the lookup, one memory access for the page-table entry, and one for the requested word: 30+90+90=210 ns. With hit ratio 0.7, EAT=0.7(120)+0.3(210)=84+63=147 ns. Hence option 2 is correct.

## Key Points

- Effective time is a weighted average of complete hit and miss paths, including the TLB lookup on both.

## Why the other options are incorrect

120 ns is only the hit-path time. 84 ns multiplies the hit time by the hit probability but omits the miss contribution. 48 ns comes from mixing probabilities or omitting required memory accesses.
