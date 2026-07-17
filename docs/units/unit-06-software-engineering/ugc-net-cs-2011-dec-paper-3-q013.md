# Question 13

*UGC NET CS · 2011 Dec Paper 3 · Software Process Models · Iterative Waterfall and Spiral Models*

Compare the relative advantages of using the iterative waterf all model and the spiral model of software development. Explain with the help of few suitable examples, the types of problem for which you would adopt above models. _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: Iterative waterfall suits largely understood work with controlled feedback; spiral suits large, novel or high-risk work**

## Solution

The iterative waterfall model retains recognizable sequential phases—requirements, design, implementation and testing—but permits feedback to an earlier phase when a defect or misunderstanding is found. It is simple to plan, creates clear documents and milestones, and works well when the domain and architecture are familiar. Its weakness is that usable software and major risk discovery may still occur late, and repeated backward movement can be expensive.

The spiral model organizes development into repeated risk-driven cycles. Each cycle (1) sets objectives and alternatives, (2) identifies and reduces the most important risks, often with prototypes, simulations or experiments, (3) develops and verifies the next-level product, and (4) plans the following cycle with stakeholder review. It handles changing requirements, new technology and costly failure better, but requires risk-analysis expertise and more management effort.

Choose iterative waterfall for a payroll upgrade, examination-record system or migration whose requirements and technology are stable but where reviews may require limited rework. Choose spiral for air-traffic control, medical-device software, a new distributed platform or a product using unproven hardware, because safety, performance, usability or feasibility risks must be attacked early. For a small low-risk application, spiral overhead is usually unjustified.

## Key Points

- Model selection follows uncertainty and risk: controlled phase feedback for understood work, risk-driven prototyping and evolution for uncertain high-stakes work.

## Common mistakes to avoid

Do not describe iterative waterfall as unrestricted agile iteration; it still uses phase-oriented planning. Do not describe spiral as merely repeated waterfall—the defining activity is explicit risk analysis and mitigation in every loop.
