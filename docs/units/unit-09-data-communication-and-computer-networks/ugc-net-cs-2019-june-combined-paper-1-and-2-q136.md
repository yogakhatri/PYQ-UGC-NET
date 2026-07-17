# Question 136

*UGC NET CS · 2019 June Paper 1 And 2 · OSI and TCP/IP Layer Functions · TCP/IP Layer Functions*

In the TCP/IP model, encryption and decryption are functions of which layer?

- **1.** Data link
- **2.** Network
- **3.** Transport
- **4.** Application

> [!TIP]
> **Correct answer: 4. Application**

## Solution

The TCP/IP model does not have separate presentation and session layers. Functions that the OSI model associates with presentation—such as encryption, decryption, compression and data representation—are handled within the TCP/IP application layer or by application-facing protocols. Therefore application is the expected layer.

## Key Points

- TCP/IP's application layer combines the roles of the OSI application, presentation and session layers.

## Why the other options are incorrect

The data-link layer frames local-link traffic, the network layer routes IP packets, and the transport layer provides end-to-end process communication. None is the TCP/IP layer that absorbs the OSI presentation function.
