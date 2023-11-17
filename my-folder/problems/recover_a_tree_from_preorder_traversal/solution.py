# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, trav: str) -> Optional[TreeNode]:
        nodes = []
        i = 0
        while i < len(trav):
            d = 0
            while i < len(trav) and trav[i] == '-':
                d += 1
                i += 1
            num = 0
            while i < len(trav) and trav[i] != '-':
                num = num*10 + int(trav[i])
                i += 1
            nodes.append((d, num))

        i = 0
        def get_node(d):
            nonlocal i
            if i == len(nodes): return None
            if nodes[i][0] != d: return None
            num = nodes[i][1]
            i += 1
            return TreeNode(num, get_node(d+1), get_node(d+1))

        return get_node(0)