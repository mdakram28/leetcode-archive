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
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return None
        level = [root]
        next_level = []

        while level:
            next_level.clear()

            for i,node in enumerate(level):
                if i < len(level)-1:
                    node.next = level[i+1]
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            level, next_level = next_level, level
        
        return root