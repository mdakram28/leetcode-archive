# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        count = defaultdict(int)
        rootbyval = {}

        for root in trees:
            count[root.val] += 1
            rootbyval[root.val] = root
            if root.left:
                count[root.left.val] += 1
                if root.left.left:
                    count[root.left.left.val] += 1
                if root.left.right:
                    count[root.left.right.val] += 1
            if root.right:
                count[root.right.val] += 1
                if root.right.left:
                    count[root.right.left.val] += 1
                if root.right.right:
                    count[root.right.right.val] += 1
        

        # retrurns l, r
        prev = -float('inf')
        def isvalid(node):
            nonlocal prev

            if node.left is None and node.right is None:
                if node.val in rootbyval:
                    root = rootbyval[node.val]
                    del rootbyval[node.val]
                    node.left = root.left
                    node.right = root.right
                
            if node.left is not None:
                if not isvalid(node.left): return False
            
            if node.val in rootbyval:
                return False
            elif node.val <= prev:
                return False
            else:
                # print(node.val)
                prev = node.val
            
            if node.right is not None:
                if not isvalid(node.right): return False
            
            return True


        rootvals = [v for v, c in count.items() if c==1 and v in rootbyval]
        # print(rootvals, count)
        if len(rootvals) != 1: return None
        root = rootbyval[rootvals[0]]
        del rootbyval[rootvals[0]]

        return root if isvalid(root) and len(rootbyval)==0 else None



