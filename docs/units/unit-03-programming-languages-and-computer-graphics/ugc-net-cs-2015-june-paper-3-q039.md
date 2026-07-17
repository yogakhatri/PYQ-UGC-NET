# Question 39

*UGC NET CS · 2015 June Paper 3 · Web Programming · Java Applet Execution Model*

Which one of the following is correct ?

- **1.** Java applets can not be written in any programming language
- **2.** An applet is not a small program
- **3.** An applet can be run on its own
- **4.** Applets are embedded in another applications

> [!TIP]
> **Correct answer: 4. Applets are embedded in another applications**

## Solution

In the historical Java applet model, an applet is a small program embedded in a host such as a web page and executed by an applet viewer or Java-enabled browser. It does not use a normal standalone `main` entry point. Thus option 4 is the correct textbook statement.

## Key Points

- A legacy applet is embedded and host-managed, unlike a standalone Java application with `main`.

## Why the other options are incorrect

An applet is indeed a small program, so option 2 is false. It normally requires a host environment rather than running on its own, so option 3 is false. Option 1 is nonsensically absolute; applets were classically written for the Java platform. Applets are now obsolete, but that does not change the historical concept tested.
