# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = [root]
        nextlevel = []

        maxlevel = 0
        maxtotal = -float('inf')
        l = 0

        while level:
            l += 1
            total = 0
            nextlevel.clear()
            for node in level:
                if node.left: nextlevel.append(node.left)
                if node.right: nextlevel.append(node.right)
                total += node.val
            if total > maxtotal:
                maxtotal = total
                maxlevel = l
            level, nextlevel = nextlevel, level
        
        return maxlevel
