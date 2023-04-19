# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = 0
        if root.left:
            s += root.left.val
        if root.right:
            s += root.right.val
        
        total_root = s
        
        q = Deque()
        root.val = 0
        
        if root.left:
            q.append((root.left, total_root))
        if root.right:
            q.append((root.right, total_root))
        
        
        while q:
            next_s = 0
            for _ in range(len(q)):
                node, total_parent = q.popleft()
                node.val = s - total_parent
                total_node = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                next_s += total_node
                
                if node.left:
                    q.append((node.left, total_node))
                if node.right:
                    q.append((node.right, total_node))
            s = next_s
        
        return root
            
        