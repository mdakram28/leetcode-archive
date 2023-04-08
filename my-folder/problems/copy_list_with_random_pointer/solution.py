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
        if head is None:
            return None

        nodes = {}
        nodes[head] = Node(head.val)
        tail = nodes[head]

        node = head.next
        while node and node not in nodes:
            nodes[node] = Node(node.val)
            tail.next = nodes[node]
            tail = tail.next

            node = node.next

        cycle_entry = node
        tail.next = cycle_entry

        
        node = head
        while node is not cycle_entry:
            if node.random:
                nodes[node].random = nodes[node.random]
            node = node.next

        return nodes[head]