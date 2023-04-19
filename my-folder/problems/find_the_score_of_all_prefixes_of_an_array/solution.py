class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = []
        total = 0
        total_m = 0
        m = 0
        for num in nums:
            total += num
            m = max(m, num)
            total_m += m
            ans.append(total + total_m)
        return ans