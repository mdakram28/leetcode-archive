"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        nodes = [root]
        next_nodes = []
        while len(nodes) > 0:
            next_nodes.clear()
            # print(nodes)
            # print(list(map(lambda n: n.val, nodes)))
            for i in range(len(nodes)):
                if i < (len(nodes)-1):
                    nodes[i].next = nodes[i+1] 
                if nodes[i].left is not None:
                    next_nodes.append(nodes[i].left)
                if nodes[i].right is not None:
                    next_nodes.append(nodes[i].right)

            nodes, next_nodes = next_nodes, nodes
        return root