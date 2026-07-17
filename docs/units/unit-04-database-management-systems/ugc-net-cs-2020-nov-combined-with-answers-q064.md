# Question 64

*UGC NET CS · 2020 Nov With Answers · Functional Dependencies · Candidate Keys by Attribute Closure*

For relational schema S(U,V,W,X,Y,Z), the functional dependencies are U→V, VW→X, Y→W, and X→U. Which listed sets are exactly candidate keys?

- **1.** UY, VY
- **2.** UY, VY, XY
- **3.** UYZ. VYZ. VWZ
- **4.** UYZ, VYZ, XYZ

> [!TIP]
> **Correct answer: 4. UYZ, VYZ, XYZ**

## Solution

Y and Z never appear on any dependency's right side, so every candidate key must contain both. Add one attribute that enters the U–V–X cycle. For UYZ: U→V, Y→W, and VW→X, giving every attribute. For VYZ: Y→W, then VW→X and X→U. For XYZ: X→U→V and Y→W. Each is minimal because removing Y or Z loses an underivable attribute, and removing the third attribute cannot generate U,V, or X. Thus UYZ, VYZ, and XYZ are the candidate keys—option 4.

## Key Points

- Attributes absent from all FD right sides must be in every key; then use closures to find minimal additions.

## Why the other options are incorrect

Options 1 and 2 omit mandatory Z. Option 3 includes VWZ, which cannot derive Y because Y never appears on a right side. It also omits the valid key XYZ.
