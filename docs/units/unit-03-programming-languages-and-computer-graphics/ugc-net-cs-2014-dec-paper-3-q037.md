# Question 37

*UGC NET CS · 2014 Dec Paper 3 · Object-Oriented Programming · Synchronized Methods in Java*

Which methods are used to control access to an object in multithreaded programming?

- **A.** Asynchronized methods
- **B.** Synchronized methods
- **C.** Serialized methods
- **D.** None of the above

> [!TIP]
> **Correct answer: B. Synchronized methods**

## Solution

A synchronized method associates entry with an object's monitor lock (or the class monitor for a static method). Only a thread holding the relevant monitor may execute the protected synchronized region, so competing threads wait and shared object state is not concurrently modified through that region. Therefore synchronized methods control multithreaded access.

## Key Points

- Synchronization controls concurrent entry through a monitor; serialization controls representation for storage or transmission.

## Why the other options are incorrect

'Asynchronized methods' is not the locking construct and generally suggests the absence of synchronization. Serialization converts object state to a storable/transmittable form; it does not provide mutual exclusion. Since B names the actual concurrency mechanism, 'none' is false.
