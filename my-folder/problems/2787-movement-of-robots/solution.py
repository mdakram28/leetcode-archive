class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        nums = sorted(v+d if direc == 'R' else v-d for direc, v in zip(s, nums))

        ans = 0
        prev = 0
        for i, num in enumerate(nums):
            ans = (ans + num*i - prev)%(10**9+7)
            prev += num
        return ans
