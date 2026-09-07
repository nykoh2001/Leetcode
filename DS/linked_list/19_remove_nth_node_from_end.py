# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_pointers = []
        curr_node = head
        while curr_node:
            node_pointers.append(curr_node)
            curr_node = curr_node.next

        if len(node_pointers) == n:
            head = head.next
            return head

        node_to_remove = node_pointers[-1 * n]
        prev_remove = node_pointers[-1 * (n + 1)]
        prev_remove.next = node_to_remove.next
        return head
