# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            num_sum = l1.val + l2.val + carry_over
            carry_over = 0

            if num_sum >= 10:
                carry_over = 1
                num_sum -= 10

            sum_node = ListNode(num_sum)
            tail.next = sum_node
            tail = tail.next

            l1 = l1.next
            l2 = l2.next

        remaining_list = l1 if l1 else l2
        while remaining_list:
            num_sum = remaining_list.val + carry_over
            carry_over = 0

            if num_sum >= 10:
                carry_over = 1
                num_sum -= 10

            sum_node = ListNode(num_sum)
            tail.next = sum_node
            tail = tail.next

            remaining_list = remaining_list.next

        if carry_over:
            tail.next = ListNode(carry_over)

        return dummy.next
