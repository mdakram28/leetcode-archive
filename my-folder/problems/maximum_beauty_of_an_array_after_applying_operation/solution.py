from sortedcontainers import SortedList

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        sl = SortedList(nums)
        ans = 1
        for num in range(min(nums), max(nums)+1):
            count = sl.bisect_left(num+k+1)-sl.bisect_left(num-k)
            # print(f"[{num-k}:{num+k}] = {count}")
            ans = max(ans, count)
        return ans
        