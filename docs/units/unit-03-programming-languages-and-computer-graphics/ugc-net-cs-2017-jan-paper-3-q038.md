# Question 38

*UGC NET CS · 2017 Jan Paper 3 · Java Programming · Array Copying and Reference Aliasing*

Given the array of integers ‘array’ shown below : 13 7 27 2 18 33 9 11 22 8 What is the output of the following JAVA statements ? int [ ] p = new int [10]; int [ ] q = new int [10]; for (int k = 0; k < 10; k ++) p[k] = array [k]; q = p; p[4] = 20; System.out.println(array [4] + “:” + q[4]);

- **1.** 20 : 20
- **2.** 18 : 18
- **3.** 18 : 20
- **4.** 20 : 18

> [!TIP]
> **Correct answer: 3. 18 : 20**

## Solution

The loop copies each integer value from `array` into the separate array object `p`, so changing p later cannot change the original `array`. The assignment `q=p` does not copy elements; it makes q and p refer to the same array object. Consequently `p[4]=20` also makes `q[4]` equal 20, while `array[4]` remains its original value 18. The output is `18:20`, option 3.

## Key Points

- Element-by-element copying creates a new array's values; assigning one array variable to another copies only the reference.

## Why the other options are incorrect

Options 1 and 4 incorrectly assume the original array aliases p. Option 2 correctly preserves array[4] but misses the alias created by q=p. Java array variables hold references, whereas the explicit loop copied primitive int values.
