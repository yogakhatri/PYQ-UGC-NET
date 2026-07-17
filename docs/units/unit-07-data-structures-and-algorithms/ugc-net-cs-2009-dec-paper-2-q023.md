# Question 23

*UGC NET CS · 2009 Dec Paper 2 · Performance Analysis and Recurrences · Time and Space Complexity*

At a hill station, the parking lot is one long drive way snaking up a hill side. Cars drive in and park right behind the car in front of them, one behind another. A car can’t leave until all the cars in front of it have left. Is the parking lot more like

- **A.** An array
- **B.** A stack
- **C.** A queue
- **D.** A linked list

> [!TIP]
> **Correct answer: B. A stack**

## Solution

The last car to enter is positioned nearest the exit end of the accessible chain and must leave before cars parked earlier behind it can leave. Thus entry and removal follow last-in, first-out order, exactly the behavior of a stack.

## Key Points

- When the most recently inserted item must be removed first, the structure is a stack.

## Why the other options are incorrect

A queue is FIFO, while array and linked list describe storage layouts rather than the access discipline emphasized by the question.
