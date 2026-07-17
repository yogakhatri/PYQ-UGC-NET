# Question 9

*UGC NET CS · 2018 July Paper 2 · 3-D Object Representation, Geometric Transformations and Viewing · Painter's Algorithm and Backface Culling*

Which statements about visibility in 3D graphics are true? S1: The Painter's algorithm sorts polygons by depth and paints them starting with the nearest polygon. S2: Backface culling eliminates geometry with back-facing normals.

- **1.** S1 only
- **2.** S2 only
- **3.** Both S1 and S2
- **4.** Neither S1 nor S2

> [!TIP]
> **Correct answer: 2. S2 only**

## Solution

S1 is false because the Painter's algorithm draws from farthest to nearest: later, nearer polygons paint over farther ones. Starting with the nearest would allow farther polygons to overwrite visible surfaces incorrectly. S2 is true: backface culling discards polygon faces whose orientation/normals point away from the viewer. Therefore S2 only is true, option 2.

## Key Points

- Painter's algorithm is back-to-front; backface culling removes outward faces oriented away from the camera.

## Why the other options are incorrect

Options 1 and 3 accept the reversed Painter order. Option 4 rejects the correct definition of backface culling. Backface culling reduces work but does not by itself solve all occlusion among front-facing surfaces.
