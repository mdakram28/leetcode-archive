class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        
        c = Counter(nums)
        total = 0
        maxCount = 0
        for val, count in c.items():
            if count > maxCount:
                total = count
                maxCount = count
            elif count == maxCount:
                total += count
        
        return total