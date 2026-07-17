# Question 100

*UGC NET CS · 2018 Dec Paper 1 And 2 · Web Programming · CSS Alignment in HTML Table Cells*

Which of the following HTML5 codes will affect the horizontal as well as vertical alignment of the table content?

- **1.** <td halign="middle" valign="center"> BASH </td>
- **2.** <td align="middle" valign="center"> BASH </td>
- **3.** <td style="horizontal-align: center; vertical-align: middle;"> BASH </td>
- **4.** <td style="text-align: center; vertical-align: middle;"> BASH </td>

> [!TIP]
> **Correct answer: 4. <td style="text-align: center; vertical-align: middle;"> BASH </td>**

## Solution

For a table cell, CSS `text-align: center` controls the horizontal alignment of inline content, while `vertical-align: middle` controls its vertical alignment within the cell. Option 4 uses both valid CSS declarations in the style attribute, so it affects both directions.

## Key Points

- In HTML table cells, horizontal centering uses `text-align: center`; vertical centering uses `vertical-align: middle`.

## Why the other options are incorrect

`halign` is not an HTML attribute, and `horizontal-align` is not a CSS property, eliminating options 1 and 3. Option 2 uses obsolete presentational attributes and also supplies inappropriate values: horizontal `align` uses values such as center, whereas vertical alignment uses middle. Modern HTML5 uses the CSS declarations in option 4.
