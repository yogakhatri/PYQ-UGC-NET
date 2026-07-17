# Question 41

*UGC NET CS · 2017 Jan Paper 3 · Web Programming · CSS Vertical Alignment in HTML Tables*

Which of the following HTML code will affect the vertical alignment of the table content ?

- **1.** <td style = “vertical-align : middle”> Text Here </td>
- **2.** <td valign = “centre”> Text Here </td>
- **3.** <td style = “text-align : center”> Text Here </td>
- **4.** <td align = “middle”> Text Here </td>

> [!TIP]
> **Correct answer: 1. <td style = “vertical-align : middle”> Text Here </td>**

## Solution

The CSS declaration `vertical-align: middle` applies vertical alignment to a table cell, so option 1 directly affects the vertical position of its content. It is also the standards-oriented approach compared with obsolete presentational table attributes.

## Key Points

- In table cells, CSS `vertical-align` controls vertical placement; `text-align` controls horizontal placement.

## Why the other options are incorrect

`text-align:center` controls horizontal alignment. The old `valign` attribute expects a value such as `middle`, not `centre`, and is obsolete in modern HTML. The `align` attribute is horizontal and `middle` is not the appropriate value there.
