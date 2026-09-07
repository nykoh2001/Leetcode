# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        prev_node = None
        curr_node = head

        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        return prev_node

    def reorderList(self, head: Optional[ListNode]) -> None:
        fast_pointer = head
        slow_pointer = head
        while fast_pointer != None:
            fast_pointer = fast_pointer.next
            if fast_pointer == None:
                break
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
        
        second_half = slow_pointer.next
        slow_pointer.next = None

        original_list = head
        reversed_list = self.reverseList(second_half)
        
        while original_list != None and reversed_list != None:
            original_next = original_list.next
            reversed_next = reversed_list.next

            original_list.next = reversed_list
            original_list = original_next

            reversed_list.next = original_list
            reversed_list = reversed_next