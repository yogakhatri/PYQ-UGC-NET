# Question 18

*UGC NET CS · 2011 Dec Paper 3 · Data Structures · Hash Collision Resolution*

What are the types of collision resolution techniques and the method used in each of these types ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ ______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: Use separate chaining or open addressing; open addressing includes linear probing, quadratic probing and double hashing**

## Solution

A collision occurs when different keys map to the same table position. The main resolution families are:

**Separate chaining (open hashing):** Each table slot points to a bucket or linked/dynamic collection of all records hashing there. Insert into the chain; search and deletion examine that chain. With load factor alpha=n/m, expected time is O(1+alpha) under uniform hashing, and alpha may exceed 1.

**Open addressing (closed hashing):** Every record stays in the table. On collision follow a probe sequence until the key or an empty slot is found. Linear probing uses h(k,i)=(h(k)+i) mod m and suffers primary clustering. Quadratic probing uses h(k,i)=(h(k)+c1 i+c2 i^2) mod m and reduces primary clustering but may not visit every slot without suitable constants/table size. Double hashing uses h(k,i)=(h1(k)+i h2(k)) mod m and approximates independent probes when h2 is relatively prime to m. Deletion uses tombstones so probe chains are not broken, and load factor must stay below 1.

Other variants include fixed overflow buckets, coalesced hashing (in-table chains), cuckoo hashing (move keys among alternative positions) and rehashing/resizing when load grows. The hash function and table-size choice remain essential.

## Key Points

- Chaining stores colliding keys in per-slot collections; open addressing keeps all keys in the table and searches a deterministic probe sequence.

## Common mistakes to avoid

Simply overwriting the occupied slot loses a record. Marking an open-addressed deletion as never-used can make later keys unreachable. Linear probing is simple but should not be described as free from clustering.
