# Question 8

*UGC NET CS · 2017 Jan Paper 2 · Digital Logic Circuits and Components · Registers and Counters*

A binary 3-bit down counter uses J-K flip-flops FFᵢ with inputs Jᵢ,Kᵢ and outputs Qᵢ for i=0,1,2. Choose the correct minimized input expressions: I. J₀=K₀=0; II. J₀=K₀=1; III. J₁=K₁=Q₀; IV. J₁=K₁=Q̅₀; V. J₂=K₂=Q₁Q₀; VI. J₂=K₂=Q̅₁Q̅₀.

- **1.** I, III, V
- **2.** I, IV, VI
- **3.** II, III, V
- **4.** II, IV, VI

> [!TIP]
> **Correct answer: 4. II, IV, VI**

## Solution

A J-K flip-flop toggles when J=K=1. In a synchronous binary down counter, the least-significant bit Q₀ toggles on every clock, so J₀=K₀=1 (II). Q₁ toggles when the lower bit is 0, giving J₁=K₁=Q̅₀ (IV). Q₂ toggles when both lower bits are 0, giving J₂=K₂=Q̅₁Q̅₀ (VI). Thus II, IV, and VI are correct, which is option 4.

## Key Points

- Synchronous up counter: toggle on all lower 1s; synchronous down counter: toggle on all lower 0s.

## Why the other options are incorrect

I would freeze Q₀ instead of toggling it. III and V are the enabling conditions used for an up counter, where a higher bit toggles when all lower bits are 1. A down counter uses the complemented lower bits.
