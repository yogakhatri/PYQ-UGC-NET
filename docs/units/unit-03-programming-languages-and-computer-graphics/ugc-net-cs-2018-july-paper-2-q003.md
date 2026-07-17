# Question 3

*UGC NET CS · 2018 July Paper 2 · Java Programming · Array Reference Passing and Aliasing*

What is the output of the following JAVA program ? class simple { public static void main(String[ ] args) { simple obj = new simple( ); obj.start( ); } void start( ) { long [ ] P= {3, 4, 5}; long [ ] Q= method (P); System.out.print (P[0] + P[1] + P[2]+”:”); System.out.print (Q[0] + Q[1] + Q[2]); } long [ ] method (long [ ] R) { R [1]=7; return R; } } //end of class

- **1.** 12 : 15
- **2.** 15 : 12
- **3.** 12 : 12
- **4.** 15 : 15

> [!TIP]
> **Correct answer: 4. 15 : 15**

## Solution

Java passes the value of the array reference to `method`. Thus `R` and `P` refer to the same array object. The assignment `R[1]=7` changes that shared array from {3,4,5} to {3,7,5}, and the method returns the same reference, so `Q` also points to it. Both sums are 3+7+5=15, producing `15:15`. Hence option 4 is correct.

## Key Points

- Java is pass-by-value, but for objects the value passed is a reference; mutating the referenced object is visible through every alias.

## Why the other options are incorrect

Options 1 and 2 assume only one variable observes the mutation, but P, R, and Q alias the same array. Option 3 assumes a copy of the elements was passed, which Java does not do automatically.
