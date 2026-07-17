# Question 80

*UGC NET CS · 2019 June Paper 1 And 2 · 3-D Object Representation, Geometric Transformations and Viewing · Phong illumination model*

Using the phong reflectance model, the strength of the specular highlight is determined by the angle between

- **1.** the view vector and the normal vector
- **2.** the light vector and the normal vector
- **3.** the light vector and the reflected vector
- **4.** the reflected vector and the view vector

> [!TIP]
> **Correct answer: 4. the reflected vector and the view vector**

## Solution

In the Phong reflectance model, the specular term is proportional to max(0,R·V)^s, where R is the perfect reflection direction of the incoming light and V points toward the viewer. Thus highlight strength depends on the angle between the reflected vector and the view vector. The highlight is strongest when these directions nearly coincide.

## Key Points

- Phong diffuse intensity uses N·L; Phong specular intensity uses R·V raised to a shininess exponent.

## Why the other options are incorrect

- **Option 1:** normal-view angle is not the Phong specular comparison.
- **Option 2:** light-normal angle controls diffuse reflection.
- **Option 3:** comparing light with its reflection does not determine what the viewer sees.
