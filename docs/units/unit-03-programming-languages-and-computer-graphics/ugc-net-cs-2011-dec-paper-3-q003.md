# Question 3

*UGC NET CS · 2011 Dec Paper 3 · Computer Graphics · Image Restoration and Huffman Coding*

(a) What are the kinds of degradation that can be easily restore d ? Explain inverse filteration and wiener filteration method. (b) A source emits 6 symbols with probabilities 1/2, 1/4, 1/8, 1/16, 1/32, 1/32. Determine its Huffman code.


> [!TIP]
> **Correct answer: Use inverse/Wiener restoration; one valid Huffman code is 0, 10, 110, 1110, 11110, 11111**

## Solution

**Image restoration:** A common linear degradation model is g(x,y)=h(x,y)*f(x,y)+n(x,y), or G(u,v)=H(u,v)F(u,v)+N(u,v) in the frequency domain. Linear, spatially invariant degradations whose point-spread function can be known or estimated—uniform motion blur, out-of-focus blur and some atmospheric blur—are the easiest to restore. Severe clipping, missing information, nonlinear distortion and unknown spatially varying blur are harder.

Inverse filtering ignores noise and estimates F_hat=G/H wherever H is nonzero. It can undo known blur exactly in an ideal noiseless case, but near frequencies where |H| is small it greatly amplifies noise; practical versions threshold or regularize the inverse.

The Wiener filter minimizes mean-square reconstruction error while accounting for signal and noise spectra: F_hat=[H*/(|H|^2+S_N/S_F)]G. Where the signal-to-noise ratio is high it behaves like an inverse; where noise dominates it suppresses unstable amplification.

**Huffman coding:** Label the six symbols A-F with probabilities 1/2, 1/4, 1/8, 1/16, 1/32 and 1/32. Repeatedly combine the two smallest weights: 1/32+1/32=1/16, then 1/16+1/16=1/8, then 1/8+1/8=1/4, then 1/4+1/4=1/2, and finally 1/2+1/2=1. A valid prefix code is A=0, B=10, C=110, D=1110, E=11110, F=11111. Its average length is 1/2(1)+1/4(2)+1/8(3)+1/16(4)+1/32(5)+1/32(5)=1.9375 bits/symbol, equal to the entropy because the probabilities are powers of two.

## Key Points

- Inverse filtering divides out known blur; Wiener filtering balances deblurring against noise.
- Dyadic probabilities give exact Huffman lengths -log2(p).

## Common mistakes to avoid

Direct inverse filtering without guarding small values of H is numerically unstable in noise. Huffman codewords may differ from those shown, but they must be prefix-free and have lengths 1,2,3,4,5,5 for these probabilities.
