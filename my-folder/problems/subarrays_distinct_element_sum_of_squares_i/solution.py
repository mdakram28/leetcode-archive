class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            dist = set()
            for j in range(i, len(nums)):
                dist.add(nums[j])
                ans += len(dist)**2
                # print(len(dist))
            # print()
        return ans
        
            
        