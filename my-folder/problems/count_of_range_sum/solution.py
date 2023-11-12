from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: List[int], l: int, u: int) -> int:
        sl = SortedList()

        sl.add(0)
        y = 0
        ans = 0
        for num in nums:
            y += num
            ans += sl.bisect_right(y-l)-sl.bisect_left(y-u)
            sl.add(y)
        return ans