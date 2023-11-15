class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        val = 0
        arr.sort()
        for num in arr:
            if num > val:
                val += 1
        return val

                