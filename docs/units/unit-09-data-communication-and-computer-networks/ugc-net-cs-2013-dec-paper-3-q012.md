# Question 12

*UGC NET CS · 2013 Dec Paper 3 · Application-Layer Protocols · SOAP Remote Procedure Calls*

Which is the protocol for performing RPCs between applications in a language and system independent way ?

- **A.** Hyper Text Transmission Protocol (HTTP)
- **B.** Simple Network Management Protocol (SNMP)
- **C.** Simple Object Access Protocol (SOAP)
- **D.** Simple Mail Transfer Protocol (SMTP)

> [!TIP]
> **Correct answer: C. Simple Object Access Protocol (SOAP)**

## Solution

SOAP is an XML-based messaging protocol designed for structured information exchange between applications independent of implementation language and operating system. Web-service operations can use SOAP messages to implement remote procedure calls, commonly transported over HTTP.

## Key Points

- SOAP supplies the structured, language-neutral message envelope; HTTP is often only its transport.

## Why the other options are incorrect

HTTP transports resources/messages but does not itself define language-neutral RPC envelopes. SNMP manages network devices, and SMTP transfers email. Neither is the requested application RPC protocol.
