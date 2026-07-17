# Question 22

*UGC NET CS · 2021 Nov With Answers · Discrete Structures · Floor-Function Identities*

Which statements about the floor function are correct? Statement I: floor(2x) = floor(x) + floor(x + 1/2) for every real x. Statement II: floor(x+y) = floor(x) + floor(y) for all real x and y.

- **1.** Both Statement I and Statement II are true
- **2.** Both Statement I and Statement II are false
- **3.** Statement I is true but Statement II is false
- **4.** Statement I is false but Statement II is true

> [!TIP]
> **Correct answer: 3. Statement I is true but Statement II is false**

## Solution

Write x=n+r with n integer and 0≤r<1. Then floor(2x)=2n+floor(2r), while floor(x)+floor(x+1/2)=n+[n+floor(r+1/2)]=2n+floor(r+1/2). Both added floors are 0 for r<1/2 and 1 for r≥1/2, so Statement I is true. Statement II is false: x=y=0.6 gives floor(x+y)=1 but floor(x)+floor(y)=0. Hence option 3.

## Key Points

- Floor addition may gain a carry of one; splitting x into integer and fractional parts exposes when that happens.

## Why the other options are incorrect

Options 1 and 4 claim unrestricted additivity, but fractional parts can carry across an integer boundary. Option 2 rejects the valid doubling identity.
