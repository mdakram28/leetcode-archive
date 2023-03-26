class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        min_elem = max(freq.keys(), key=lambda c: freq[c])
        return min_elem