# Question 29

*UGC NET CS · 2021 Nov With Answers · Algebraic Structures · Semigroups with No Distinct Commuting Elements*

Let (X,*) be a semigroup such that for all a,b∈X, a≠b implies a*b≠b*a. Which identities follow? A. a*a=a for every a∈X. B. (a*b)*a=a for every a,b∈X. C. (a*b)*c=a*c for every a,b,c∈X.

- **1.** A and B only
- **2.** A and C only
- **3.** B and C only
- **4.** A, B and C

> [!TIP]
> **Correct answer: 4. A, B and C**

## Solution

The hypothesis is equivalent to saying that commuting elements must be equal. First, a and a² commute because a·a²=a³=a²·a; hence a=a², proving A. Next, aba commutes with a: (aba)a=aba and a(aba)=aba using a²=a, so aba=a, proving B. Finally compare abc and ac. Using B, cac=c and aca=a; therefore (abc)(ac)=ab(cac)=abc and (ac)(abc)=(aca)bc=abc. They commute, so abc=ac, proving C. All three identities follow: option 4.

## Key Points

- No two distinct elements commute forces an idempotent rectangular-band structure: a²=a, aba=a, and abc=ac.

## Why the other options are incorrect

Options 1–3 omit at least one consequence. The key is not to assume commutativity globally; instead construct pairs that associativity and the derived identities force to commute, then apply the contrapositive of the hypothesis.
