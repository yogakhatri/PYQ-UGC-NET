# Question 127

*UGC NET CS · 2018 Dec Paper 1 And 2 · SQL · CHAR and VARCHAR Storage*

Attribute A has data type VARCHAR(20) and value 'xyz'. Attribute B has data type CHAR(20) and value 'lmnop'. Under the fixed-versus-variable-length storage model used by the question, how many character positions do A and B occupy, respectively?

- **1.** 3,5
- **2.** 20,20
- **3.** 3, 20
- **4.** 20, 5

> [!TIP]
> **Correct answer: 3. 3, 20**

## Solution

Under the simplified storage model intended by the question, VARCHAR stores only the actual characters up to its declared maximum, so 'xyz' occupies 3 character positions. CHAR is fixed-length and pads a shorter value to the declared length, so CHAR(20) occupies 20 positions even though 'lmnop' has only 5 visible characters. The pair is (3,20), option 3.

## Key Points

- VARCHAR(n) uses variable content length up to n; CHAR(n) is fixed width and pads shorter values.

## Why the other options are incorrect

Options 1 and 4 treat CHAR as though it stored only the five supplied characters. Option 2 treats VARCHAR(20) as fixed-width. In a real DBMS, VARCHAR also has length/record overhead and character encodings affect bytes; the options are asking only for the textbook fixed-versus-variable character capacity.
