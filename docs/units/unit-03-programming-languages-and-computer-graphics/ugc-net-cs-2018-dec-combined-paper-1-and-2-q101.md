# Question 101

*UGC NET CS · 2018 Dec Paper 1 And 2 · Programming in C · Array Swapping and Loop Effects*

Consider the C/C++ function: void f(char w[]) { int x = strlen(w); char c; for (int i = 0; i < x; i++) { c = w[i]; w[i] = w[x-i-1]; w[x-i-1] = c; } } Which option describes the final contents of the array?

- **1.** It outputs the contents of the array in reverse order.
- **2.** It outputs the contents of the array in the original order.
- **3.** It outputs the contents of the array with the characters shifted over by one position.
- **4.** It outputs the contents of the array with the characters rearranged so they are no longer recognized as the words in the original phrase.

> [!TIP]
> **Correct answer: 2. It outputs the contents of the array in the original order.**

## Solution

At iteration i, the code swaps w[i] with w[x-i-1]. During the first half of the loop this appears to reverse the array. However, the loop continues through all x positions. When it later reaches the mirror index j=x-i-1, it swaps the same two characters again, restoring both to their starting positions. If x is odd, the centre element is merely swapped with itself. Consequently every pair is swapped twice and the final array is in its original order, option 2.

## Key Points

- When a reversal loop runs to x instead of x/2, every symmetric pair is exchanged twice and the second exchange undoes the first.

## Why the other options are incorrect

Option 1 would be correct only if the loop stopped at x/2. The code performs no one-position shift, so option 3 is inapplicable. The transformations are deterministic pairwise swaps that cancel, not an arbitrary scrambling as in option 4.
