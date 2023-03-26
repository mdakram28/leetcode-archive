class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        piles = []

        def bs(target):
            l = 0
            r = len(piles)
            while l<r:
                mid = (l+r) // 2
                if target > piles[mid]:
                    l = mid+1
                else:
                    r = mid
            return l
        
        for num in nums:
            pi = bs(num)
            if pi < len(piles):
                piles[pi] = num
            else:
                piles.append(num)
        return len(piles)
    
    def lengthOfLIS_DP(self, nums: List[int]) -> int:
        dp = []
        max_count = 1
        for i in range(len(nums)):
            num = nums[i]
            count = 1
            for j in range(i):
                if nums[j] < num:
                    count = max(count, dp[j]+1)
            dp.append(count)
            max_count = max(max_count, count)
        return max_count
