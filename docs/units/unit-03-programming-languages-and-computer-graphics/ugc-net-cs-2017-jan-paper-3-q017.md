# Question 17

*UGC NET CS · 2017 Jan Paper 3 · Computer Graphics · Scan-Conversion Artifacts and Aliasing*

Which of the following is/are side effects of scan conversion ? a. Aliasing b. Unequal intensity of diagonal lines c. Overstriking in photographic applications d. Local or Global aliasing

- **1.** a and b
- **2.** a, b and c
- **3.** a, c and d
- **4.** a, b, c and d

> [!TIP]
> **Correct answer: 4. a, b, c and d**

## Solution

Scan conversion maps continuous geometry onto a discrete pixel grid, so aliasing and its local or global forms can appear. A diagonal line can look dimmer than a horizontal line because its lit pixels are farther apart, causing unequal intensity. If two generated samples address the same photographic pixel, repeated exposure produces overstriking. Thus a, b, c, and d are all recognized scan-conversion side effects, giving option 4.

## Key Points

- Rasterization can distort shape, spacing, brightness, and exposure because continuous primitives are forced onto discrete samples.

## Why the other options are incorrect

Options 1–3 omit at least one genuine artifact. Aliasing is the umbrella sampling distortion, local/global aliasing describe two manifestations, unequal intensity is an orientation-dependent brightness artifact, and overstriking is repeated writing or exposure of a pixel.
