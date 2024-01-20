from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        right = SortedList()
        left = SortedList()
        
        n = len(nums)
        l = 1
        total = 0
        ans = float('inf')
        
        for r in range(1, n):
            right.add((nums[r], r))
            if len(right) + len(left) > (dist+1):
                t = (nums[l], l)
                if t in left:
                    total -= t[0]
                    left.discard(t)
                right.discard((nums[l], l))
                l += 1
                
            if len(right) > 0:
                t = right.pop(0)
                total += t[0]
                left.add(t)
                
            while len(left) > k-1:
                t = left.pop()
                total -= t[0]
                right.add(t)
        
            if len(left) == k-1:
                ans = min(ans, total)
        
        return ans + nums[0]
        
        