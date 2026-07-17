# Question 42

*UGC NET CS · 2017 Jan Paper 3 · Web Programming · XML, CSS, and JavaScript Conformance Rules*

What can you say about the following statements ? I. XML tags are case-insensitive. II. In JavaScript, identifier names are case-sensitive. III. Cascading Style Sheets (CSS) cannot be used with XML. IV. All well-formed XML documents must contain a document type definition.

- **1.** only I and II are false.
- **2.** only III and IV are false.
- **3.** only I and III are false.
- **4.** only II and IV are false.

> [!TIP]
> **Correct answer: No valid option: statements I, III, and IV are false; only II is true.**

## Solution

XML element and attribute names are case-sensitive, so I is false. JavaScript identifiers are case-sensitive, so II is true. CSS can be associated with and used to present XML documents, so III is false. A document can be well-formed without a DTD; a DTD is relevant to validation, which is a stronger and separate condition, so IV is false. The false set is {I,III,IV}, which none of the four choices gives.

## Key Points

- Well-formed XML obeys XML syntax; valid XML additionally conforms to a declared grammar such as a DTD.
- Styling XML with CSS is explicitly supported.

## Why the other options are incorrect

Option 3 is probably the intended key because it identifies I and III, but it wrongly leaves IV as true. Options 1, 2, and 4 also misclassify at least one clear statement. Standards-correct study material should not force any listed option here.

## References

- [W3C XML 1.0 (Fifth Edition)](https://www.w3.org/TR/xml/)
- [W3C — Associating Style Sheets with XML Documents](https://www.w3.org/TR/xml-stylesheet/)
