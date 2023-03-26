# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_pq(node: Optional[TreeNode]):
            if node is None:
                return None, None
            if node is p and node is q:
                return node, node
            elif node is p:
                left = find_pq(node.left)
                right = find_pq(node.right)
                if left[1] or right[1]:
                    return node, node
                else:
                    return node, None
            elif node is q:
                left = find_pq(node.left)
                right = find_pq(node.right)
                if left[0] or right[0]:
                    return node, node
                else:
                    return None, node
            else:
                left = find_pq(node.left)
                right = find_pq(node.right)
                if left[0] and left[1]:
                    return left
                elif right[0] and right[1]:
                    return right
                elif (left[0] or right[0]) and (left[1] or right[1]):
                    return node, node
                else:
                    return left[0] or right[0], left[1] or right[1]
        return find_pq(root)[0]
