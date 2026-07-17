# Question 127

*UGC NET CS · 2020 Nov With Answers · Software Design · Cohesion Strength Ordering*

Arrange these types of cohesion from best to worst: A. Logical cohesion; B. Sequential cohesion; C. Communication cohesion; D. Temporal cohesion; E. Procedural cohesion.

- **1.** A-D-E-C-B
- **2.** A-E-D-C-B
- **3.** B-E-C-D-A
- **4.** B-C-E-D-A

> [!TIP]
> **Correct answer: 4. B-C-E-D-A**

## Solution

Cohesion is stronger when a module's elements contribute to one focused purpose. Sequential cohesion is strongest here because one activity's output becomes the next activity's input. Communicational cohesion follows because the activities operate on the same data. Procedural cohesion merely groups steps that must follow a control sequence; temporal cohesion groups activities executed at the same time, such as initialization; logical cohesion groups activities only because they belong to the same broad category. Thus B > C > E > D > A, which is option 4.

## Key Points

- For these five types, remember: sequential > communicational > procedural > temporal > logical.

## Why the other options are incorrect

Options 1 and 2 put logical cohesion first even though it is weak. Option 3 places procedural cohesion above communicational cohesion, although sharing data creates a tighter relationship than sharing only an execution order.
