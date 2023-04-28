class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i, num in enumerate(nums):
            nums[i] = -num
            
        heapify(nums)
        score = 0
        for _ in range(k):
            num = -heappop(nums)
            score += num
            heappush(nums, -math.ceil(num/3))
        
        return score