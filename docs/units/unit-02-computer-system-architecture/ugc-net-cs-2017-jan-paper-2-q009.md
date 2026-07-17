# Question 9

*UGC NET CS · 2017 Jan Paper 2 · Data Representation · Fractional Number-System Conversion*

Convert the octal number 0.4051 into its equivalent decimal number.

- **1.** 0.5100098
- **2.** 0.2096
- **3.** 0.52
- **4.** 0.4192

> [!TIP]
> **Correct answer: 1. 0.5100098**

## Solution

Each octal fractional digit has weight 8⁻ᵏ. Therefore (0.4051)₈=4/8+0/64+5/512+1/4096=0.5+0+0.009765625+0.000244140625=0.510009765625. Rounded to the digits shown in the choices, this is 0.5100098, option 1.

## Key Points

- For a radix-r fraction, the first digit after the point has weight r⁻¹, the next r⁻², and so on.

## Why the other options are incorrect

The other values do not use the positional weights 8⁻¹,8⁻²,8⁻³,8⁻⁴ correctly. Octal digits after the point are not interpreted as a decimal fraction.
