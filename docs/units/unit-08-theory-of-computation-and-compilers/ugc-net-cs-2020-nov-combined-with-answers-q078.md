# Question 78

*UGC NET CS · 2020 Nov With Answers · Regular Language Models · Regular-Expression Equivalence*

Let L1 and L2 be languages over Sigma={a,b}, represented by the regular expressions (a*+b)* and (a+b)*, respectively. Which statement is true?

- **1.** L1 is a proper subset of L2
- **2.** L2 is a proper subset of L1
- **3.** L1 = L2
- **4.** L1 intersection L2 is empty

> [!TIP]
> **Correct answer: 3. L1 = L2**

## Solution

L2=(a+b)* is all strings over {a,b}. In L1=(a*+b)*, each repeated unit is either a string of zero or more a's or the single symbol b. Any word over {a,b} can be split into individual symbols: choose a from a* for each a and choose b for each b. Conversely, L1 can generate no symbols outside {a,b}. Hence both languages equal {a,b}*, so L1=L2, option 3.

## Key Points

- Show two inclusions: every L1 token is over {a,b}, and every {a,b} word can be tokenized using a from a* or b.

## Why the other options are incorrect

Neither language is a proper subset of the other, and their intersection is certainly not empty—it contains ε and every binary word. The ε alternative inside a* does not restrict the language.
