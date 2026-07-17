# Question 98

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Web Programming · CSS cascading and overrides*

stOption 1D= 458921 PBT0:82048 Suppose that a corporate website appearance varies according to the department that owns various documents. All the documents need to follow the corporate look and feel. The HR department does not need a separate style sheet. It needs only the sheet containing the difference from the corporate sheet. Which of the following statements justify the above scenario? A. The styles sheets cannot stack on each other B. The style sheets can stack on each other C. The style sheets can override each other D. The style sheets cannot override each other Choose the most appropriate answer from the options given below:

- **1.** A, C Only
- **2.** B, C Only
- **3.** B, D only
- **4.** A, D only

> [!TIP]
> **Correct answer: 2. B, C Only**

## Solution

CSS is cascading: multiple sheets can stack, and later/more-specific rules can override inherited corporate rules. HR can therefore load the corporate sheet and a small department-specific override sheet. B and C are true.

## Key Points

- The CSS cascade combines style sources and resolves conflicts by origin, importance, specificity, and order.

## Why the other options are incorrect

A and D deny the two cascade behaviors the scenario relies on.
