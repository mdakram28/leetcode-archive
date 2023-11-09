class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        x = sum(nums)-x
        tl = {0: -1}
        ans = float('inf')
        for i, acc in enumerate(accumulate(nums)):
            tl[acc] = i
            if (acc-x) in tl:
                ans = min(ans, n-i+tl[acc-x])
        
        return ans if ans != float('inf') else -1