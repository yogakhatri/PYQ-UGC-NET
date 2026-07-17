# Question 36

*UGC NET CS · 2015 Dec Paper 3 · Object-Oriented Programming · Abstract Classes and Interfaces*

Which of the following is/are correct with reference to Abstract class and interface ? (a) A class can inherit only one Abstract class but may inherit several interfaces. (b) An Abstract class can provide complete and default code but an interface has no code. Codes :

- **1.** (a) is true
- **2.** (b) is true
- **3.** Both (a) and (b) are true
- **4.** Neither (a) nor (b) is true

> [!TIP]
> **Correct answer: 3. Both (a) and (b) are true**

## Solution

Under the traditional Java-style model assumed by this question, a class extends at most one class—abstract or concrete—but may implement multiple interfaces, so (a) is true. An abstract class may contain fully implemented methods and default behavior, whereas the classic interface model supplies declarations without method bodies, so (b) is also true. The intended answer is both.

## Key Points

- Traditional contrast: single class inheritance with implementation versus multiple interface implementation contracts.

## Why the other options are incorrect

Options 1 and 2 accept only half of the traditional distinction, and option 4 rejects both. Modern Java interfaces can contain default, static, and private method implementations, so the blanket ‘interface has no code’ statement is historically dated; the answer reflects the model used by the paper.
