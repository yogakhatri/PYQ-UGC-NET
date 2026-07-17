# Question 26

*UGC NET CS · 2010 June Paper 2 · Computer Networks · SNMP protocol data units*

The ______ field is the SNMP PDV reports an error in a response message.

- **A.** error index
- **B.** error status
- **C.** set request
- **D.** agent index

> [!TIP]
> **Correct answer: B. error status**

## Solution

An SNMP response PDU uses the error-status field to state whether an error occurred and what class it belongs to. If relevant, error-index identifies the variable binding associated with that error.

## Key Points

- error-status says what happened; error-index says where in the variable list.

## Why the other options are incorrect

Error-index locates an offending binding but does not itself report the error type. Set-request is a PDU operation, and agent-index is not the required response field.
