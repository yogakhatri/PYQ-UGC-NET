# Question 38

*UGC NET CS · 2017 Jan Paper 2 · File and Input/Output Systems · Controller, Driver, Interrupt, and Kernel Roles*

Match the following w.r.t. Input/Output management : List – I List – II a. Device controller i. Extracts information from the controller register and store it in data buffer b. Device driver ii. I/O scheduling c. Interrupt handler iii. Performs data transfer d. Kernel I/O subsystem iv. Processing of I/O request Codes : a b c d

- **1.** iii iv i ii
- **2.** ii i iv iii
- **3.** iv i ii iii
- **4.** i iii iv ii

> [!TIP]
> **Correct answer: 1. iii iv i ii**

## Solution

The device controller is hardware that performs the actual data transfer, so a→iii. The device driver translates and processes an OS I/O request for its particular device, so b→iv. When the device interrupts, the interrupt handler reads controller status/data registers and places or accounts for the data in a buffer, so c→i. The device-independent kernel I/O subsystem performs functions such as I/O scheduling, so d→ii. The code iii,iv,i,ii is option 1.

## Key Points

- Controller=hardware transfer; driver=device-specific request; interrupt handler=completion/status; kernel I/O subsystem=scheduling and common services.

## Why the other options are incorrect

The other mappings confuse hardware transfer, device-specific request handling, interrupt completion work, and device-independent scheduling. These roles occur at different layers of the I/O path.
