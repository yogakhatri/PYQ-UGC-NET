# Question 126

*UGC NET CS · 2020 Nov With Answers · 3-D Object Representation, Geometric Transformations and Viewing · Perspective and Orthographic Projection Properties*

Given the following properties of 3-D projections, identify in order the property true of (i) perspective projection only, (ii) orthographic projection only, (iii) both perspective and orthographic projections, and (iv) neither projection. A. Straight lines are mapped to straight lines. B. Distances and angles are generally preserved. C. Far-away objects appear the same size as closer objects. D. Homogeneous coordinates are required to encode the projection as a linear transformation.

- **1.** D, C, B, A
- **2.** B, C, D, A
- **3.** D, C, A, B
- **4.** C, D, B, A

> [!TIP]
> **Correct answer: 3. D, C, A, B**

## Solution

Perspective projection needs homogeneous coordinates because the perspective divide makes its Euclidean-coordinate formula non-linear, so D is perspective-only. Orthographic projection does not shrink an object merely because it is farther from the viewer, so C is orthographic-only. Both projections map a 3-D straight line to a straight line in the image (apart from degenerate cases), so A belongs to both. General projection does not preserve all distances and angles, so B belongs to neither. The required order is D, C, A, B: option 3.

## Key Points

- Perspective changes apparent size with depth and needs a homogeneous divide; orthographic size is depth-independent; both preserve straightness, not general lengths or angles.

## Why the other options are incorrect

Options 1 and 4 wrongly treat preservation of distance and angle as a general projection property. Option 2 assigns B to perspective projection and D to both projections, reversing the essential distinction created by the perspective divide.
