# Question 15

*UGC NET CS · 2011 Dec Paper 3 · Memory Hierarchy · Set-Associative Cache Address Fields*

An eight way set associative cache consists of a total of 256 B locks. The main memory contains 8192 blocks, each consisting of 128 words. (a) How many bits are there in the main memory address ? (b) How many bits are there in TAG, SET and WORD fields ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ ______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: 20 address bits: TAG=8, SET=5, WORD=7**

## Solution

Main memory has 8192=2^13 blocks and each block has 128=2^7 words, so it contains 2^20 word-addressable locations. A main-memory word address therefore needs 20 bits.

The cache contains 256 blocks and is eight-way set associative. Number of sets=256/8=32=2^5, so the SET field uses 5 bits. A block contains 128 words, so the WORD (block-offset) field uses 7 bits. The remaining bits form the tag:

TAG=20-SET-WORD=20-5-7=8 bits.

Address format is [8-bit TAG | 5-bit SET | 7-bit WORD]. The set selects one of 32 sets, the eight stored tags are compared in parallel, and the word field selects a word from the matching 128-word block.

## Key Points

- Sets=cache blocks/ways; offset=log2(words per block); tag=total address bits-set bits-offset bits.

## Common mistakes to avoid

Using 8 set bits confuses cache blocks with sets; eight-way associativity groups eight blocks per set. Omitting the 7-bit word offset incorrectly treats every block as one addressable word.
