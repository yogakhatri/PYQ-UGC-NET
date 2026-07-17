# Question 51

*UGC NET CS · 2015 Dec Paper 3 · Image Processing · Blind Image Deconvolution*

Blind image deconvolution is ____________.

- **1.** Combination of blur identification and image restoration
- **2.** Combination of segmentation and classification
- **3.** Combination of blur and non-blur image
- **4.** None of the above

> [!TIP]
> **Correct answer: 1. Combination of blur identification and image restoration**

## Solution

A blurred observation can be modeled as g=h*f+n, where f is the unknown sharp image, h is the blur kernel or point-spread function, and n is noise. Ordinary deconvolution assumes h is known. Blind deconvolution instead estimates h from the observation while also reconstructing f, so it combines blur identification with image restoration.

## Key Points

- Blind deconvolution jointly estimates the unknown blur kernel and the latent sharp image.

## Why the other options are incorrect

Segmentation and classification label image regions but do not estimate and invert a blur process. Merely combining blurred and unblurred images does not define deconvolution. Since option 1 gives the standard definition, 'none' is false.
