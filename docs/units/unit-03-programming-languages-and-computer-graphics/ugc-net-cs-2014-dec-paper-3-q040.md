# Question 40

*UGC NET CS · 2014 Dec Paper 3 · Web Programming · XML DOM Objects and Event Handlers*

The behaviour of the document elements in XML can be defined by

- **A.** Using document object
- **B.** Registering appropriate event handlers
- **C.** Using element object
- **D.** All of the above

> [!TIP]
> **Correct answer: D. All of the above**

## Solution

In a DOM-based scripted XML environment, the Document object represents the whole XML document and Element objects represent its individual elements. A program can locate or manipulate nodes through both kinds of object and define interactive behavior by registering suitable event handlers on them. Since A, B, and C describe complementary parts of the same approach, all of the above is correct.

## Key Points

- DOM exposes the document and its element nodes as objects; behavior is attached through event handlers.

## Why the other options are incorrect

A and C each mention only one DOM object level, while B mentions only the event-response mechanism. None alone captures all the facilities listed by the question. D includes document traversal, element manipulation, and event handling together.
