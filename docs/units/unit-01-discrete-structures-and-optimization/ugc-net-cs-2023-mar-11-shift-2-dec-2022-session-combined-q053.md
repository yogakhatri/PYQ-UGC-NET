# Question 53

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Graph Theory · Degree-sequence handshake puzzles*

Suppose you are married and you and your partner attend a party with three other married couples. Several handshakes took place. No one shook hands with himself (or herself or with their partner, and no one shook hands with the same person more than once. After all hand shaking was completed, suppose you asked each person, including your partner, how many hands they had shaken. Each person gave a different answer. How many hands did your spouse shake?

- **1.** 1
- **2.** 2
- **3.** 3
- **4.** 4

> [!TIP]
> **Correct answer: 3. 3**

## Solution

There are eight people (four couples). The seven people other than the questioner give seven distinct feasible handshake counts, so their answers must be 0,1,2,3,4,5,6. The person reporting 6 shook everyone except their spouse, so that spouse must be the person reporting 0. Remove that couple. The same pairing argument then matches 5 with 1 and 4 with 2. The only unpaired answer is 3, and it must belong to the questioner’s spouse.

## Key Points

- In the couples-handshake puzzle with n couples, the distinct answers pair as 0 with 2n−2, 1 with 2n−3, and so on; the questioner’s spouse has n−1 handshakes.

## Why the other options are incorrect

Counts 1, 2, and 4 are forced into complementary spouse-pairs (5,1) and (4,2). None can be the questioner’s spouse because their complementary partner is also among the seven respondents.
