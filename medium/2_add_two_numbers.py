"""https://leetcode.com/problems/add-two-numbers/

Singly-linked list

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        node1, node2 = l1, l2
        output = ListNode()

        current_output = output
        while node1 or node2:
            if not node1:
                node1 = ListNode()
            if not node2:
                node2 = ListNode()

            val1, val2 = node1.val, node2.val
            sum_val = val1 + val2

            if sum_val + current_output.val >= 10:
                next_output = ListNode(1)
                current_output.next = next_output
                current_output.val = (current_output.val + sum_val) % 10
            else:
                current_output.val += sum_val
                if node1.next or node2.next:
                    current_output.next = ListNode()

            node1 = node1.next
            node2 = node2.next
            current_output = current_output.next
        return output


if __name__ == "__main__":
    sol = Solution()
    num1 = [2, 4, 3]
    num2 = [5, 6, 4]

    l1, l2 = ListNode(num1[0]), ListNode(num2[0])
    prev_node1, prev_node2 = l1, l2
    for n in num1[1:]:
        current_node = ListNode(n)
        prev_node1.next = current_node
        prev_node1 = prev_node1.next
    for n in num2[1:]:
        current_node = ListNode(n)
        prev_node2.next = current_node
        prev_node2 = prev_node2.next
    print(sol.addTwoNumbers(l1, l2))
