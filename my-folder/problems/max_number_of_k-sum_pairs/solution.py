class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        count = defaultdict(int)
        for num in nums:
            t = k-num
            if count[t] > 0:
                count[t] -= 1
                ans += 1
            else:
                count[num] += 1
        
        return ans
