# Question 62

*UGC NET CS · 2013 Dec Paper 3 · 2-D Geometrical Transforms and Viewing · Composition of Translation, Rotation and Scaling*

Which of the following statement(s) is (are) true ? I. Two successive translations are additive. II. Two successive rotations are additive. III. Two successive scaling operations are multiplicative.

- **A.** I and II
- **B.** I and III
- **C.** II and III
- **D.** All the above

> [!TIP]
> **Correct answer: D. All the above**

## Solution

For the standard 2-D transformations intended here, two translations by vectors t1 and t2 combine to translation by t1+t2, so I is true. Two rotations about the same origin/pivot by angles theta1 and theta2 combine to theta1+theta2, so II is true. Successive scale factors multiply componentwise: scaling by (sx1,sy1) and then (sx2,sy2) gives (sx1sx2,sy1sy2), so III is true. Hence all three statements hold.

## Key Points

- Composite 2-D transforms: translation vectors add, same-pivot rotation angles add, and scale factors multiply.

## Why the other options are incorrect

A, B and C each omit one valid composition rule. The rotation statement assumes the usual 2-D same-pivot setting; arbitrary 3-D rotations about different axes cannot be reduced merely by adding angles.
