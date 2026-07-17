# Question 113

*UGC NET CS · 2020 Nov With Answers · Game Playing · Minimax and Alpha–Beta Pruning*

Which statements are true? (A) Minimax search is breadth-first and processes every node at one level before the next. (B) Alpha–beta pruning effectiveness depends strongly on the order in which states are examined. (C) Alpha–beta search computes the same optimal move as minimax. (D) Optimal play in imperfect-information games does not require reasoning about players’ current and future belief states.

- **1.** (A) and (C) only
- **2.** (A) and (D) only
- **3.** (B) and (C) only
- **4.** (C) and (D) only

> [!TIP]
> **Correct answer: 3. (B) and (C) only**

## Solution

Minimax values are normally computed by a depth-first recursive traversal, so A is false. Alpha–beta pruning discards branches that cannot affect the minimax choice; good move ordering produces early bounds and far more pruning, making B true. Pruning never changes the backed-up minimax value, so C is true. Imperfect-information play requires maintaining and predicting belief states about hidden information, making D false. Thus B and C only, option 3.

## Key Points

- Alpha–beta is an exact minimax optimization: ordering changes work saved, not the chosen optimal move.

## Why the other options are incorrect

Options 1 and 2 include the false breadth-first claim. Option 4 includes D, which denies the central role of belief-state reasoning in games with hidden information.
