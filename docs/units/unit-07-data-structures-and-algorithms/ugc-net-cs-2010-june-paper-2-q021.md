# Question 21

*UGC NET CS · 2010 June Paper 2 · Data Structures · Valid stack permutations*

If we have six stack operations- pushing and popping each of A, B and C-such that push (A) must occur before push (B) which must occur before push (C), then A, C, B is a possible order for the pop operations, since this could be our sequence : push (A), pop (A), push (B), push (C), pop (C), pop (B). Which one of the following orders could not be the order the pop operations are run, if we are to satisfy the requirements described above ?

- **A.** ABC
- **B.** CBA
- **C.** BAC
- **D.** CAB

> [!TIP]
> **Correct answer: D. CAB**

## Solution

Pushes must occur A before B before C, but an item may be popped before later pushes. ABC is possible by pushing and immediately popping each item. CBA is possible after pushing all three. BAC is possible by push A, push B, pop B, pop A, then push/pop C. CAB is impossible: making C the first pop requires all three pushes to have occurred, leaving C above B above A, so B must pop before A.

## Key Points

- Once C is first to pop, all three pushes have occurred and the remaining B-before-A order is forced.

## Why the other options are incorrect

Explicit legal operation sequences exist for ABC, CBA, and BAC. Only CAB conflicts with the forced LIFO order after C is popped first.
