# Question 17

*UGC NET CS · 2015 June Paper 3 · Viewing and Coordinate Systems · World, Device, and Normalized Device Coordinates*

Which statement(s) is/are incorrect? (a) Mapping picture coordinates to the appropriate device or workstation coordinates is a viewing transformation. (b) The right-handed Cartesian coordinate system used to describe the picture is the world-coordinate system. (c) The coordinate system corresponding to the physical display device is the physical device-coordinate system. (d) The normalized device-coordinate system is a left-handed coordinate system whose virtual display is the unit 1×1 square with lower-left corner at the origin. Codes:

- **1.** (a) only
- **2.** (a) and (b)
- **3.** (c) only
- **4.** (d) only

> [!TIP]
> **Correct answer: 4. (d) only**

## Solution

Statements (a), (b), and (c) give the standard roles of viewing transformation, world coordinates, and physical device coordinates. Normalized device coordinates do use a device-independent unit square with its lower-left corner at the origin, but the conventional x-right, y-up system is not left-handed. Therefore the handedness claim makes statement (d) incorrect by itself.

## Key Points

- World coordinates describe the scene; viewing maps it; NDC normalizes it; device coordinates place it on the physical display.

## Why the other options are incorrect

Option 1 incorrectly rejects the world-to-device viewing mapping. Option 2 also rejects the ordinary right-handed world-coordinate description. Option 3 rejects the correct definition of physical device coordinates. Only option 4 isolates the faulty statement.
