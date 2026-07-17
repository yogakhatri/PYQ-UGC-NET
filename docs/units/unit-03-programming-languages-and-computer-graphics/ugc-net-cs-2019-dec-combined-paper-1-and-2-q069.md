# Question 69

*UGC NET CS · 2019 Dec Paper 1 And 2 · Computer Graphics · Aspect-Ratio-Preserving Image Resizing*

If we want to resize a 1024 x 768 pixels image to one that is 640 pixels wide with the same aspect ratio, what would be the height of the resized image?

- **1.** 420 Pixels
- **2.** 460 Pixels
- **3.** 480 Pixels
- **4.** 540 pixels

> [!TIP]
> **Correct answer: 3. 480 Pixels**

## Solution

Preserving aspect ratio means applying the same scale factor to both dimensions. The width scale is 640/1024=5/8. The new height is 768×5/8=96×5=480 pixels. Hence option 3.

## Key Points

- Same aspect ratio: new height = old height × new width / old width.

## Why the other options are incorrect

The other heights use a different vertical scale and would distort the image. Equivalently, the original ratio 1024:768 simplifies to 4:3, so a 640-pixel width requires height 640×3/4=480.
