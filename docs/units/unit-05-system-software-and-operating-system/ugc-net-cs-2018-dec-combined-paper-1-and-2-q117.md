# Question 117

*UGC NET CS · 2018 Dec Paper 1 And 2 · Windows Operating Systems · Windows XP Networking Architecture*

Which of the following statement/s is/are true? (i) Windows XP supports both peer-peer and client-server networks. (ii) Windows XP implements Transport protocols as drivers that can be loaded and unloaded from the system dynamically. Choose the correct answer from the code given below :

- **1.** (i) only
- **2.** (ii) only
- **3.** Neither (i) nor (ii)
- **4.** Both (i) and (ii)

> [!TIP]
> **Correct answer: 4. Both (i) and (ii)**

## Solution

Statement (i) is true: Windows XP supports peer-to-peer networking and conventional client/server networking. Statement (ii) is also true in the Windows XP architecture: transport protocols are implemented in the networking stack as drivers, allowing transport components to be installed, bound, loaded, and unloaded independently of network-adapter drivers. Thus both statements are true, option 4.

## Key Points

- Windows XP networking is both model-flexible (peer and client/server) and driver-modular (transport protocols are loadable components).

## Why the other options are incorrect

Options 1 and 2 discard one valid part of XP's networking design, and option 3 discards both. The NDIS/TDI layering separates network adapters, transport mechanisms, and higher-level clients so that the stack is modular rather than one fixed monolith.

## References

- [Microsoft Learn — What is Peer Networking?](https://learn.microsoft.com/en-us/windows/win32/p2psdk/what-is-peer-networking-)
- [Microsoft Learn — NDIS 5.1 Driver Unload Handler for Windows XP](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterunloadhandler)
