# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        self.st.append((0, root))
        self.to_ret = None
        while self.st and self.to_ret is None:
            self.tick()

    def tick(self):
        state, node = self.st.pop()
        if state == 0:
            if node == None:
                pass
            else:
                self.st.append((1, node))
                self.st.append((0, node.left))
        elif state == 1:
            self.to_ret = node.val
            self.st.append((2, node))
            self.st.append((0, node.right))
        else:
            pass

    def next(self) -> int:
        ret = self.to_ret
        self.to_ret = None
        while self.st and self.to_ret is None:
            self.tick()
        return ret

    def hasNext(self) -> bool:
        return self.to_ret is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()