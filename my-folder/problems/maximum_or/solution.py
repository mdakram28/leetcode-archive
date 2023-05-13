class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        suffix = []
        
        orr = 0
        for num in nums[::-1]:
            suffix.append(orr)
            orr |= num
        
        suffix.reverse()
        
        ans = 0
        prefix = 0
        for i, n in enumerate(nums):
            ans = max(ans, n<<k | prefix | suffix[i])
            prefix |= n
        
        return ans
        