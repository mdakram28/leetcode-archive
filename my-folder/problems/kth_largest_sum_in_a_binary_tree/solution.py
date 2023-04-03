# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        level = [root]
        next_level = []
        while level:
            next_level.clear()
            total = 0
            for node in level:
                total += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            # print(total)
            heapq.heappush(heap, -total)
            level, next_level = next_level, level
        
        if k > len(heap):
            return -1
        
        while k:
            k -= 1
            top = -heapq.heappop(heap)
        
        return top