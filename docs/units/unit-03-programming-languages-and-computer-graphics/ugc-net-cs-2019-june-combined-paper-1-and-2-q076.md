# Question 76

*UGC NET CS · 2019 June Paper 1 And 2 · Web Programming · XML well-formedness and validity*

Which statements are true? P: An XML document obeying XML syntax is well-formed. Q: An XML document validated against a DTD is both well-formed and valid. R: <xml version="1.0" encoding="UTF-8"> is a syntactically correct XML declaration.

- **1.** P and Q only
- **2.** P and R only
- **3.** Q and R only
- **4.** P, Q and R

> [!TIP]
> **Correct answer: 1. P and Q only**

## Solution

P is true because well-formedness means obeying XML's basic syntactic rules. Q is also true: validation against a DTD presupposes a well-formed document and confirms that its structure conforms to the declared grammar. R is false because an XML declaration must use the processing-instruction form <?xml version="1.0" encoding="UTF-8"?>, not an ordinary <xml ...> element.

## Key Points

- Well-formed XML follows XML syntax; valid XML is well-formed and also conforms to its DTD or schema.

## Why the other options are incorrect

Options 2–4 include R, whose declaration syntax is invalid. Option 3 also omits the true statement P.
