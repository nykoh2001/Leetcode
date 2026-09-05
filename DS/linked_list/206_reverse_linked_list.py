# https: // leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        prev_node = None

        reversed_next_node = None

        while current_node != None:
            new_node = ListNode(current_node.val, reversed_next_node)
            reversed_next_node = new_node

            prev_node = current_node
            current_node = current_node.next

        return reversed_next_node
