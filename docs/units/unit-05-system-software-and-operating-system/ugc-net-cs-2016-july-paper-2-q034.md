# Question 34

*UGC NET CS · 2016 July Paper 2 · Linking and Loading · Benefits and Costs of Dynamic Linking*

Which of the following is not typically a benefit of dynamic linking ? I. Reduction in overall program execution time. II. Reduction in overall space consumption in memory. III. Reduction in overall space consumption on disk. IV. Reduction in the cost of software updates.

- **1.** I and IV
- **2.** I only
- **3.** II and III
- **4.** IV only

> [!TIP]
> **Correct answer: 2. I only**

## Solution

Dynamic linking lets multiple programs use one shared library instead of embedding a private copy in every executable. It can therefore reduce memory use (II) and disk use (III). Updating a compatible shared library can also update many programs without relinking each one, reducing update cost (IV). It does not typically reduce program execution time; resolving symbols at load time or first use can add overhead. Hence only statement I is not a typical benefit.

## Key Points

- Dynamic linking primarily saves shared-library copies and eases updates; faster execution is not its standard advantage.

## Why the other options are incorrect

Options 1 and 4 wrongly treat cheaper software updates as a non-benefit. Option 3 selects two genuine benefits—memory and disk savings—rather than the requested non-benefit.
