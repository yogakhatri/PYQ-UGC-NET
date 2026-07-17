# Question 27

*UGC NET CS · 2010 June Paper 2 · World Wide Web · DNS and Resolution*

What does the URL need to access documents ? I. Path name II. Host name III. DNS IV. Retrieval method V. Server port number

- **A.** I, II, III
- **B.** I, III, V
- **C.** I, II, IV
- **D.** III, IV, V

> [!TIP]
> **Correct answer: C. I, II, IV**

## Solution

A URL identifies the retrieval scheme/method (such as http), the host name, and the path to the document. A port may be included but can be omitted when the scheme's default applies. DNS is a resolution service used to map the host; it is not a component that must appear in the URL. Thus I,II,IV.

## Key Points

- URL structure is scheme://host[:port]/path; DNS operates behind the name.

## Why the other options are incorrect

Options A and B include DNS as a URL component, while D omits the host/path and includes optional or external mechanisms.
