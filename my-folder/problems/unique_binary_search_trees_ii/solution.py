# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        

        def get_all_trees(l, r):
            if r<l:
                return [None]
            if r==l:
                return [TreeNode(l)]
            
            ret = []
            for val in range(l, r+1):
                left = get_all_trees(l, val-1)
                right = get_all_trees(val+1, r)
                for a, b in product(left, right):
                    ret.append(TreeNode(val, a, b))
            
            return ret
        
        return get_all_trees(1, n)