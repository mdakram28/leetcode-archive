# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = [(0, root)]
        nodes = []
        max_level = -1
        for level, node in q:
            while level > max_level:
                nodes.append([])
                max_level += 1
            nodes[level].append(node.val)
            if node.left is not None:
                q.append((level+1, node.left))
            if node.right is not None:
                q.append((level+1, node.right))
        return nodes

            