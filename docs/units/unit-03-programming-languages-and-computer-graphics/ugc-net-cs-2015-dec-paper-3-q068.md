# Question 68

*UGC NET CS · 2015 Dec Paper 3 · Computer-Graphics Input Devices · Analog-to-Digital Data Acquisition*

Which listed steps are not required in the paper's analog-to-digital data-acquisition chain? (a) Sensing, (b) Conversion, (c) Amplification, (d) Conditioning, (e) Quantization.

- **1.** (a) and (b)
- **2.** (c) and (d)
- **3.** (a), (b) and (e)
- **4.** None of the above

> [!TIP]
> **Correct answer: 4. None of the above**

## Solution

In the broad data-acquisition chain assumed by the paper, a sensor obtains the analog signal; signal conditioning may include amplification; the converter samples and quantizes that conditioned signal and encodes a digital representation. Because every proposed group contains operations treated as necessary in that chain, no listed group is wholly 'not required.' The intended answer is therefore none of the above.

## Key Points

- Data acquisition is broader than the ADC core: sense → condition/amplify as needed → sample/quantize/encode.

## Why the other options are incorrect

Option 1 incorrectly discards sensing and conversion, and option 3 also discards quantization, which is fundamental to forming discrete amplitude levels. Option 2 calls amplification and conditioning unnecessary, but the paper treats them as the analog front end that brings a sensor signal into the ADC's permitted range. In real hardware, a separate amplifier or conditioning stage can be unnecessary when the source already meets the ADC input requirements; the question's absolute wording is therefore context-dependent.
