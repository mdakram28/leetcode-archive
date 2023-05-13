class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        prevN = 0
        # prevD = 1
        nums.sort()
        ans = 0
        mod = 10**9 + 7
        for j, num in enumerate(nums):
            # print(prevN)
            ans = (ans + (prevN*num*num) + num*num*num)%mod
            # print(f"{total=}")
            # ans += total
            
            # p = 2**(j+1)
            prevN = (prevN*2 + num) % mod
        
        return ans