class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        ans = total
        for j in range(k, len(nums)):
            total += nums[j]-nums[j-k]
            ans = max(ans, total)
        return ans/k