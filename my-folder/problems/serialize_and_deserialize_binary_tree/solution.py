# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = [root]
        s = []
        for node in q:
            if node == None:
                s.append("")
            else:
                s.append(node.val)
                q.append(node.left)
                q.append(node.right)
        ret = ",".join(map(str, s))
        print(f"{ret=}")
        return ret
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """ 
        vals = data.split(",")
        q = Queue()

        if len(vals) == 0 or len(vals[0]) == 0:
            return None

        root = TreeNode(vals[0])
        q.put(root)
        
        for i in range(1, len(vals), 2):
            parent = q.get()

            left_val = vals[i]
            right_val = vals[i+1]
            # print(f"{left_val=}, {right_val=}")
            if len(left_val) != 0:
                parent.left = TreeNode(left_val)
                q.put(parent.left)
            if len(right_val) != 0:
                parent.right = TreeNode(right_val)
                q.put(parent.right)
        
        print(f"{root=}")
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))