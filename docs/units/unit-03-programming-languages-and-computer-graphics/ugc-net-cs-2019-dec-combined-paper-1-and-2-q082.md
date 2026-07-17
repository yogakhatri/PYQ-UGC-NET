# Question 82

*UGC NET CS · 2019 Dec Paper 1 And 2 · Java Programming · JVM Execution Components*

Java Virtual Machine (JVM) is used to execute architectural neutral byte code. Which of the following is needed by the JVM for execution of Java Code?

- **1.** Class loader only
- **2.** Class loader and Java Interpreter
- **3.** Class loader, Java Interpreter and API
- **4.** Java Interpreter only

> [!TIP]
> **Correct answer: 2. Class loader and Java Interpreter**

## Solution

Before bytecode can run, a class loader must locate and load the class representation into the JVM. The execution engine—represented in these options by the Java interpreter—then executes its bytecode instructions. Hence the required pair is class loader and Java interpreter, option 2. The Java API is a library that an application may call; it is not the engine required merely to load and execute arbitrary bytecode.

## Key Points

- Loading makes bytecode available; the interpreter/execution engine runs it.
- Libraries are program dependencies, not the execution engine itself.

## Why the other options are incorrect

A class loader alone does not execute instructions, eliminating option 1. An interpreter alone has no loaded class to execute, eliminating option 4. Option 3 adds the API even though a minimal bytecode class need not invoke general API libraries and the API is not the JVM execution mechanism.

## References

- [Oracle JVM components: Interpreter and Class Loader](https://docs.oracle.com/en/database/oracle/oracle-database/26/jjdev/Oracle-JVM-components.html)
