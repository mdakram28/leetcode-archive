from sortedcontainers import SortedList

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        sl = SortedList()
        nums = list(enumerate(nums))
        nums.sort(key=lambda x: x[1], reverse=True)
        
        sl.add(nums[0])
        total = 1
        for i in range(1, len(nums)):
            sl.add(nums[i])
            total += (sl.bisect_left(nums[i-1]) - sl.bisect_left(nums[i]))%len(sl)
        total += nums[-1][0]
        
        return total