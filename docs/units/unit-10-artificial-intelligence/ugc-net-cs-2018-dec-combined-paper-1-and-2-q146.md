# Question 146

*UGC NET CS · 2018 Dec Paper 1 And 2 · Nondeterministic Search · AND-OR Search Trees*

Consider the following statements related to AND-OR Search algorithm. S1 A solution is a subtree that has a goal node at every leaf. S2 OR nodes are analogous to the branching in a deterministic environment. S3 AND nodes are analogous to the branching in a non-deterministic environment. Which one of the following is true referencing the above statements? Choose the correct answer from the code given below :

- **1.** S1 - False, S2 - True, S3 - True
- **2.** S1 - True, S2 - True, S3 - False
- **3.** S1 - True, S2 - True, S3 - True
- **4.** S1 - False, S2 - True, S3 - False

> [!TIP]
> **Correct answer: 3. S1 - True, S2 - True, S3 - True**

## Solution

In an AND-OR search tree, an OR node represents the agent choosing one action or branch; finding one successful alternative is enough. An AND node represents all possible outcomes of a nondeterministic action, so a contingent plan must handle every outcome. Consequently a solution is a subtree with a goal at every leaf. S1, S2 and S3 are all true, making option 3 correct.

## Key Points

- OR means choose one action; AND means cover every possible result of that action.

## Why the other options are incorrect

Options 1 and 4 wrongly make S1 false: a leaf that is not a goal would leave some contingency unsolved. Option 2 wrongly makes S3 false; AND branching is precisely what records the multiple outcomes that a nondeterministic environment may produce.
