# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        val = 1
        def label_node(node):
            nonlocal val
            if node and node.val == 0:
                node.val = val
                val += 1
                label_node(node.left)
                label_node(node.right)

        dp = {}
        def recurse(node, parent, req):
            key = (node.val if node else 0) | parent<<16 | req << 17
            if key in dp:
                return dp[key]

            if node is None:
                ret = float('inf') if req else 0
            elif req:
                ret = recurse(node.left, 1, 0) + recurse(node.right, 1, 0) + 1
            elif parent:
                ret = min(
                    recurse(node.left, 1, 0) + recurse(node.right, 1, 0) + 1,
                    recurse(node.left, 0, 0) + recurse(node.right, 0, 0)
                )
            else:
                ret = min(
                    recurse(node.left, 1, 0) + recurse(node.right, 1, 0) + 1,
                    recurse(node.left, 0, 1) + recurse(node.right, 0, 0),
                    recurse(node.left, 0, 0) + recurse(node.right, 0, 1),
                )
            dp[key] = ret
            # print(f"{node and node.val}, {parent}, {req} => {ret}")
            return ret

        label_node(root) 
        return recurse(root, 0, 0)




