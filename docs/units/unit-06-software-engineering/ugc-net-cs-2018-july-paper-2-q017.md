# Question 17

*UGC NET CS · 2018 July Paper 2 · Software Design Patterns · Proxy Pattern and Access Control*

A software design pattern often used to restrict access to an object is :

- **1.** adapter
- **2.** decorator
- **3.** delegation
- **4.** proxy

> [!TIP]
> **Correct answer: 4. proxy**

## Solution

A proxy is a stand-in object that exposes the same interface as a real subject and controls access to it. A protection proxy can check permissions before forwarding a request; remote, virtual, and caching proxies control access for other reasons. Therefore option 4 is correct.

## Key Points

- Proxy interposes a surrogate between client and real object, making access control, lazy creation, remoting, or caching transparent.

## Why the other options are incorrect

An adapter converts one interface into another. A decorator adds responsibilities while preserving an interface. Delegation is a general technique of forwarding work, not the named access-restricting design pattern asked for.
