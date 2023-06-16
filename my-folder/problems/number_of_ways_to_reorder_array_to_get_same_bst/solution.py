class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
    
    def add(self, val):
        if val<self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.add(val)
        else:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.add(val)
        self.count += 1

class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        mod = 10**9+7

        @cache
        def perm(n1, n2):
            if n1 == 0 or n2 == 0: return 1
            return perm(n1-1, n2) + perm(n1, n2-1)

        root = Node(nums[0])
        for num in nums[1:]:
            root.add(num)
        
        def numWays(node):
            if node.left is None and node.right is None: return 1
            elif node.left is None: return numWays(node.right)
            elif node.right is None: return numWays(node.left)
            
            w1 = numWays(node.left)
            w2 = numWays(node.right)
            # print(node.left.val, w1, node.right.val, w2, perm(node.left.count, node.right.count))
            return (w1 * w2 * perm(node.left.count, node.right.count))%mod
        
        return (numWays(root)-1)%mod


        
            