class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        first = [int(str(num)[0]) for num in nums]
        for i in range(n):
            for j in range(i+1, n):
                if math.gcd(first[i], nums[j]%10) == 1: 
                    ans += 1
                    # print(i, j)
        return ans