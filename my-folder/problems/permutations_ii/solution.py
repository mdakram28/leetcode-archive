class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        f = {}
        prev = []
        ans = []
        n = len(nums)
        def permutate():
            if len(prev) == len(nums):
                ans.append(tuple(prev))
                return
            for num, count in f.items():
                if count:
                    prev.append(num)
                    f[num] -= 1
                    permutate()
                    f[num] += 1
                    prev.pop()
        
        for num in nums:
            if num not in f:
                f[num] = 1
            else:
                f[num] += 1
                
        permutate()
        return ans