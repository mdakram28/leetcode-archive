class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # i-ri = j - rj
        count = defaultdict(int)

        total = 0
        for num in nums:
            val = num - int(str(num)[::-1])
            total = (total + count[val])%(10**9+7)
            count[val] += 1
        return total