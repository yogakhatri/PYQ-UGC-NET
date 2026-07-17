# Question 16

*UGC NET CS · 2012 June Paper 2 · Data Communication · Time-Division Circuit Switching*

In which circuit switching, delivery of data is delayed because data must be stored and retrieved from RAM ?

- **A.** Space division
- **B.** Time division
- **C.** Virtual
- **D.** Packet www.solutionsadda.in

> [!TIP]
> **Correct answer: B. Time division**

## Solution

Time-division switching interchanges data among time slots. A time-slot interchanger writes incoming samples or words into RAM and reads them in a different sequence for the outgoing slots. Because a value must be stored and later retrieved, the switching process introduces memory-cycle and frame/slot delay. Space-division switching instead establishes a physical path through switching elements.

## Key Points

- Time switching rearranges time slots with memory; space switching connects physical paths through a matrix.

## Why the other options are incorrect

Space division does not require the same store-and-read time-slot operation. Virtual and packet switching are not the two circuit-switching implementation categories being contrasted in this question.
