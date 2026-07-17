# Question 16

*UGC NET CS · 2015 June Paper 3 · Computer Graphics Standards · GKS Output Primitives*

Which of the following is not a basic primitive of the Graphics Kernel System (GKS) ?

- **1.** POLYLINE
- **2.** POLYDRAW
- **3.** FILL AREA
- **4.** POLYMARKER

> [!TIP]
> **Correct answer: 2. POLYDRAW**

## Solution

GKS defines standard output primitives including POLYLINE for connected line segments, POLYMARKER for marker symbols, TEXT, FILL AREA for filled polygons, CELL ARRAY, and generalized drawing primitives. `POLYDRAW` is not one of the named basic GKS primitives, so option 2 is the exception.

## Key Points

- Core GKS primitives include polyline, polymarker, text, fill area, and cell array—not polydraw.

## Why the other options are incorrect

POLYLINE, FILL AREA, and POLYMARKER are all explicit GKS output primitives. A system may provide other drawing functions, but that does not make `POLYDRAW` part of the basic standardized set.
