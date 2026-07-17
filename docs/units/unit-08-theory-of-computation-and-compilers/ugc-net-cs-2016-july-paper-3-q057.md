# Question 57

*UGC NET CS · 2016 July Paper 3 · Turing Machines · Transition Tracing and Accepted Language*

Given a Turing Machine M = ({q0, q1, q2, q3}, {a, b}, {a, b, B}, δ, B, {q3}) Where δ is a transition function defined as δ(q0, a) = (q1, a, R) δ(q1, b) = (q2, b, R) δ(q2, a) = (q2, a, R) δ(q2, b) = (q3, b, R) The language L(M) accepted by the Turing Machine is given as :

- **1.** aa*b
- **2.** abab
- **3.** aba*b
- **4.** aba*

> [!TIP]
> **Correct answer: 3. aba*b**

## Solution

Trace the defined transitions from q0. The first symbol must be a, taking the machine to q1. The next must be b, taking it to q2. In q2 the machine may read zero or more a symbols, and the next b takes it to accepting state q3. Under the end-of-input convention intended by the choices, the accepted pattern is therefore ab a* b, written aba*b. This is option 3.

## Key Points

- Convert a transition trace into a regular pattern: forced symbols become literals and a self-loop becomes a Kleene star.

## Why the other options are incorrect

aa*b fails because q1 has a transition only on b. The single string abab is merely one member of aba*b, not the whole pattern. aba* never performs the final b-transition into q3, so it does not reach the accepting state.

## Additional Information

Formal caveat: in the usual 'accept immediately upon entering q3' Turing-machine semantics, unread suffix symbols would also be allowed, giving aba*b{a,b}*. The exam options implicitly require the transition to q3 on the last input symbol; option 3 is the intended answer under that convention.
