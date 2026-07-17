# Question 21

*UGC NET CS · 2012 Dec Paper 2 · Computer Graphics APIs · Windows GDI Circle Drawing*

Which API is used to draw a circle?

- **1.** Circle()
- **2.** Ellipse()
- **3.** RoundRect()
- **4.** Pie()

> [!TIP]
> **Correct answer: 2. Ellipse()**

## Solution

In the Windows Graphics Device Interface (GDI), Ellipse() draws an ellipse inside a supplied bounding rectangle. If that bounding rectangle has equal width and height, the ellipse has equal radii and is therefore a circle. There is no standard GDI Circle() function in this API set.

## Key Points

- A circle is a special ellipse.
- In Windows GDI, call Ellipse() with a square bounding box.

## Why the other options are incorrect

Circle() is the tempting name but is not the relevant Windows GDI function. RoundRect() draws a rectangle with rounded corners. Pie() draws a pie-shaped wedge bounded by an ellipse and radial lines, not a complete circle by itself.
