# Question 12

*UGC NET CS · 2011 Dec Paper 3 · Knowledge Representation · Predicate Logic and Resolution*

Consider the following piece of Knowledge: Mary, Micky and John ar e members of rotary club. Every rotary club member who is not a swimmer is a mountain climber. Mountain climber do not like rains. Any one who does not like water is not a swimmer. Micky dislikes whatever Mary likes and likes whateve r Mary dislikes. Mary likes rain and water. (a) Represent this Knowledge as predicate statement. (b) Answer the query. Is there a member of Rotary club who is not a mountain climber but a swimmer using resolution method. _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: The query is not entailed by the knowledge base**

## Solution

Use constants mary, micky, john, rain and water, and predicates Member(x), Swimmer(x), Climber(x), Likes(x,y) and Dislikes(x,y). A direct formalization is:

1. Member(mary), Member(micky), Member(john).
2. For all x, Member(x) AND NOT Swimmer(x) -> Climber(x).
3. For all x, Climber(x) -> Dislikes(x,rain).
4. For all x, Dislikes(x,water) -> NOT Swimmer(x).
5. For all y, Likes(mary,y) -> Dislikes(micky,y).
6. For all y, Dislikes(mary,y) -> Likes(micky,y).
7. Likes(mary,rain), Likes(mary,water).

From 5 and 7, Micky dislikes rain and water. Rule 4 gives NOT Swimmer(micky), and with Member(micky), rule 2 gives Climber(micky). For Mary, liking water does not imply Swimmer(mary); implication 4 cannot be reversed. Nothing establishes whether John swims or climbs.

The query is EXISTS x [Member(x) AND NOT Climber(x) AND Swimmer(x)]. Resolution can prove it only if some constant has all three required literals. No Swimmer literal can be derived for any person, and no rule derives NOT Climber. Consequently the query is not a logical consequence of the facts. Under open-world semantics this means 'unknown/not provable', not that its negation has been proved.

## Key Points

- Resolution proves entailment from explicit clauses; it does not license contraposition of one-way rules in an ad hoc forward chain or assume missing facts are false.

## Common mistakes to avoid

Do not use the invalid converse 'likes water -> swimmer' from 'dislikes water -> not swimmer'. Do not treat absence of Climber(x) as proof of NOT Climber(x) unless a closed-world assumption is explicitly introduced.
