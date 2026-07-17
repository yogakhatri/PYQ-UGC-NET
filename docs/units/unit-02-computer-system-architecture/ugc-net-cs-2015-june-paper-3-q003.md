# Question 3

*UGC NET CS · 2015 June Paper 3 · Microprocessors · 8085 RST Vectors*

The RST 7 instruction in 8085 microprocessor is equivalent to :

- **1.** CALL 0010 H
- **2.** CALL 0034 H
- **3.** CALL 0038 H
- **4.** CALL 003C H

> [!TIP]
> **Correct answer: 3. CALL 0038 H**

## Solution

In the 8085, `RST n` is a one-byte call to restart vector `8 × n`. For `RST 7`, the address is `7 × 8 = 56₁₀ = 38₁₆`. It is therefore equivalent in control transfer to `CALL 0038H`.

## Key Points

- 8085 restart vector address = `8n`; RST 7 jumps to 0038H.

## Why the other options are incorrect

The other hexadecimal addresses do not equal `8 × 7`. A quick vector list is 0000H, 0008H, 0010H, 0018H, 0020H, 0028H, 0030H, 0038H for RST 0 through RST 7.
