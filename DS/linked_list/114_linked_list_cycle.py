# https: // leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return False

        fast_pointer = head.next.next
        slow_pointer = head.next
        while (fast_pointer != None and fast_pointer != slow_pointer):
            fast_pointer = fast_pointer.next
            if fast_pointer == None:
                return False
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
        return True
