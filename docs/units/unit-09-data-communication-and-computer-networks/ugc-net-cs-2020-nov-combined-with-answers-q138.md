# Question 138

*UGC NET CS · 2020 Nov With Answers · Data Communication · Noiseless and Noisy Channels*

Statement I: For a noiseless channel of bandwidth H hertz, the Nyquist limit restricts the number of independent samples per second to 2H. Statement II: For a noisy channel of bandwidth H hertz and signal-to-noise ratio S/N, Shannon capacity is C=H log2(1+S/N) bits per second. Choose the correct evaluation.

- **1.** Both Statement I and Statement Il are true
- **2.** Both Statement I and Statement II are false
- **3.** Statement I is correct but Statement Il is false
- **4.** Statement I is incorrect but Statement II is true.

> [!TIP]
> **Correct answer: 1. Both Statement I and Statement Il are true**

## Solution

For an ideal noiseless band-limited channel of bandwidth H, the Nyquist sampling/signalling limit is 2H independent symbols per second; with V signal levels, the corresponding bit rate is 2H log2 V. Thus Statement I is correct. For a noisy channel with signal-to-noise power ratio S/N, the Shannon–Hartley capacity is C=H log2(1+S/N) bits/s, exactly as stated. Statement II is also correct, so option 1 is the answer.

## Key Points

- Nyquist: 2H symbols/s for a noiseless band-limited channel.
- Shannon: H log2(1+S/N) bits/s for a noisy channel.

## Why the other options are incorrect

Options 2–4 make at least one fundamental limit false. Nyquist addresses symbol rate in the noiseless idealization, while Shannon gives an upper bit-rate capacity in the presence of noise; the formulas are complementary, not competing.
