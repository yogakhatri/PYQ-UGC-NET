# Question 19

*UGC NET CS · 2011 Dec Paper 3 · Memory Management · Combined Segmentation and Paging*

Why are segmentation and paging sometimes combined into one scheme ? _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ ______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ ____________


> [!TIP]
> **Correct answer: Segmentation supplies the logical protection/sharing view; paging supplies fixed-size physical allocation without external fragmentation**

## Solution

Segmentation divides a process into meaningful variable-size units such as code, stack, heap or modules. Each segment has its own base, limit and protection/sharing rights, which matches the programmer's logical view. Its physical allocation is difficult, however: variable-size segments create external fragmentation and may require compaction.

Paging divides virtual memory and physical memory into equal-size pages and frames. Any page can occupy any free frame, so allocation is simple and external fragmentation disappears. Paging alone provides a flat page-number view and does not naturally express module-level bounds, sharing or protection.

A combined system divides each segment into pages. A logical address is (segment number, page number within segment, offset). The segment-table entry checks the segment boundary and permissions and locates that segment's page table; the page-table entry maps the page to a physical frame. Thus code/data segments can be protected and shared independently, while their pages can be placed noncontiguously and demand-paged.

Costs include two-level translation, extra tables and internal fragmentation in the last page of a segment. TLBs and multilevel/inverted page-table techniques reduce overhead.

## Key Points

- Segment for logical organization and protection; page each segment for efficient noncontiguous physical-memory management.

## Common mistakes to avoid

Saying the combination removes all fragmentation is wrong: it removes segment-level external fragmentation but retains page-level internal fragmentation. Paging does not preserve contiguous physical placement of a segment, nor does it remove the need for segment bounds and permissions.
