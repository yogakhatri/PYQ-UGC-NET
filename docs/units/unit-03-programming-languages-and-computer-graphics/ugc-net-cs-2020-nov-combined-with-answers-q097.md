# Question 97

*UGC NET CS · 2020 Nov With Answers · Computer Graphics · Gouraud and Phong Shading*

Concerning Phong shading and Gouraud shading in a 3D scene, which statements are true? (A) Gouraud shading requires more computation than Phong shading. (B) Gouraud shading linearly interpolates the colour of an interior pixel from colours computed at the vertices. (C) Phong shading interpolates the normal vectors specified at the vertices.

- **1.** (A) and (B) only
- **2.** (A) and (C) only
- **3.** (B) and (C) only
- **4.** (A), (B) and (C)

> [!TIP]
> **Correct answer: 3. (B) and (C) only**

## Solution

Gouraud shading evaluates the illumination model at polygon vertices and linearly interpolates the resulting vertex colours across the interior, so B is true. Phong shading instead interpolates vertex normals across the polygon and evaluates illumination per pixel, so C is true. Per-pixel lighting is more expensive than interpolating already computed colours; therefore A reverses the cost comparison and is false. The correct combination is B and C, option 3.

## Key Points

- Gouraud interpolates colour; Phong interpolates normals and lights each pixel.

## Why the other options are incorrect

Options 1, 2, and 4 include A. Gouraud shading is normally cheaper, though it can miss a narrow specular highlight whose peak lies between vertices; Phong shading better captures such highlights at a higher computational cost.
