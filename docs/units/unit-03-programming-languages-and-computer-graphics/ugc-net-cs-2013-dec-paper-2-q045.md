# Question 45

*UGC NET CS · 2013 Dec Paper 2 · Web Programming and E-Commerce · EDI Software Layers*

Electronic Data In terchange Software consists of the following four layers :

- **A.** Business application, Internal format conversion, Network translator, EDI envelope
- **B.** Business application, Internal format conversion, EDI translator, EDI envelope
- **C.** Application layer, Transport layer, EDI translator, EDI envelope
- **D.** Application layer, Transport layer, IP layer, EDI envelope

> [!TIP]
> **Correct answer: B. Business application, Internal format conversion, EDI translator, EDI envelope**

## Solution

An EDI software path begins with the business application, converts its internal proprietary format, translates the result into the agreed EDI standard format, and wraps it in an EDI envelope for interchange. Thus the four named layers are business application, internal format conversion, EDI translator and EDI envelope.

## Key Points

- EDI flow: business application → internal-format conversion → EDI-standard translation → EDI envelope.

## Why the other options are incorrect

A incorrectly calls the standards-conversion component a network translator. C and D substitute generic Internet/OSI transport layers for the EDI application-processing stages. IP transport may carry messages but is not one of these four EDI software layers.
