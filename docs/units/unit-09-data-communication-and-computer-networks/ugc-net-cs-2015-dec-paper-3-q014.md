# Question 14

*UGC NET CS · 2015 Dec Paper 3 · Application Layer · MIME and Multimedia E-Mail*

In electronic mail, which of the following protocols allows the transfer of multimedia messages ?

- **1.** IMAP
- **2.** SMTP
- **3.** POP 3
- **4.** MIME

> [!TIP]
> **Correct answer: 4. MIME**

## Solution

MIME extends Internet e-mail so non-ASCII text, images, audio, video, and multipart bodies can be encoded and described with content types. SMTP can then transport the resulting MIME-formatted message. Thus MIME is the intended answer, though it is more precisely a message-format extension than a transport protocol.

## Key Points

- MIME describes and encodes multimedia content; SMTP carries the message.

## Why the other options are incorrect

SMTP transfers mail between servers; POP3 and IMAP retrieve/manage messages. Without MIME's content typing and transfer encodings, those protocols do not by themselves define multimedia message representation.
