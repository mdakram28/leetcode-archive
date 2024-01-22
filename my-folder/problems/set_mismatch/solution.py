class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = [False]*(n+1)
        rep = None
        for num in nums:
            if seen[num]:
                rep = num
                break
            seen[num] = True
        
        return [rep, (n*(n+1))//2 - sum(nums)+rep]