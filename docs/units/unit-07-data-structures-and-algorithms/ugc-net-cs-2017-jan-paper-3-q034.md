# Question 34

*UGC NET CS · 2017 Jan Paper 3 · Dynamic Programming · Matrix-Chain Multiplication*

The minimum number of scalar multiplication required, for parenthesization of a matrix- chain product whose sequence of dimensions for four matrices is <5, 10, 3, 12, 5> is

- **1.** 630
- **2.** 580
- **3.** 480
- **4.** 405

> [!TIP]
> **Correct answer: 4. 405**

## Solution

The matrices have sizes A1=5×10, A2=10×3, A3=3×12, and A4=12×5. The best split is (A1A2)(A3A4): A1A2 costs 5·10·3=150 and yields 5×3; A3A4 costs 3·12·5=180 and yields 3×5; multiplying those results costs 5·3·5=75. Total cost is 150+180+75=405 scalar multiplications, so option 4 is correct.

## Key Points

- Matrix-chain cost depends on parenthesization even though the mathematical product is the same; evaluate split costs using p(i−1)·p(k)·p(j).

## Why the other options are incorrect

The other principal costs are 630 for (((A1A2)A3)A4), 580 for A1(A2(A3A4)), 1,260 for ((A1(A2A3))A4), and 1,210 for A1((A2A3)A4). None beats 405; 480 is not the optimum for these dimensions.
