# Question 18

*UGC NET CS · 2016 July Paper 3 · 3-D Object Representation, Geometric Transformations and Viewing · Hermite and Bezier Curve Properties*

Which of the following statement(s) is/are correct with reference to curve generation ? I. Hermite curves are generated using the concepts of interpolation. II. Bezier curves are generated using the concepts of approximation. III. The Bezier curve lies entirely within the convex hull of its control points. IV. The degree of Bezier curve does not depend on the number of control points.

- **1.** I, II and IV only
- **2.** II and III only
- **3.** I and II only
- **4.** I, II and III only

> [!TIP]
> **Correct answer: 4. I, II and III only**

## Solution

I is true because a cubic Hermite segment interpolates its endpoint positions while using endpoint tangents. II is true because a Bezier curve generally approximates its control polygon rather than passing through every control point. III is true by the nonnegative Bernstein basis whose weights sum to 1, keeping the curve in the control points' convex hull. IV is false: n+1 control points define a degree-n Bezier curve. Thus I, II and III only.

## Key Points

- Hermite interpolates endpoints; Bezier approximates a control polygon, lies in its convex hull, and has degree one less than its control-point count.

## Why the other options are incorrect

Options 1 and 3 omit the convex-hull property, while option 2 omits the true Hermite interpolation statement. Any option containing IV ignores the direct degree/control-point relationship.
