# Question 13

*UGC NET CS · 2015 June Paper 3 · 3-D Viewing · Principal Vanishing Points in Perspective Projection*

Give the number of principal vanishing point(s) along with their direction for the standard perspective transformation :

- **1.** Only one in the direction K
- **2.** Two in the directions I and J
- **3.** Three in the directions I, J and K
- **4.** Only two in the directions J and K

> [!TIP]
> **Correct answer: 1. Only one in the direction K**

## Solution

The standard perspective transformation places the center of projection on the principal viewing axis and projects toward the view plane. Lines parallel to the I and J axes remain parallel to the view plane, while lines parallel to the K (depth) axis converge. Hence there is one principal vanishing point, in the K direction.

## Key Points

- Axis-aligned standard perspective is one-point perspective: only the depth/K direction vanishes.

## Why the other options are incorrect

Two- and three-point perspective arise after orienting the object or camera so that two or three principal axes have depth components relative to the view plane. That is not the standard axis-aligned perspective transformation specified here.
