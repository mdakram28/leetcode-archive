# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        def min_swaps(nums):
            s = sorted(nums)
            
            pos = {}
            for i, num in enumerate(nums):
                pos[num] = i
                
            swaps = 0
            for i in range(len(nums)):
                if nums[i] == s[i]: continue
                p = pos[s[i]]
                nums[i], nums[p] = nums[p], nums[i]
                pos[nums[i]] = i
                pos[nums[p]] = p
                swaps += 1
            return swaps
        
        
        level = [root]
        nums = []
        next_level = []
        ans = 0
        
        while level:
            next_level.clear()
            nums.clear()
            for node in level:
                nums.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            ans += min_swaps(nums)
            level, next_level = next_level, level
        
        return ans
        