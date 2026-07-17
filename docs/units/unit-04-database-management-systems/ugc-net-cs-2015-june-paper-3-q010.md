# Question 10

*UGC NET CS · 2015 June Paper 3 · Relational Database Design · Second Normal Form and Partial Dependencies*

The Relation Vendor Order (V_no, V_ord_no, V_name, Qty_sup, unit_price) is in 2NF because :

- **1.** Non_key attribute V_name is dependent on V_no which is part of composite key
- **2.** Non_key attribute V_name is dependent on Qty_sup
- **3.** Key attribute Qty_sup is dependent on primary_key unit price
- **4.** Key attribute V_ord_no is dependent on primary_key unit price

> [!TIP]
> **Correct answer: The relation is not in 2NF; option 1 states the partial dependency that violates 2NF. The printed stem appears to have omitted the word 'not'.**

## Solution

With composite key `(V_no, V_ord_no)`, the vendor name depends on `V_no` alone: `V_no → V_name`. Because `V_name` is non-prime and depends on only a proper subset of the composite key, this is a partial functional dependency. A relation with such a dependency is in 1NF but not 2NF. Thus option 1 identifies the defect, despite the stem saying `is in 2NF`.

## Key Points

- 2NF removes dependencies of non-prime attributes on a proper subset of a candidate key.

## Why the other options are incorrect

Option 2 asserts an implausible dependency from supplied quantity to vendor name. Options 3 and 4 mislabel attributes and dependencies: quantity and order number are not determined by unit price in the stated schema. None explains that the relation is in 2NF, so the stem and choices are inconsistent unless `not` is restored.
