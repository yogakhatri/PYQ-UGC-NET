# Question 6

*UGC NET CS · 2021 Nov With Answers · Multimedia · Bitmap Image Storage Calculation*

Suppose you have eight 'black and white' images taken with a 1‐megapixel camera and one '8‐color' image taken by an 8‐megapixel camera. How much hard disk space in total do you need to store these images on your computer?

- **1.** 1 GB
- **2.** 4 MB
- **3.** 3 MB
- **4.** 3 GB

> [!TIP]
> **Correct answer: 2. 4 MB**

## Solution

A black-and-white image needs 1 bit per pixel. Eight 1-megapixel images therefore need 8×1 million bits=8 million bits≈1 MB. Eight colours require log2 8=3 bits per pixel. One 8-megapixel, 8-colour image needs 8 million×3=24 million bits≈3 MB. Total storage is approximately 1+3=4 MB, option 2.

## Key Points

- Image bits = pixels × bits per pixel, and bits per pixel = log2(number of colours).

## Why the other options are incorrect

Option 3 omits the black-and-white images. The GB choices confuse bits, bytes, and megapixels by orders of magnitude. The calculation assumes uncompressed pixel data and the units intended by the choices.
