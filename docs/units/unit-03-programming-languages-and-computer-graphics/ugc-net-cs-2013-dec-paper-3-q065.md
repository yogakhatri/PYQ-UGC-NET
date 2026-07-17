# Question 65

*UGC NET CS · 2013 Dec Paper 3 · Colour Models · CMY-to-RGB Conversion*

The transformation matrix required for conversion of CMY colour model to RGB colour model is given as :

- **A.** [R,G,B]^T = [C,M,Y]^T - [1,1,1]^T
- **B.** [R,G,B]^T = [C,M,Y]^T - [1,2,3]^T
- **C.** [R,G,B]^T = [1,1,1]^T - [C,M,Y]^T
- **D.** [R,G,B]^T = [C,M,Y]^T - [0.5,0.5,0.5]^T

> [!TIP]
> **Correct answer: C. [R,G,B]^T = [1,1,1]^T - [C,M,Y]^T**

## Solution

In the normalized CMY model, each subtractive component is the complement of its additive RGB component: C=1-R, M=1-G and Y=1-B. Solving gives R=1-C, G=1-M and B=1-Y. In vector form, [R,G,B]^T=[1,1,1]^T-[C,M,Y]^T, which is option C.

## Key Points

- Normalized RGB and CMY are componentwise complements: RGB=1-CMY.

## Why the other options are incorrect

A reverses the subtraction and would give negative RGB values for ordinary CMY inputs. B subtracts unrelated constants 1,2,3. D subtracts 0.5 from each CMY component rather than taking the complement about 1.
