# Question 83

*UGC NET CS · 2019 Dec Paper 1 And 2 · Object-Oriented Analysis and Design · Sequence-Diagram Lifelines and Messages*

A restaurant-order scenario is: the customer reads the menu, places an order, the order is sent to the kitchen, food is served, the customer requests a bill, the bill is prepared and delivered, and the customer pays. At least how many interacting objects/roles are needed as lifelines in a sequence diagram for this scenario?

- **1.** 3
- **2.** 4
- **3.** 5
- **4.** 6

> [!TIP]
> **Correct answer: 3. 5**

## Solution

A sequence-diagram lifeline represents one participant in the interaction. The scenario needs five distinct participating roles at minimum: the customer, the order-taking/front-of-house role, the kitchen or cook, the serving role, and the billing/cashier role. Messages such as place order, send to kitchen, serve items, request/prepare/deliver bill, and pay connect these five lifelines. Therefore the minimum is 5, option 3.

## Key Points

- Count active interaction participants, not every noun or data object mentioned in the narrative.

## Why the other options are incorrect

Three or four lifelines would force distinct responsibilities named by the scenario—order handling, preparation, serving, and billing—into too few participants and would not show the required handoffs. Six is possible in a more detailed design, but the question asks for the minimum; menu/order data can be message payloads rather than separate active lifelines.

## References

- [OMG UML issue clarification: a lifeline represents an interaction participant such as a class or actor instance](https://issues.omg.org/issues/UML25-404)
