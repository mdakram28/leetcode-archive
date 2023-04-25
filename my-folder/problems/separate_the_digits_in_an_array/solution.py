class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums[::-1]:
            while num:
                ans.append(num%10)
                num //= 10
        ans.reverse()
        return ans