# Question 95

*UGC NET CS · 2018 Dec Paper 1 And 2 · Visible-Surface Detection · Back-Face Culling and Z-Buffer*

In 3D graphics, which statements are true? P: Back-face culling is an image-precision visible-surface determination procedure. Q: A Z-buffer is a 16-, 32-, or 64-bit field associated with each frame-buffer pixel and can determine the visible surface at each pixel.

- **1.** P only
- **2.** Q only
- **3.** P and Q
- **4.** Neither P nor Q

> [!TIP]
> **Correct answer: 2. Q only**

## Solution

P is false. Back-face culling rejects whole polygons using their orientation/normal before per-pixel raster comparison, so it is an object-space (object-precision) procedure. Q is true: a Z-buffer stores a depth value for each frame-buffer pixel and retains the fragment closest to the viewer; common depth fields use widths such as 16, 32, or 64 bits. Thus Q only is true, option 2.

## Key Points

- Back-face culling is polygon/object based; Z-buffering is per-pixel/image based.

## Why the other options are incorrect

Options 1 and 3 misclassify back-face culling as image precision. Option 4 rejects the valid per-pixel Z-buffer description. Image-precision methods decide visibility at sampled screen pixels, which is exactly what a Z-buffer does.
