# Question 17

*UGC NET CS · 2011 Dec Paper 3 · Software Design · Cohesion and Coupling*

How would you improve a software design that displays very low cohesion and high coupling ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ ______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: Refactor responsibilities into cohesive modules and reduce dependencies through small stable interfaces and information hiding**

## Solution

Low cohesion means a module contains unrelated responsibilities; high coupling means modules know too much about each other's data or implementation. Start by measuring change reasons and dependencies, then refactor in small tested steps:

1. Split 'god' modules by one responsibility or coherent domain capability. Move each behaviour beside the data it owns.
2. Encapsulate internal state; remove shared globals and direct field access. Expose intention-revealing operations rather than raw representation.
3. Define small, stable interfaces and pass only required data. Replace long parameter lists and control flags with focused abstractions.
4. Invert unstable dependencies: depend on interfaces, inject collaborators, and isolate databases, UI, network and third-party services behind adapters.
5. Remove cyclic dependencies. Place genuinely shared abstractions in a lower layer, or use events/callbacks where one-way notification is appropriate.
6. Eliminate duplicated logic and unrelated utility dumping grounds, but avoid creating a universal shared module that everything depends on.
7. Protect behaviour with unit and integration tests; monitor coupling, cohesion, fan-in/fan-out and change history after each refactor.

The target is functional cohesion inside a module and data/message coupling across clear boundaries—not zero coupling, which is neither possible nor desirable.

## Key Points

- Put things that change for the same reason together; hide them from things that change for different reasons.

## Common mistakes to avoid

Merging modules may reduce the number of links while making cohesion worse. Adding a global helper or shared database creates hidden coupling. Interfaces alone do not help if they expose another module's internal data model or become overly broad.
