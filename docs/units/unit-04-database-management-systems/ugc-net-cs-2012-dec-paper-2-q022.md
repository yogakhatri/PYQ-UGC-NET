# Question 22

*UGC NET CS · 2012 Dec Paper 2 · Network Database Model · CODASYL Set Retention and RECONNECT*

In DML, the RECONNECT command cannot be used with:

- **1.** OPTIONAL set
- **2.** FIXED set
- **3.** MANDATORY set
- **4.** All of the above

> [!TIP]
> **Correct answer: 2. FIXED set**

## Solution

In the CODASYL network model, a FIXED retention constraint permanently associates a member record with the set occurrence into which it is inserted. Because the membership cannot be changed to another owner, the DML RECONNECT operation is not permitted for a FIXED set.

## Key Points

- CODASYL retention: OPTIONAL can detach, MANDATORY can reconnect, FIXED cannot change set occurrence.

## Why the other options are incorrect

An OPTIONAL member may exist without set membership and can be connected or disconnected as required. A MANDATORY member must remain in some set occurrence, so RECONNECT is precisely the one-step operation used to move it from one occurrence to another without leaving it unattached. Therefore the restriction is not common to all three.
