# Question 60

*UGC NET CS · 2019 June Paper 1 And 2 · Optimization · Simplex Method*

Consider the LPP: maximize Z=2x1-x2+2x3, subject to 2x1+x2<=10, x1+2x2-2x3<=20, x1+2x3<=5, and x1,x2,x3>=0. What is the solution after the first iteration of the simplex method?

- **1.** x1=5/2, x2=0, x3=0, Z=5
- **2.** x1=0, x2=0, x3=5/2, Z=5
- **3.** x1=0, x2=5/2, x3=0, Z=-5/2
- **4.** x1=0, x2=0, x3=10, Z=20

> [!TIP]
> **Correct answer: 2. x1=0, x2=0, x3=5/2, Z=5**

## Solution

In the initial simplex tableau, x3 has a positive objective coefficient 2 and can enter the basis. Its constraint-column coefficients are 0, -2 and 2; only the positive entry in the third constraint participates in the minimum-ratio test. The ratio is 5/2, so the first pivot makes x3=5/2 while x1=x2=0. The objective becomes Z=2(5/2)=5.

## Key Points

- In a primal simplex iteration, choose an improving entering variable and use the minimum positive ratio to select the leaving variable.

## Why the other options are incorrect

- **Option 1:** x1=5/2 is not the result of the stated first pivot.
- **Option 3:** entering x2 would decrease the maximization objective because its coefficient is -1.
- **Option 4:** x3=10 violates x1+2x3≤5.
