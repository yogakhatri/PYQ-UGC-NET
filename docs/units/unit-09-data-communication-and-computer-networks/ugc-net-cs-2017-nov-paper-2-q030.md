# Question 30

*UGC NET CS · 2017 Nov Paper 2 · IPv4 Addressing · Unspecified Address during Bootstrapping*

The IP address __________ is used by hosts when they are being booted.

- **1.** 0.0.0.0
- **2.** 1.0.0.0
- **3.** 1.1.1.1
- **4.** 255.255.255.255

> [!TIP]
> **Correct answer: 1. 0.0.0.0**

## Solution

Before a booting host has obtained its own IPv4 address, it cannot place a normal assigned address in the source field. DHCP specifies a zero source address for client broadcasts sent before address acquisition; dotted-decimal zero is 0.0.0.0. Hence option 1 is the intended answer. The discovery is normally sent to the limited-broadcast destination 255.255.255.255, which is a different role.

## Key Points

- During DHCP initialization: source address 0.0.0.0; local broadcast destination 255.255.255.255.

## Why the other options are incorrect

1.0.0.0 and 1.1.1.1 are not bootstrap placeholders. 255.255.255.255 is the local limited-broadcast destination, not the booting host's unspecified source address. The stem is best read as asking which address the unconfigured host uses for itself.

## References

- [RFC 2131 — Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131)
