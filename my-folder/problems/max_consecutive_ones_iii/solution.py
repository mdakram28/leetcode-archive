class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        count = 0
        ans = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                count += 1
            while count > k:
                if nums[start] == 0:
                    count -= 1
                start += 1
            ans = max(ans, end-start+1)
        return ans