# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def delete(node, val):
            if node is None:
                return None
            elif val < node.val:
                node.left = delete(node.left, val)
                return node
            elif val > node.val:
                node.right = delete(node.right, val)
                return node
            else:
                if node.left:
                    prev = node
                    repl_node = node.left
                    while repl_node.right:
                        prev = repl_node
                        repl_node = repl_node.right
                    
                    node.val = repl_node.val
                    if prev == node:
                        node.left = delete(node.left, node.val)
                    else:
                        prev.right = delete(prev.right, node.val)
                    return node

                elif node.right:
                    prev = node
                    repl_node = node.right
                    while repl_node.left:
                        prev = repl_node
                        repl_node = repl_node.left
                    node.val = repl_node.val
                    if prev == node:
                        node.right = delete(node.right, node.val)
                    else:
                        prev.left = delete(prev.left, node.val)
                    return node
                else:
                    return None
        return delete(root, key)
                


                    

