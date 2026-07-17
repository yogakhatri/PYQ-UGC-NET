# Question 42

*UGC NET CS · 2014 Dec Paper 3 · Web Programming · Java Applet Lifecycle*

Which method is called first by an applet program ?

- **A.** start( )
- **B.** run( )
- **C.** init( )
- **D.** begin( )

> [!TIP]
> **Correct answer: C. init( )**

## Solution

When a Java applet is loaded, the environment invokes `init()` once to perform initialization. It then calls `start()` when the applet becomes active; `start()` may be called again after a stop. `paint()` handles display, while `stop()` and `destroy()` occur later in the lifecycle. Thus `init()` is first among the listed methods.

## Key Points

- Applet lifecycle begins with one-time `init()`, then activation through `start()`.

## Why the other options are incorrect

`start()` follows `init()`. `run()` is associated with a thread's execution and is not the first applet lifecycle callback. `begin()` is not a standard applet lifecycle method. Option C alone matches the lifecycle order.
