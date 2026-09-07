import heapq as hq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merge_ready_queue = []
        for idx, lp in enumerate([_list for _list in lists if _list]):
            hq.heappush(merge_ready_queue, (lp.val, idx, lp))

        dummy = ListNode()
        tail = dummy
        while merge_ready_queue:
            _, idx, lp = hq.heappop(merge_ready_queue)
            tail.next = lp
            tail = tail.next

            if not lp.next:
                continue

            hq.heappush(merge_ready_queue, (lp.next.val, idx, lp.next))

        return dummy.next
