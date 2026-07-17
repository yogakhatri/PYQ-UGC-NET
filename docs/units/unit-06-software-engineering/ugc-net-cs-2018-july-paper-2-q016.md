# Question 16

*UGC NET CS · 2018 July Paper 2 · Software Design · Data, Stamp, Control and Common Coupling*

Which statements about module coupling are correct? P: Common coupling occurs when one module controls another's flow by passing information on what to do. Q: In data coupling, a complete data structure is passed through parameters. R: Stamp coupling occurs when modules share a composite data structure and use only parts of it.

- **1.** P and Q only
- **2.** P and R only
- **3.** Q and R only
- **4.** All of P, Q and R

> [!TIP]
> **Correct answer: No valid option: only statement R is correct, but no choice lists R alone.**

## Solution

P is false because passing information that directs another module's logic is control coupling, not common coupling; common coupling means sharing global data. Q is false because passing an entire composite structure when only part is needed is stamp coupling; data coupling passes only the simple data items required. R correctly defines stamp coupling. The true set is therefore {R}, absent from the options.

## Key Points

- Data coupling passes needed values; stamp coupling passes a composite record; control coupling passes decision/control information; common coupling shares global data.

## Why the other options are incorrect

Every listed option includes P or Q, and both are mislabeled definitions. The item appears to have shifted the names: P describes control coupling and Q describes stamp coupling, while R already correctly describes stamp coupling.
