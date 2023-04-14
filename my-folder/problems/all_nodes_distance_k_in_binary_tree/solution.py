# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        ret = []

        def add_children(node, dist):
            if node is None or dist < 0:
                return
            if dist == 0:
                ret.append(node.val)
                return
            
            add_children(node.left, dist-1)
            add_children(node.right, dist-1)

        def dfs(node):
            if node is None:
                return 0
            if node is target:
                add_children(node, k)
                return 1

            left_dist = dfs(node.left)
            if left_dist:
                if left_dist == k:
                    ret.append(node.val)
                else:
                    add_children(node.right, k-left_dist-1)
                return left_dist+1
            
            right_dist = dfs(node.right)
            if right_dist:
                if right_dist == k:
                    ret.append(node.val)
                else:
                    add_children(node.left, k-right_dist-1)
                return right_dist+1
            
            return 0
        
        dfs(root)
        return ret
            