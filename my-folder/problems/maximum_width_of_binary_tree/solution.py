# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level = Deque([(0, root)])
        max_diff = 0
        while level:
            max_diff = max(max_diff, level[-1][0]-level[0][0])
            for _ in range(len(level)):
                pos, node = level.popleft()
                if node.left:
                    level.append((pos*2, node.left))
                if node.right:
                    level.append((pos*2+1, node.right))
            
        return max_diff+1
