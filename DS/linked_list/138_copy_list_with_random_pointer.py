"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        original_pointers_to_idx = {}
        node_pointers = []

        tail = None
        curr_node = head
        idx = 0
        while curr_node:
            original_pointers_to_idx[curr_node] = idx
            copied_node = Node(curr_node.val, None, curr_node.random)
            if tail:
                tail.next = copied_node
                tail = tail.next

            node_pointers.append(copied_node)
            tail = copied_node
            curr_node = curr_node.next
            idx += 1

        for copied_node in node_pointers:
            if copied_node.random == None:
                continue
            random_idx = original_pointers_to_idx[copied_node.random]
            copied_node.random = node_pointers[random_idx]

        return node_pointers[0]
