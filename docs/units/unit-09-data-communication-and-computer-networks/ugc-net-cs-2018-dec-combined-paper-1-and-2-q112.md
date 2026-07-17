# Question 112

*UGC NET CS · 2018 Dec Paper 1 And 2 · IP Addressing · Network and Host Portions of IPv4 Addresses*

The four-byte IP address consists of:

- **1.** Network address
- **2.** Host address
- **3.** Both network and host addresses
- **4.** Neither network nor host address

> [!TIP]
> **Correct answer: 3. Both network and host addresses**

## Solution

A four-byte IPv4 address is a 32-bit hierarchical address. The prefix identifies the network (or subnet), and the remaining bits identify an interface/host within that network. The boundary is determined by the prefix length or subnet mask rather than always occurring at a fixed byte boundary. Therefore an IPv4 address contains both network and host portions, option 3.

## Key Points

- IPv4 address = network prefix + host/interface suffix, with the subnet mask defining the split.

## Why the other options are incorrect

Options 1 and 2 mention only one of the two hierarchical components. Option 4 denies both even though routing uses the network prefix and local delivery distinguishes the host/interface part.
