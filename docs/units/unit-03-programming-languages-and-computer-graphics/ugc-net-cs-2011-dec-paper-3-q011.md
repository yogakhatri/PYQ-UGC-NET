# Question 11

*UGC NET CS · 2011 Dec Paper 3 · 2-D Geometrical Transforms and Viewing · Window-to-Viewport Transformation*

Find the Normalization transformation that maps a windows whose lowe r left is at (1,1) and Upper right (3, 5) onto a view port that has lower left corner at (0, 0) and Upper right corner at (½, ½). _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: x_v=(x-1)/4 and y_v=(y-1)/8**

## Solution

For a window [xw_min,xw_max]x[yw_min,yw_max] and viewport [xv_min,xv_max]x[yv_min,yv_max], preserve normalized position:

x_v=xv_min+(x-xw_min)(xv_max-xv_min)/(xw_max-xw_min),
y_v=yv_min+(y-yw_min)(yv_max-yv_min)/(yw_max-yw_min).

Here the x scale is (1/2-0)/(3-1)=1/4 and the y scale is (1/2-0)/(5-1)=1/8. Therefore x_v=(x-1)/4 and y_v=(y-1)/8. The lower-left window point (1,1) maps to (0,0), and the upper-right point (3,5) maps to (1/2,1/2), confirming the result.

In homogeneous coordinates the transformation is:

~~~text
[ x_v ]   [ 1/4   0   -1/4 ] [ x ]
[ y_v ] = [  0   1/8  -1/8 ] [ y ]
[  1  ]   [  0    0      1  ] [ 1 ]
~~~

It can also be viewed as translate the window lower-left to the origin, then scale x and y independently.

## Key Points

- Window-to-viewport normalization is translate to the window origin, scale by viewport/window extent on each axis, then translate to the viewport origin.

## Common mistakes to avoid

Using one uniform scale distorts the specified mapping because the window aspect ratio (2:4) differs from the square viewport. Scaling without the -1 translation incorrectly sends (1,1) away from the viewport origin.
