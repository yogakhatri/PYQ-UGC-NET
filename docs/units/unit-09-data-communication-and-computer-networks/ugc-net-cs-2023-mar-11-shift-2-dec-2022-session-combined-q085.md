# Question 85

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · OSI and TCP/IP Layer Functions · Error Detection and Correction*

at to 1-30391 SID: TD:187035 In the standard Ethernet with transmission rate of 10Mbps, assume that the length of the medium is 2500m and size of a frame is 512 bytes. The propagation speed of a signal in a cable is normally 2 x 10s m/s. Calculate Transmission delay and propagation delay.

- **1.** 25.25us and 51.2us
- **2.** 51.2us and 12.5us
- **3.** 10.24us and 50.12us
- **4.** 12.Sus and 51.2us

> [!TIP]
> **Correct answer: 2. 51.2us and 12.5us**

## Solution

The propagation delay is unambiguous: 2500/(2×10^8)=12.5 μs. If the frame size is the printed 512 bytes, however, transmission delay is (512×8)/(10×10^6)=409.6 μs, and none of the options is correct. Option 2 results only if the intended frame size was 512 bits: 512/(10×10^6)=51.2 μs, paired with 12.5 μs. Thus option 2 is the apparent intended answer, but the printed unit makes the question defective.

## Key Points

- Transmission delay L/R uses frame length in bits; propagation delay distance/speed is independent of frame size.

## Why the other options are incorrect

Options 1, 3, and 4 either swap the two delays or use values inconsistent with both the link rate and propagation speed. More importantly, no listed option matches a literal 512-byte frame.
