# Question 61

*UGC NET CS · 2018 Dec Paper 1 And 2 · Boolean Algebra · Verification of Boolean Identities*

Consider the Boolean identities: (i) wx+w(x+y)+x(x+y)=x+wy. (ii) [w x̅(y+xz̅)+w̅x̅]y=x̅y. Which identities are true?

- **1.** (i) is true and (ii) is false
- **2.** (i) is false and (ii) is true
- **3.** Both (i) and (ii) are true
- **4.** Both (i) and (ii) are false

> [!TIP]
> **Correct answer: 3. Both (i) and (ii) are true**

## Solution

For (i), wx+w(x+y)+x(x+y)=wx+(wx+wy)+(x+xy)=wx+wy+x=x+wy, using x+xy=x and x+wx=x. Thus (i) is true. For (ii), [w x̅(y+xz̅)+w̅x̅]y = w x̅y(y+xz̅)+w̅x̅y. Since x̅x=0 and y²=y, this becomes wx̅y+w̅x̅y=x̅y(w+w̅)=x̅y. Thus (ii) is also true, so option 3 is correct.

## Key Points

- Boolean simplification repeatedly uses idempotence, complementarity, distributivity, and absorption.

## Why the other options are incorrect

Options 1, 2, and 4 declare at least one verified identity false. The main traps are failing to distribute the final y in (ii) and overlooking absorption in (i).
