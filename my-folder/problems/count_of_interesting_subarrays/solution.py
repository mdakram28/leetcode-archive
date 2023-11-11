class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = 0
        rem = defaultdict(int)
        ans = 0
        rem[0] = 1
        for num in nums:
            if num%modulo == k:
                count += 1
            ans += rem[(count - k)%modulo]

            rem[count%modulo] += 1
        return ans