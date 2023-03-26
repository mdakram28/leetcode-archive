# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        level = [root]
        next_level = []
        ret = [[root.val]]
        rev = True

        while len(level) > 0:
            next_level.clear()
            if rev:
                for node in level[::-1]:
                    if node.right is not None:
                        next_level.append(node.right)
                    if node.left is not None:
                        next_level.append(node.left)
            else:
                for node in level[::-1]:
                    if node.left is not None:
                        next_level.append(node.left)
                    if node.right is not None:
                        next_level.append(node.right)
            rev = not rev
            if len(next_level) > 0:
                ret.append(list(map(lambda x: x.val, next_level)))
            level, next_level = next_level, level
        
        return ret