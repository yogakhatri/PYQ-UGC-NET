# Question 93

*UGC NET CS · 2018 July Paper 2 · Digital Logic Circuits and Components · Decoder, Multiplexer and Demultiplexer*

Match: (a) decoder, (b) multiplexer, (c) demultiplexer; with (i) 1 line to 2^n lines, (ii) n lines to 2^n lines, (iii) 2^n lines to 1 line, and (iv) 2^n lines to 2^(n−1) lines.

- **1.** (ii) (i) (iii)
- **2.** (ii) (iii) (i)
- **3.** (ii) (i) (iv)
- **4.** (iv) (ii) (i)

> [!TIP]
> **Correct answer: 2. (ii) (iii) (i)**

## Solution

An n-to-2^n decoder activates one of 2^n output lines, so a→ii. A multiplexer selects one of 2^n inputs and sends it to one output, so b→iii. A demultiplexer routes one input to one of 2^n outputs, so c→i. The sequence (ii),(iii),(i) is option 2.

## Key Points

- Decoder n→2^n; MUX 2^n→1; DEMUX 1→2^n.

## Why the other options are incorrect

The other codes interchange the opposite selection roles of multiplexer and demultiplexer or assign the decoder an impossible line count. A decoder has n binary select/input bits but 2^n mutually decoded outputs.
