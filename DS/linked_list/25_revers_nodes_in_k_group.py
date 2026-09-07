# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: ListNode) -> list[ListNode]:
        original_head = head
        curr_node = head
        prev_node = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        # head, tail
        return [prev_node, original_head]

    def get_group_last_pointer(self, head: ListNode, k: int) -> Optional[ListNode]:
        curr_node = head
        for _ in range(k - 1):
            curr_node = curr_node.next
            if curr_node == None:
                return None

        return curr_node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result_head = None
        result_tail = None
        start_pointer = head
        last_pointer = self.get_group_last_pointer(start_pointer, k)

        while last_pointer:
            new_start_pointer = last_pointer.next
            last_pointer.next = None
            reversed_head, reversed_tail = self.reverse(start_pointer)
            if not result_head:
                result_head = reversed_head
            if result_tail:
                result_tail.next = reversed_head

            if not new_start_pointer:
                break
            result_tail = reversed_tail
            start_pointer = new_start_pointer
            last_pointer = self.get_group_last_pointer(start_pointer, k)

        if new_start_pointer:
            result_tail.next = new_start_pointer

        return result_head
