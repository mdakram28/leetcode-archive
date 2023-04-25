from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left = SortedList()
        right = SortedList()
        n = len(nums)
        
        for i in range(k-1):
            right.add(nums[i])
        
        while len(right)-len(left) > 1:
            left.add(right.pop(0))
        
        ans = []
        for i in range(k-1, n):
            right.add(nums[i])
            left.add(right.pop(0))

            if len(left) - len(right) > 1:
                right.add(left.pop(-1))
            
            med = left[-1] if k%2 else (left[-1] + right[0])/2
            ans.append(med)

            rem = nums[i-k+1]
            if rem <= med:
                left.remove(rem)
            else:
                right.remove(rem)
        
        return ans