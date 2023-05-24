class Solution:
    def maxScore(self, nums: List[int]) -> int:
        gcd = {}
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                gcd[(nums[i], nums[j])] = math.gcd(nums[i], nums[j])
        N = len(nums)

        @cache
        def sub_score(nums: Tuple[int]) -> int:
            nonlocal N
            if len(nums) == 0: return 0
            ans = 0
            ind = (N - len(nums))//2 + 1
            for i in range(len(nums)-1):
                for j in range(i+1, len(nums)):
                    sub_arr = tuple(n for k,n in enumerate(nums) if k != i and k != j)
                    ans = max(ans, ind*gcd[(nums[i], nums[j])] + sub_score(sub_arr))
            # print(nums, ind, ans)
            return ans
        
        return sub_score(tuple(nums))