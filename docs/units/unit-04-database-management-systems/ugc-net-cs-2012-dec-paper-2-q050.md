# Question 50

*UGC NET CS · 2012 Dec Paper 2 · SQL · Self-Joins for Distinct Pairs*

Given relation POSITION(Posting-No, Skill), which query retrieves all distinct pairs of posting numbers requiring the same skill?

- **1.** SELECT p.posting_No, p.posting_No FROM position p WHERE p.skill=p.skill AND p.posting_No<p.posting_No
- **2.** SELECT p1.posting_No, p2.posting_No FROM position p1, position p2 WHERE p1.skill=p2.skill
- **3.** SELECT p1.posting_No, p2.posting_No FROM position p1, position p2 WHERE p1.skill=p2.skill AND p1.posting_No<p2.posting_No
- **4.** SELECT p1.posting_No, p2.posting_No FROM position p1, position p2 WHERE p1.skill=p2.skill AND p1.posting_No=p2.posting_No

> [!TIP]
> **Correct answer: 3. SELECT p1.posting_No, p2.posting_No FROM position p1, position p2 WHERE p1.skill=p2.skill AND p1.posting_No<p2.posting_No**

## Solution

The relation must be joined with itself: p1 and p2 represent two posting rows. The predicate p1.skill=p2.skill keeps pairs requiring the same skill. The additional condition p1.posting_No<p2.posting_No removes self-pairs and keeps only one orientation of each pair, so (10,20) appears without the duplicate reverse pair (20,10). This is exactly query 3.

## Key Points

- To find unordered distinct pairs with a self-join, match the shared attribute and impose p1.key < p2.key.

## Why the other options are incorrect

Query 1 compares each row with itself and also requires a posting number to be less than itself, so it returns nothing. Query 2 includes self-pairs and both orientations of each pair. Query 4 deliberately selects only equal posting numbers, not distinct pairs.
