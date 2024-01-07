class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        prev = [defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                diff = nums[j]-nums[i]
                ans += prev[i][diff]
                prev[j][diff] += 1 + prev[i][diff]
        
        return ans