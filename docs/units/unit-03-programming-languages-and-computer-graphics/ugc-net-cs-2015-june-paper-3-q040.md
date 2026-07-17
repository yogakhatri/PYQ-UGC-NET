# Question 40

*UGC NET CS · 2015 June Paper 3 · Web Programming · XML DTD Occurrence Indicators*

In XML we can specify the frequency of an element by using the symbols :

- **1.** + * !
- **2.** # * !
- **3.** + * ?
- **4.** − * ?

> [!TIP]
> **Correct answer: 3. + * ?**

## Solution

XML DTD content models use three occurrence indicators: `?` means zero or one occurrence, `*` means zero or more, and `+` means one or more. Therefore the complete set is `+`, `*`, and `?`, as shown in option 3.

## Key Points

- DTD frequency operators mirror regular expressions: `?` optional, `*` any count, `+` one or more.

## Why the other options are incorrect

`!` and `#` appear in other XML declaration syntax but are not the three repetition suffixes. A minus sign is not a DTD occurrence indicator either, eliminating options 1, 2, and 4.
