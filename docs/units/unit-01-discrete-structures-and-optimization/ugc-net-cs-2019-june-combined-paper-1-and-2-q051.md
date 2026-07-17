# Question 51

*UGC NET CS · 2019 June Paper 1 And 2 · Sets and Relations · Partial Ordering*

Consider the poset ({3, 5, 9, 15, 24, 45}, |), where | denotes divisibility. Which statement is correct?

- **1.** There exists a greatest element and a least element
- **2.** There exists a greatest element but not a least element
- **3.** There exists a least element but not a greatest element
- **4.** There does not exist a greatest element and a least element

> [!TIP]
> **Correct answer: 4. There does not exist a greatest element and a least element**

## Solution

A least element must divide every element of the set. Although 3 divides 3, 9, 15, 24 and 45, it does not divide 5; similarly, no other listed number divides all six elements. A greatest element must be divisible by every element of the set. Neither 24 nor 45 is divisible by all the others, and no remaining element can be greatest. Therefore the poset has neither a least element nor a greatest element.

## Key Points

- In a divisibility poset, a least element divides every member and a greatest element is divisible by every member.

## Why the other options are incorrect

- **Option 1:** fails because neither required element exists.
- **Option 2:** incorrectly claims a greatest element.
- **Option 3:** incorrectly treats one of the minimal elements as a least element. Minimal and least are not the same.

## Additional Information

The set has more than one minimal element, including 3 and 5. A poset may have several minimal elements while having no single least element.
