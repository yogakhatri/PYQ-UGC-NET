# Question 100

*UGC NET CS · 2018 July Paper 2 · Programming the Basic Computer · 8085 Data Transfer and Arithmetic Instructions*

In the 8085 microprocessor, what does this program do? LDA 8000H; MVI B,30H; ADD B; STA 8001H.

- **1.** Read a number from input port and store it in memory
- **2.** Read a number from input device with address 8000H and store it in memory at location 8001H
- **3.** Read a number from memory at location 8000H and store it in memory location 8001H
- **4.** Load A with data from input device with address 8000H and display it on the output device with address 8001H - o 0 o -

> [!TIP]
> **Correct answer: No option states the full behavior: the byte at memory[8000H] is increased by 30H (modulo 256) and the result is stored in memory[8001H]. Option 3 is only the nearest incomplete description.**

## Solution

Execute the instructions in order. `LDA 8000H` loads A←M[8000H]. `MVI B,30H` loads B←30H. `ADD B` computes A←A+B, updating flags; for an 8-bit accumulator the stored byte is (M[8000H]+30H) mod 100H. `STA 8001H` then writes that result to M[8001H]. The program uses memory addresses, not input/output ports or devices.

## Key Points

- 8085 sequence: LDA reads memory into A, ADD changes A, and STA writes the changed A back to memory.

## Why the other options are incorrect

Options 1, 2, and 4 incorrectly describe port or device I/O; `LDA` and `STA` are direct memory instructions. Option 3 correctly identifies the source and destination memory locations but omits the essential addition of 30H, so it is not a complete answer.
