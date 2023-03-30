# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        st = []
        nodes = []
        node = root
        while node:
            st.append(node)
            node = node.left
        while st:
            # Stack item => item's left subtree has been traversed
            node = st.pop()
            nodes.append(node)
            if node.right:
                node = node.right
                st.append(node)
                node = node.left
                while node:
                    st.append(node)
                    node = node.left
        
        sorted_vals = sorted(n.val for n in nodes)
        for node, val in zip(nodes, sorted_vals):
            node.val = val
        